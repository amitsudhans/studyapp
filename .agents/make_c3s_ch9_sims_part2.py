#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 9: Staying Healthy and Happy
Interactive Simulators Generator - Part 2 (Simulators 9 to 16)
"""

simulators_part2 = {}

# Simulator 9: Safe Play Zones
simulators_part2[9] = """
<div class="sim-container space-y-4" id="sim9-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏞️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Safe Playgrounds &amp; Curb-Stop Decision Explorer</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Play Safety #1</span>
    </div>

    <p class="text-xs text-slate-300">Inspect verified safe play zones and test the smart curb rule whenever a bouncing ball heads toward an open street gate!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectSafePlace('park')" id="btn-sp-park" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">🌳 Fenced Grass Park</button>
        <button onclick="inspectSafePlace('school')" id="btn-sp-school" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏫 School Playground</button>
        <button onclick="inspectSafePlace('curb')" id="btn-sp-curb" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">⚽ Ball Near Street Gate</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="sp-emoji">🌳✅</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="sp-title">Fenced Public Parks With Soft Green Lawns</h4>
            <p class="text-slate-300" id="sp-desc">Safe perimeter fences keep traffic completely separated from running children, while level grassy lawns cushion slips during tag, cricket, and skipping games!</p>
        </div>
    </div>
</div>

