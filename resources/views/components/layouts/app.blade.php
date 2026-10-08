<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}" class="h-full bg-slate-950 text-slate-100">
<head>
    <meta charset="utf-8">
    <meta name="viewport" content="width=device-width, initial-scale=1">
    <meta name="csrf-token" content="{{ csrf_token() }}">

    <title>{{ $title ?? config('app.name', 'Laravel Study App') }}</title>

    <!-- Google Fonts / Instrument Sans -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Instrument+Sans:ital,wght@0,400..700;1,400..700&display=swap" rel="stylesheet">

    <!-- Vite Assets -->
    @vite(['resources/css/app.css', 'resources/js/app.js'])

    <!-- PWA Metadata & Mobile App Tags -->
    <link rel="manifest" href="/manifest.json">
    <meta name="theme-color" content="#4f46e5">
    <meta name="mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-capable" content="yes">
    <meta name="apple-mobile-web-app-status-bar-style" content="black-translucent">
    <meta name="apple-mobile-web-app-title" content="Study App">
    <link rel="apple-touch-icon" href="/icons/apple-touch-icon.png">
    <link rel="icon" type="image/svg+xml" href="/icons/icon.svg">
    <link rel="shortcut icon" href="/icons/icon-192x192.png">
    <script src="/pwa-init.js" defer></script>

    <!-- Standalone CSS fallback for instant styling -->
    <style>
        body {
            font-family: 'Instrument Sans', ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", Roboto, "Helvetica Neue", Arial, sans-serif;
        }
    </style>
