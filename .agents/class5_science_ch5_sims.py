"""
16 Bespoke SVG/HTML Interactive Simulators for NCERT Class 5 Science Chapter 5: Our Vibrant Country
Zero raw LaTeX! Clean Unicode symbols.
"""

SIMULATORS = {
    1: """
        <!-- Sim 1: Republic Day Parade & Flag Unfurling -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-orange-400 uppercase tracking-wider block mb-1">Tiranga Flagpole & Flower Shower</span>
                <p class="text-[11px] text-slate-400">Pull the halyard cord to hoist and unfurl the tricolour flag, showering rose petals!</p>
            </div>
            <div class="relative h-56 bg-gradient-to-b from-sky-900/40 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden flex items-center justify-center p-2">
                <svg viewBox="0 0 400 240" class="w-full h-full">
                    <!-- Base & Ground -->
                    <rect x="0" y="215" width="400" height="25" fill="#1e293b"/>
                    <rect x="160" y="200" width="80" height="15" rx="3" fill="#334155"/>
                    <rect x="175" y="190" width="50" height="10" rx="2" fill="#475569"/>

                    <!-- Flagpole -->
                    <line x1="200" y1="20" x2="200" y2="190" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
                    <circle cx="200" cy="18" r="5" fill="#f59e0b"/>

                    <!-- Halyard Cord -->
                    <line x1="198" y1="22" x2="190" y2="185" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="3,2"/>
                    <line x1="202" y1="22" x2="210" y2="185" stroke="#cbd5e1" stroke-width="1.2" stroke-dasharray="3,2"/>

                    <!-- Flag Group (moves up when hoisted) -->
                    <g id="flagGroup" transform="translate(202, 120)">
                        <!-- Saffron Band -->
                        <path d="M 0,0 Q 25,-4 50,0 Q 75,4 100,0 L 100,16 Q 75,20 50,16 Q 25,12 0,16 Z" fill="#ff9933"/>
                        <!-- White Band -->
                        <path d="M 0,16 Q 25,12 50,16 Q 75,20 100,16 L 100,32 Q 75,36 50,32 Q 25,28 0,32 Z" fill="#ffffff"/>
                        <!-- Green Band -->
                        <path d="M 0,32 Q 25,28 50,32 Q 75,36 100,32 L 100,48 Q 75,52 50,48 Q 25,44 0,48 Z" fill="#138808"/>
                        <!-- Ashoka Chakra -->
                        <circle cx="50" cy="24" r="6.5" fill="none" stroke="#000080" stroke-width="1"/>
                        <circle cx="50" cy="24" r="1.5" fill="#000080"/>
                        <!-- 8 Major Spokes Representation -->
                        <line x1="50" y1="17.5" x2="50" y2="30.5" stroke="#000080" stroke-width="0.8"/>
                        <line x1="43.5" y1="24" x2="56.5" y2="24" stroke="#000080" stroke-width="0.8"/>
                        <line x1="45.5" y1="19.5" x2="54.5" y2="28.5" stroke="#000080" stroke-width="0.8"/>
                        <line x1="45.5" y1="28.5" x2="54.5" y2="19.5" stroke="#000080" stroke-width="0.8"/>
                    </g>

                    <!-- Falling Petals (hidden until unfurled) -->
                    <g id="petalShower" class="hidden">
                        <circle cx="210" cy="40" r="3" fill="#f43f5e" opacity="0.9"/>
                        <circle cx="225" cy="55" r="2.5" fill="#fb7185" opacity="0.8"/>
                        <circle cx="240" cy="35" r="3" fill="#e11d48" opacity="0.9"/>
                        <circle cx="255" cy="65" r="2" fill="#f43f5e" opacity="0.7"/>
                        <circle cx="220" cy="75" r="3" fill="#fb7185" opacity="0.85"/>
                        <circle cx="270" cy="50" r="2.5" fill="#fda4af" opacity="0.9"/>
                        <circle cx="235" cy="90" r="2" fill="#f43f5e" opacity="0.8"/>
                    </g>
                </svg>
            </div>
            <div class="flex items-center space-x-2">
                <button onclick="hoistFlag()" id="hoistBtn" class="flex-1 py-2 rounded-xl text-xs font-bold bg-orange-600 hover:bg-orange-500 text-white transition flex items-center justify-center space-x-1.5">
                    <span>🚩</span>
                    <span>Hoist Flag</span>
                </button>
                <button onclick="unfurlFlag()" id="unfurlBtn" class="flex-1 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition flex items-center justify-center space-x-1.5">
                    <span>🌸</span>
                    <span>Unfurl Petals</span>
                </button>
            </div>
            <div id="flagStatusText" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-center text-xs text-slate-300">
                Flag is currently positioned at the base. Click <strong>Hoist Flag</strong>.
            </div>
        </div>
    """,

    2: """
        <!-- Sim 2: Constitution Timeline & Preamble Explorer -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-indigo-400 uppercase tracking-wider block mb-1">Foundational Pillars of the Constitution</span>
                <p class="text-[11px] text-slate-400">Click on any supreme constitutional value to explore its democratic guarantee:</p>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <button onclick="selectPreambleWord('justice')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-indigo-950/60 border border-slate-800 hover:border-indigo-500/50 text-left transition">
                    <span class="text-xs font-bold text-indigo-400 block">⚖️ JUSTICE</span>
                    <span class="text-[10px] text-slate-400">Social, Economic, Political</span>
                </button>
                <button onclick="selectPreambleWord('liberty')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-indigo-950/60 border border-slate-800 hover:border-indigo-500/50 text-left transition">
                    <span class="text-xs font-bold text-sky-400 block">🕊️ LIBERTY</span>
                    <span class="text-[10px] text-slate-400">Thought, Expression, Belief</span>
                </button>
                <button onclick="selectPreambleWord('equality')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-indigo-950/60 border border-slate-800 hover:border-indigo-500/50 text-left transition">
                    <span class="text-xs font-bold text-emerald-400 block">🤝 EQUALITY</span>
                    <span class="text-[10px] text-slate-400">Status and Opportunity</span>
                </button>
                <button onclick="selectPreambleWord('fraternity')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-indigo-950/60 border border-slate-800 hover:border-indigo-500/50 text-left transition">
                    <span class="text-xs font-bold text-amber-400 block">🌺 FRATERNITY</span>
                    <span class="text-[10px] text-slate-400">Dignity and National Unity</span>
                </button>
            </div>
            <div id="preambleDetails" class="p-3.5 rounded-xl bg-indigo-950/40 border border-indigo-500/30 text-xs text-slate-200 leading-relaxed">
                <strong class="text-indigo-300 block mb-1">Preamble Essence:</strong>
                Select a pillar above to discover how Dr. Ambedkar and the Drafting Committee framed the rights of every citizen!
            </div>
        </div>
    """,

    3: """
        <!-- Sim 3: Currency Note Detective (Micro-Scanner) -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Banknote Micro-Inspector (₹500 / ₹10)</span>
                <p class="text-[11px] text-slate-400">Switch sensor zones to detect hidden security features on Indian currency:</p>
            </div>
            <div class="relative h-44 bg-slate-900 rounded-xl border border-slate-800 p-2 overflow-hidden flex items-center justify-center">
                <svg viewBox="0 0 360 170" class="w-full h-full">
                    <!-- Banknote Body -->
                    <rect x="20" y="15" width="320" height="140" rx="8" fill="#334155" stroke="#64748b" stroke-width="2"/>
                    <!-- Border pattern -->
                    <rect x="26" y="21" width="308" height="128" rx="5" fill="#1e293b" stroke="#475569" stroke-dasharray="3,3"/>

                    <!-- Watermark Window (Left) -->
                    <rect id="noteWatermarkBox" x="35" y="30" width="70" height="110" rx="4" fill="#0f172a" stroke="#334155"/>
                    <g id="gandhiWatermark" opacity="0.15">
                        <ellipse cx="70" cy="75" rx="18" ry="24" fill="#cbd5e1"/>
                        <circle cx="65" cy="72" r="5" fill="none" stroke="#475569" stroke-width="1"/>
                        <circle cx="75" cy="72" r="5" fill="none" stroke="#475569" stroke-width="1"/>
                        <path d="M 60,88 Q 70,95 80,88" stroke="#475569" stroke-width="1.5" fill="none"/>
                    </g>

                    <!-- Security Thread (Centre-Left) -->
                    <line id="securityThread" x1="120" y1="15" x2="120" y2="155" stroke="#10b981" stroke-width="3" stroke-dasharray="8,4"/>

                    <!-- Mahatma Gandhi Portrait (Centre-Right) -->
                    <rect x="195" y="35" width="60" height="85" rx="4" fill="#334155"/>
                    <ellipse cx="225" cy="70" rx="16" ry="22" fill="#cbd5e1"/>
                    <circle cx="220" cy="68" r="5" fill="none" stroke="#0f172a" stroke-width="1.5"/>
                    <circle cx="230" cy="68" r="5" fill="none" stroke="#0f172a" stroke-width="1.5"/>
                    <text x="212" y="105" fill="#f8fafc" font-size="9" font-weight="bold">GANDHI</text>

                    <!-- Denomination Stamp -->
                    <text x="270" y="55" fill="#f59e0b" font-size="22" font-weight="extrabold">₹500</text>

                    <!-- Swachh Bharat Spectacles (Bottom Left) -->
                    <g id="spectaclesLogo" transform="translate(138, 120)">
                        <circle cx="8" cy="8" r="6" fill="none" stroke="#e2e8f0" stroke-width="1.2"/>
                        <circle cx="24" cy="8" r="6" fill="none" stroke="#e2e8f0" stroke-width="1.2"/>
                        <line x1="14" y1="8" x2="18" y2="8" stroke="#e2e8f0" stroke-width="1.2"/>
                        <text x="4" y="10" fill="#94a3b8" font-size="4" font-weight="bold">स्वच्छ</text>
                        <text x="20" y="10" fill="#94a3b8" font-size="4" font-weight="bold">भारत</text>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-3 gap-2">
                <button onclick="scanCurrencyFeature('watermark')" class="py-2 px-1 text-center rounded-xl bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-amber-400 border border-slate-800">
                    💡 Watermark
                </button>
                <button onclick="scanCurrencyFeature('thread')" class="py-2 px-1 text-center rounded-xl bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-emerald-400 border border-slate-800">
                    🟢 Shift Thread
                </button>
                <button onclick="scanCurrencyFeature('swachh')" class="py-2 px-1 text-center rounded-xl bg-slate-900 hover:bg-slate-800 text-[11px] font-bold text-sky-400 border border-slate-800">
                    👓 Swachh Bharat
                </button>
            </div>
            <div id="currencyScanResult" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300">
                Click a detector button above to reveal the scientific security engineering!
            </div>
        </div>
    """,

    4: """
        <!-- Sim 4: Accessibility & Tactile Feature Tester -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Fingertip Tactile Reader & MANI App</span>
                <p class="text-[11px] text-slate-400">Select a note denomination to inspect its raised bleed lines and test MANI voice identification:</p>
            </div>
            <div class="grid grid-cols-3 gap-2">
                <button onclick="setAccessibilityNote(100)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-bold text-slate-200 text-center">
                    ₹100 Note
                </button>
                <button onclick="setAccessibilityNote(200)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-bold text-slate-200 text-center">
                    ₹200 Note
                </button>
                <button onclick="setAccessibilityNote(500)" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-bold text-emerald-400 border-emerald-500/40 text-center">
                    ₹500 Note
                </button>
            </div>
            <div id="tactileNoteDisplay" class="p-4 rounded-xl bg-slate-900 border border-slate-800 space-y-2 text-xs">
                <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                    <span class="font-bold text-white text-sm" id="tactileNoteTitle">₹500 Banknote</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300" id="tactileShapeBadge">Circle Symbol</span>
                </div>
                <div class="flex items-center space-x-3 text-slate-300">
                    <div class="w-12 h-12 rounded-lg bg-slate-950 border border-slate-700 flex items-center justify-center text-xl" id="tactileIcon">
                        🖐️
                    </div>
                    <div class="space-y-1 text-[11px]" id="tactileDesc">
                        <p><strong>Raised Bleed Lines:</strong> 5 diagonal lines on both left and right edges.</p>
                        <p><strong>Identification Shape:</strong> Raised circle above the Ashoka Pillar emblem.</p>
                    </div>
                </div>
            </div>
            <button onclick="triggerMANIVoice()" class="w-full py-2.5 rounded-xl bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs transition flex items-center justify-center space-x-2">
                <span>🔊</span>
                <span>Trigger RBI MANI Voice Announcement</span>
            </button>
            <div id="maniAudioOutput" class="hidden p-2 rounded-lg bg-emerald-950/40 border border-emerald-500/30 text-center text-xs text-emerald-300"></div>
        </div>
    """,

    5: """
        <!-- Sim 5: National Emblem 3D-Style Capital -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">State Emblem of India & Gir Lion Recovery</span>
                <p class="text-[11px] text-slate-400">Rotate the Sarnath Lion Capital and check Asiatic Lion conservation in Gir Forest:</p>
            </div>
            <div class="relative h-48 bg-slate-900 rounded-xl border border-slate-800 p-2 flex items-center justify-center overflow-hidden">
                <svg viewBox="0 0 280 180" class="w-full h-full">
                    <!-- Base Pedestal -->
                    <rect x="70" y="145" width="140" height="20" rx="3" fill="#475569"/>
                    <text x="140" y="159" text-anchor="middle" fill="#f8fafc" font-size="11" font-weight="extrabold">सत्यमेव जयते</text>

                    <!-- Circular Abacus -->
                    <rect x="80" y="115" width="120" height="30" rx="4" fill="#334155"/>
                    <!-- Ashoka Chakra on Abacus -->
                    <circle cx="140" cy="130" r="10" fill="none" stroke="#000080" stroke-width="1.5"/>
                    <circle cx="140" cy="130" r="2" fill="#000080"/>
                    <!-- Galloping Horse (Left) -->
                    <path d="M 95,130 Q 100,123 108,128 Q 112,133 118,130" stroke="#cbd5e1" stroke-width="2" fill="none"/>
                    <text x="96" y="142" fill="#94a3b8" font-size="8">Horse</text>
                    <!-- Humped Bull (Right) -->
                    <path d="M 165,130 Q 170,124 176,126 Q 182,132 188,129" stroke="#cbd5e1" stroke-width="2" fill="none"/>
                    <text x="170" y="142" fill="#94a3b8" font-size="8">Bull</text>

                    <!-- 3 Visible Asiatic Lions (Stylized) -->
                    <!-- Left Lion -->
                    <g transform="translate(85, 35)">
                        <ellipse cx="20" cy="30" rx="14" ry="22" fill="#f59e0b"/>
                        <circle cx="20" cy="15" r="10" fill="#d97706"/>
                        <circle cx="16" cy="14" r="1.5" fill="#0f172a"/>
                        <path d="M 10,25 Q 20,40 30,25" fill="#b45309"/>
                    </g>
                    <!-- Central Lion -->
                    <g transform="translate(120, 25)">
                        <ellipse cx="20" cy="35" rx="16" ry="26" fill="#f59e0b"/>
                        <circle cx="20" cy="18" r="12" fill="#d97706"/>
                        <circle cx="15" cy="17" r="2" fill="#0f172a"/>
                        <circle cx="25" cy="17" r="2" fill="#0f172a"/>
                        <path d="M 8,30 Q 20,50 32,30" fill="#b45309"/>
                    </g>
                    <!-- Right Lion -->
                    <g transform="translate(155, 35)">
                        <ellipse cx="20" cy="30" rx="14" ry="22" fill="#f59e0b"/>
                        <circle cx="20" cy="15" r="10" fill="#d97706"/>
                        <circle cx="24" cy="14" r="1.5" fill="#0f172a"/>
                        <path d="M 10,25 Q 20,40 30,25" fill="#b45309"/>
                    </g>
                </svg>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
                <button onclick="showEmblemPerspective('front')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-amber-400 font-bold text-center">
                    🏛️ 2D View (3 Lions)
                </button>
                <button onclick="showEmblemPerspective('all')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-emerald-400 font-bold text-center">
                    🦁 3D Reality (4 Lions)
                </button>
            </div>
            <div id="emblemInfoBox" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300">
                In 2D views, three lions are visible; the fourth lion faces directly backward, guarding all four compass directions.
            </div>
        </div>
    """,

    6: """
        <!-- Sim 6: Royal Bengal Tiger Camouflage & Reserve Radar -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-orange-400 uppercase tracking-wider block mb-1">Striped Camouflage & Project Tiger</span>
                <p class="text-[11px] text-slate-400">Toggle grass camouflage and inspect India's wild tiger population growth:</p>
            </div>
            <div class="relative h-44 bg-slate-900 rounded-xl border border-slate-800 p-2 overflow-hidden flex items-center justify-center">
                <svg viewBox="0 0 340 160" class="w-full h-full">
                    <!-- Forest background -->
                    <rect x="0" y="0" width="340" height="160" fill="#14532d" opacity="0.3"/>

                    <!-- Tiger Body -->
                    <g id="tigerGraphic" transform="translate(60, 40)">
                        <!-- Torso -->
                        <ellipse cx="110" cy="55" rx="65" ry="32" fill="#ea580c"/>
                        <!-- Head -->
                        <circle cx="40" cy="40" r="24" fill="#ea580c"/>
                        <circle cx="32" cy="22" r="7" fill="#c2410c"/>
                        <circle cx="48" cy="22" r="7" fill="#c2410c"/>
                        <!-- White Muzzle -->
                        <ellipse cx="38" cy="48" rx="10" ry="8" fill="#f8fafc"/>
                        <circle cx="34" cy="38" r="3" fill="#0f172a"/>
                        <!-- Stripes -->
                        <path d="M 75,30 Q 78,55 75,80" stroke="#0f172a" stroke-width="4" fill="none"/>
                        <path d="M 95,25 Q 98,55 95,85" stroke="#0f172a" stroke-width="4" fill="none"/>
                        <path d="M 115,25 Q 118,55 115,85" stroke="#0f172a" stroke-width="4" fill="none"/>
                        <path d="M 135,28 Q 138,55 135,82" stroke="#0f172a" stroke-width="4" fill="none"/>
                        <path d="M 155,35 Q 158,55 155,75" stroke="#0f172a" stroke-width="4" fill="none"/>
                        <!-- Tail -->
                        <path d="M 175,55 Q 210,65 215,95" stroke="#ea580c" stroke-width="8" fill="none" stroke-linecap="round"/>
                        <path d="M 185,62 Q 190,65 190,70" stroke="#0f172a" stroke-width="4" fill="none"/>
                        <path d="M 200,75 Q 205,78 205,82" stroke="#0f172a" stroke-width="4" fill="none"/>
                    </g>

                    <!-- Foreground Tall Grass Reeds (Camouflage) -->
                    <g id="tallGrassReeds" opacity="0.9">
                        <line x1="30" y1="160" x2="45" y2="20" stroke="#84cc16" stroke-width="4"/>
                        <line x1="55" y1="160" x2="65" y2="10" stroke="#65a30d" stroke-width="3"/>
                        <line x1="80" y1="160" x2="90" y2="30" stroke="#a3e635" stroke-width="4"/>
                        <line x1="110" y1="160" x2="115" y2="15" stroke="#84cc16" stroke-width="3"/>
                        <line x1="135" y1="160" x2="145" y2="25" stroke="#65a30d" stroke-width="4"/>
                        <line x1="165" y1="160" x2="175" y2="10" stroke="#a3e635" stroke-width="3"/>
                        <line x1="195" y1="160" x2="205" y2="30" stroke="#84cc16" stroke-width="4"/>
                        <line x1="225" y1="160" x2="235" y2="20" stroke="#65a30d" stroke-width="3"/>
                        <line x1="255" y1="160" x2="265" y2="25" stroke="#a3e635" stroke-width="4"/>
                    </g>
                </svg>
            </div>
            <div class="flex items-center space-x-2">
                <button onclick="toggleTigerCamouflage()" id="camoToggleBtn" class="flex-1 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-orange-400 border border-slate-700">
                    🌾 Remove Grass Reeds
                </button>
                <button onclick="showTigerCensus()" class="flex-1 py-2 rounded-xl text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white">
                    📈 3,682 Tigers Today
                </button>
            </div>
            <div id="tigerCamoText" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300">
                In tall savannah grass, vertical black stripes disrupt the tiger's outline, blending seamlessly with shadows.
            </div>
        </div>
    """,

    7: """
        <!-- Sim 7: Indian Peafowl Iridescent Feather Optics -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Photonic Iridescence & Monsoon Dance</span>
                <p class="text-[11px] text-slate-400">Slide lighting angle to observe structural colour shift on peacock feathers:</p>
            </div>
            <div class="relative h-44 bg-slate-900 rounded-xl border border-slate-800 p-2 overflow-hidden flex items-center justify-center">
                <svg viewBox="0 0 320 160" class="w-full h-full">
                    <!-- Fan of Feathers -->
                    <g id="peacockFan" transform="translate(160, 130)">
                        <!-- Feather Eyes radiating outward -->
                        <path d="M 0,0 L -90,-80" stroke="#0284c7" stroke-width="3"/>
                        <circle cx="-90" cy="-80" r="14" id="eye1" fill="#0369a1" stroke="#38bdf8" stroke-width="3"/>
                        <circle cx="-90" cy="-80" r="6" fill="#1e3a8a"/>

                        <path d="M 0,0 L -50,-105" stroke="#0284c7" stroke-width="3"/>
                        <circle cx="-50" cy="-105" r="14" id="eye2" fill="#0369a1" stroke="#38bdf8" stroke-width="3"/>
                        <circle cx="-50" cy="-105" r="6" fill="#1e3a8a"/>

                        <path d="M 0,0 L 0,-115" stroke="#0284c7" stroke-width="3"/>
                        <circle cx="0" cy="-115" r="16" id="eye3" fill="#0369a1" stroke="#38bdf8" stroke-width="3"/>
                        <circle cx="0" cy="-115" r="7" fill="#1e3a8a"/>

                        <path d="M 0,0 L 50,-105" stroke="#0284c7" stroke-width="3"/>
                        <circle cx="50" cy="-105" r="14" id="eye4" fill="#0369a1" stroke="#38bdf8" stroke-width="3"/>
                        <circle cx="50" cy="-105" r="6" fill="#1e3a8a"/>

                        <path d="M 0,0 L 90,-80" stroke="#0284c7" stroke-width="3"/>
                        <circle cx="90" cy="-80" r="14" id="eye5" fill="#0369a1" stroke="#38bdf8" stroke-width="3"/>
                        <circle cx="90" cy="-80" r="6" fill="#1e3a8a"/>

                        <!-- Central Peacock Body -->
                        <ellipse cx="0" cy="-10" rx="16" ry="24" fill="#1d4ed8"/>
                        <circle cx="0" cy="-30" r="10" fill="#2563eb"/>
                        <!-- Crest -->
                        <line x1="0" y1="-40" x2="-4" y2="-48" stroke="#38bdf8" stroke-width="1.5"/>
                        <line x1="0" y1="-40" x2="0" y2="-50" stroke="#38bdf8" stroke-width="1.5"/>
                        <line x1="0" y1="-40" x2="4" y2="-48" stroke="#38bdf8" stroke-width="1.5"/>
                    </g>
                </svg>
            </div>
            <div class="space-y-1.5">
                <div class="flex justify-between text-xs text-slate-300">
                    <span>Incident Sunbeam Angle:</span>
                    <span id="lightAngleVal" class="text-sky-400 font-bold">45° (Cobalt Blue)</span>
                </div>
                <input type="range" min="10" max="80" value="45" oninput="setPeacockOptics(this.value)" class="w-full accent-sky-500 cursor-pointer">
            </div>
            <div id="featherOpticDesc" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300">
                Microscopic 2D photonic lattices in feather barbules shift reflected wavelength as light angle changes!
            </div>
        </div>
    """,

    8: """
        <!-- Sim 8: National Natural Heritage Mosaic -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-pink-400 uppercase tracking-wider block mb-1">Sacred Botanical & Wildlife Wonders</span>
                <p class="text-[11px] text-slate-400">Click any national heritage treasure to inspect its unique ecological adaptation:</p>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
                <button onclick="selectSacredSymbol('banyan')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left transition">
                    <span class="text-emerald-400 font-bold block">🌳 Banyan Tree</span>
                    <span class="text-[10px] text-slate-400">Aerial Prop Roots</span>
                </button>
                <button onclick="selectSacredSymbol('lotus')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left transition">
                    <span class="text-pink-400 font-bold block">🪷 Lotus Flower</span>
                    <span class="text-[10px] text-slate-400">Water-Repelling Petals</span>
                </button>
                <button onclick="selectSacredSymbol('dolphin')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left transition">
                    <span class="text-cyan-400 font-bold block">🐬 Ganges Dolphin</span>
                    <span class="text-[10px] text-slate-400">Ultrasonic Biosonar</span>
                </button>
                <button onclick="selectSacredSymbol('elephant')" class="p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-left transition">
                    <span class="text-amber-400 font-bold block">🐘 Indian Elephant</span>
                    <span class="text-[10px] text-slate-400">Keystone Seed Disperser</span>
                </button>
            </div>
            <div id="sacredSymbolDisplay" class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-200 leading-relaxed">
                <strong class="text-pink-300 block mb-1">Ecological Marvel:</strong>
                Select a symbol above to explore how Indian heritage celebrates nature's most extraordinary adaptations!
            </div>
        </div>
    """,

    9: """
        <!-- Sim 9: Linguistic Tapestry & Script Explorer -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Linguistic Tapestry & Brahmi Roots</span>
                <p class="text-[11px] text-slate-400">Select an Indian regional greeting to explore its script and ancient Brahmi lineage:</p>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
                <button onclick="displayGreeting('hindi')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200">
                    नमस्ते (Hindi)
                </button>
                <button onclick="displayGreeting('tamil')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200">
                    வணக்கம் (Tamil)
                </button>
                <button onclick="displayGreeting('bengali')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200">
                    নমস্কার (Bengali)
                </button>
                <button onclick="displayGreeting('punjabi')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-200">
                    ਸਤਿ ਸ੍ਰੀ ਅਕਾਲ (Punjabi)
                </button>
            </div>
            <div id="greetingInfoBox" class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 text-xs text-slate-300 space-y-1.5">
                <div class="flex items-center justify-between border-b border-slate-800 pb-1.5">
                    <span class="font-bold text-white text-base" id="greetingWord">नमस्ते (Namaste)</span>
                    <span class="text-[10px] text-amber-400 font-semibold" id="greetingScript">Devanagari Script</span>
                </div>
                <p class="text-slate-300 text-[11px]" id="greetingDesc">
                    Rooted in Sanskrit, meaning 'I bow to the divine spark within you'. Written in Devanagari script, which directly evolved from ancient Brahmi.
                </p>
            </div>
        </div>
    """,

    10: """
        <!-- Sim 10: Garden vs Forest Resilience Simulator -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Monoculture Garden vs Biodiverse Forest</span>
                <p class="text-[11px] text-slate-400">Trigger a pest or drought crisis to observe how ecological diversity saves the forest:</p>
            </div>
            <div class="grid grid-cols-2 gap-2.5">
                <!-- Garden Card -->
                <div id="gardenCard" class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5 text-center">
                    <span class="text-xs font-bold text-amber-400 block">Single-Crop Garden</span>
                    <div class="text-2xl" id="gardenEmoji">🌹 🌹 🌹</div>
                    <span class="text-[10px] text-slate-400 block" id="gardenStatus">Healthy under artificial care</span>
                </div>
                <!-- Forest Card -->
                <div id="forestCard" class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5 text-center">
                    <span class="text-xs font-bold text-emerald-400 block">Biodiverse Forest</span>
                    <div class="text-2xl" id="forestEmoji">🌲 🍄 🐦 🌿</div>
                    <span class="text-[10px] text-slate-400 block" id="forestStatus">Thriving self-sustaining web</span>
                </div>
            </div>
            <div class="flex items-center space-x-2">
                <button onclick="triggerEcoCrisis('pest')" class="flex-1 py-2 rounded-xl text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition">
                    🐛 Release Pest Attack
                </button>
                <button onclick="triggerEcoCrisis('reset')" class="flex-1 py-2 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 transition">
                    🔄 Reset Ecosystem
                </button>
            </div>
            <div id="ecoSimResult" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300">
                Click <strong>Release Pest Attack</strong> to test how monoculture vulnerability contrasts with forest resilience!
            </div>
        </div>
    """,

    11: """
        <!-- Sim 11: Regional Headgear & Cultural Wardrobe -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-orange-400 uppercase tracking-wider block mb-1">Traditional Saafas, Topis & Safety Helmets</span>
                <p class="text-[11px] text-slate-400">Select a regional headgear to inspect its climate adaptation and physics:</p>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
                <button onclick="equipHeadgear('saafa')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-orange-400 font-bold text-center">
                    🏜️ Rajasthani Saafa
                </button>
                <button onclick="equipHeadgear('topi')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-sky-400 font-bold text-center">
                    🏔️ Himachali Topi
                </button>
                <button onclick="equipHeadgear('peta')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-amber-400 font-bold text-center">
                    👑 Mysore Peta
                </button>
                <button onclick="equipHeadgear('helmet')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-emerald-400 font-bold text-center">
                    🪖 Safety Helmet
                </button>
            </div>
            <div id="headgearDisplayBox" class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5 text-xs text-slate-300">
                <div class="flex items-center justify-between border-b border-slate-800 pb-1.5">
                    <span class="font-bold text-white text-sm" id="headgearName">Rajasthani Saafa (Pagri)</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500/20 text-orange-300" id="headgearRegion">Thar Desert, Rajasthan</span>
                </div>
                <p class="text-[11px]" id="headgearPhysics">
                    Multi-metre folded cotton creates insulating dead-air chambers, shielding the scalp from 48°C radiant solar rays.
                </p>
            </div>
        </div>
    """,

    12: """
        <!-- Sim 12: Indian Drums Acoustic Resonance Lab -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Acoustic Science: The Loaded Syahi Patch</span>
                <p class="text-[11px] text-slate-400">Toggle the black Syahi patch on a drumhead to hear C.V. Raman's acoustic discovery:</p>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
                <button onclick="setDrumTuning('unloaded')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-slate-300 font-bold text-center">
                    ⚪ Plain Drum Skin (Noisy)
                </button>
                <button onclick="setDrumTuning('syahi')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-amber-400 font-bold text-center">
                    ⚫ Syahi-Loaded (Harmonic)
                </button>
            </div>
            <div class="relative h-32 bg-slate-900 rounded-xl border border-slate-800 p-2 flex items-center justify-center">
                <svg viewBox="0 0 260 110" class="w-full h-full">
                    <!-- Drumhead -->
                    <circle cx="130" cy="55" r="45" fill="#f8fafc" stroke="#64748b" stroke-width="4"/>
                    <!-- Syahi Patch (Centre) -->
                    <circle id="syahiPatchCircle" cx="130" cy="55" r="18" fill="#0f172a" stroke="#334155" stroke-width="2"/>
                    <!-- Tuning Pegs -->
                    <circle cx="85" cy="55" r="3" fill="#cbd5e1"/>
                    <circle cx="175" cy="55" r="3" fill="#cbd5e1"/>
                    <circle cx="130" cy="10" r="3" fill="#cbd5e1"/>
                    <circle cx="130" cy="100" r="3" fill="#cbd5e1"/>
                </svg>
            </div>
            <div id="acousticSoundResult" class="p-2.5 rounded-lg bg-slate-900 border border-slate-800 text-xs text-slate-300">
                The central black Syahi patch adds mass, dampening non-harmonic dissonant vibrations to produce pure musical harmonics.
            </div>
        </div>
    """,

    13: """
        <!-- Sim 13: Classical Dance Mudras & Rhythms -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-pink-400 uppercase tracking-wider block mb-1">Classical Storytelling Hastas (Mudras)</span>
                <p class="text-[11px] text-slate-400">Select a classical dance hand gesture to discover its symbolic representation:</p>
            </div>
            <div class="grid grid-cols-3 gap-2 text-xs">
                <button onclick="selectMudra('mayura')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-sky-400 font-bold text-center">
                    🪶 Mayura
                </button>
                <button onclick="selectMudra('hamsasya')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-emerald-400 font-bold text-center">
                    🦢 Hamsasya
                </button>
                <button onclick="selectMudra('padma')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-pink-400 font-bold text-center">
                    🪷 Padmakosha
                </button>
            </div>
            <div id="mudraDisplayBox" class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5 text-xs text-slate-300">
                <div class="flex items-center justify-between border-b border-slate-800 pb-1.5">
                    <span class="font-bold text-white text-sm" id="mudraName">Mayura Mudra (Peacock Gesture)</span>
                    <span class="text-[10px] text-sky-400 font-semibold" id="mudraDance">Bharatanatyam & Kathak</span>
                </div>
                <p class="text-[11px]" id="mudraMeaning">
                    Formed by joining the ring fingertip to the thumb while keeping index, middle, and little fingers straight like peacock crest plumes.
                </p>
            </div>
        </div>
    """,

    14: """
        <!-- Sim 14: Ancient Wellness & Phytotherapy Lab -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Ayurvedic Botany & Pranayama Pulse</span>
                <p class="text-[11px] text-slate-400">Extract bioactive compounds from Indian herbs or trigger deep Pranayama:</p>
            </div>
            <div class="grid grid-cols-3 gap-2 text-xs">
                <button onclick="extractBioactive('turmeric')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-amber-400 font-bold text-center">
                    🟡 Turmeric
                </button>
                <button onclick="extractBioactive('tulsi')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-emerald-400 font-bold text-center">
                    🍃 Tulsi
                </button>
                <button onclick="extractBioactive('neem')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-lime-400 font-bold text-center">
                    🌿 Neem
                </button>
            </div>
            <div id="bioactiveResult" class="p-3 rounded-xl bg-slate-900 border border-slate-800 space-y-1 text-xs text-slate-300">
                <span class="font-bold text-amber-300 block" id="herbTitle">Turmeric (Haridra)</span>
                <p class="text-[11px]" id="herbDetails">
                    Contains <strong>Curcumin</strong>, a natural polyphenol that inhibits cellular inflammation and speeds wound healing.
                </p>
            </div>
            <button onclick="testPranayamaBreathing()" class="w-full py-2 rounded-xl bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs transition">
                🧘 Test 60-Second Pranayama Breath Effect
            </button>
            <div id="pranayamaEffect" class="hidden p-2 rounded-lg bg-indigo-950/40 border border-indigo-500/30 text-center text-xs text-indigo-300">
                Deep slow breathing lowers heart rate from 92 bpm to 68 bpm, calming the nervous system!
            </div>
        </div>
    """,

    15: """
        <!-- Sim 15: India's Modern Innovation Launchpad -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">High-Tech India: ISRO, UPI & High-Speed Rail</span>
                <p class="text-[11px] text-slate-400">Launch a test to experience India's cutting-edge scientific achievements:</p>
            </div>
            <div class="grid grid-cols-3 gap-2 text-xs">
                <button onclick="runTechDemo('isro')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-orange-400 font-bold text-center">
                    🚀 ISRO Moon
                </button>
                <button onclick="runTechDemo('upi')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-cyan-400 font-bold text-center">
                    📱 UPI Instant Pay
                </button>
                <button onclick="runTechDemo('train')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-emerald-400 font-bold text-center">
                    🚅 Vande Bharat
                </button>
            </div>
            <div id="techDemoDisplay" class="p-3.5 rounded-xl bg-slate-900 border border-slate-800 space-y-1.5 text-xs text-slate-300">
                <div class="flex items-center justify-between border-b border-slate-800 pb-1.5">
                    <span class="font-bold text-white text-sm" id="techTitle">Chandrayaan-3 Moon Landing</span>
                    <span class="px-2 py-0.5 rounded text-[10px] font-bold bg-orange-500/20 text-orange-300" id="techBadge">Space Frontier</span>
                </div>
                <p class="text-[11px]" id="techDesc">
                    On August 23, 2023, India became the first country on Earth to soft-land near the lunar South Pole!
                </p>
            </div>
        </div>
    """,

    16: """
        <!-- Sim 16: The Vibrant Unity Tapestry -->
        <div class="space-y-3">
            <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
                <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">The Great Loom of Indian Unity</span>
                <p class="text-[11px] text-slate-400">Click to weave diverse regional threads into the unbreakable national fabric:</p>
            </div>
            <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-center space-y-2">
                <div class="text-2xl tracking-widest" id="tapestryLoom">
                    🧵 🧵 🧵 🧵
                </div>
                <span class="text-xs text-amber-400 font-bold" id="threadCountBadge">4 Cultural Strands Woven</span>
            </div>
            <div class="grid grid-cols-2 gap-2 text-xs">
                <button onclick="weaveTapestry('language')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-sky-400 font-bold text-center">
                    + Add Language Strand
                </button>
                <button onclick="weaveTapestry('festival')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-orange-400 font-bold text-center">
                    + Add Festival Strand
                </button>
                <button onclick="weaveTapestry('science')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-emerald-400 font-bold text-center">
                    + Add Science Strand
                </button>
                <button onclick="weaveTapestry('dance')" class="p-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-pink-400 font-bold text-center">
                    + Add Dance Strand
                </button>
            </div>
            <div id="tapestryMessage" class="p-2.5 rounded-lg bg-amber-950/30 border border-amber-500/20 text-xs text-amber-200 text-center">
                Every diverse thread strengthens the composite fabric of our great motherland!
            </div>
        </div>
    """
}

print(f"Bespoke simulators defined: {len(SIMULATORS)}")

