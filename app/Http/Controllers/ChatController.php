<?php

namespace App\Http\Controllers;

use App\Models\ChatMessage;
use App\Models\Standard;
use App\Models\User;
use Illuminate\Http\JsonResponse;
use Illuminate\Http\RedirectResponse;
use Illuminate\Http\Request;
use Illuminate\Support\Facades\Auth;

class ChatController extends Controller
{
    /**
     * Fetch list of contacts for chat with unread counts and last messages.
     */
    public function contacts(Request $request): JsonResponse
    {
        /** @var User $currentUser */
        $currentUser = Auth::user();

        // Include any user with whom current user already has chat history
        $chatUserIds = ChatMessage::where('sender_id', $currentUser->id)
            ->pluck('receiver_id')
            ->merge(
                ChatMessage::where('receiver_id', $currentUser->id)->pluck('sender_id')
            )
            ->unique()
            ->reject(fn ($id) => (int) $id === (int) $currentUser->id)
            ->toArray();

        $query = User::query()->where('id', '!=', $currentUser->id);

        if ($currentUser->isTeacher()) {
            // Teachers see students belonging to their assigned/created standards, colleagues, admins, or existing chat contacts
            $teacherStandardIds = $currentUser->standards->pluck('id')->toArray();
            $createdStandardIds = Standard::where('created_by', $currentUser->id)->pluck('id')->toArray();
            $allTeacherStandardIds = array_unique(array_merge($teacherStandardIds, $createdStandardIds));

            $query->where(function ($q) use ($allTeacherStandardIds, $chatUserIds) {
                if (! empty($allTeacherStandardIds)) {
                    $q->where(function ($sub) use ($allTeacherStandardIds) {
                        $sub->whereHas('studentStandards', fn ($st) => $st->whereIn('standards.id', $allTeacherStandardIds))
                            ->orWhereHas('student', fn ($st) => $st->whereIn('standard_id', $allTeacherStandardIds));
                    });
                } else {
                    $q->whereRaw('1 = 0');
                }

                $q->orWhereHas('profile', fn ($p) => $p->whereIn('type', [1, 3, 0, 99]))
                    ->orWhereDoesntHave('profile')
                    ->orWhereIn('id', $chatUserIds);
            });
        } elseif ($currentUser->isStudent()) {
            // Students ONLY see teachers assigned to their class standards (or contacts with existing chat history)
            $studentStandardIds = $currentUser->studentStandards->pluck('id')
                ->merge(array_filter([$currentUser->student?->standard_id]))
                ->unique()
                ->toArray();

            $query->where(function ($q) use ($studentStandardIds, $chatUserIds) {
                if (! empty($studentStandardIds)) {
                    $q->where(function ($sub) use ($studentStandardIds) {
                        $sub->whereHas('standards', fn ($s) => $s->whereIn('standards.id', $studentStandardIds))
                            ->orWhereIn('id', Standard::whereIn('id', $studentStandardIds)->pluck('created_by')->filter()->toArray());
                    });
                } else {
                    $q->whereHas('profile', fn ($p) => $p->where('type', 1));
                }

                if (! empty($chatUserIds)) {
                    $q->orWhereIn('id', $chatUserIds);
                }
            });
        }

        $contacts = $query->with('profile')->get()->map(function (User $user) use ($currentUser) {
            $unreadCount = ChatMessage::where('sender_id', $user->id)
                ->where('receiver_id', $currentUser->id)
                ->where('is_read', false)
                ->count();

            $lastMessage = ChatMessage::where(function ($q) use ($currentUser, $user) {
                $q->where(function ($sub) use ($currentUser, $user) {
                    $sub->where('sender_id', $currentUser->id)->where('receiver_id', $user->id);
                })->orWhere(function ($sub) use ($currentUser, $user) {
                    $sub->where('sender_id', $user->id)->where('receiver_id', $currentUser->id);
                });
            })->latest()->first();

            $role = 'Student';
            if ($user->isTeacher()) {
                $role = 'Teacher';
            } elseif ($user->isAdmin()) {
                $role = 'Administrator';
            }

            return [
                'id' => $user->id,
                'name' => $user->name,
                'email' => $user->email,
                'role' => $role,
                'unread_count' => $unreadCount,
                'last_message' => $lastMessage ? $lastMessage->message : null,
                'last_message_time' => $lastMessage ? $lastMessage->created_at->diffForHumans() : null,
            ];
        });

        return response()->json([
            'contacts' => $contacts,
        ]);
    }