</head>
<body class="h-full flex flex-col antialiased bg-slate-950 text-slate-100">
    <!-- Top Navigation Bar -->
    <nav class="border-b border-slate-800 bg-slate-900/80 backdrop-blur-md sticky top-0 z-50">
        <div class="w-full px-4 sm:px-6 lg:px-8">
            <div class="flex justify-between h-16 items-center">
                <div class="flex items-center space-x-6">
                    <a href="{{ route('dashboard') }}" class="flex items-center space-x-2 font-bold text-xl tracking-tight text-white hover:text-indigo-400 transition-colors">
                        <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center shadow-lg shadow-indigo-500/20">
                            <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                            </svg>
                        </div>
                        <span>Study App</span>
                    </a>

                    @auth
                        <div class="hidden md:flex items-center space-x-1 pl-4 border-l border-slate-800">
                            <a href="{{ route('dashboard') }}" class="px-3 py-1.5 rounded-lg text-xs font-semibold {{ Route::is('dashboard') ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/30' : 'text-slate-400 hover:text-slate-200' }} transition-colors">
                                Dashboard
                            </a>
                            <a href="{{ route('questions.index') }}" class="px-3 py-1.5 rounded-lg text-xs font-semibold {{ Route::is('questions.*') ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/30' : 'text-slate-400 hover:text-slate-200' }} transition-colors">
                                Question Bank
                            </a>
                            <a href="{{ route('exams.index') }}" class="px-3 py-1.5 rounded-lg text-xs font-semibold {{ Route::is('exams.*') ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/30' : 'text-slate-400 hover:text-slate-200' }} transition-colors">
                                Exams
                            </a>
                        </div>
                    @endauth
                </div>

                <div class="flex items-center space-x-4">
                    @auth
                        <!-- Chat & Notifications Bell Button -->
                        <button type="button" onclick="openChatModal()" class="relative p-2 text-slate-400 hover:text-white bg-slate-800 hover:bg-slate-700 rounded-xl border border-slate-700 transition-all cursor-pointer flex items-center justify-center" title="Open Chat & Notifications">
                            <svg class="w-5 h-5 text-indigo-400" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                            </svg>
                            <span id="nav_chat_unread_badge" class="hidden absolute -top-1 -right-1 px-1.5 py-0.5 text-[10px] font-black bg-rose-600 text-white rounded-full border border-slate-900 shadow-md">0</span>
                        </button>

                        <div class="hidden sm:flex items-center space-x-3 mr-2">
                            <div class="w-8 h-8 rounded-full bg-indigo-500/20 border border-indigo-500/40 text-indigo-300 font-semibold flex items-center justify-center text-sm">
                                {{ strtoupper(substr(Auth::user()->name, 0, 1)) }}
                            </div>
                            <span class="text-sm font-medium text-slate-300">{{ Auth::user()->name }}</span>
                        </div>
                        <form method="POST" action="{{ route('logout') }}">
                            @csrf
                            <button type="submit" class="px-4 py-2 text-sm font-medium text-slate-300 hover:text-white bg-slate-800 hover:bg-slate-700 rounded-lg border border-slate-700 transition-all duration-150 shadow-sm flex items-center space-x-2 cursor-pointer">
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
                                </svg>
                                <span>Logout</span>
                            </button>
                        </form>
                    @else
                        @if(!Route::is('login'))
                            <a href="{{ route('login') }}" class="px-4 py-2 text-sm font-medium text-slate-300 hover:text-white transition-colors">Log in</a>
                        @endif
                        @if(!Route::is('register'))
                            <a href="{{ route('register') }}" class="px-4 py-2 text-sm font-medium text-white bg-indigo-600 hover:bg-indigo-500 rounded-lg shadow-md shadow-indigo-600/30 transition-all duration-150">Register</a>
                        @endif
                    @endauth
                </div>
            </div>
        </div>
    </nav>

    <!-- Main Content Area -->
    <main class="flex-1 pb-16 sm:pb-0">
        @if (session('status'))
            <div class="w-full px-4 sm:px-6 lg:px-8 mt-4">
                <div class="p-4 rounded-xl bg-indigo-950/80 border border-indigo-500/30 text-indigo-200 text-sm flex items-center justify-between shadow-lg">
                    <div class="flex items-center space-x-2">
                        <svg class="w-5 h-5 text-indigo-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span>{{ session('status') }}</span>
                    </div>
                </div>
            </div>
        @endif

        {{ $slot }}
    </main>

    @auth
        <!-- Mobile Bottom Navigation Bar (PWA / Touch Optimized) -->
        <div class="sm:hidden fixed bottom-0 left-0 right-0 z-40 bg-slate-900/95 border-t border-slate-800/80 backdrop-blur-xl flex justify-around items-center py-2 px-2 shadow-2xl">
            <a href="{{ route('dashboard') }}" class="flex flex-col items-center py-1 px-3 rounded-xl transition-colors {{ Route::is('dashboard') ? 'text-indigo-400 font-semibold' : 'text-slate-400 hover:text-slate-200' }}">
                <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M3 12l2-2m0 0l7-7 7 7M5 10v10a1 1 0 001 1h3m10-11l2 2m-2-2v10a1 1 0 01-1 1h-3m-6 0a1 1 0 00-1-1v-4a1 1 0 011-1h2a1 1 0 011 1v4a1 1 0 001 1m-6 0h6" />
                </svg>
                <span class="text-[10px]">Dashboard</span>
            </a>
            <button type="button" onclick="openChatModal()" class="relative flex flex-col items-center py-1 px-3 rounded-xl text-slate-400 hover:text-slate-200 transition-colors">
                <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
                <span class="text-[10px]">Chat</span>
                <span id="mobile_chat_unread_badge" class="hidden absolute top-0 right-2 px-1 py-0.2 text-[9px] font-black bg-rose-600 text-white rounded-full">0</span>
            </button>
            <a href="{{ route('questions.index') }}" class="flex flex-col items-center py-1 px-3 rounded-xl transition-colors {{ Route::is('questions.*') ? 'text-indigo-400 font-semibold' : 'text-slate-400 hover:text-slate-200' }}">
                <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                </svg>
                <span class="text-[10px]">Questions</span>
            </a>
            <a href="{{ route('exams.index') }}" class="flex flex-col items-center py-1 px-3 rounded-xl transition-colors {{ Route::is('exams.*') ? 'text-indigo-400 font-semibold' : 'text-slate-400 hover:text-slate-200' }}">
                <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                </svg>
                <span class="text-[10px]">Exams</span>
            </a>
        </div>

        <!-- CHAT & NOTIFICATION MODAL -->
        <div id="chatModal" class="hidden fixed inset-0 z-50 bg-slate-950/80 backdrop-blur-md flex items-center justify-center p-2 sm:p-4 overflow-hidden">
            <div class="bg-slate-900 border border-slate-800 rounded-2xl w-full max-w-4xl h-[85vh] flex flex-col shadow-2xl overflow-hidden">
                
                <!-- Modal Header -->
                <div class="px-5 py-3.5 bg-slate-950 border-b border-slate-800 flex items-center justify-between shrink-0">
                    <div class="flex items-center space-x-3">
                        <div class="w-9 h-9 rounded-xl bg-indigo-500/20 border border-indigo-500/40 text-indigo-400 flex items-center justify-center font-bold">
                            <svg class="w-5 h-5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z"/></svg>
                        </div>
                        <div>
                            <h3 class="text-base font-extrabold text-white">Study App Chat & Notifications</h3>
                            <p class="text-xs text-slate-400">Direct messaging between Teachers & Students</p>
                        </div>
                    </div>

                    <button type="button" onclick="closeChatModal()" class="text-slate-400 hover:text-white p-1.5 rounded-lg hover:bg-slate-800 transition-colors">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
                    </button>
                </div>

                <!-- Chat Body: Grid of Contacts + Chat Room -->
                <div class="flex-1 grid grid-cols-1 md:grid-cols-3 overflow-hidden bg-slate-950/60">
                    <!-- Contact List (Left Panel) -->
                    <div class="border-r border-slate-800/80 flex flex-col bg-slate-950/40 h-full overflow-hidden">
                        <div class="p-3 border-b border-slate-800/80">
                            <input type="text" id="chat_contact_search" oninput="filterChatContacts()" placeholder="Search contacts..." class="w-full px-3 py-1.5 bg-slate-900 border border-slate-800 rounded-xl text-xs text-slate-200 placeholder-slate-500 focus:ring-1 focus:ring-indigo-500 focus:border-indigo-500">
                        </div>
                        <div id="chat_contacts_list" class="flex-1 overflow-y-auto divide-y divide-slate-900">
                            <div class="p-4 text-center text-slate-500 text-xs">Loading contacts...</div>
                        </div>
                    </div>

                    <!-- Chat Window (Right Panel) -->
                    <div class="md:col-span-2 flex flex-col h-full bg-slate-900/50 overflow-hidden">
                        <!-- Selected Contact Header -->
                        <div id="chat_active_header" class="px-5 py-3 border-b border-slate-800/80 bg-slate-950/80 flex items-center justify-between shrink-0">
                            <div class="flex items-center space-x-3">
                                <div id="active_contact_avatar" class="w-8 h-8 rounded-full bg-indigo-600/30 border border-indigo-500/40 text-indigo-300 font-bold text-xs flex items-center justify-center">?</div>
                                <div>
                                    <h4 id="active_contact_name" class="text-sm font-bold text-white">Select a contact to start chatting</h4>
                                    <span id="active_contact_role" class="text-[11px] text-slate-400 block">No user selected</span>
                                </div>
                            </div>
                        </div>

                        <!-- Messages Stream -->
                        <div id="chat_messages_container" class="flex-1 p-4 overflow-y-auto space-y-3">
                            <div class="text-center py-12 text-slate-500 text-xs">
                                Select a contact on the left to start a conversation or reply to messages.
                            </div>
                        </div>

                        <!-- Message Input Box -->
                        <form id="chat_send_form" onsubmit="handleSendChatMessage(event)" class="p-3 border-t border-slate-800/80 bg-slate-950/90 flex items-center space-x-2 shrink-0">
                            <input type="hidden" id="chat_receiver_id" value="">
                            <input type="text" id="chat_message_input" placeholder="Type a message..." disabled class="flex-1 px-4 py-2 bg-slate-900 border border-slate-800 rounded-xl text-xs text-white placeholder-slate-500 focus:outline-none focus:border-indigo-500 disabled:opacity-50">
                            <button type="submit" id="chat_send_btn" disabled class="px-4 py-2 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold rounded-xl shadow-lg shadow-indigo-600/30 transition-all disabled:opacity-40 cursor-pointer flex items-center space-x-1">
                                <span>Send</span>
                                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 19l9-7-7-7-7 7 9 7z"/></svg>
                            </button>
                        </form>
                    </div>
                </div>
            </div>
        </div>

        <script>
            let chatContactsData = [];
            let activeChatUserId = null;
            let chatPollInterval = null;

            function openChatModal(targetUserId = null) {
                document.getElementById('chatModal').classList.remove('hidden');
                loadChatContacts(targetUserId);
                if (!chatPollInterval) {
                    chatPollInterval = setInterval(refreshChatState, 4000);
                }
            }

            function closeChatModal() {
                document.getElementById('chatModal').classList.add('hidden');
            }

            function loadChatContacts(autoSelectUserId = null) {
                fetch('/chat/contacts')
                    .then(res => res.json())
                    .then(data => {
                        chatContactsData = data.contacts || [];
                        renderChatContacts(chatContactsData);

                        if (autoSelectUserId) {
                            selectChatContact(autoSelectUserId);
                        } else if (!activeChatUserId && chatContactsData.length > 0) {
                            selectChatContact(chatContactsData[0].id);
                        }
                    })
                    .catch(err => console.error('Error loading contacts:', err));
            }

            function renderChatContacts(contacts) {
                const container = document.getElementById('chat_contacts_list');
                if (!contacts || contacts.length === 0) {
                    container.innerHTML = `<div class="p-4 text-center text-slate-500 text-xs">No contacts available.</div>`;
                    return;
                }

                let html = '';
                contacts.forEach(c => {
                    const isSelected = activeChatUserId == c.id;
                    const bgClass = isSelected ? 'bg-indigo-950/50 border-l-4 border-indigo-500' : 'hover:bg-slate-900/60';
                    const initial = c.name ? c.name.charAt(0).toUpperCase() : '?';

                    html += `
                        <div onclick="selectChatContact(${c.id})" class="p-3 cursor-pointer transition-colors ${bgClass} flex items-center justify-between">
                            <div class="flex items-center space-x-3 overflow-hidden">
                                <div class="w-8 h-8 rounded-full bg-slate-800 text-indigo-300 border border-slate-700 flex items-center justify-center font-bold text-xs shrink-0">
                                    ${initial}
                                </div>
                                <div class="overflow-hidden">
                                    <h5 class="text-xs font-bold text-slate-200 truncate">${c.name}</h5>
                                    <span class="text-[10px] text-slate-400 block truncate">${c.role} ${c.last_message ? '• ' + c.last_message : ''}</span>
                                </div>
                            </div>
                            ${c.unread_count > 0 ? `<span class="px-2 py-0.5 text-[10px] font-extrabold bg-rose-500 text-white rounded-full shrink-0 shadow-sm">${c.unread_count}</span>` : ''}
                        </div>
                    `;
                });
                container.innerHTML = html;
            }

            function filterChatContacts() {
                const q = document.getElementById('chat_contact_search').value.toLowerCase();
                const filtered = chatContactsData.filter(c => c.name.toLowerCase().includes(q) || c.role.toLowerCase().includes(q));
                renderChatContacts(filtered);
            }

            function selectChatContact(userId) {
                activeChatUserId = userId;
                renderChatContacts(chatContactsData);

                const contact = chatContactsData.find(c => c.id == userId);
                if (contact) {
                    document.getElementById('active_contact_name').textContent = contact.name;
                    document.getElementById('active_contact_role').textContent = contact.role;
                    document.getElementById('active_contact_avatar').textContent = contact.name.charAt(0).toUpperCase();
                }

                document.getElementById('chat_receiver_id').value = userId;
                document.getElementById('chat_message_input').disabled = false;
                document.getElementById('chat_send_btn').disabled = false;

                loadChatMessages(userId);
            }

            function loadChatMessages(userId) {
                fetch(`/chat/messages/${userId}`)
                    .then(res => res.json())
                    .then(data => {
                        renderChatStream(data.messages);
                        fetchChatNotifications();
                    })
                    .catch(err => console.error('Error fetching messages:', err));
            }

            function renderChatStream(messages) {
                const container = document.getElementById('chat_messages_container');
                if (!messages || messages.length === 0) {
                    container.innerHTML = `
                        <div class="text-center py-12 text-slate-500 text-xs">
                            No messages yet. Send a message below to start chatting!
                        </div>
                    `;
                    return;
                }

                let html = '';
                messages.forEach(m => {
                    if (m.is_me) {
                        html += `
                            <div class="flex flex-col items-end">
                                <div class="max-w-[75%] px-4 py-2 rounded-2xl rounded-tr-none bg-indigo-600 text-white text-xs shadow-md">
                                    ${escapeHtml(m.message)}
                                </div>
                                <span class="text-[9px] text-slate-500 mt-1">${m.created_at}</span>
                            </div>
                        `;
                    } else {
                        html += `
                            <div class="flex flex-col items-start">
                                <div class="max-w-[75%] px-4 py-2 rounded-2xl rounded-tl-none bg-slate-800 text-slate-200 border border-slate-700 text-xs shadow-md">
                                    ${escapeHtml(m.message)}
                                </div>
                                <span class="text-[9px] text-slate-500 mt-1">${m.created_at}</span>
                            </div>
                        `;
                    }
                });

                container.innerHTML = html;
                container.scrollTop = container.scrollHeight;
            }

            function handleSendChatMessage(e) {
                e.preventDefault();
                const receiverId = document.getElementById('chat_receiver_id').value;
                const messageInput = document.getElementById('chat_message_input');
                const message = messageInput.value.trim();

                if (!receiverId || !message) return;

                const csrfToken = document.querySelector('meta[name="csrf-token"]')?.getAttribute('content');

                fetch('/chat/send', {
                    method: 'POST',
                    headers: {
                        'Content-Type': 'application/json',
                        'Accept': 'application/json',
                        'X-CSRF-TOKEN': csrfToken
                    },
                    body: JSON.stringify({
                        receiver_id: receiverId,
                        message: message
                    })
                })
                .then(res => res.json())
                .then(data => {
                    if (data.success) {
                        messageInput.value = '';
                        loadChatMessages(receiverId);
                        loadChatContacts();
                    } else if (data.error) {
                        alert(data.error);
                    }
                })
                .catch(err => console.error('Error sending message:', err));
            }

            function refreshChatState() {
                fetchChatNotifications();
                if (!document.getElementById('chatModal').classList.contains('hidden') && activeChatUserId) {
                    loadChatMessages(activeChatUserId);
                }
            }

            function fetchChatNotifications() {
                fetch('/chat/notifications')
                    .then(res => res.json())
                    .then(data => {
                        const badge = document.getElementById('nav_chat_unread_badge');
                        const mobileBadge = document.getElementById('mobile_chat_unread_badge');
                        if (badge) {
                            if (data.unread_count > 0) {
                                badge.textContent = data.unread_count;
                                badge.classList.remove('hidden');
                            } else {
                                badge.classList.add('hidden');
                            }
                        }
                        if (mobileBadge) {
                            if (data.unread_count > 0) {
                                mobileBadge.textContent = data.unread_count;
                                mobileBadge.classList.remove('hidden');
                            } else {
                                mobileBadge.classList.add('hidden');
                            }
                        }
                    })
                    .catch(err => console.error('Error fetching notifications:', err));
            }

            function escapeHtml(text) {
                const map = {
                    '&': '&amp;',
                    '<': '&lt;',
                    '>': '&gt;',
                    '"': '&quot;',
                    "'": '&#039;'
                };
                return text.replace(/[&<>"']/g, m => map[m]);
            }

            document.addEventListener('DOMContentLoaded', () => {
                fetchChatNotifications();
                setInterval(fetchChatNotifications, 5000);
            });
        </script>
    @endauth
    <!-- Footer -->
    <footer class="border-t border-slate-800/60 py-6 text-center text-xs text-slate-500 mb-12 sm:mb-0">
        <p>&copy; {{ date('Y') }} {{ config('app.name', 'Laravel') }}. All rights reserved.</p>
    </footer>
</body>
</html>
