#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 7: Water - A Precious Gift
Interactive Simulators Generator - Part 1 (Simulators 1 to 8)
"""

simulators_part1 = {}

# Simulator 1: Watching Rain Clouds (Sky Observation & Forecast Predictor)
simulators_part1[1] = """
<div class="sim-container space-y-4" id="sim1-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⛅</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Sky Clues & Rain Forecast Station</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Meteorology Lab</span>
    </div>

    <p class="text-xs text-slate-300">Inspect shifting sky conditions, breeze humidity, and wildlife signals to predict if rain is approaching!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="setSkyCondition('sunny')" id="btn-sky-sunny" class="p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 shadow flex items-center gap-2 text-left">
            <span class="text-2xl">☀️</span>
            <div>
                <span class="text-xs block">Clear Sunny Sky</span>
                <span class="text-[10px] text-cyan-200">White Fluffy Clouds</span>
            </div>
        </button>
        <button onclick="setSkyCondition('breeze')" id="btn-sky-breeze" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">🌬️</span>
            <div>
                <span class="text-xs block">Cool Humid Gusts</span>
                <span class="text-[10px] text-slate-400">Low Swallows & Frogs</span>
            </div>
        </button>
        <button onclick="setSkyCondition('nimbus')" id="btn-sky-nimbus" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left">
            <span class="text-2xl">⛈️</span>
            <div>
                <span class="text-xs block">Dark Nimbus Clouds</span>
                <span class="text-[10px] text-slate-400">Heavy Moisture Packed</span>
            </div>
        </button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl border border-slate-800" id="sky-svg">
            <rect id="sky-bg-rect" x="0" y="0" width="700" height="175" fill="#0369a1" />
            <rect x="0" y="175" width="700" height="55" fill="#14532d" />

            <!-- Sun -->
            <circle id="sky-sun" cx="590" cy="52" r="28" fill="#fbbf24" />
            <!-- Clouds -->
            <g id="sky-clouds" fill="#ffffff" opacity="0.95">
                <circle cx="150" cy="60" r="28" />
                <circle cx="185" cy="52" r="34" />
                <circle cx="222" cy="60" r="26" />
                <circle cx="380" cy="70" r="24" />
                <circle cx="412" cy="65" r="28" />
            </g>

            <!-- Birds / Wildlife -->
            <g id="sky-wildlife">
                <text id="sky-bird-1" x="270" y="45" font-size="18">🕊️</text>
                <text id="sky-bird-2" x="480" y="55" font-size="18">🐦</text>
                <text id="sky-frog" x="560" y="205" font-size="22" opacity="0.3">🐸</text>
            </g>

            <!-- House & Tree -->
            <rect x="70" y="125" width="90" height="50" fill="#cbd5e1" />
            <polygon points="60,125 115,90 170,125" fill="#b45309" />
            <rect x="103" y="145" width="24" height="30" fill="#78350f" />
            <rect x="615" y="130" width="16" height="45" fill="#78350f" />
            <circle cx="623" cy="115" r="34" fill="#15803d" />

            <!-- Forecast Gauge Badge -->
            <g transform="translate(245, 186)">
                <rect x="0" y="0" width="210" height="30" rx="8" fill="#0f172a" stroke="#38bdf8" stroke-width="1.5" />
                <text id="sky-gauge-text" x="105" y="19" fill="#fde047" font-size="12" font-weight="bold" text-anchor="middle">Rain Chance: 10% (Clear Day)</text>
            </g>
        </svg>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-cyan-800/60 flex items-start gap-3 text-xs">
        <span class="text-3xl" id="sky-info-icon">☀️</span>
        <div class="space-y-1">
            <h4 class="text-sm font-bold text-cyan-300" id="sky-info-title">Sunny Blue Skies & Light White Cumulus</h4>
            <p class="text-slate-300" id="sky-info-desc">Widely spaced fluffy white clouds float gently high above while warm sunlight dries laundry swiftly. Birds glide high without worry.</p>
            <div class="text-[11px] text-amber-300 font-semibold" id="sky-info-cue">🔍 Field Clue: Dry warm wind and bright shadows mean no umbrella is needed right now!</div>
        </div>
    </div>
</div>

