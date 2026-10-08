// Service Worker Registration & PWA Install Banner Script
(function () {
    if (!('serviceWorker' in navigator)) return;

    // Register Service Worker
    window.addEventListener('load', () => {
        navigator.serviceWorker.register('/sw.js')
            .then((registration) => {
                console.log('[PWA] ServiceWorker registered with scope:', registration.scope);
            })
            .catch((error) => {
                console.error('[PWA] ServiceWorker registration failed:', error);
            });
    });

    let deferredPrompt = null;

    // Listen for install prompt trigger
    window.addEventListener('beforeinstallprompt', (e) => {
        e.preventDefault();
        deferredPrompt = e;

        // Don't show if user previously dismissed prompt in last 24 hours
        const lastDismissed = localStorage.getItem('pwa_banner_dismissed');
        if (lastDismissed && Date.now() - parseInt(lastDismissed) < 86400000) {
            return;
        }

        showInstallBanner();
    });

    function showInstallBanner() {
        if (document.getElementById('pwa-install-banner')) return;

        const banner = document.createElement('div');
        banner.id = 'pwa-install-banner';
        banner.className = 'fixed bottom-4 left-4 right-4 sm:left-auto sm:right-6 sm:max-w-md z-[100] p-4 bg-slate-900/95 border border-indigo-500/40 rounded-2xl shadow-2xl backdrop-blur-xl transition-all duration-300 flex items-center justify-between space-x-4 animate-bounce-short text-slate-100';

        banner.innerHTML = `
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-xl bg-gradient-to-tr from-indigo-600 to-violet-500 flex items-center justify-center shrink-0 shadow-md shadow-indigo-500/30">
                    <svg class="w-5 h-5 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 10V3L4 14h7v7l9-11h-7z" />
                    </svg>
                </div>
                <div>
                    <h4 class="text-sm font-bold text-white tracking-tight">Install Study App</h4>
                    <p class="text-xs text-slate-400">Get fast, offline access on your home screen!</p>
                </div>
            </div>
            <div class="flex items-center space-x-2 shrink-0">
                <button id="pwa-install-btn" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 active:scale-95 text-white text-xs font-semibold rounded-lg shadow-md transition-all">
                    Install
                </button>
                <button id="pwa-dismiss-btn" class="p-1.5 text-slate-400 hover:text-slate-200 rounded-lg hover:bg-slate-800 transition-colors">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24">
                        <path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12" />
                    </svg>
                </button>
            </div>
        `;

        document.body.appendChild(banner);

        document.getElementById('pwa-install-btn')?.addEventListener('click', async () => {
            if (!deferredPrompt) return;
            deferredPrompt.prompt();
            const { outcome } = await deferredPrompt.userChoice;
            console.log(`[PWA] User response to install prompt: ${outcome}`);
            deferredPrompt = null;
            banner.remove();
        });

        document.getElementById('pwa-dismiss-btn')?.addEventListener('click', () => {
            localStorage.setItem('pwa_banner_dismissed', Date.now().toString());
            banner.remove();
        });
    }

    // App installed handler
    window.addEventListener('appinstalled', () => {
        console.log('[PWA] Study App was installed successfully');
        const banner = document.getElementById('pwa-install-banner');
        if (banner) banner.remove();
    });
})();
