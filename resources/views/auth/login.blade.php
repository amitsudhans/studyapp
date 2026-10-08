<x-layouts.app title="Sign In - Study App">
    <div class="min-h-[calc(100vh-8rem)] flex flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md text-center">
            <div class="mx-auto w-14 h-14 rounded-2xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-violet-500 flex items-center justify-center shadow-xl shadow-indigo-500/20 mb-4">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M11 16l-4-4m0 0l4-4m-4 4h14m-5 4v1a3 3 0 01-3 3H6a3 3 0 01-3-3V7a3 3 0 013-3h7a3 3 0 013 3v1" />
                </svg>
            </div>
            <h2 class="text-3xl font-extrabold text-white tracking-tight">Sign in to your account</h2>
            <p class="mt-2 text-sm text-slate-400">
                Enter your email address and password to access your dashboard
            </p>
        </div>

        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
            <div class="bg-slate-900 border border-slate-800 py-8 px-6 shadow-2xl rounded-2xl sm:px-10">
                <form method="POST" action="{{ route('login') }}" class="space-y-6">
                    @csrf

                    <!-- Email Address -->
                    <div>
                        <label for="email" class="block text-sm font-medium text-slate-200">Email Address</label>
                        <div class="mt-2 relative rounded-lg shadow-sm">
                            <input id="email" 
                                   name="email" 
                                   type="email" 
                                   autocomplete="email" 
                                   required 
                                   value="{{ old('email') }}"
                                   placeholder="name@example.com"
                                   class="block w-full px-4 py-3 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-sm transition-all @error('email') border-red-500 focus:ring-red-500 focus:border-red-500 @enderror">
                        </div>
                        @error('email')
                            <p class="mt-2 text-xs text-red-400 flex items-center space-x-1">
                                <svg class="w-4 h-4 inline shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <span>{{ $message }}</span>
                            </p>
                        @enderror
                    </div>

                    <!-- Password -->
                    <div>
                        <div class="flex items-center justify-between">
                            <label for="password" class="block text-sm font-medium text-slate-200">Password</label>
                        </div>
                        <div class="mt-2 relative rounded-lg shadow-sm">
                            <input id="password" 
                                   name="password" 
                                   type="password" 
                                   autocomplete="current-password" 
                                   required 
                                   placeholder="••••••••"
                                   class="block w-full px-4 py-3 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-sm transition-all @error('password') border-red-500 focus:ring-red-500 focus:border-red-500 @enderror">
                        </div>
                        @error('password')
                            <p class="mt-2 text-xs text-red-400 flex items-center space-x-1">
                                <svg class="w-4 h-4 inline shrink-0" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 8v4m0 4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z" />
                                </svg>
                                <span>{{ $message }}</span>
                            </p>
                        @enderror
                    </div>

                    <!-- Remember Me -->
                    <div class="flex items-center justify-between">
                        <div class="flex items-center">
                            <input id="remember" 
                                   name="remember" 
                                   type="checkbox" 
                                   class="h-4 w-4 rounded bg-slate-950 border-slate-700 text-indigo-600 focus:ring-indigo-500 focus:ring-offset-slate-900">
                            <label for="remember" class="ml-2 block text-sm text-slate-300">
                                Remember me
                            </label>
                        </div>
                    </div>

                    <!-- Submit Button -->
                    <div>
                        <button type="submit" 
                                class="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-lg text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 focus:ring-offset-slate-900 transition-all duration-150 cursor-pointer">
                            Sign In
                        </button>
                    </div>
                </form>

                <!-- Footer link -->
                <div class="mt-6 text-center text-sm border-t border-slate-800 pt-6">
                    <span class="text-slate-400">Don't have an account?</span>
                    <a href="{{ route('register') }}" class="font-medium text-indigo-400 hover:text-indigo-300 transition-colors ml-1">
                        Register here
                    </a>
                </div>
            </div>

            <!-- Demo Credentials Helper -->
            <div class="mt-6 p-4 rounded-xl bg-slate-900/50 border border-slate-800 text-center text-xs text-slate-400">
                <p class="font-medium text-slate-300 mb-1">Default Test User:</p>
                <p>Email: <code class="text-indigo-300">test@example.com</code> | Password: <code class="text-indigo-300">password</code></p>
            </div>
        </div>
    </div>
</x-layouts.app>