<script>
function setSkyCondition(cond) {
    const states = {
        sunny: {
            bg: '#0369a1', sunOpacity: '1', cloudFill: '#ffffff',
            birdY1: 45, birdY2: 55, frogOp: '0.3',
            gauge: 'Rain Chance: 10% (Clear Day)',
            icon: '☀️',
            title: 'Sunny Blue Skies & Light White Cumulus',
            desc: 'Widely spaced fluffy white clouds float gently high above while warm sunlight dries laundry swiftly. Birds glide high without worry.',
            cue: '🔍 Field Clue: Dry warm wind and bright shadows mean no umbrella is needed right now!'
        },
        breeze: {
            bg: '#334155', sunOpacity: '0.35', cloudFill: '#94a3b8',
            birdY1: 115, birdY2: 120, frogOp: '0.9',
            gauge: 'Rain Chance: 65% (Storm Brewing)',
            icon: '🌬️',
            title: 'Cool Humid Breeze & Low-Flying Wildlife',
            desc: 'Moist gusts blow across the courtyard dropping air temperature, dragonflies and swallows dip low chasing insects, and frogs start croaking!',
            cue: '🔍 Field Clue: Feel damp air on your skin and smell faint earthy moisture on the wind!'
        },
        nimbus: {
            bg: '#1e293b', sunOpacity: '0.05', cloudFill: '#475569',
            birdY1: 145, birdY2: 145, frogOp: '1',
            gauge: 'Rain Chance: 95% (Downpour Imminent!)',
            icon: '⛈️',
            title: 'Towering Dark Nimbus Clouds Blocking Sun',
            desc: 'Millions of heavy condensed water droplets pack thick charcoal-gray clouds overhead, darkening afternoon light right before rainfall starts.',
            cue: '🔍 Field Clue: Fetch outdoor clothes inside quickly and set out clean rainwater collection jars!'
        }
    };
    const d = states[cond];
    if (!d) return;

    ['sunny', 'breeze', 'nimbus'].forEach(k => {
        const b = document.getElementById('btn-sky-' + k);
        if (b) {
            b.className = (k === cond)
                ? 'p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 shadow flex items-center gap-2 text-left'
                : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 transition flex items-center gap-2 text-left';
        }
    });

    document.getElementById('sky-bg-rect').setAttribute('fill', d.bg);
    document.getElementById('sky-sun').setAttribute('opacity', d.sunOpacity);
    document.getElementById('sky-clouds').setAttribute('fill', d.cloudFill);
    document.getElementById('sky-bird-1').setAttribute('y', d.birdY1);
    document.getElementById('sky-bird-2').setAttribute('y', d.birdY2);
    document.getElementById('sky-frog').setAttribute('opacity', d.frogOp);
    document.getElementById('sky-gauge-text').textContent = d.gauge;
    document.getElementById('sky-info-icon').textContent = d.icon;
    document.getElementById('sky-info-title').textContent = d.title;
    document.getElementById('sky-info-desc').textContent = d.desc;
    document.getElementById('sky-info-cue').textContent = d.cue;
}
</script>
"""

# Simulator 2: Weekly Weather Logs (7-Day Observation Tracker)
simulators_part1[2] = """
<div class="sim-container space-y-4" id="sim2-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">📅</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Seven-Day Schoolyard Sky Logbook</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Weekly Weather Data</span>
    </div>

    <p class="text-xs text-slate-300">Click any day of the week to inspect recorded morning sky clues, student rainfall predictions, and real afternoon results!</p>

    <div class="grid grid-cols-4 sm:grid-cols-7 gap-2">
        <button onclick="selectLogDay(0)" id="btn-day-0" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-center">Mon ☀️</button>
        <button onclick="selectLogDay(1)" id="btn-day-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">Tue ⛅</button>
        <button onclick="selectLogDay(2)" id="btn-day-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">Wed 🌧️</button>
        <button onclick="selectLogDay(3)" id="btn-day-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">Thu ⛈️</button>
        <button onclick="selectLogDay(4)" id="btn-day-4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">Fri 🌦️</button>
        <button onclick="selectLogDay(5)" id="btn-day-5" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">Sat ☀️</button>
        <button onclick="selectLogDay(6)" id="btn-day-6" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">Sun ⛅</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 text-xs">
        <div class="space-y-2.5">
            <div class="flex items-center justify-between border-b border-slate-800 pb-2">
                <span class="font-bold text-cyan-300 text-sm" id="logday-name">Monday — Observation #1</span>
                <span class="px-2 py-0.5 rounded bg-emerald-950 text-emerald-300 border border-emerald-800 text-[10px]" id="logday-match">Forecast Match ✓</span>
            </div>
            <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                <span class="text-slate-400 block text-[10px]">Morning Sky Observation:</span>
                <span class="text-slate-100 font-semibold" id="logday-sky">Clear bright blue horizon, crisp golden sun, calm gentle dry breeze.</span>
            </div>
            <div class="grid grid-cols-2 gap-2">
                <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Morning Prediction:</span>
                    <span class="text-amber-300 font-bold" id="logday-pred">Dry — No Rain</span>
                </div>
                <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
                    <span class="text-slate-400 block text-[10px]">Actual Afternoon Outcome:</span>
                    <span class="text-cyan-300 font-bold" id="logday-actual">Zero Rainfall (Dry)</span>
                </div>
            </div>
        </div>

        <div class="bg-slate-900/90 p-4 rounded-xl border border-slate-800 flex flex-col justify-between">
            <div class="flex items-center gap-3">
                <span class="text-4xl" id="logday-emoji">☀️</span>
                <div>
                    <span class="text-slate-400 text-[10px] uppercase tracking-wider block">Scientific Reflection Note</span>
                    <p class="text-slate-200 leading-relaxed mt-1" id="logday-note">
                        Warm bright sunshine dried school courtyard puddles completely. Clear high clouds carried too little moisture to rain.
                    </p>
                </div>
            </div>
            <div class="mt-3 pt-2 border-t border-slate-800 flex items-center justify-between text-[11px] text-emerald-300 font-semibold">
                <span>Weekly Tracker Accuracy:</span>
                <span>6 of 7 Days Correct (86%) 📊</span>
            </div>
        </div>
    </div>
</div>

