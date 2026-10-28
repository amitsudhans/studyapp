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

    <!-- KaTeX Mathematical Typography -->
    <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/katex@0.16.9/dist/katex.min.css">

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
                            <a href="{{ route('multimedia.index') }}" class="px-3 py-1.5 rounded-lg text-xs font-semibold {{ Route::is('multimedia.*') ? 'bg-emerald-600/20 text-emerald-300 border border-emerald-500/30' : 'text-slate-400 hover:text-slate-200' }} flex items-center space-x-1.5 transition-colors" title="Textbook Multimedia Curriculum Tree">
                                <span>📚</span>
                                <span>Curriculum Tree</span>
                            </a>
                            @if(!Auth::user()->isStudent())
                                <a href="{{ route('standards.index') }}" class="px-3 py-1.5 rounded-lg text-xs font-semibold {{ Route::is('standards.*') ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/30' : 'text-slate-400 hover:text-slate-200' }} transition-colors">
                                    Standards
                                </a>
                                <a href="{{ route('exams.index') }}" class="px-3 py-1.5 rounded-lg text-xs font-semibold {{ Route::is('exams.*') ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/30' : 'text-slate-400 hover:text-slate-200' }} transition-colors">
                                    Exams & Reports
                                </a>
                                <a href="{{ route('questions.index') }}" class="px-3 py-1.5 rounded-lg text-xs font-semibold {{ Route::is('questions.*') ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/30' : 'text-slate-400 hover:text-slate-200' }} transition-colors">
                                    Question Bank
                                </a>
                                <a href="{{ route('students.index') }}" class="px-3 py-1.5 rounded-lg text-xs font-semibold {{ Route::is('students.*') ? 'bg-indigo-600/20 text-indigo-300 border border-indigo-500/30' : 'text-slate-400 hover:text-slate-200' }} transition-colors">
                                    My Students
                                </a>
                            @endif
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

        @if (session('error'))
            <div class="w-full px-4 sm:px-6 lg:px-8 mt-4">
                <div class="p-4 rounded-xl bg-rose-950/80 border border-rose-500/30 text-rose-200 text-sm flex items-center justify-between shadow-lg">
                    <div class="flex items-center space-x-2">
                        <svg class="w-5 h-5 text-rose-400 shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                            <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                        </svg>
                        <span>{{ session('error') }}</span>
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
            <a href="{{ route('multimedia.index') }}" class="flex flex-col items-center py-1 px-3 rounded-xl transition-colors {{ Route::is('multimedia.*') ? 'text-emerald-400 font-semibold' : 'text-slate-400 hover:text-slate-200' }}">
                <span class="text-base leading-none mb-0.5">📚</span>
                <span class="text-[10px]">Curriculum</span>
            </a>
            <button type="button" onclick="openChatModal()" class="relative flex flex-col items-center py-1 px-3 rounded-xl text-slate-400 hover:text-slate-200 transition-colors">
                <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8 10h.01M12 10h.01M16 10h.01M9 16H5a2 2 0 01-2-2V6a2 2 0 012-2h14a2 2 0 012 2v8a2 2 0 01-2 2h-5l-5 5v-5z" />
                </svg>
                <span class="text-[10px]">Chat</span>
                <span id="mobile_chat_unread_badge" class="hidden absolute top-0 right-2 px-1 py-0.2 text-[9px] font-black bg-rose-600 text-white rounded-full">0</span>
            </button>
            @if(!Auth::user()->isStudent())
                <a href="{{ route('standards.index') }}" class="flex flex-col items-center py-1 px-2 rounded-xl transition-colors {{ Route::is('standards.*') ? 'text-indigo-400 font-semibold' : 'text-slate-400 hover:text-slate-200' }}">
                    <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11H5m14 0a2 2 0 012 2v6a2 2 0 01-2 2H5a2 2 0 01-2-2v-6a2 2 0 012-2m14 0V9a2 2 0 00-2-2M5 11V9a2 2 0 012-2m0 0V5a2 2 0 012-2h6a2 2 0 012 2v2M7 7h10" />
                    </svg>
                    <span class="text-[10px]">Standards</span>
                </a>
                <a href="{{ route('exams.index') }}" class="flex flex-col items-center py-1 px-2 rounded-xl transition-colors {{ Route::is('exams.*') ? 'text-indigo-400 font-semibold' : 'text-slate-400 hover:text-slate-200' }}">
                    <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z" />
                    </svg>
                    <span class="text-[10px]">Exams</span>
                </a>
                <a href="{{ route('questions.index') }}" class="flex flex-col items-center py-1 px-2 rounded-xl transition-colors {{ Route::is('questions.*') ? 'text-indigo-400 font-semibold' : 'text-slate-400 hover:text-slate-200' }}">
                    <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M8.228 9c.549-1.165 2.03-2 3.772-2 2.21 0 4 1.343 4 3 0 1.4-1.278 2.575-3.006 2.907-.542.104-.994.54-.994 1.093m0 3h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                    </svg>
                    <span class="text-[10px]">Questions</span>
                </a>
                <a href="{{ route('students.index') }}" class="flex flex-col items-center py-1 px-2 rounded-xl transition-colors {{ Route::is('students.*') ? 'text-indigo-400 font-semibold' : 'text-slate-400 hover:text-slate-200' }}">
                    <svg class="w-5 h-5 mb-0.5" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l9-5-9-5-9 5 9 5z" />
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 14l6.16-3.422a12.083 12.083 0 01.665 6.479A11.952 11.952 0 0112 20.055a11.952 11.952 0 01-6.824-2.998 12.078 12.078 0 01.665-6.479L12 14z" />
                    </svg>
                    <span class="text-[10px]">Students</span>
                </a>
            @endif
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
                        <!-- Contacts Pagination Bar (10 per page) -->
                        <div id="chat_contacts_pagination" class="p-2.5 border-t border-slate-800/80 bg-slate-950 flex items-center justify-between shrink-0 text-xs text-slate-400">
                            <button type="button" id="chat_contacts_prev" onclick="changeChatContactsPage(-1)" class="px-2.5 py-1 bg-slate-900 border border-slate-800 text-slate-300 font-semibold rounded-lg hover:bg-slate-800 transition-all disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer flex items-center space-x-1 text-[11px]">
                                <span>&larr; Prev</span>
                            </button>
                            <span id="chat_contacts_page_info" class="text-[11px] font-bold text-slate-300 font-mono">Page 1 of 1</span>
                            <button type="button" id="chat_contacts_next" onclick="changeChatContactsPage(1)" class="px-2.5 py-1 bg-slate-900 border border-slate-800 text-slate-300 font-semibold rounded-lg hover:bg-slate-800 transition-all disabled:opacity-40 disabled:cursor-not-allowed cursor-pointer flex items-center space-x-1 text-[11px]">
                                <span>Next &rarr;</span>
                            </button>
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
            let filteredContactsData = [];
            let activeChatUserId = null;
            let chatPollInterval = null;
            let chatContactsCurrentPage = 1;
            const chatContactsPerPage = 10;

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
                        const query = document.getElementById('chat_contact_search')?.value.toLowerCase() || '';
                        if (query) {
                            filteredContactsData = chatContactsData.filter(c => c.name.toLowerCase().includes(query) || c.role.toLowerCase().includes(query));
                        } else {
                            filteredContactsData = [...chatContactsData];
                        }

                        if (autoSelectUserId) {
                            const targetIdx = filteredContactsData.findIndex(c => c.id == autoSelectUserId);
                            if (targetIdx !== -1) {
                                chatContactsCurrentPage = Math.floor(targetIdx / chatContactsPerPage) + 1;
                            }
                        }

                        renderChatContacts();

                        if (autoSelectUserId) {
                            selectChatContact(autoSelectUserId);
                        } else if (!activeChatUserId && filteredContactsData.length > 0) {
                            selectChatContact(filteredContactsData[0].id);
                        }
                    })
                    .catch(err => console.error('Error loading contacts:', err));
            }

            function renderChatContacts() {
                const container = document.getElementById('chat_contacts_list');
                const pageInfo = document.getElementById('chat_contacts_page_info');
                const prevBtn = document.getElementById('chat_contacts_prev');
                const nextBtn = document.getElementById('chat_contacts_next');

                if (!filteredContactsData || filteredContactsData.length === 0) {
                    container.innerHTML = `<div class="p-4 text-center text-slate-500 text-xs">No contacts available.</div>`;
                    if (pageInfo) pageInfo.textContent = 'Page 1 of 1';
                    if (prevBtn) prevBtn.disabled = true;
                    if (nextBtn) nextBtn.disabled = true;
                    return;
                }

                const totalPages = Math.ceil(filteredContactsData.length / chatContactsPerPage) || 1;
                if (chatContactsCurrentPage > totalPages) {
                    chatContactsCurrentPage = totalPages;
                }
                if (chatContactsCurrentPage < 1) {
                    chatContactsCurrentPage = 1;
                }

                const startIdx = (chatContactsCurrentPage - 1) * chatContactsPerPage;
                const endIdx = startIdx + chatContactsPerPage;
                const pageContacts = filteredContactsData.slice(startIdx, endIdx);

                let html = '';
                pageContacts.forEach(c => {
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

                if (pageInfo) pageInfo.textContent = `Page ${chatContactsCurrentPage} of ${totalPages}`;
                if (prevBtn) prevBtn.disabled = chatContactsCurrentPage <= 1;
                if (nextBtn) nextBtn.disabled = chatContactsCurrentPage >= totalPages;
            }

            function filterChatContacts() {
                const q = document.getElementById('chat_contact_search').value.toLowerCase();
                filteredContactsData = chatContactsData.filter(c => c.name.toLowerCase().includes(q) || c.role.toLowerCase().includes(q));
                chatContactsCurrentPage = 1;
                renderChatContacts();
            }

            function changeChatContactsPage(direction) {
                const totalPages = Math.ceil(filteredContactsData.length / chatContactsPerPage) || 1;
                chatContactsCurrentPage += direction;
                if (chatContactsCurrentPage < 1) chatContactsCurrentPage = 1;
                if (chatContactsCurrentPage > totalPages) chatContactsCurrentPage = totalPages;
                renderChatContacts();
            }

            function selectChatContact(userId) {
                activeChatUserId = userId;
                renderChatContacts();

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
        <p>&copy; {{ date('Y') }} {{ config('app.name', 'Study App') }}. All rights reserved.</p>
    </footer>

    <!-- GLOBAL MULTIMEDIA ANIMATION LAB MODAL (Accessible by Students, Teachers & Admin) -->
    <div id="studentAnimationModal" style="z-index: 9999999 !important; display: none;" class="hidden fixed inset-0 bg-black/90 backdrop-blur-md p-2 sm:p-4 flex flex-col items-center justify-center">
        <div style="height: 92vh; max-height: 95vh; min-height: 540px; display: flex; flex-direction: column;" class="bg-slate-900 border border-slate-700/80 rounded-2xl w-full max-w-6xl overflow-hidden shadow-2xl">
            <!-- Modal Header -->
            <div style="flex-shrink: 0;" class="px-4 py-3 bg-slate-950 border-b border-slate-800 flex items-center justify-between gap-3">
                <div class="flex items-center space-x-2.5 min-w-0">
                    <span class="text-xl">🎬</span>
                    <span id="studentAnimationTitle" class="font-bold text-white text-sm truncate">NCERT Chapter 1 — Real Numbers</span>
                    <span id="studentAnimationBadge" class="hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0">NCERT Reprint 2026-27</span>
                </div>

                <!-- Actions -->
                <div class="flex items-center space-x-2 shrink-0">
                    <a id="studentAnimationFullscreenLink" href="{{ asset('animations/real-numbers.html') }}" target="_blank" class="px-3 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 hover:text-white text-xs border border-slate-700 flex items-center space-x-1 transition-all" title="Open in dedicated tab">
                        <span>Fullscreen ↗</span>
                    </a>
                    <button type="button" onclick="closeStudentAnimationModal()" class="w-8 h-8 rounded-lg bg-slate-800 hover:bg-rose-900/60 text-slate-400 hover:text-rose-200 border border-slate-700 flex items-center justify-center cursor-pointer transition-colors" title="Close">✕</button>
                </div>
            </div>

            <!-- Modal Iframe Body (Bulletproof relative + absolute container) -->
            <div style="flex: 1 1 0%; min-height: 0; position: relative; width: 100%; height: 100%;" class="bg-slate-950 overflow-hidden">
                <iframe id="studentAnimationIframe" src="" style="position: absolute; top: 0; left: 0; width: 100%; height: 100%; border: 0;" class="block" allow="autoplay; speech"></iframe>
            </div>
        </div>
    </div>

    <script>
        function openStudentAnimationModal(type = 'real-numbers') {
            const modal = document.getElementById('studentAnimationModal');
            const iframe = document.getElementById('studentAnimationIframe');
            const title = document.getElementById('studentAnimationTitle');
            const badge = document.getElementById('studentAnimationBadge');
            const fullLink = document.getElementById('studentAnimationFullscreenLink');

            if (modal && iframe) {
                let fileUrl = "{{ asset('animations/real-numbers.html') }}";
                let titleText = "NCERT Chapter 1 — Real Numbers (Fundamental Theorem, Irrationals & Track Simulation)";
                let badgeText = "NCERT Reprint 2026-27 • Class 10";
                let badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";

                if (type === 'probability') {
                    fileUrl = "{{ asset('animations/probability.html') }}";
                    titleText = "NCERT Chapter 14 — Probability Lab (Theoretical Approach, Dice, Cards & Geometry)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30 shrink-0";
                } else if (type === 'statistics') {
                    fileUrl = "{{ asset('animations/statistics.html') }}";
                    titleText = "NCERT Chapter 13 — Statistics Lab (Mean, Median, Mode & Cumulative Frequency)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'surface-areas-and-volumes') {
                    fileUrl = "{{ asset('animations/surface-areas-and-volumes.html') }}";
                    titleText = "NCERT Chapter 12 — Surface Areas and Volumes Lab (Composite Solids & Volumes)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'areas-related-to-circles') {
                    fileUrl = "{{ asset('animations/areas-related-to-circles.html') }}";
                    titleText = "NCERT Chapter 11 — Areas Related to Circles Lab (Sectors & Segments)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'circles') {
                    fileUrl = "{{ asset('animations/circles.html') }}";
                    titleText = "NCERT Chapter 10 — Circles Lab (Tangents, Theorem 10.1 & 10.2)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30 shrink-0";
                } else if (type === 'applications-of-trigonometry') {
                    fileUrl = "{{ asset('animations/applications-of-trigonometry.html') }}";
                    titleText = "NCERT Chapter 9 — Some Applications of Trigonometry Lab (Heights & Distances)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0";
                } else if (type === 'trigonometry') {
                    fileUrl = "{{ asset('animations/trigonometry.html') }}";
                    titleText = "NCERT Chapter 8 — Introduction to Trigonometry Lab (Ratios, Table & Identities)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30 shrink-0";
                } else if (type === 'coordinate-geometry') {
                    fileUrl = "{{ asset('animations/coordinate-geometry.html') }}";
                    titleText = "NCERT Chapter 7 — Coordinate Geometry Lab (Distance & Section Formulas)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'triangles') {
                    fileUrl = "{{ asset('animations/triangles.html') }}";
                    titleText = "NCERT Chapter 6 — Triangles Lab (Similarity, BPT & Shadow Modeling)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";
                } else if (type === 'arithmetic-progressions') {
                    fileUrl = "{{ asset('animations/arithmetic-progressions.html') }}";
                    titleText = "NCERT Chapter 5 — Arithmetic Progressions Lab (nth Term, Sum & Applications)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0";
                } else if (type === 'quadratic-equations') {
                    fileUrl = "{{ asset('animations/quadratic-equations.html') }}";
                    titleText = "NCERT Chapter 4 — Quadratic Equations Lab (Formula, Roots & Discriminant)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 shrink-0";
                } else if (type === 'linear-equations') {
                    fileUrl = "{{ asset('animations/linear-equations.html') }}";
                    titleText = "NCERT Chapter 3 — Pair of Linear Equations in Two Variables Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'polynomials') {
                    fileUrl = "{{ asset('animations/polynomials.html') }}";
                    titleText = "NCERT Chapter 2 — Polynomials (Degrees, Parabolas, Zeroes & Coefficients)";
                    badgeText = "NCERT Reprint 2026-27 • Class 10";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'relations-and-functions') {
                    fileUrl = "{{ asset('animations/relations-and-functions.html') }}";
                    titleText = "NCERT Class 12 Part - 1 — Chapter 1: Relations and Functions Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 1";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'inverse-trigonometric-functions') {
                    fileUrl = "{{ asset('animations/inverse-trigonometric-functions.html') }}";
                    titleText = "NCERT Class 12 Part - 1 — Chapter 2: Inverse Trigonometric Functions Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 1";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'matrices') {
                    fileUrl = "{{ asset('animations/matrices.html') }}";
                    titleText = "NCERT Class 12 Part - 1 — Chapter 3: Matrices Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 1";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'determinants') {
                    fileUrl = "{{ asset('animations/determinants.html') }}";
                    titleText = "NCERT Class 12 Part - 1 — Chapter 4: Determinants Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 1";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-violet-500/20 text-violet-300 border border-violet-500/30 shrink-0";
                } else if (type === 'continuity-and-differentiability') {
                    fileUrl = "{{ asset('animations/continuity-and-differentiability.html') }}";
                    titleText = "NCERT Class 12 Part - 1 — Chapter 5: Continuity and Differentiability Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 1";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-fuchsia-500/20 text-fuchsia-300 border border-fuchsia-500/30 shrink-0";
                } else if (type === 'application-of-derivatives') {
                    fileUrl = "{{ asset('animations/application-of-derivatives.html') }}";
                    titleText = "NCERT Class 12 Part - 1 — Chapter 6: Application of Derivatives Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 1";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30 shrink-0";
                } else if (type === 'integrals') {
                    fileUrl = "{{ asset('animations/integrals.html') }}";
                    titleText = "NCERT Class 12 Part - 2 — Chapter 7: Integrals Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 2";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'application-of-integrals') {
                    fileUrl = "{{ asset('animations/application-of-integrals.html') }}";
                    titleText = "NCERT Class 12 Part - 2 — Chapter 8: Application of Integrals Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 2";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0";
                } else if (type === 'differential-equations') {
                    fileUrl = "{{ asset('animations/differential-equations.html') }}";
                    titleText = "NCERT Class 12 Part - 2 — Chapter 9: Differential Equations Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 2";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'vector-algebra') {
                    fileUrl = "{{ asset('animations/vector-algebra.html') }}";
                    titleText = "NCERT Class 12 Part - 2 — Chapter 10: Vector Algebra Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 2";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30 shrink-0";
                } else if (type === 'three-dimensional-geometry') {
                    fileUrl = "{{ asset('animations/three-dimensional-geometry.html') }}";
                    titleText = "NCERT Class 12 Part - 2 — Chapter 11: Three Dimensional Geometry Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 2";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30 shrink-0";
                } else if (type === 'linear-programming') {
                    fileUrl = "{{ asset('animations/linear-programming.html') }}";
                    titleText = "NCERT Class 12 Part - 2 — Chapter 12: Linear Programming Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 2";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'probability-class12') {
                    fileUrl = "{{ asset('animations/probability-class12.html') }}";
                    titleText = "NCERT Class 12 Part - 2 — Chapter 13: Probability Lab";
                    badgeText = "NCERT Reprint 2026-27 • Class 12 Part - 2";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 shrink-0";
                } else if (type === 'chemical-reactions-and-equations') {
                    fileUrl = "{{ asset('animations/chemical-reactions-and-equations.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 1: Chemical Reactions and Equations Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'acids-bases-and-salts') {
                    fileUrl = "{{ asset('animations/acids-bases-and-salts.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 2: Acids, Bases and Salts Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'metals-and-non-metals') {
                    fileUrl = "{{ asset('animations/metals-and-non-metals.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 3: Metals and Non-metals Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'life-processes') {
                    fileUrl = "{{ asset('animations/life-processes.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 5: Life Processes Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'control-and-coordination') {
                    fileUrl = "{{ asset('animations/control-and-coordination.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 6: Control and Coordination Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'how-do-organisms-reproduce') {
                    fileUrl = "{{ asset('animations/how-do-organisms-reproduce.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 7: How do Organisms Reproduce? Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 shrink-0";
                } else if (type === 'light-reflection-and-refraction' || type === 'chapter09' || type === 'chapter-09' || type === 'chapter9' || type === 'chapter-9') {
                    fileUrl = "{{ asset('animations/light-reflection-and-refraction.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 9: Light - Reflection and Refraction Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'the-human-eye-and-the-colourful-world' || type === 'chapter10' || type === 'chapter-10') {
                    fileUrl = "{{ asset('animations/the-human-eye-and-the-colourful-world.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 10: The Human Eye and the Colourful World Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'electricity' || type === 'chapter11' || type === 'chapter-11') {
                    fileUrl = "{{ asset('animations/electricity.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 11: Electricity Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'magnetic-effects-of-electric-current' || type === 'chapter12' || type === 'chapter-12') {
                    fileUrl = "{{ asset('animations/magnetic-effects-of-electric-current.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 12: Magnetic Effects of Electric Current Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'our-environment' || type === 'chapter13' || type === 'chapter-13') {
                    fileUrl = "{{ asset('animations/our-environment.html') }}";
                    titleText = "NCERT Class 10 Science — Chapter 13: Our Environment Lab";
                    badgeText = "NCERT Class 10 Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'surdas-ke-pad' || type === 'chapter1-hindi' || type === 'hindi-class10-chapter-1') {
                    fileUrl = "{{ asset('animations/surdas-ke-pad.html') }}";
                    titleText = "NCERT Class 10 Hindi (क्षितिज भाग-2) — पाठ 1: सूरदास के पद";
                    badgeText = "NCERT Class 10 Hindi";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'ram-lakshman-parashuram-samvad' || type === 'chapter2-hindi' || type === 'hindi-class10-chapter-2') {
                    fileUrl = "{{ asset('animations/ram-lakshman-parashuram-samvad.html') }}";
                    titleText = "NCERT Class 10 Hindi (क्षितिज भाग-2) — पाठ 2: राम-लक्ष्मण-परशुराम संवाद";
                    badgeText = "NCERT Class 10 Hindi";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'number-system') {
                    fileUrl = "{{ asset('animations/number-system.html') }}";
                    titleText = "Class 9 Mathematics — Number System Multimedia Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-polynomials' || type === 'chapter2-maths-class9' || type === 'algebra-linear-polynomials') {
                    fileUrl = "{{ asset('animations/class9-polynomials.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 2: Polynomials & Linear Functions Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-sequences-progressions' || type === 'chapter3-maths-class9' || type === 'sequences-and-progressions') {
                    fileUrl = "{{ asset('animations/class9-sequences-progressions.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 3: Sequences & Progressions Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-algebraic-identities' || type === 'chapter4-maths-class9' || type === 'algebraic-identities') {
                    fileUrl = "{{ asset('animations/class9-algebraic-identities.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 4: Exploring Algebraic Identities Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-linear-equations' || type === 'chapter5-maths-class9' || type === 'linear-equations-in-two-variables') {
                    fileUrl = "{{ asset('animations/class9-linear-equations.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 5: Linear Equations in Two Variables Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-coordinate-geometry' || type === 'chapter6-maths-class9' || type === 'class9-coord-geom') {
                    fileUrl = "{{ asset('animations/class9-coordinate-geometry.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 6: Coordinate Geometry Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-euclids-geometry' || type === 'chapter7-maths-class9' || type === 'euclids-geometry') {
                    fileUrl = "{{ asset('animations/class9-euclids-geometry.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 7: Introduction to Euclid's Geometry Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-lines-and-angles' || type === 'chapter8-maths-class9' || type === 'lines-and-angles') {
                    fileUrl = "{{ asset('animations/class9-lines-and-angles.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 8: Lines and Angles Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-triangles-congruence' || type === 'chapter9-maths-class9' || type === 'triangles-congruence') {
                    fileUrl = "{{ asset('animations/class9-triangles-congruence.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 9: Triangles: Congruence Theorems Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-quadrilaterals' || type === 'chapter10-maths-class9' || type === 'quadrilaterals-4gons') {
                    fileUrl = "{{ asset('animations/class9-quadrilaterals.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 10: 4-gons (Quadrilaterals) Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-circles' || type === 'chapter11-maths-class9' || type === 'circles-geometry') {
                    fileUrl = "{{ asset('animations/class9-circles.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 11: Circles Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-mensuration' || type === 'chapter12-maths-class9' || type === 'mensuration-area-perimeter') {
                    fileUrl = "{{ asset('animations/class9-mensuration.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 12: Mensuration: Area and Perimeter Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-surface-areas-volumes' || type === 'chapter13-maths-class9' || type === 'surface-areas-volumes-3d') {
                    fileUrl = "{{ asset('animations/class9-surface-areas-volumes.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 13: Mensuration: Surface Area and Volume Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-statistics' || type === 'chapter14-maths-class9' || type === 'statistics-data-analysis') {
                    fileUrl = "{{ asset('animations/class9-statistics.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 14: Statistics Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-probability' || type === 'chapter15-maths-class9' || type === 'probability-intro') {
                    fileUrl = "{{ asset('animations/class9-probability.html') }}";
                    titleText = "NCERT Class 9 Mathematics — Chapter 15: Introduction to Probability Lab";
                    badgeText = "Class 9 • NCERT / CBSE";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class9-cell-fundamental-unit' || type === 'chapter1-science-class9' || type === 'the-fundamental-unit-of-life' || type === 'cell-structure-and-function') {
                    fileUrl = "{{ asset('animations/class9-cell-fundamental-unit.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 1: The Fundamental Unit of Life (Cell) Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class9-tissues' || type === 'chapter2-science-class9' || type === 'tissues' || type === 'plant-and-animal-tissues') {
                    fileUrl = "{{ asset('animations/class9-tissues.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 2: Tissues Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0";
                } else if (type === 'class9-reproduction' || type === 'chapter3-science-class9' || type === 'class9-sexual-asexual-reproduction' || type === 'reproduction-modes-and-health') {
                    fileUrl = "{{ asset('animations/class9-reproduction.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 3: Reproduction Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-rose-500/20 text-rose-300 border border-rose-500/30 shrink-0";
                } else if (type === 'class9-diversity-in-living-organisms' || type === 'chapter4-science-class9' || type === 'diversity-in-living-organisms' || type === 'biological-diversity-and-classification') {
                    fileUrl = "{{ asset('animations/class9-diversity-in-living-organisms.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 4: Diversity in Living Organisms Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class9-exploring-mixtures-and-separation' || type === 'chapter5-science-class9' || type === 'exploring-mixtures-and-their-separation' || type === 'mixtures-and-separation-techniques') {
                    fileUrl = "{{ asset('animations/class9-exploring-mixtures-and-separation.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 5: Exploring Mixtures & Separation Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-structure-of-atom' || type === 'chapter6-science-class9' || type === 'structure-of-an-atom' || type === 'atomic-structure-and-models') {
                    fileUrl = "{{ asset('animations/class9-structure-of-atom.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 6: Structure of an Atom Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'class9-atoms-and-molecules' || type === 'chapter7-science-class9' || type === 'atoms-and-molecules' || type === 'chemical-formulae-and-molecular-mass') {
                    fileUrl = "{{ asset('animations/class9-atoms-and-molecules.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 7: Atoms and Molecules Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-blue-500/20 text-blue-300 border border-blue-500/30 shrink-0";
                } else if (type === 'class9-earth-as-a-system' || type === 'chapter8-science-class9' || type === 'earth-as-a-system' || type === 'energy-matter-and-life') {
                    fileUrl = "{{ asset('animations/class9-earth-as-a-system.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 8: Earth as a System: Energy, Matter & Life Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class9-motion' || type === 'chapter9-science-class9' || type === 'motion' || type === 'kinematics-and-motion') {
                    fileUrl = "{{ asset('animations/class9-motion.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 9: Motion Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class9-force-and-laws-of-motion' || type === 'chapter10-science-class9' || type === 'force-and-laws-of-motion' || type === 'laws-of-motion') {
                    fileUrl = "{{ asset('animations/class9-force-and-laws-of-motion.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 10: Force and Laws of Motion Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'class9-work-energy-simple-machines' || type === 'chapter11-science-class9' || type === 'work-energy-and-simple-machines' || type === 'work-and-energy') {
                    fileUrl = "{{ asset('animations/class9-work-energy-simple-machines.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 11: Work, Energy and Simple Machines Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class9-sound' || type === 'chapter12-science-class9' || type === 'sound' || type === 'sound-waves-and-acoustics') {
                    fileUrl = "{{ asset('animations/class9-sound.html') }}";
                    titleText = "NCERT Class 9 Science — Chapter 12: Sound Master Lab";
                    badgeText = "Class 9 • NCERT / CBSE Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-violet-500/20 text-violet-300 border border-violet-500/30 shrink-0";
                } else if (type === 'class9-english-communication-writing' || type === 'chapter1-english-class9' || type === 'class9-english-writing' || type === 'effective-communication-writing') {
                    fileUrl = "{{ asset('animations/class9-english-communication-writing.html') }}";
                    titleText = "NCERT Class 9 English — Chapter 1: Effective Communication & Writing in Diverse Forms";
                    badgeText = "Class 9 • NCERT / CBSE English";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class8-math-square-and-cube' || type === 'chapter1-math-class8' || type === 'a-square-and-a-cube' || type === 'square-and-a-cube') {
                    fileUrl = "{{ asset('animations/class8-math-square-and-cube.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 1: Exploring Squares and Cubes Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class8-math-linear-polynomials' || type === 'chapter2-math-class8' || type === 'introduction-to-linear-polynomials' || type === 'linear-polynomials-class8') {
                    fileUrl = "{{ asset('animations/class8-math-linear-polynomials.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 2: Fundamentals of Linear Polynomials Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'class8-math-story-of-numbers' || type === 'chapter3-math-class8' || type === 'a-story-of-numbers' || type === 'story-of-numbers-class8') {
                    fileUrl = "{{ asset('animations/class8-math-story-of-numbers.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 3: The Evolution of Number Systems Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class8-math-quadrilaterals' || type === 'chapter4-math-class8' || type === 'quadrilaterals-class8' || type === 'class8-quadrilaterals') {
                    fileUrl = "{{ asset('animations/class8-math-quadrilaterals.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 4: Properties and Types of Quadrilaterals Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class8-math-number-play' || type === 'chapter5-math-class8' || type === 'number-play-class8' || type === 'class8-number-play') {
                    fileUrl = "{{ asset('animations/class8-math-number-play.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 5: Investigating Numbers & Divisibility Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class8-math-distributive-property' || type === 'chapter6-math-class8' || type === 'distributive-property-class8' || type === 'class8-distributive-property') {
                    fileUrl = "{{ asset('animations/class8-math-distributive-property.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 6: The Distributive Property & Algebraic Multiplication Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class8-math-proportional-reasoning' || type === 'chapter7-math-class8' || type === 'proportional-reasoning-class8' || type === 'class8-proportional-reasoning') {
                    fileUrl = "{{ asset('animations/class8-math-proportional-reasoning.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 7: Comparing Quantities (Proportional Reasoning) Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'class8-math-percentages-applications' || type === 'chapter8-math-class8' || type === 'percentages-applications-class8' || type === 'class8-percentages-applications' || type === 'class8-math-percentages' || type === 'percentages-and-applications') {
                    fileUrl = "{{ asset('animations/class8-math-percentages-applications.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 8: Comparing Quantities (Percentages & Applications) Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class8-math-baudhayana-pythagoras' || type === 'chapter9-math-class8' || type === 'baudhayana-pythagoras-class8' || type === 'class8-baudhayana-pythagoras' || type === 'class8-math-pythagoras' || type === 'baudhayana-pythagoras-theorem' || type === 'the-baudhayana-pythagoras-theorem') {
                    fileUrl = "{{ asset('animations/class8-math-baudhayana-pythagoras.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 9: The Baudhāyana-Pythagoras Theorem Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class8-math-proportional-reasoning-2' || type === 'chapter10-math-class8' || type === 'proportional-reasoning-2-class8' || type === 'class8-proportional-reasoning-2' || type === 'class8-math-inverse-proportions' || type === 'inverse-proportions-class8' || type === 'class8-inverse-proportions' || type === 'proportional-reasoning-2') {
                    fileUrl = "{{ asset('animations/class8-math-proportional-reasoning-2.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 10: Advanced Proportional Reasoning & Inverse Variation Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0";
                } else if (type === 'class8-math-geometric-themes-solids' || type === 'chapter11-math-class8' || type === 'geometric-themes-solids-class8' || type === 'class8-geometric-themes-solids' || type === 'class8-math-visualising-solids' || type === 'visualising-solids-class8' || type === 'class8-visualising-solids' || type === 'geometric-themes-class8' || type === 'visualising-solids' || type === 'exploring-geometric-themes') {
                    fileUrl = "{{ asset('animations/class8-math-geometric-themes-solids.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 11: Exploring Geometric Themes (Fractals & Visualising Solids) Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'class8-math-data-handling-dots-lines' || type === 'chapter12-math-class8' || type === 'data-handling-dots-lines-class8' || type === 'class8-data-handling-dots-lines' || type === 'class8-math-data-handling' || type === 'data-handling-class8' || type === 'class8-data-handling' || type === 'tales-by-dots-and-lines' || type === 'data-handling') {
                    fileUrl = "{{ asset('animations/class8-math-data-handling-dots-lines.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 12: Data Handling (Tales by Dots and Lines) Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class8-math-algebra-play' || type === 'chapter13-math-class8' || type === 'algebra-play-class8' || type === 'class8-algebra-play' || type === 'class8-math-algebra' || type === 'algebra-play') {
                    fileUrl = "{{ asset('animations/class8-math-algebra-play.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 13: Algebra Play Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class8-math-area-polygons' || type === 'chapter14-math-class8' || type === 'area-polygons-class8' || type === 'class8-area-polygons' || type === 'class8-math-area' || type === 'area-class8' || type === 'area-polygons' || type === 'area') {
                    fileUrl = "{{ asset('animations/class8-math-area-polygons.html') }}";
                    titleText = "NCERT Class 8 Mathematics — Chapter 14: Area (Polygons & Mensuration) Master Lab";
                    badgeText = "Class 8 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class8-science-microbes-health' || type === 'chapter1-science-class8' || type === 'microbes-and-health-class8' || type === 'class8-microbes-and-health' || type === 'class8-science-microbes' || type === 'microbes-and-health' || type === 'microbes') {
                    fileUrl = "{{ asset('animations/class8-science-microbes-health.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 1: Microbes and Health Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'class8-science-cells-microbes' || type === 'chapter2-science-class8' || type === 'cell-structure-and-functions-class8' || type === 'class8-cell-structure' || type === 'cell-structure-and-functions' || type === 'cells-and-microorganisms-class8' || type === 'class8-cells-microbes' || type === 'cell-structure' || type === 'cells') {
                    fileUrl = "{{ asset('animations/class8-science-cells-microbes.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 2: Cell Structure & Microorganisms Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class8-science-health-disease' || type === 'chapter3-science-class8' || type === 'health-and-disease-class8' || type === 'class8-health-disease' || type === 'class8-science-health' || type === 'health-and-disease' || type === 'health-disease-prevention-class8') {
                    fileUrl = "{{ asset('animations/class8-science-health-disease.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 3: Health, Diseases and Prevention Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0";
                } else if (type === 'class8-science-electric-current' || type === 'chapter4-science-class8' || type === 'electric-current-and-effects-class8' || type === 'class8-electric-current' || type === 'class8-science-electricity' || type === 'electric-current-class8' || type === 'electric-current-and-its-effects') {
                    fileUrl = "{{ asset('animations/class8-science-electric-current.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 4: Electric Current, Magnetism & Cells Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class8-science-force-buoyancy' || type === 'chapter5-science-class8' || type === 'force-and-buoyancy-class8' || type === 'class8-force-buoyancy' || type === 'class8-science-force' || type === 'forces-and-pressure-class8' || type === 'force-and-its-effects') {
                    fileUrl = "{{ asset('animations/class8-science-force-buoyancy.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 5: Force, Types of Forces & Buoyancy Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";
                } else if (type === 'class8-science-pressure-winds' || type === 'chapter6-science-class8' || type === 'pressure-and-winds-class8' || type === 'class8-pressure-winds' || type === 'class8-science-pressure' || type === 'winds-storms-cyclones-class8' || type === 'pressure-winds-and-cyclones') {
                    fileUrl = "{{ asset('animations/class8-science-pressure-winds.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 6: Pressure, Winds, Storms & Cyclones Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";
                } else if (type === 'class8-science-particles-matter' || type === 'chapter7-science-class8' || type === 'particles-and-matter-class8' || type === 'class8-particles-matter' || type === 'class8-science-particles' || type === 'particulate-nature-matter-class8' || type === 'particles-matter-class8') {
                    fileUrl = "{{ asset('animations/class8-science-particles-matter.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 7: Particles and Matter Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";
                } else if (type === 'class8-science-elements-compounds' || type === 'chapter8-science-class8' || type === 'elements-compounds-and-mixtures' || type === 'class8-elements-compounds' || type === 'class8-science-elements' || type === 'pure-substances-and-mixtures' || type === 'elements-compounds-mixtures-class8') {
                    fileUrl = "{{ asset('animations/class8-science-elements-compounds.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 8: Elements, Compounds, and Mixtures Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";
                } else if (type === 'class8-science-solutions-density' || type === 'chapter9-science-class8' || type === 'solutions-solubility-and-density' || type === 'class8-solutions-density' || type === 'class8-science-solutions' || type === 'nature-of-solutions-and-density' || type === 'solutions-and-density-class8') {
                    fileUrl = "{{ asset('animations/class8-science-solutions-density.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 9: Solutions, Solubility, and Density Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";
                } else if (type === 'class8-science-light-optics' || type === 'chapter10-science-class8' || type === 'light-and-optics-class8' || type === 'class8-light-optics' || type === 'class8-science-light' || type === 'reflection-and-refraction-class8' || type === 'spherical-mirrors-and-lenses') {
                    fileUrl = "{{ asset('animations/class8-science-light-optics.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 10: Light and Optics Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class8-science-astronomy-calendars' || type === 'chapter11-science-class8' || type === 'astronomy-and-calendars-class8' || type === 'class8-astronomy-calendars' || type === 'class8-science-astronomy' || type === 'phases-of-the-moon-and-calendars' || type === 'moon-phases-and-satellites') {
                    fileUrl = "{{ asset('animations/class8-science-astronomy-calendars.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 11: Astronomy and Calendars Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class8-science-nature-harmony' || type === 'chapter12-science-class8' || type === 'how-nature-works-in-harmony' || type === 'class8-nature-harmony' || type === 'class8-science-ecosystems' || type === 'nature-works-in-harmony-class8' || type === 'ecosystems-and-communities') {
                    fileUrl = "{{ asset('animations/class8-science-nature-harmony.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 12: How Nature Works in Harmony Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class8-science-earth-life-planet' || type === 'chapter13-science-class8' || type === 'earth-unique-life-sustaining-planet' || type === 'class8-earth-life-planet' || type === 'class8-science-earth-planet' || type === 'our-home-earth-unique-planet' || type === 'earth-life-sustaining-planet') {
                    fileUrl = "{{ asset('animations/class8-science-earth-life-planet.html') }}";
                    titleText = "NCERT Class 8 Science — Chapter 13: Our Home: Earth, a Unique Life Sustaining Planet Master Lab";
                    badgeText = "Class 8 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";
                } else if (type === 'class7-math-large-numbers' || type === 'chapter1-math-class7' || type === 'large-numbers-around-us' || type === 'class7-large-numbers' || type === 'class7-math-large-numbers-around-us' || type === 'numbers-around-us-class7' || type === 'large-numbers-class7') {
                    fileUrl = "{{ asset('animations/class7-math-large-numbers.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 1: Large Numbers Around Us Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class7-math-arithmetic-expressions' || type === 'chapter2-math-class7' || type === 'arithmetic-expressions' || type === 'class7-arithmetic-expressions' || type === 'class7-math-expressions' || type === 'expressions-class7' || type === 'arithmetic-expressions-class7') {
                    fileUrl = "{{ asset('animations/class7-math-arithmetic-expressions.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 2: Arithmetic Expressions Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";
                } else if (type === 'class7-math-decimals' || type === 'chapter3-math-class7' || type === 'a-peek-beyond-the-point' || type === 'class7-a-peek-beyond-the-point' || type === 'class7-math-peek-beyond-the-point' || type === 'decimals-class7' || type === 'class7-decimals') {
                    fileUrl = "{{ asset('animations/class7-math-decimals.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 3: A Peek Beyond the Point (Decimals) Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'class7-math-expressions-letter-numbers' || type === 'chapter4-math-class7' || type === 'expressions-using-letter-numbers' || type === 'class7-expressions-letter-numbers' || type === 'letter-numbers-class7' || type === 'class7-math-algebraic-expressions' || type === 'using-letter-numbers-class7') {
                    fileUrl = "{{ asset('animations/class7-math-expressions-letter-numbers.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 4: Expressions Using Letter-Numbers Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class7-math-parallel-intersecting-lines' || type === 'chapter5-math-class7' || type === 'parallel-and-intersecting-lines' || type === 'class7-parallel-intersecting-lines' || type === 'parallel-lines-class7' || type === 'class7-math-lines-angles' || type === 'intersecting-lines-class7') {
                    fileUrl = "{{ asset('animations/class7-math-parallel-intersecting-lines.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 5: Parallel and Intersecting Lines Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";
                } else if (type === 'class7-math-number-play' || type === 'chapter6-math-class7' || type === 'number-play' || type === 'class7-number-play' || type === 'number-play-class7' || type === 'class7-math-playing-with-numbers' || type === 'playing-with-numbers-class7') {
                    fileUrl = "{{ asset('animations/class7-math-number-play.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 6: Number Play Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-purple-500/20 text-purple-300 border border-purple-500/30 shrink-0";
                } else if (type === 'class7-math-tale-of-three-intersecting-lines' || type === 'chapter7-math-class7' || type === 'tale-of-three-intersecting-lines' || type === 'class7-tale-of-three-intersecting-lines' || type === 'tale-of-three-lines-class7' || type === 'class7-math-triangles' || type === 'triangles-class7' || type === 'class7-triangles') {
                    fileUrl = "{{ asset('animations/class7-math-tale-of-three-intersecting-lines.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 7: A Tale of Three Intersecting Lines Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class7-math-working-with-fractions' || type === 'chapter8-math-class7' || type === 'working-with-fractions' || type === 'class7-working-with-fractions' || type === 'working-with-fractions-class7' || type === 'class7-math-fractions' || type === 'fractions-class7' || type === 'class7-fractions') {
                    fileUrl = "{{ asset('animations/class7-math-working-with-fractions.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 8: Working with Fractions Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";
                } else if (type === 'class7-math-geometric-twins' || type === 'chapter9-math-class7' || type === 'geometric-twins' || type === 'class7-geometric-twins' || type === 'geometric-twins-class7' || type === 'class7-math-congruence' || type === 'congruence-class7' || type === 'class7-congruence') {
                    fileUrl = "{{ asset('animations/class7-math-geometric-twins.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 9: Geometric Twins (Congruence) Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-indigo-500/20 text-indigo-300 border border-indigo-500/30 shrink-0";
                } else if (type === 'class7-math-operations-with-integers' || type === 'chapter10-math-class7' || type === 'operations-with-integers' || type === 'class7-operations-with-integers' || type === 'operations-with-integers-class7' || type === 'class7-math-integers' || type === 'integers-class7' || type === 'class7-integers') {
                    fileUrl = "{{ asset('animations/class7-math-operations-with-integers.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 10: Operations with Integers Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-cyan-500/20 text-cyan-300 border border-cyan-500/30 shrink-0";
                } else if (type === 'class7-math-finding-common-ground' || type === 'chapter11-math-class7' || type === 'finding-common-ground' || type === 'class7-finding-common-ground' || type === 'finding-common-ground-class7' || type === 'class7-math-hcf-lcm' || type === 'hcf-lcm-class7' || type === 'class7-hcf-lcm') {
                    fileUrl = "{{ asset('animations/class7-math-finding-common-ground.html') }}";
                    titleText = "NCERT Class 7 Mathematics — Chapter 11: Finding Common Ground (HCF & LCM) Master Lab";
                    badgeText = "Class 7 • NCERT Mathematics";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-teal-500/20 text-teal-300 border border-teal-500/30 shrink-0";
                }

                if (iframe.src !== fileUrl) {
                    iframe.src = fileUrl;
                }
                if (fullLink) fullLink.href = fileUrl;
                if (title) title.textContent = titleText;
                if (badge) {
                    badge.textContent = badgeText;
                    badge.className = badgeClass;
                }

                modal.classList.remove('hidden');
                modal.style.display = 'flex';
                document.body.style.overflow = 'hidden';
            }
        }

        function closeStudentAnimationModal() {
            const modal = document.getElementById('studentAnimationModal');
            const iframe = document.getElementById('studentAnimationIframe');
            if (modal) {
                modal.classList.add('hidden');
                modal.style.display = 'none';
            }
            if (iframe) {
                iframe.src = "";
            }
            document.body.style.overflow = '';
        }

        // Close on Escape key
        document.addEventListener('keydown', function(e) {
            if (e.key === 'Escape') {
                const modal = document.getElementById('studentAnimationModal');
                if (modal && modal.style.display === 'flex') {
                    closeStudentAnimationModal();
                }
            }
        });
    </script>
</body>
</html>