    /**
     * Fetch messages for a specific conversation partner and mark incoming as read.
     */
    public function getMessages(User $user): JsonResponse
    {
        /** @var User $currentUser */
        $currentUser = Auth::user();

        // Mark incoming unread messages as read
        ChatMessage::where('sender_id', $user->id)
            ->where('receiver_id', $currentUser->id)
            ->where('is_read', false)
            ->update(['is_read' => true]);

        $messages = ChatMessage::where(function ($q) use ($currentUser, $user) {
            $q->where(function ($sub) use ($currentUser, $user) {
                $sub->where('sender_id', $currentUser->id)->where('receiver_id', $user->id);
            })->orWhere(function ($sub) use ($currentUser, $user) {
                $sub->where('sender_id', $user->id)->where('receiver_id', $currentUser->id);
            });
        })
            ->orderBy('created_at', 'asc')
            ->get()
            ->map(function (ChatMessage $msg) use ($currentUser) {
                return [
                    'id' => $msg->id,
                    'sender_id' => $msg->sender_id,
                    'receiver_id' => $msg->receiver_id,
                    'message' => $msg->message,
                    'is_me' => $msg->sender_id === $currentUser->id,
                    'is_read' => $msg->is_read,
                    'created_at' => $msg->created_at->format('M d, H:i'),
                    'time_ago' => $msg->created_at->diffForHumans(),
                ];
            });

        $role = 'Student';
        if ($user->isTeacher()) {
            $role = 'Teacher';
        } elseif ($user->isAdmin()) {
            $role = 'Administrator';
        }

        return response()->json([
            'contact' => [
                'id' => $user->id,
                'name' => $user->name,
                'role' => $role,
            ],
            'messages' => $messages,
        ]);
    }

    /**
     * Store and send a new chat message.
     */
    public function sendMessage(Request $request): JsonResponse|RedirectResponse
    {
        /** @var User $currentUser */
        $currentUser = Auth::user();

        $validated = $request->validate([
            'receiver_id' => ['required', 'integer', 'exists:users,id'],
            'message' => ['required', 'string', 'max:2000'],
        ]);

        if ((int) $validated['receiver_id'] === $currentUser->id) {
            if ($request->wantsJson()) {
                return response()->json(['error' => 'You cannot send a message to yourself.'], 422);
            }

            return back()->with('error', 'You cannot send a message to yourself.');
        }

        $chatMessage = ChatMessage::create([
            'sender_id' => $currentUser->id,
            'receiver_id' => $validated['receiver_id'],
            'message' => trim($validated['message']),
            'is_read' => false,
        ]);

        if ($request->wantsJson()) {
            return response()->json([
                'success' => true,
                'message' => [
                    'id' => $chatMessage->id,
                    'sender_id' => $chatMessage->sender_id,
                    'receiver_id' => $chatMessage->receiver_id,
                    'message' => $chatMessage->message,
                    'is_me' => true,
                    'is_read' => false,
                    'created_at' => $chatMessage->created_at->format('M d, H:i'),
                    'time_ago' => $chatMessage->created_at->diffForHumans(),
                ],
            ]);
        }

        return back()->with('status', 'Message sent successfully!');
    }

    /**
     * Fetch unread notification metrics and recent unread messages.
     */
    public function notifications(): JsonResponse
    {
        /** @var User $currentUser */
        $currentUser = Auth::user();

        $unreadCount = ChatMessage::where('receiver_id', $currentUser->id)
            ->where('is_read', false)
            ->count();

        $recentUnread = ChatMessage::where('receiver_id', $currentUser->id)
            ->where('is_read', false)
            ->with('sender')
            ->latest()
            ->take(5)
            ->get()
            ->map(function (ChatMessage $msg) {
                return [
                    'id' => $msg->id,
                    'sender_id' => $msg->sender_id,
                    'sender_name' => $msg->sender?->name ?? 'Unknown',
                    'message' => $msg->message,
                    'time_ago' => $msg->created_at->diffForHumans(),
                ];
            });

        return response()->json([
            'unread_count' => $unreadCount,
            'recent_notifications' => $recentUnread,
        ]);
    }
}