<script>
const logDays = [
    { name: 'Monday — Observation #1', emoji: '☀️', match: 'Forecast Match ✓', sky: 'Clear bright blue horizon, crisp golden sun, calm gentle dry breeze.', pred: 'Dry — No Rain', actual: 'Zero Rainfall (Dry)', note: 'Warm bright sunshine dried school courtyard puddles completely. Clear high clouds carried too little moisture to rain.' },
    { name: 'Tuesday — Observation #2', emoji: '⛅', match: 'Surprising Shift 🌬️', sky: 'Gray overcast clouds drifted over rooftops around 10 AM with warm air.', pred: 'Rain Expected', actual: 'Zero Rainfall (Blew Past)', note: 'High-altitude winds pushed thick gray clouds swiftly toward distant eastern hills before droplets grew heavy enough to fall!' },
    { name: 'Wednesday — Observation #3', emoji: '🌧️', match: 'Forecast Match ✓', sky: 'Dark low clouds thickened by noon; humid breeze and petrichor aroma rose.', pred: 'Steady Monsoon Rain', actual: 'Moderate Afternoon Rain', note: 'Cool humid gusts preceded 45 minutes of refreshing steady rainfall that cooled warm stone verandas.' },
    { name: 'Thursday — Observation #4', emoji: '⛈️', match: 'Forecast Match ✓', sky: 'Dense black-gray nimbus clouds covered the sky early; frogs croaked near ditches.', pred: 'Heavy Storm Downpour', actual: 'Heavy Rain & Puddles', note: 'Heavy roaring downpour filled collection jars rapidly and sent muddy streams coursing into garden beds.' },
    { name: 'Friday — Observation #5', emoji: '🌦️', match: 'Forecast Match ✓', sky: 'Patchy sunbeams breaking between scattered silver clouds after cool morning dampness.', pred: 'Light Passing Drizzle', actual: 'Brief Gentle Drizzle', note: 'A sunny shower created a faint rainbow arc across eastern clouds while leaving light droplets on leaves.' },
    { name: 'Saturday — Observation #6', emoji: '☀️', match: 'Forecast Match ✓', sky: 'Crisp blue sky rinsed spotless by yesterday\\'s rains; soft morning warmth.', pred: 'Dry Sunny Day', actual: 'Zero Rainfall (Sunny)', note: 'Clean post-rain air allowed crisp distant hill views with pleasant warmth throughout play hours.' },
    { name: 'Sunday — Observation #7', emoji: '⛅', match: 'Forecast Match ✓', sky: 'Scattered fair-weather puffy cumulus clouds drifting slowly overhead.', pred: 'Dry With Shade', actual: 'Zero Rainfall (Breezy)', note: 'Comparing all seven days reveals that dark dense clouds plus humid breezes reliably forecast rain.' }
];

function selectLogDay(idx) {
    const d = logDays[idx];
    if (!d) return;
    for (let i = 0; i < 7; i++) {
        const b = document.getElementById('btn-day-' + i);
        if (b) {
            b.className = (i === idx)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-center'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center';
        }
    }
    document.getElementById('logday-name').textContent = d.name;
    document.getElementById('logday-match').textContent = d.match;
    document.getElementById('logday-sky').textContent = d.sky;
    document.getElementById('logday-pred').textContent = d.pred;
    document.getElementById('logday-actual').textContent = d.actual;
    document.getElementById('logday-emoji').textContent = d.emoji;
    document.getElementById('logday-note').textContent = d.note;
}
</script>
"""

# Simulator 3: Studying Raindrops Closely (Intensity & Wind Slant Lab)
simulators_part1[3] = """
<div class="sim-container space-y-4" id="sim3-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌧️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Raindrop Size, Intensity & Wind Slant Lab</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Activity 1 Physics</span>
    </div>

    <p class="text-xs text-slate-300">Switch rainfall intensity and horizontal wind gusts to watch raindrop size, falling speed, and diagonal slant angle change!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="setRainPhysics('drizzle', currentWind)" id="btn-rain-drizzle" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2">
            <span class="text-xl">🌦️</span>
            <div><span class="block">Light Drizzle</span><span class="text-[10px] opacity-80">Tiny Slow Mist Drops</span></div>
        </button>
        <button onclick="setRainPhysics('downpour', currentWind)" id="btn-rain-downpour" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🌧️</span>
            <div><span class="block">Heavy Downpour</span><span class="text-[10px] text-slate-400">Giant Fast Splashes</span></div>
        </button>
        <button onclick="setRainPhysics(currentRainMode, currentWind === 'calm' ? 'gusty' : 'calm')" id="btn-wind-toggle" class="p-2.5 rounded-xl bg-amber-600/80 hover:bg-amber-500 text-white font-bold text-xs border border-amber-500 text-left flex items-center gap-2">
            <span class="text-xl">💨</span>
            <div><span class="block" id="wind-btn-title">Wind: Calm (0° Tilt)</span><span class="text-[10px] opacity-90">Click to Toggle Gusts</span></div>
        </button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 220" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <rect x="0" y="0" width="700" height="175" fill="#0f172a" />
            <rect x="0" y="175" width="700" height="45" fill="#1e293b" />
            <!-- Cloud Deck -->
            <ellipse cx="350" cy="25" rx="280" ry="28" fill="#475569" />

            <!-- Animated Rain Streaks -->
            <g id="rain-streaks-group" stroke="#38bdf8" stroke-linecap="round">
                <line x1="120" y1="45" x2="120" y2="62" stroke-width="1.5" opacity="0.7" />
                <line x1="210" y1="65" x2="210" y2="82" stroke-width="1.5" opacity="0.7" />
                <line x1="300" y1="50" x2="300" y2="67" stroke-width="1.5" opacity="0.7" />
                <line x1="400" y1="75" x2="400" y2="92" stroke-width="1.5" opacity="0.7" />
                <line x1="510" y1="55" x2="510" y2="72" stroke-width="1.5" opacity="0.7" />
                <line x1="600" y1="68" x2="600" y2="85" stroke-width="1.5" opacity="0.7" />
            </g>

            <!-- Person with Umbrella -->
            <g transform="translate(335, 130)">
                <g id="umbrella-tilt" transform="rotate(0 15 10)">
                    <path d="M -25 0 Q 15 -28 55 0 Z" fill="#ef4444" stroke="#fca5a5" stroke-width="2" />
                    <line x1="15" y1="0" x2="15" y2="30" stroke="#cbd5e1" stroke-width="2.5" />
                </g>
                <circle cx="15" cy="25" r="7" fill="#fde047" />
                <line x1="15" y1="32" x2="15" y2="55" stroke="#38bdf8" stroke-width="4" />
            </g>

            <!-- Ground Puddle -->
            <ellipse id="rain-puddle" cx="180" cy="195" rx="45" ry="7" fill="#0284c7" opacity="0.6" />
        </svg>
    </div>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2 text-xs text-center">
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Droplet Diameter:</span>
            <span id="stat-drop-size" class="text-cyan-300 font-bold">~0.4 mm (Fine Mist)</span>
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Sound & Splash:</span>
            <span id="stat-drop-sound" class="text-emerald-300 font-bold">Soft Whisper on Leaves</span>
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] block">Falling Trajectory:</span>
            <span id="stat-drop-angle" class="text-amber-300 font-bold">Straight Vertical (0° Tilt)</span>
        </div>
    </div>
