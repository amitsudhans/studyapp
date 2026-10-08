<x-layouts.app title="Create Account - Study App">
    <div class="min-h-[calc(100vh-8rem)] flex flex-col justify-center py-12 sm:px-6 lg:px-8">
        <div class="sm:mx-auto sm:w-full sm:max-w-md text-center">
            <div class="mx-auto w-14 h-14 rounded-2xl bg-gradient-to-tr from-indigo-600 via-indigo-500 to-violet-500 flex items-center justify-center shadow-xl shadow-indigo-500/20 mb-4">
                <svg class="w-8 h-8 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                    <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M18 9v3m0 0v3m0-3h3m-3 0h-3m-2-5a4 4 0 11-8 0 4 4 0 018 0zM3 20a6 6 0 0112 0v1H3v-1z" />
                </svg>
            </div>
            <h2 class="text-3xl font-extrabold text-white tracking-tight">Create your account</h2>
            <p class="mt-2 text-sm text-slate-400">
                Join now to access your dashboard
            </p>
        </div>

        <div class="mt-8 sm:mx-auto sm:w-full sm:max-w-md">
            <div class="bg-slate-900 border border-slate-800 py-8 px-6 shadow-2xl rounded-2xl sm:px-10">
                <form method="POST" action="{{ route('register') }}" class="space-y-6">
                    @csrf

                    <!-- Name -->
                    <div>
                        <label for="name" class="block text-sm font-medium text-slate-200">Full Name</label>
                        <div class="mt-2 relative rounded-lg shadow-sm">
                            <input id="name" 
                                   name="name" 
                                   type="text" 
                                   autocomplete="name" 
                                   required 
                                   value="{{ old('name') }}"
                                   placeholder="John Doe"
                                   class="block w-full px-4 py-3 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-sm transition-all @error('name') border-red-500 focus:ring-red-500 focus:border-red-500 @enderror">
                        </div>
                        @error('name')
                            <p class="mt-2 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

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
                            <p class="mt-2 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <!-- Password -->
                    <div>
                        <label for="password" class="block text-sm font-medium text-slate-200">Password</label>
                        <div class="mt-2 relative rounded-lg shadow-sm">
                            <input id="password" 
                                   name="password" 
                                   type="password" 
                                   autocomplete="new-password" 
                                   required 
                                   placeholder="Minimum 8 characters"
                                   class="block w-full px-4 py-3 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-sm transition-all @error('password') border-red-500 focus:ring-red-500 focus:border-red-500 @enderror">
                        </div>
                        @error('password')
                            <p class="mt-2 text-xs text-red-400">{{ $message }}</p>
                        @enderror
                    </div>

                    <!-- Confirm Password -->
                    <div>
                        <label for="password_confirmation" class="block text-sm font-medium text-slate-200">Confirm Password</label>
                        <div class="mt-2 relative rounded-lg shadow-sm">
                            <input id="password_confirmation" 
                                   name="password_confirmation" 
                                   type="password" 
                                   autocomplete="new-password" 
                                   required 
                                   placeholder="Repeat password"
                                   class="block w-full px-4 py-3 rounded-lg bg-slate-950 border border-slate-700 text-slate-100 placeholder-slate-500 focus:outline-none focus:ring-2 focus:ring-indigo-500 focus:border-indigo-500 text-sm transition-all">
                        </div>
                    </div>

                    <!-- Submit Button -->
                    <div>
                        <button type="submit" 
                                class="w-full flex justify-center py-3 px-4 border border-transparent rounded-lg shadow-lg text-sm font-semibold text-white bg-indigo-600 hover:bg-indigo-500 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500 focus:ring-offset-slate-900 transition-all duration-150 cursor-pointer">
                            Create Account
                        </button>
                    </div>
                </form>

                <!-- Footer link -->
                <div class="mt-6 text-center text-sm border-t border-slate-800 pt-6">
                    <span class="text-slate-400">Already have an account?</span>
                    <a href="{{ route('login') }}" class="font-medium text-indigo-400 hover:text-indigo-300 transition-colors ml-1">
                        Sign in instead
                    </a>
                </div>
            </div>
        </div>
    </div>
</x-layouts.app>