<script>
function inspectSafePlace(p) {
    const map = {
        park: { e: '🌳✅', t: 'Fenced Public Parks With Soft Green Lawns', d: 'Safe perimeter fences keep traffic completely separated from running children, while level grassy lawns cushion slips during tag, cricket, and skipping games!' },
        school: { e: '🏫✅', t: 'Supervised School Sports Grounds', d: 'Watchful teachers, clean level grounds free of broken glass or rusted nails, and calm open sightlines ensure carefree joyful sports!' },
        curb: { e: '🛑⚽', t: 'Curb-Stop Rule: NEVER Chase Balls Into Moving Streets!', d: 'Freeze immediately at the safe gate edge whenever a ball rolls outside—always ask a watchful parent or guard to retrieve it after checking traffic!' }
    };
    const d = map[p];
    if (!d) return;

    ['park', 'school', 'curb'].forEach(k => {
        const b = document.getElementById('btn-sp-' + k);
        if (b) {
            b.className = (k === p)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('sp-emoji').textContent = d.e;
    document.getElementById('sp-title').textContent = d.t;
    document.getElementById('sp-desc').textContent = d.d;
}
</script>
"""

# Simulator 10: Hazards Around Sites
simulators_part2[10] = """
<div class="sim-container space-y-4" id="sim10-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">⚠️</span>
            <h3 class="text-sm sm:text-base font-bold text-rose-300">Hazard Detector: Three Strictly Off-Limits Zones</h3>
        </div>
        <span class="text-[11px] bg-rose-950/80 text-rose-300 px-2.5 py-1 rounded-full border border-rose-800">Play Safety #2</span>
    </div>

    <p class="text-xs text-slate-300">Inspect three dangerous everyday places that look exciting for play yet hide serious injury risks—always avoid them!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectHazard('road')" id="btn-hz-road" class="p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500">🚗 Busy Traffic Road</button>
        <button onclick="inspectHazard('roof')" id="btn-hz-roof" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🏢 Unrailed Open Roof</button>
        <button onclick="inspectHazard('site')" id="btn-hz-site" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🚧 Construction Site</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="hz-emoji">🚗🚫</div>
        <div class="space-y-1">
            <h4 class="font-bold text-rose-300 text-sm" id="hz-title">Danger #1: Busy Roads &amp; Unguarded Corners</h4>
            <p class="text-slate-300" id="hz-desc">Heavy buses and fast scooters sit high above small children and cannot brake instantaneously! Never turn streets or driveways into playfields.</p>
        </div>
    </div>
</div>

<script>
function inspectHazard(hz) {
    const map = {
        road: { e: '🚗🚫', t: 'Danger #1: Busy Roads & Unguarded Corners', d: 'Heavy buses and fast scooters sit high above small children and cannot brake instantaneously! Never turn streets or driveways into playfields.' },
        roof: { e: '🏢🚫', t: 'Danger #2: Rooftops Lacking Sturdy Guard Railings', d: 'When staring upward flying kites or chasing bouncy balls backward, one tiny unnoticed step over an unrailed edge causes catastrophic falls!' },
        site: { e: '🚧🚫', t: 'Danger #3: Active Building & Construction Lots', d: 'Protruding rusted iron nails, slippery wet cement, deep open ditches, and unstable brick stacks make construction zones strictly off-limits!' }
    };
    const d = map[hz];
    if (!d) return;

    ['road', 'roof', 'site'].forEach(k => {
        const b = document.getElementById('btn-hz-' + k);
        if (b) {
            b.className = (k === hz)
                ? 'p-2.5 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('hz-emoji').textContent = d.e;
    document.getElementById('hz-title').textContent = d.t;
    document.getElementById('hz-desc').textContent = d.d;
}
</script>
"""

# Simulator 11: Smart Stranger Safety
simulators_part2[11] = """
<div class="sim-container space-y-4" id="sim11-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🛡️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Public Stranger Safety Action Drill</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Personal Boundaries</span>
    </div>

    <p class="text-xs text-slate-300">Practice confident street-smart safety steps across three common public situations involving unfamiliar adults!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="practiceStranger('candy')" id="btn-st-candy" class="p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500">🍬 Free Gift / Candy</button>
        <button onclick="practiceStranger('ride')" id="btn-st-ride" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🚙 Unverified Ride Offer</button>
        <button onclick="practiceStranger('shout')" id="btn-st-shout" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">📢 Grabbed Arm Alert</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="str-emoji">🍬✋</div>
        <div class="space-y-1">
            <h4 class="font-bold text-cyan-300 text-sm" id="str-title">Golden Rule #1: Say 'NO Thank You' to Stranger Gifts</h4>
            <p class="text-slate-300" id="str-desc">Even if an unfamiliar adult smiles warmly, NEVER accept sweets, snacks, or shiny toys without parent permission—step back calmly toward family!</p>
        </div>
    </div>
</div>

<script>
function practiceStranger(sc) {
    const map = {
        candy: { e: '🍬✋', t: 'Golden Rule #1: Say "NO Thank You" to Stranger Gifts', d: 'Even if an unfamiliar adult smiles warmly, NEVER accept sweets, snacks, or shiny toys without parent permission—step back calmly toward family!' },
        ride: { e: '🚙🚫', t: 'Golden Rule #2: NEVER Enter Unverified Pickup Vehicles', d: 'If someone claims parents sent them late to drive you home, refuse firmly, stay inside school gates, and ask teachers to call parents directly!' },
        shout: { e: '📢🏃', t: 'Golden Rule #3: Shout Loudly & Run Into Bright Crowds!', d: 'If an unknown person blocks your path or pulls your sleeve, shout "NO! Help, I don\\'t know this person!" and dash to crowded shops or security guards!' }
    };
    const d = map[sc];
    if (!d) return;

    ['candy', 'ride', 'shout'].forEach(k => {
        const b = document.getElementById('btn-st-' + k);
        if (b) {
            b.className = (k === sc)
                ? 'p-2.5 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('str-emoji').textContent = d.e;
    document.getElementById('str-title').textContent = d.t;
    document.getElementById('str-desc').textContent = d.d;
}
</script>
"""

# Simulator 12: Identifying Trusted Adults
simulators_part2[12] = """
<div class="sim-container space-y-4" id="sim12-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">👮</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Trusted Helpers &amp; Emergency Memory Card</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Safe Preparation</span>
    </div>

    <p class="text-xs text-slate-300">Explore who counts as a verified trusted helper when lost in busy places, plus essential family facts every student must memorize!</p>

    <div class="grid grid-cols-1 sm:grid-cols-3 gap-2">
        <button onclick="inspectTrusted('police')" id="btn-tr-police" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">👮 Uniformed Police / Guard</button>
        <button onclick="inspectTrusted('desk')" id="btn-tr-desk" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🛎️ Help Desk / Cashier</button>
        <button onclick="inspectTrusted('memory')" id="btn-tr-memory" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">📞 Address &amp; Phone Card</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 flex items-center gap-4 text-xs">
        <div class="text-5xl p-3 rounded-xl bg-slate-900 border border-slate-800" id="tr-emoji">👮‍♂️🛡️</div>
        <div class="space-y-1">
            <h4 class="font-bold text-emerald-300 text-sm" id="tr-title">Uniformed Police Officers &amp; Security Guards</h4>
            <p class="text-slate-300" id="tr-desc">Look for official uniforms, name badges, and fixed guard posts—police and school security staff have radios and phones ready to contact your family swiftly!</p>
        </div>
    </div>
</div>

<script>
function inspectTrusted(t) {
    const map = {
        police: { e: '👮‍♂️🛡️', t: 'Uniformed Police Officers & Security Guards', d: 'Look for official uniforms, name badges, and fixed guard posts—police and school security staff have radios and phones ready to contact your family swiftly!' },
        desk: { e: '🛎️🏪', t: 'Station Help Desks & Store Checkout Cashiers', d: 'If separated inside a fair, railway hall, or large mall, step straight to an official information booth or bright store billing counter and wait there calmly!' },
        memory: { e: '📞🏠', t: 'Memorize: Home Address + Parent Phone + Safety Codeword', d: 'Practice repeating your full street address, one parent\\'s 10-digit mobile number, and secret family pickup password so official helpers reunite you fast!' }
    };
    const d = map[t];
    if (!d) return;

    ['police', 'desk', 'memory'].forEach(k => {
        const b = document.getElementById('btn-tr-' + k);
        if (b) {
            b.className = (k === t)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('tr-emoji').textContent = d.e;
    document.getElementById('tr-title').textContent = d.t;
    document.getElementById('tr-desc').textContent = d.d;
}
</script>
"""

# Simulator 13: Refreshing Sleep Rest
simulators_part2[13] = """
<div class="sim-container space-y-4" id="sim13-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">😴</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">Nighttime Sleep Maintenance Workshop Simulator</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Restorative Sleep</span>
    </div>

    <p class="text-xs text-slate-300">Compare late midnight phone screen watching against 8.5 hours of peaceful sleep to witness inside-the-body growth &amp; memory effects!</p>

    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3">
        <button onclick="setSleepMode('late')" id="btn-sl-late" class="p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left">
            <span class="block">📱 Midnight Flashing Screens (5 Hrs)</span>
            <span class="text-[10px] text-rose-400">Interrupted Sleep Cycle</span>
        </button>
        <button onclick="setSleepMode('good')" id="btn-sl-good" class="p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left shadow">
            <span class="block">🌙 Screen-Free Early Sleep (8.5 Hrs)</span>
            <span class="text-[10px] text-cyan-200">Full Repair Workshop</span>
        </button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 sm:grid-cols-3 gap-3 text-center text-xs">
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Bone Growth Hormones:</span>
            <span id="sl-growth" class="font-bold text-emerald-400 text-sm">Peak Night Release ✓</span>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-slate-400 block text-[10px]">School Memory Filing:</span>
            <span id="sl-memory" class="font-bold text-cyan-300 text-sm">Sharp &amp; Organized ✓</span>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-slate-400 block text-[10px]">Morning Mood &amp; Focus:</span>
            <span id="sl-mood" class="font-bold text-amber-300 text-sm">Smiling &amp; Alert 😄</span>
        </div>
    </div>
</div>

<script>
function setSleepMode(m) {
    const isGood = (m === 'good');
    document.getElementById('btn-sl-good').className = isGood
        ? 'p-3 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500 text-left shadow'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';
    document.getElementById('btn-sl-late').className = !isGood
        ? 'p-3 rounded-xl bg-rose-600 text-white font-bold text-xs border border-rose-500 text-left shadow'
        : 'p-3 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800 text-left';

    document.getElementById('sl-growth').textContent = isGood ? 'Peak Night Release ✓' : 'Low / Cut Short ⚠️';
    document.getElementById('sl-growth').className = isGood ? 'font-bold text-emerald-400 text-sm' : 'font-bold text-rose-400 text-sm';
    document.getElementById('sl-memory').textContent = isGood ? 'Sharp & Organized ✓' : 'Foggy & Forgetful ⚠️';
    document.getElementById('sl-mood').textContent = isGood ? 'Smiling & Alert 😄' : 'Yawning & Grumpy 🥱';
}
</script>
"""

# Simulator 14: Weekly Mood Logs
simulators_part2[14] = """
<div class="sim-container space-y-4" id="sim14-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🗓️</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Seven-Day Habits &amp; Happiness Reflection Log</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Weekly Self-Check</span>
    </div>

    <p class="text-xs text-slate-300">Click across all seven days of a student's wellness diary to spot how daily habits directly shape body energy and joyful mood!</p>

    <div class="grid grid-cols-4 sm:grid-cols-7 gap-1.5">
        <button onclick="viewMoodDay(0)" id="btn-md-0" class="p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">Mon 😄</button>
        <button onclick="viewMoodDay(1)" id="btn-md-1" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Tue 😄</button>
        <button onclick="viewMoodDay(2)" id="btn-md-2" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Wed 🥱</button>
        <button onclick="viewMoodDay(3)" id="btn-md-3" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Thu 😄</button>
        <button onclick="viewMoodDay(4)" id="btn-md-4" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Fri 🤕</button>
        <button onclick="viewMoodDay(5)" id="btn-md-5" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Sat 😄</button>
        <button onclick="viewMoodDay(6)" id="btn-md-6" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">Sun 😄</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-3 text-xs">
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] uppercase block">Practiced Healthy Habits:</span>
            <p id="md-habits" class="text-slate-200 mt-1 font-medium">Brushed twice, 7 glasses water, hearty dal-roti lunch, 1 hr soccer in park, 8.5 hrs sleep.</p>
        </div>
        <div class="bg-slate-900 p-3 rounded-xl border border-slate-800">
            <span class="text-slate-400 text-[10px] uppercase block">Body Energy &amp; Emotional Mood:</span>
            <p id="md-mood" class="text-emerald-300 mt-1 font-bold">Bright, cheerful, sharp during math puzzles, and slept peacefully at 9 PM!</p>
        </div>
    </div>
</div>

<script>
const moodDays = [
    { h: 'Brushed twice, 7 glasses water, hearty dal-roti lunch, 1 hr soccer in park, 8.5 hrs sleep.', m: 'Bright, cheerful, sharp during math puzzles, and slept peacefully at 9 PM!', mc: 'text-emerald-300 mt-1 font-bold' },
    { h: 'Morning neem datun & bath, crisp fruit chaat snack, chess indoors + skipping rhymes outdoors.', m: 'Calm focus, friendly patience with teammates, joyful confidence all evening!', mc: 'text-emerald-300 mt-1 font-bold' },
    { h: 'Stayed awake late watching cartoons (only 5.5 hrs sleep), rushed morning with 2 glasses water.', m: 'Yawning through reading class, sluggish legs, grumpy afternoon irritation!', mc: 'text-amber-300 mt-1 font-bold' },
    { h: 'Back to 9 PM early bedtime, full 7 glasses water, duck walks & frog jumps outside.', m: 'Recharged wonderfully! Active bouncing legs and happy smiles with parents.', mc: 'text-emerald-300 mt-1 font-bold' },
    { h: 'Forgot afternoon water bottle completely during hot play, ate salty chips instead of lunch.', m: 'Mild thirst headache and tired slump—drank fresh coconut water & felt better!', mc: 'text-rose-300 mt-1 font-bold' },
    { h: 'Trimmed nails neat, washed hands 20s with soap, helped wipe kitchen table & park tag!', m: 'Proud family helper, energetic sprints, and sparkling cleanliness.', mc: 'text-emerald-300 mt-1 font-bold' },
    { h: 'Prepared lemon citrus cleaner with elders, balanced 24-hr wheel, calm early bed.', m: 'Deep gratitude, fresh happy spirit ready for joyful Monday morning!', mc: 'text-emerald-300 mt-1 font-bold' }
];

function viewMoodDay(idx) {
    const d = moodDays[idx];
    if (!d) return;
    for (let i = 0; i < 7; i++) {
        const b = document.getElementById('btn-md-' + i);
        if (b) {
            b.className = (i === idx)
                ? 'p-2 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    }
    document.getElementById('md-habits').textContent = d.h;
    document.getElementById('md-mood').textContent = d.m;
    document.getElementById('md-mood').className = d.mc;
}
</script>
"""

# Simulator 15: Daily Time Wheel (Interactive 24-Hour Pie Chart)
simulators_part2[15] = """
<div class="sim-container space-y-4" id="sim15-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🕰️</span>
            <h3 class="text-sm sm:text-base font-bold text-cyan-300">24-Hour Daily Routine Pie Wheel Explorer</h3>
        </div>
        <span class="text-[11px] bg-cyan-950/80 text-cyan-300 px-2.5 py-1 rounded-full border border-cyan-800">Time Allocation</span>
    </div>

    <p class="text-xs text-slate-300">Click each slice of the 24-hour pie chart to inspect how healthy students balance sleep, school, meals, play, and helping parents!</p>

    <div class="grid grid-cols-2 sm:grid-cols-5 gap-1.5">
        <button onclick="selectPieSlice('sleep')" id="btn-pie-sleep" class="p-2 rounded-xl bg-indigo-600 text-white font-bold text-xs border border-indigo-500">😴 Sleep (8h)</button>
        <button onclick="selectPieSlice('study')" id="btn-pie-study" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">📚 Study (7h)</button>
        <button onclick="selectPieSlice('eat')" id="btn-pie-eat" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍽️ Meals (2h)</button>
        <button onclick="selectPieSlice('play')" id="btn-pie-play" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">⚽ Play (2h)</button>
        <button onclick="selectPieSlice('help')" id="btn-pie-help" class="p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🤝 Home (5h)</button>
    </div>

    <div class="bg-slate-900/90 rounded-2xl p-4 border border-slate-800 grid grid-cols-1 md:grid-cols-2 gap-4 items-center">
        <!-- SVG 24-Hour Pie Chart -->
        <svg viewBox="0 0 220 220" class="w-48 h-48 mx-auto">
            <!-- Sleep: 8h = 120deg (from 0 to 120 deg -> top to lower right) -->
            <path d="M 110 110 L 110 20 A 90 90 0 0 1 187.9 155 Z" fill="#4f46e5" stroke="#0f172a" stroke-width="2" class="cursor-pointer" onclick="selectPieSlice('sleep')" />
            <!-- Study: 7h = 105deg (120 to 225 deg) -->
            <path d="M 110 110 L 187.9 155 A 90 90 0 0 1 46.4 173.6 Z" fill="#0284c7" stroke="#0f172a" stroke-width="2" class="cursor-pointer" onclick="selectPieSlice('study')" />
            <!-- Eat & Hygiene: 2h = 30deg (225 to 255 deg) -->
            <path d="M 110 110 L 46.4 173.6 A 90 90 0 0 1 23.1 133.3 Z" fill="#f59e0b" stroke="#0f172a" stroke-width="2" class="cursor-pointer" onclick="selectPieSlice('eat')" />
            <!-- Play Outdoors/Indoors: 2h = 30deg (255 to 285 deg) -->
            <path d="M 110 110 L 23.1 133.3 A 90 90 0 0 1 23.1 86.7 Z" fill="#10b981" stroke="#0f172a" stroke-width="2" class="cursor-pointer" onclick="selectPieSlice('play')" />
            <!-- Helping Parents & Hobbies: 5h = 75deg (285 to 360 deg) -->
            <path d="M 110 110 L 23.1 86.7 A 90 90 0 0 1 110 20 Z" fill="#ec4899" stroke="#0f172a" stroke-width="2" class="cursor-pointer" onclick="selectPieSlice('help')" />
            <circle cx="110" cy="110" r="30" fill="#0f172a" />
            <text x="110" y="106" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">24 Hours</text>
            <text x="110" y="121" fill="#38bdf8" font-size="9" text-anchor="middle">Total Day</text>
        </svg>

        <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 space-y-2 text-xs">
            <h4 class="font-bold text-indigo-300 text-sm" id="pie-title">Sleep &amp; Night Rest — 8 Hours (One-Third of Day)</h4>
            <p class="text-slate-300 leading-relaxed" id="pie-desc">
                One-third of our entire 24-hour day recharges growing bones, immune shields, and daytime memories cleanly—keeping screens off early preserves this vital slice!
            </p>
        </div>
    </div>
</div>

<script>
function selectPieSlice(sl) {
    const map = {
        sleep: { c: 'font-bold text-indigo-300 text-sm', t: 'Sleep & Night Rest — 8 Hours (One-Third of Day)', d: 'One-third of our entire 24-hour day recharges growing bones, immune shields, and daytime memories cleanly—keeping screens off early preserves this vital slice!' },
        study: { c: 'font-bold text-sky-300 text-sm', t: 'School Learning & Homework — 7 Hours', d: 'Focused classroom discovery, science experiments, reading storybooks, and neat unhurried afternoon homework build curious confident minds!' },
        eat: { c: 'font-bold text-amber-300 text-sm', t: 'Meals, Brushing & Clean Hygiene — 2 Hours', d: 'Unhurried breakfast, lunch, dinner, 20-second handwashing, daily showers, and brushing twice daily keep nourishment and cleanliness steady.' },
        play: { c: 'font-bold text-emerald-300 text-sm', t: 'Outdoor Sports & Mindful Board Play — 2 Hours', d: 'Energetic park tag, frog jumps, skipping rhymes, or indoor chess and carrom keep hearts beating strongly and minds nimble!' },
        help: { c: 'font-bold text-pink-300 text-sm', t: 'Helping Parents, Family Chat & Hobbies — 5 Hours', d: 'Folding uniforms, watering plants, drawing, chatting warmly with grandparents, and quiet relaxation round out a joyful balanced day!' }
    };
    const d = map[sl];
    if (!d) return;

    ['sleep', 'study', 'eat', 'play', 'help'].forEach(k => {
        const b = document.getElementById('btn-pie-' + k);
        if (b) {
            b.className = (k === sl)
                ? 'p-2 rounded-xl bg-cyan-600 text-white font-bold text-xs border border-cyan-500'
                : 'p-2 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('pie-title').textContent = d.t;
    document.getElementById('pie-title').className = d.c;
    document.getElementById('pie-desc').textContent = d.d;
}
</script>
"""

# Simulator 16: Helping Happy Homes (Family Chores & Chapter Synthesis)
simulators_part2[16] = """
<div class="sim-container space-y-4" id="sim16-container">
    <div class="flex items-center justify-between pb-2 border-b border-slate-700/60">
        <div class="flex items-center gap-2">
            <span class="text-xl">🏡</span>
            <h3 class="text-sm sm:text-base font-bold text-emerald-300">Happy Home Helper &amp; Whole-Wellness Synthesis</h3>
        </div>
        <span class="text-[11px] bg-emerald-950/80 text-emerald-300 px-2.5 py-1 rounded-full border border-emerald-800">Chapter 9 Finale</span>
    </div>

    <p class="text-xs text-slate-300">Select thoughtful home chores below to grow proud family belonging and complete Chapter 9's Healthy &amp; Happy Circle!</p>

    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2">
        <button onclick="selectHomeChore('fold')" id="btn-hc-fold" class="p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500">👕 Fold Uniforms</button>
        <button onclick="selectHomeChore('water')" id="btn-hc-water" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🪴 Water Plants</button>
        <button onclick="selectHomeChore('wipe')" id="btn-hc-wipe" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🧽 Wipe Table</button>
        <button onclick="selectHomeChore('clean')" id="btn-hc-clean" class="p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800">🍊 Eco Cleaning</button>
    </div>

    <div class="bg-slate-950 rounded-2xl p-4 border border-emerald-800/50 space-y-2.5 text-xs">
        <div class="flex items-center gap-3">
            <span class="text-4xl" id="hc-emoji">👕✨</span>
            <div>
                <h4 class="font-bold text-emerald-300 text-sm" id="hc-title">Organizing Clean School Uniforms &amp; Shoes</h4>
                <p class="text-slate-300 mt-0.5" id="hc-desc">Arranging tomorrow's school uniform and placing dusty shoes neatly beside doors prevents rushed morning stress and builds proud responsibility!</p>
            </div>
        </div>
        <div class="bg-slate-900 p-2.5 rounded-xl border border-slate-800 text-amber-300 font-semibold text-[11px]">
            🌟 Chapter 9 Mastery Formula: Clean Hygiene + Active Body &amp; Mind Play + Safe Choices + Sound 8-Hour Sleep + Helping Hands = Healthy &amp; Happy Life!
        </div>
    </div>
</div>

<script>
function selectHomeChore(c) {
    const map = {
        fold: { e: '👕✨', t: 'Organizing Clean School Uniforms & Shoes', d: 'Arranging tomorrow\\'s school uniform and placing dusty shoes neatly beside doors prevents rushed morning stress and builds proud responsibility!' },
        water: { e: '🪴💧', t: 'Watering Balcony Tulsi & Potted Herbs', d: 'Using leftover kitchen rice or veggie rinse water to hydrate balcony plants shares gentle nature care right alongside parents!' },
        wipe: { e: '🧽🍽️', t: 'Clearing Plates & Wiping Dining Surfaces', d: 'Pitching in cheerfully after tasty family dinners lifts teamwork spirit and shows gratitude toward whoever cooked the meal!' },
        clean: { e: '🍊🧴', t: 'Mopping With Homemade Citrus-Vinegar Cleaner', d: 'Helping adults polish sinks using safe orange-peel and clove spray keeps bedrooms fresh without chemical pollution!' }
    };
    const d = map[c];
    if (!d) return;

    ['fold', 'water', 'wipe', 'clean'].forEach(k => {
        const b = document.getElementById('btn-hc-' + k);
        if (b) {
            b.className = (k === c)
                ? 'p-2.5 rounded-xl bg-emerald-600 text-white font-bold text-xs border border-emerald-500'
                : 'p-2.5 rounded-xl bg-slate-900 text-slate-300 font-bold text-xs border border-slate-700 hover:bg-slate-800';
        }
    });
    document.getElementById('hc-emoji').textContent = d.e;
    document.getElementById('hc-title').textContent = d.t;
    document.getElementById('hc-desc').textContent = d.d;
}
</script>
"""

if __name__ == "__main__":
    print(f"Generated {len(simulators_part2)} simulators for Part 2 (9 to 16).")
    for k in sorted(simulators_part2.keys()):
        print(f"Sim {k}: {len(simulators_part2[k])} chars")