</div>

<script>
let currentRainMode = 'drizzle';
let currentWind = 'calm';

function setRainPhysics(mode, wind) {
    currentRainMode = mode;
    currentWind = wind;

    document.getElementById('btn-rain-drizzle').className = (mode === 'drizzle')
        ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2'
        : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
    document.getElementById('btn-rain-downpour').className = (mode === 'downpour')
        ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2'
        : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';

    const dx = (wind === 'gusty') ? 22 : 0;
    const len = (mode === 'downpour') ? 32 : 16;
    const sw = (mode === 'downpour') ? 3.5 : 1.5;

    const coords = [[90,40],[150,80],[210,55],[270,95],[330,45],[390,85],[450,50],[510,90],[570,60],[630,45],[120,120],[240,130],[480,125],[590,135]];
    const group = document.getElementById('rain-streaks-group');
    group.innerHTML = coords.map(c =>
        `<line x1="${c[0]}" y1="${c[1]}" x2="${c[0]-dx}" y2="${c[1]+len}" stroke="#38bdf8" stroke-width="${sw}" opacity="${mode === 'downpour' ? 0.95 : 0.65}" />`
    ).join('');

    document.getElementById('umbrella-tilt').setAttribute('transform', `rotate(${wind === 'gusty' ? 22 : 0} 15 10)`);
    document.getElementById('rain-puddle').setAttribute('rx', mode === 'downpour' ? 115 : 45);
    document.getElementById('wind-btn-title').textContent = (wind === 'gusty') ? 'Wind: Strong Gusts (Slanted!)' : 'Wind: Calm (0° Tilt)';
    document.getElementById('stat-drop-size').textContent = (mode === 'downpour') ? '~4.0 mm (Heavy Raindrops)' : '~0.4 mm (Fine Drizzle)';
    document.getElementById('stat-drop-sound').textContent = (mode === 'downpour') ? 'Thunderous Roof Drumbeat' : 'Soft Whisper on Leaves';
    document.getElementById('stat-drop-angle').textContent = (wind === 'gusty') ? 'Slanted Diagonal Path (~30°)' : 'Straight Vertical (0° Tilt)';
}
</script>
"""

# Simulator 4: Testing Rainwater Purity (Open Field vs Roof Runoff)
simulators_part1[4] = """
<div class="sim-container space-y-4" id="sim4-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🧪</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Rainwater Collection & Clarity Experiment</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Purity Check Lab</span>
    </div>

    <p class="text-xs text-slate-300">Compare rainwater collected directly from open skies against rooftop drainpipe water, then test cloth-and-sand filtration!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectJar('open')" id="btn-jar-open" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2">
            <span class="text-xl">🫙</span><span>1. Open Courtyard Jar</span>
        </button>
        <button onclick="inspectJar('roof')" id="btn-jar-roof" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🏠</span><span>2. Roof Drainpipe Jar</span>
        </button>
        <button onclick="inspectJar('filtered')" id="btn-jar-filtered" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2">
            <span class="text-xl">🔬</span><span>3. Filtered & Boiled</span>
        </button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <svg viewBox="0 0 320 200" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Jar Outline -->
            <rect x="95" y="45" width="130" height="130" rx="14" fill="#0f172a" stroke="#94a3b8" stroke-width="3" />
            <rect x="115" y="30" width="90" height="15" rx="4" fill="#475569" />
            <!-- Water Fill inside Jar -->
            <rect id="jar-water-rect" x="100" y="75" width="120" height="95" rx="10" fill="#38bdf8" opacity="0.65" />
            <!-- Floating Dirt Specks (Hidden for Open / Filtered) -->
            <g id="jar-dirt-specks" opacity="0">
                <circle cx="130" cy="110" r="3" fill="#78350f" />
                <circle cx="170" cy="140" r="4" fill="#451a03" />
                <circle cx="150" cy="155" r="3.5" fill="#78350f" />
                <ellipse cx="185" cy="105" rx="6" ry="2.5" fill="#713f12" />
                <circle cx="122" cy="152" r="2.5" fill="#451a03" />
            </g>
            <text id="jar-badge-txt" x="160" y="192" fill="#7dd3fc" font-size="11" font-weight="bold" text-anchor="middle">Sample A: Direct Sky Rain</text>
        </svg>

        <div class="space-y-2.5 text-xs">
            <h4 class="text-sm font-bold text-cyan-300" id="jar-title">Direct Sky Collection (Open Courtyard)</h4>
            <p class="text-slate-300 leading-relaxed" id="jar-desc">
                Placed safely away from overhanging roofs and leafy branches, this glass jar captures fresh raindrops directly from clouds. The collected sample looks crystal-clear and almost spotless!
            </p>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-[11px] space-y-1">
                <div><span class="text-slate-400">Water Color:</span> <strong id="jar-color" class="text-cyan-300">Crystal Clear</strong></div>
                <div><span class="text-slate-400">Safe to Drink Directly?:</span> <strong id="jar-drink" class="text-amber-300">Filter & Boil First</strong></div>
            </div>
        </div>
    </div>
