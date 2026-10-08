<!DOCTYPE html>
<html lang="{{ str_replace('_', '-', app()->getLocale()) }}" class="h-full bg-slate-900 text-slate-100">
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
        <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8">
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
                        <div class="hidden sm:flex items-center space-x-1 border-l border-slate-800 pl-6">
                            <a href="{{ route('dashboard') }}" class="px-3 py-2 rounded-lg text-sm font-medium {{ Route::is('dashboard') ? 'bg-indigo-600/20 text-indigo-400 border border-indigo-500/30' : 'text-slate-300 hover:text-white hover:bg-slate-800' }} transition-colors">
                                Dashboard
                            </a>
                            <a href="{{ route('questions.index') }}" class="px-3 py-2 rounded-lg text-sm font-medium {{ Route::is('questions.*') ? 'bg-indigo-600/20 text-indigo-400 border border-indigo-500/30' : 'text-slate-300 hover:text-white hover:bg-slate-800' }} transition-colors">
                                Questions
                            </a>
                        </div>
                    @endauth
                </div>

                <div class="flex items-center space-x-4">
                    @auth
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
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M17 16l4-4m0 0l-4-4m4 4H7m6 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h4a3 3 0 013 3v1" />
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
            <div class="max-w-7xl mx-auto px-4 sm:px-6 lg:px-8 mt-4">
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
    @endauth

    <!-- Footer -->
    <footer class="border-t border-slate-800/60 py-6 text-center text-xs text-slate-500 mb-12 sm:mb-0">
        <p>&copy; {{ date('Y') }} {{ config('app.name', 'Laravel') }}. All rights reserved.</p>
    </footer>
</body>
</html>