</div>

<script>
function inspectJar(sample) {
    const info = {
        open: {
            fill: '#38bdf8', op: '0.65', dirt: '0',
            badge: 'Sample A: Direct Sky Rain',
            title: 'Direct Sky Collection (Open Courtyard)',
            desc: 'Placed safely away from overhanging roofs and leafy branches, this glass jar captures fresh raindrops directly from clouds. The collected sample looks crystal-clear and almost spotless!',
            color: 'Crystal Clear',
            drink: 'Strain & Boil Briefly to Be Safe'
        },
        roof: {
            fill: '#92400e', op: '0.75', dirt: '1',
            badge: 'Sample B: Rooftop Runoff Water',
            title: 'Rooftop Gutter Collection (Dirty First Flush)',
            desc: 'Water running off house tiles washes along dust, dried leaves, soot, and bird droppings settled during sunny weeks—turning the water cloudy brownish!',
            color: 'Muddy Brown with Specks',
            drink: 'NO! Must Discard First Flush & Purify'
        },
        filtered: {
            fill: '#22d3ee', op: '0.80', dirt: '0',
            badge: 'Sample C: Cloth Filtered + Boiled',
            title: 'Purified Rainwater (Ready for Safe Storage)',
            desc: 'After discarding the muddy first roof wash, passing water through clean cloth-and-sand layers traps sediment, and boiling eliminates invisible microbes safely!',
            color: 'Sparkling Pure & Clear',
            drink: 'YES! Clean & Germ-Free'
        }
    };
    const d = info[sample];
    if (!d) return;

    ['open', 'roof', 'filtered'].forEach(k => {
        const b = document.getElementById('btn-jar-' + k);
        if (b) {
            b.className = (k === sample)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left flex items-center gap-2'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left flex items-center gap-2';
        }
    });

    document.getElementById('jar-water-rect').setAttribute('fill', d.fill);
    document.getElementById('jar-water-rect').setAttribute('opacity', d.op);
    document.getElementById('jar-dirt-specks').setAttribute('opacity', d.dirt);
    document.getElementById('jar-badge-txt').textContent = d.badge;
    document.getElementById('jar-title').textContent = d.title;
    document.getElementById('jar-desc').textContent = d.desc;
    document.getElementById('jar-color').textContent = d.color;
    document.getElementById('jar-drink').textContent = d.drink;
}
</script>
"""

# Simulator 5: Soil Soaking Rainwater (Percolation vs Concrete Runoff)
simulators_part1[5] = """
<div class="sim-container space-y-4" id="sim5-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌱</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Ground Percolation vs Concrete Runoff Simulator</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Groundwater Recharge</span>
    </div>

    <p class="text-xs text-slate-300">Switch ground surface types to observe how soft soil recharges underground wells while sealed concrete triggers surface floods!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="setSurfaceType('soil')" id="btn-surf-soil" class="p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 flex items-center gap-2 text-left">
            <span class="text-2xl">🌿</span>
            <div><span class="block">Natural Porous Soil & Grass</span><span class="text-[10px] text-emerald-200">Percolation Refills Wells</span></div>
        </button>
        <button onclick="setSurfaceType('concrete')" id="btn-surf-concrete" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 flex items-center gap-2 text-left">
            <span class="text-2xl">🛣️</span>
            <div><span class="block">Sealed Concrete & Tar Road</span><span class="text-[10px] text-slate-400">Blocks Soaking -> Street Floods</span></div>
        </button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 240" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Sky & Rain -->
            <rect x="0" y="0" width="700" height="80" fill="#1e293b" />
            <text x="120" y="45" font-size="28">🌧️</text>
            <text x="310" y="45" font-size="28">🌧️</text>
            <text x="500" y="45" font-size="28">🌧️</text>

            <!-- Surface Layer -->
            <rect id="surf-top-bar" x="0" y="80" width="700" height="20" fill="#16a34a" />
            <!-- Deep Soil & Gravel Layer -->
            <rect x="0" y="100" width="700" height="85" fill="#5c2d16" />
            <!-- Underground Aquifer Chamber -->
            <rect x="0" y="185" width="700" height="55" fill="#1e293b" />
            <rect id="aquifer-water" x="0" y="195" width="700" height="45" fill="#0284c7" opacity="0.85" />

            <!-- Percolating Droplets (Soil Mode) -->
            <g id="percolate-arrows" fill="#38bdf8" font-size="14" font-weight="bold">
                <text x="140" y="135">💧↓</text>
                <text x="270" y="160">💧↓</text>
                <text x="410" y="140">💧↓</text>
                <text x="140" y="175">💧↓</text>
            </g>

            <!-- Street Flood Layer (Concrete Mode) -->
            <rect id="street-flood-bar" x="0" y="70" width="700" height="10" fill="#38bdf8" opacity="0" />

            <!-- Village Open Well on Right -->
            <rect x="570" y="55" width="75" height="165" fill="#475569" stroke="#94a3b8" stroke-width="2" />
            <rect id="well-water-level" x="575" y="140" width="65" height="75" fill="#38bdf8" />
            <text x="607" y="47" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Village Well</text>

            <text id="aquifer-label" x="280" y="220" fill="#e0f2fe" font-size="13" font-weight="bold" text-anchor="middle">Underground Aquifer: FULL &amp; RECHARGED</text>
        </svg>
    </div>

    <div class="bg-slate-900/90 p-3.5 rounded-xl border border-slate-800 text-xs flex items-center gap-3">
        <span class="text-2xl" id="surf-icon">💧</span>
        <p id="surf-summary" class="text-slate-200">
            Soft porous soil absorbs falling rain smoothly through microscopic grain gaps, naturally filtering water down into aquifers to keep village wells brimming during summer!
        </p>
    </div>
</div>

<script>
function setSurfaceType(type) {
    const isSoil = (type === 'soil');
    document.getElementById('btn-surf-soil').className = isSoil
        ? 'p-3 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500 flex items-center gap-2 text-left'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 flex items-center gap-2 text-left';
    document.getElementById('btn-surf-concrete').className = !isSoil
        ? 'p-3 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500 flex items-center gap-2 text-left'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 flex items-center gap-2 text-left';

    document.getElementById('surf-top-bar').setAttribute('fill', isSoil ? '#16a34a' : '#64748b');
    document.getElementById('percolate-arrows').setAttribute('opacity', isSoil ? '1' : '0');
    document.getElementById('street-flood-bar').setAttribute('opacity', isSoil ? '0' : '0.9');
    document.getElementById('aquifer-water').setAttribute('y', isSoil ? '190' : '225');
    document.getElementById('aquifer-water').setAttribute('height', isSoil ? '50' : '15');
    document.getElementById('well-water-level').setAttribute('y', isSoil ? '140' : '202');
    document.getElementById('well-water-level').setAttribute('height', isSoil ? '75' : '13');
    document.getElementById('aquifer-label').textContent = isSoil
        ? 'Underground Aquifer: FULL & RECHARGED'
        : 'Underground Aquifer: DEPLETED! (Street Flooding Above)';
    document.getElementById('surf-icon').textContent = isSoil ? '💧' : '⚠️';
    document.getElementById('surf-summary').textContent = isSoil
        ? 'Soft porous soil absorbs falling rain smoothly through microscopic grain gaps, naturally filtering water down into aquifers to keep village wells brimming during summer!'
        : 'Waterproof concrete and tar seal off the soil completely! Rainwater rushes across streets creating dangerous flash floods while underground wells run dry.';
}
</script>
"""

# Simulator 6: Streams To Oceans (Surface Rainwater Journey Map)
simulators_part1[6] = """
<div class="sim-container space-y-4" id="sim6-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🌊</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Surface Raindrop Journey: Puddles to Oceans</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Water Cycle Trail</span>
    </div>

    <p class="text-xs text-slate-300">Click each sequential stop to trace how flowing rainwater travels downhill across landscapes back to the sky!</p>

    <div class="grid grid-cols-2 sm:grid-cols-5 gap-2">
        <button onclick="moveDropStage(1)" id="btn-drop-1" class="p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">1. Puddle</button>
        <button onclick="moveDropStage(2)" id="btn-drop-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Stream</button>
        <button onclick="moveDropStage(3)" id="btn-drop-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. River</button>
        <button onclick="moveDropStage(4)" id="btn-drop-4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">4. Lake / Pond</button>
        <button onclick="moveDropStage(5)" id="btn-drop-5" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">5. Ocean &amp; Sun</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Sun in top right -->
            <circle cx="620" cy="42" r="24" fill="#fbbf24" />
            <!-- Mountains / Downhill Slope -->
            <polygon points="0,230 0,60 150,115 320,145 480,170 700,185 700,230" fill="#14532d" />
            <!-- Flowing Water Path -->
            <path d="M 60 85 Q 150 120 260 140 T 460 175 L 700 190 L 700 230 L 450 230 Q 250 165 60 95 Z" fill="#0284c7" opacity="0.8" />
            <!-- Ocean Basin Right -->
            <rect x="520" y="175" width="180" height="55" fill="#0369a1" />
            <!-- Evaporation Up Arrows -->
            <text x="605" y="135" fill="#fde047" font-size="14">⬆️☁️</text>

            <!-- Labels -->
            <text x="65" y="75" fill="#bae6fd" font-size="10" font-weight="bold">Puddle</text>
            <text x="200" y="112" fill="#bae6fd" font-size="10" font-weight="bold">Hill Stream</text>
            <text x="340" y="138" fill="#bae6fd" font-size="10" font-weight="bold">Broad River</text>
            <text x="455" y="162" fill="#bae6fd" font-size="10" font-weight="bold">Pond/Lake</text>
            <text x="600" y="210" fill="#e0f2fe" font-size="11" font-weight="bold">Vast Salty Ocean</text>

            <!-- Active Droplet Token -->
            <g id="journey-drop-token" transform="translate(75, 92)">
                <circle cx="0" cy="0" r="14" fill="#38bdf8" stroke="#ffffff" stroke-width="2.5" />
                <text x="-8" y="5" font-size="15">💧</text>
            </g>
        </svg>
    </div>

    <div class="bg-slate-900/90 p-3.5 rounded-xl border border-cyan-800/60 text-xs">
        <h4 class="font-bold text-cyan-300 text-sm mb-1" id="drop-stage-title">Stage 1: Shimmering Courtyard Puddle</h4>
        <p class="text-slate-300" id="drop-stage-desc">Initial rainwater fills shallow stone depressions and grassy hollows into sparkling puddles where joyful sparrows splash and paper boats float!</p>
    </div>
</div>

<script>
function moveDropStage(stage) {
    const stages = {
        1: { x: 75, y: 92, title: 'Stage 1: Shimmering Courtyard Puddle', desc: 'Initial rainwater fills shallow stone depressions and grassy hollows into sparkling puddles where joyful sparrows splash and paper boats float!' },
        2: { x: 215, y: 128, title: 'Stage 2: Bubbling Hillside Stream', desc: 'Overflow from thousands of brimming puddles merges downward along slopes into lively mountain brooks bubbling over pebbles.' },
        3: { x: 350, y: 152, title: 'Stage 3: Mighty Flowing River', desc: 'Tributary streams unite into wide freshwater rivers winding across lush plains, nourishing green farmlands, cities, and riparian trees.' },
        4: { x: 465, y: 175, title: 'Stage 4: Tranquil Lake & Village Pond', desc: 'Natural landscape basins trap freshwater into peaceful lakes and ponds sheltering lotus blooms, frogs, fish, and wading herons.' },
        5: { x: 600, y: 185, title: 'Stage 5: Endless Ocean & Solar Evaporation', desc: 'Rivers deliver waters to vast salty oceans. Sun warmth lifts invisible water vapor back skyward—closing nature\\'s eternal water cycle!' }
    };
    const s = stages[stage];
    if (!s) return;

    for (let i = 1; i <= 5; i++) {
        const b = document.getElementById('btn-drop-' + i);
        if (b) {
            b.className = (i === stage)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    }
    document.getElementById('journey-drop-token').setAttribute('transform', `translate(${s.x}, ${s.y})`);
    document.getElementById('drop-stage-title').textContent = s.title;
    document.getElementById('drop-stage-desc').textContent = s.desc;
}
</script>
"""

# Simulator 7: Home Water Pipes (Gravity Overhead Tank Plumbing)
simulators_part1[7] = """
<div class="sim-container space-y-4" id="sim7-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🚰</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Overhead Rooftop Tank & Home Pipe Network</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Gravity Plumbing</span>
    </div>

    <p class="text-xs text-slate-300">Operate the municipal treatment pump and lower-floor taps to watch how rooftop height uses gravity to feed sinks smoothly!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="toggleHomePipe('pump')" id="btn-pipe-pump" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">1. Fill Rooftop Tank</button>
        <button onclick="toggleHomePipe('kitchen')" id="btn-pipe-kitchen" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">2. Open Kitchen Tap</button>
        <button onclick="toggleHomePipe('garden')" id="btn-pipe-garden" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">3. Open Yard Hose</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 text-center">
        <svg viewBox="0 0 700 230" class="w-full h-auto rounded-xl bg-slate-950 border border-slate-800">
            <!-- Street Underground Pipe -->
            <rect x="0" y="200" width="220" height="14" fill="#0284c7" />
            <text x="95" y="224" fill="#7dd3fc" font-size="10" font-weight="bold" text-anchor="middle">Purified City Supply Pipe</text>

            <!-- House Wall & Floors -->
            <rect x="220" y="65" width="320" height="150" fill="#1e293b" stroke="#475569" stroke-width="3" />
            <line x1="220" y1="140" x2="540" y2="140" stroke="#475569" stroke-width="2" />

            <!-- Overhead Rooftop Tank -->
            <rect x="440" y="15" width="85" height="50" rx="6" fill="#0f172a" stroke="#38bdf8" stroke-width="3" />
            <rect id="rooftop-water" x="443" y="22" width="79" height="40" fill="#0284c7" />
            <text x="482" y="12" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Rooftop Tank</text>

            <!-- Supply Pipe Up & Down -->
            <polyline points="200,207 200,40 440,40" fill="none" stroke="#38bdf8" stroke-width="5" />
            <polyline points="482,65 482,175 300,175" fill="none" stroke="#0ea5e9" stroke-width="5" />

            <!-- Kitchen Sink on Ground Floor -->
            <rect x="265" y="170" width="45" height="22" rx="3" fill="#cbd5e1" />
            <text x="288" y="205" fill="#94a3b8" font-size="10" text-anchor="middle">Kitchen Tap</text>
            <text id="kitchen-stream" x="287" y="168" font-size="16" opacity="0">💧</text>

            <!-- Garden Yard Hose Right -->
            <path d="M 525 175 L 610 175" stroke="#22c55e" stroke-width="4" />
            <text id="garden-stream" x="620" y="180" font-size="18" opacity="0">💦</text>
            <text x="640" y="200" font-size="24">🪴</text>
        </svg>
    </div>

    <div class="bg-slate-900/90 p-3.5 rounded-xl border border-cyan-800/60 text-xs">
        <p id="pipe-status-text" class="text-slate-200">
            <strong class="text-cyan-300">Gravity Pressure Active:</strong> Purified water pumped from municipal treatment plants fills the high rooftop tank. Gravity pushes it smoothly downstairs whenever any tap opens!
        </p>
    </div>
</div>

<script>
function toggleHomePipe(mode) {
    ['pump', 'kitchen', 'garden'].forEach(k => {
        const b = document.getElementById('btn-pipe-' + k);
        if (b) {
            b.className = (k === mode)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('kitchen-stream').setAttribute('opacity', mode === 'kitchen' ? '1' : '0');
    document.getElementById('garden-stream').setAttribute('opacity', mode === 'garden' ? '1' : '0');
    document.getElementById('rooftop-water').setAttribute('y', mode === 'pump' ? '20' : '32');
    document.getElementById('rooftop-water').setAttribute('height', mode === 'pump' ? '42' : '30');

    const msgs = {
        pump: '<strong class="text-cyan-300">Tank Refilled Cleanly:</strong> Municipal filtration clears river mud and germs before main pipes pump safe water up into the rooftop tank.',
        kitchen: '<strong class="text-cyan-300">Kitchen Tap Flowing:</strong> Water stored high on the roof rushes downward via gravity through sealed indoor pipes directly to kitchen sinks!',
        garden: '<strong class="text-emerald-300">Measured Garden Hydrating:</strong> Always shut outdoor yard valves tightly once plants are watered so overhead tanks do not drain wastefully!'
    };
    document.getElementById('pipe-status-text').innerHTML = msgs[mode];
}
</script>
"""

# Simulator 8: Village Water Sources (Pulley, Hand Pump, Electric Pump, Tanker)
simulators_part1[8] = """
<div class="sim-container space-y-4" id="sim8-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🪣</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Community Water-Lifting Devices Explorer</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Wells &amp; Pumps</span>
    </div>

    <p class="text-xs text-slate-300">Inspect four clever ways communities gather fresh groundwater and emergency supplies when pipeline grids are absent!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectWaterLifter('pulley')" id="btn-lift-pulley" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-center">🛞 Well + Pulley</button>
        <button onclick="selectWaterLifter('handpump')" id="btn-lift-handpump" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">🔩 Iron Hand Pump</button>
        <button onclick="selectWaterLifter('motor')" id="btn-lift-motor" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">⚡ Electric Pump</button>
        <button onclick="selectWaterLifter('tanker')" id="btn-lift-tanker" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center">🚚 Water Tanker</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <div class="bg-slate-950 rounded-xl p-5 border border-slate-800 text-center space-y-2">
            <div class="text-5xl" id="lifter-emoji">🛞🪣</div>
            <div class="text-sm font-bold text-cyan-300" id="lifter-name">Stone Open Well with Pulley Wheel</div>
            <span class="inline-block px-2.5 py-0.5 rounded-full bg-slate-800 text-amber-300 text-[10px] font-semibold" id="lifter-power">Power Source: Human Pull + Simple Machine</span>
        </div>

        <div class="space-y-2.5 text-xs">
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span class="text-emerald-400 font-bold block mb-1">How It Works:</span>
                <p id="lifter-desc" class="text-slate-300">A grooved wheel mounted over the open stone well lets villagers pull downward smoothly to hoist heavy water buckets upward with less strain.</p>
            </div>
            <div class="bg-slate-950 p-3 rounded-xl border border-slate-800">
                <span class="text-cyan-400 font-bold block mb-1">Key Strength:</span>
                <p id="lifter-strength" class="text-slate-300">Works reliably without electricity and taps naturally filtered groundwater inside stone wells.</p>
            </div>
        </div>
    </div>
</div>

<script>
function selectWaterLifter(type) {
    const map = {
        pulley: {
            emoji: '🛞🪣', name: 'Stone Open Well with Pulley Wheel', power: 'Power Source: Human Pull + Simple Machine',
            desc: 'A grooved wheel mounted over the open stone well lets villagers pull downward smoothly to hoist heavy water buckets upward with less strain.',
            strength: 'Works reliably without electricity and taps naturally filtered groundwater inside stone wells.'
        },
        handpump: {
            emoji: '🔩💧', name: 'Village Iron Lever Hand Pump', power: 'Power Source: Muscle Lever Suction',
            desc: 'Pumping the iron handle up and down lifts internal piston suction valves, drawing cool deep borehole water straight out of the clean metal spout.',
            strength: 'Sealed narrow pipe blocks falling surface dust and leaves—delivering safer drinking water anywhere without power!'
        },
        motor: {
            emoji: '⚡🚰', name: 'Electric Submersible Borewell Pump', power: 'Power Source: Electric Motor Impeller',
            desc: 'A sealed waterproof motor sits submerged far underground, spinning blades briskly to pump large volumes up to farm canals and village storage tanks.',
            strength: 'Lifts high volumes rapidly from very deep aquifers, though requires electricity and careful limits so groundwater is not over-pumped.'
        },
        tanker: {
            emoji: '🚚💦', name: 'Municipal Road Water Tanker & Pot Carriers', power: 'Power Source: Diesel Vehicle / Manual Carry',
            desc: 'During dry scorching summers when village wells dry out, bright yellow municipal tankers transport clean water miles down dusty roads to waiting families.',
            strength: 'Crucial emergency lifeline during severe droughts, reminding urban residents never to waste piped water!'
        }
    };
    const d = map[type];
    if (!d) return;

    ['pulley', 'handpump', 'motor', 'tanker'].forEach(k => {
        const b = document.getElementById('btn-lift-' + k);
        if (b) {
            b.className = (k === type)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-center'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-center';
        }
    });
    document.getElementById('lifter-emoji').textContent = d.emoji;
    document.getElementById('lifter-name').textContent = d.name;
    document.getElementById('lifter-power').textContent = d.power;
    document.getElementById('lifter-desc').textContent = d.desc;
    document.getElementById('lifter-strength').textContent = d.strength;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part1)} simulators for Part 1 (1 to 8).")
    for k in sorted(simulators_part1.keys()):
        print(f"Sim {k}: {len(simulators_part1[k])} chars")
