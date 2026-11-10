# -*- coding: utf-8 -*-
"""Simulators 9 to 16 for Class 3 Mathematics Chapter 5: Fun with Shapes."""

simulators_part2 = {}

# 9. Counting Nested Rectangles
simulators_part2['sim_counting_nested_rectangles'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 9</span>
            <h3 class="text-lg font-bold text-slate-100">Counting Nested Rectangles</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-violet-500/20 text-violet-300 font-semibold border border-violet-500/30">Systematic Counting</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Click the category buttons below to highlight individual panes, merged pairs, and the grand outer frame to find all 9 rectangles!
    </p>

    <!-- Window Visualizer Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="nestedRectSvg" viewBox="0 0 360 180" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <!-- 2x2 Grid Window -->
            <!-- Pane 1 (Top-Left) -->
            <rect id="pane1" x="90" y="20" width="85" height="65" fill="#1e293b" stroke="#64748b" stroke-width="2" class="transition-all duration-300"/>
            <text x="132" y="58" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">1</text>

            <!-- Pane 2 (Top-Right) -->
            <rect id="pane2" x="185" y="20" width="85" height="65" fill="#1e293b" stroke="#64748b" stroke-width="2" class="transition-all duration-300"/>
            <text x="227" y="58" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">2</text>

            <!-- Pane 3 (Bottom-Left) -->
            <rect id="pane3" x="90" y="95" width="85" height="65" fill="#1e293b" stroke="#64748b" stroke-width="2" class="transition-all duration-300"/>
            <text x="132" y="133" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">3</text>

            <!-- Pane 4 (Bottom-Right) -->
            <rect id="pane4" x="185" y="95" width="85" height="65" fill="#1e293b" stroke="#64748b" stroke-width="2" class="transition-all duration-300"/>
            <text x="227" y="133" fill="#94a3b8" font-size="12" font-weight="bold" text-anchor="middle">4</text>

            <!-- Overlay Highlight Box -->
            <rect id="nestedHighlight" x="90" y="20" width="180" height="140" fill="none" stroke="#f59e0b" stroke-width="4" stroke-dasharray="0" class="transition-all duration-300 opacity-0"/>
        </svg>

        <div id="nestedCountBanner" class="mt-2 text-xs text-violet-300 font-semibold bg-violet-950/40 px-3 py-1.5 rounded-lg border border-violet-800/40 text-center w-full font-mono">
            🔍 Total Rectangles: 4 Single + 2 Horizontal Pairs + 2 Vertical Pairs + 1 Outer Frame = 9 Rectangles
        </div>
    </div>

    <!-- Category Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button onclick="highlightNestedRect('single')" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            1. Single (4)
        </button>
        <button onclick="highlightNestedRect('horiz')" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            2. Horiz Pairs (2)
        </button>
        <button onclick="highlightNestedRect('vert')" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            3. Vert Pairs (2)
        </button>
        <button onclick="highlightNestedRect('outer')" class="px-2.5 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            4. Outer (1)
        </button>
    </div>
</div>

<script>
window.highlightNestedRect = function(type) {
    const hl = document.getElementById('nestedHighlight');
    const banner = document.getElementById('nestedCountBanner');
    if (!hl || !banner) return;

    hl.style.opacity = '1';

    if (type === 'single') {
        hl.setAttribute('x', '90');
        hl.setAttribute('y', '20');
        hl.setAttribute('width', '85');
        hl.setAttribute('height', '65');
        hl.setAttribute('stroke', '#3b82f6');
        banner.innerText = "🔍 Single Unit Panes: Exactly 4 individual rectangular panes (Pane 1, 2, 3, and 4).";
    } else if (type === 'horiz') {
        hl.setAttribute('x', '90');
        hl.setAttribute('y', '20');
        hl.setAttribute('width', '180');
        hl.setAttribute('height', '65');
        hl.setAttribute('stroke', '#10b981');
        banner.innerText = "🔍 Horizontal Combined Pairs: Exactly 2 wide rectangles (Top: 1+2, Bottom: 3+4).";
    } else if (type === 'vert') {
        hl.setAttribute('x', '90');
        hl.setAttribute('y', '20');
        hl.setAttribute('width', '85');
        hl.setAttribute('height', '140');
        hl.setAttribute('stroke', '#a855f7');
        banner.innerText = "🔍 Vertical Combined Pairs: Exactly 2 tall rectangles (Left: 1+3, Right: 2+4).";
    } else if (type === 'outer') {
        hl.setAttribute('x', '90');
        hl.setAttribute('y', '20');
        hl.setAttribute('width', '180');
        hl.setAttribute('height', '140');
        hl.setAttribute('stroke', '#f59e0b');
        banner.innerText = "🔍 Master Outer Frame: Exactly 1 large overarching rectangle enclosing the whole window.";
    }
};
</script>
"""

# 10. Squares Versus Rectangles
simulators_part2['sim_squares_versus_rectangles'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 10</span>
            <h3 class="text-lg font-bold text-slate-100">Square vs Rectangle Inspector</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-blue-500/20 text-blue-300 font-semibold border border-blue-500/30">Geometric Rule Test</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Adjust side lengths to see when a quadrilateral qualifies as a square, a rectangle, or both!
    </p>

    <!-- Visualizer Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="sqVsRectSvg" viewBox="0 0 360 170" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <rect id="compShape" x="80" y="30" width="120" height="120" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6" stroke-width="3" rx="2" class="transition-all duration-200"/>

            <!-- Right Angle Markers -->
            <path d="M 80 42 L 92 42 L 92 30" fill="none" stroke="#94a3b8" stroke-width="1.5"/>
            <path d="M 188 30 L 188 42 L 200 42" id="cornerTopRight" fill="none" stroke="#94a3b8" stroke-width="1.5"/>

            <!-- Dimension Text -->
            <text id="compWidthTxt" x="140" y="22" fill="#60a5fa" font-size="11" font-weight="bold" text-anchor="middle">Width = 4 cm</text>
            <text id="compHeightTxt" x="65" y="95" fill="#60a5fa" font-size="11" font-weight="bold" text-anchor="middle">4 cm</text>
        </svg>

        <div id="compResultNotice" class="mt-2 text-xs text-blue-300 font-semibold bg-blue-950/40 px-3 py-1.5 rounded-lg border border-blue-800/40 text-center w-full font-mono">
            ⭐ Width = 4 cm, Height = 4 cm: All 4 sides equal! This shape is BOTH a Square AND a Rectangle.
        </div>
    </div>

    <!-- Quick Switcher -->
    <div class="grid grid-cols-2 gap-3 pt-1">
        <button onclick="setCompShape(4, 4)" class="px-3 py-2 bg-blue-600 hover:bg-blue-500 rounded-xl text-xs font-bold transition">
            ■ Make Square (4 cm × 4 cm)
        </button>
        <button onclick="setCompShape(7, 4)" class="px-3 py-2 bg-indigo-600 hover:bg-indigo-500 rounded-xl text-xs font-bold transition">
            ▬ Make Rectangle (7 cm × 4 cm)
        </button>
    </div>
</div>

<script>
window.setCompShape = function(wUnits, hUnits) {
    const shape = document.getElementById('compShape');
    const wTxt = document.getElementById('compWidthTxt');
    const hTxt = document.getElementById('compHeightTxt');
    const cTR = document.getElementById('cornerTopRight');
    const notice = document.getElementById('compResultNotice');

    if (!shape) return;

    const pxW = wUnits * 25;
    const pxH = hUnits * 25;

    shape.setAttribute('width', pxW.toString());
    shape.setAttribute('height', pxH.toString());

    if (wTxt) {
        wTxt.setAttribute('x', (80 + pxW / 2).toString());
        wTxt.innerText = "Width = " + wUnits + " cm";
    }
    if (hTxt) {
        hTxt.setAttribute('y', (30 + pxH / 2).toString());
        hTxt.innerText = hUnits + " cm";
    }
    if (cTR) {
        cTR.setAttribute('d', "M " + (80 + pxW - 12) + " 30 L " + (80 + pxW - 12) + " 42 L " + (80 + pxW) + " 42");
    }

    if (notice) {
        if (wUnits === hUnits) {
            shape.setAttribute('fill', 'rgba(59, 130, 246, 0.2)');
            shape.setAttribute('stroke', '#3b82f6');
            notice.innerText = "⭐ Width = " + wUnits + " cm, Height = " + hUnits + " cm: All 4 sides equal! This is a Square (and a special Rectangle).";
        } else {
            shape.setAttribute('fill', 'rgba(168, 85, 247, 0.2)');
            shape.setAttribute('stroke', '#a855f7');
            notice.innerText = "📐 Width = " + wUnits + " cm, Height = " + hUnits + " cm: Opposite sides equal! This is a Rectangle, NOT a square.";
        }
    }
};
</script>
"""

# 11. Matchstick Shape Tiling
simulators_part2['sim_matchstick_shape_tiling'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 11</span>
            <h3 class="text-lg font-bold text-slate-100">Matchstick Shape & Shared Seam Tiling</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Shared Boundary Walls</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Construct connected squares and triangles using wooden matchsticks to see how shared boundary walls save sticks!
    </p>

    <!-- Matchstick Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="matchstickSvg" viewBox="0 0 360 170" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <g id="matchstickDrawGroup">
                <!-- 2 Connected Squares (Default) -->
                <!-- Outer Sticks (Cyan) -->
                <line x1="90" y1="45" x2="160" y2="45" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
                <line x1="160" y1="45" x2="230" y2="45" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
                <line x1="90" y1="115" x2="160" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
                <line x1="160" y1="115" x2="230" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
                <line x1="90" y1="45" x2="90" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
                <line x1="230" y1="45" x2="230" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>

                <!-- Shared Middle Wall (Gold) -->
                <line x1="160" y1="45" x2="160" y2="115" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>

                <!-- Labels -->
                <text x="125" y="85" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Square 1</text>
                <text x="195" y="85" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Square 2</text>
                <text x="160" y="32" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Shared Wall ⭐</text>
            </g>
        </svg>

        <div id="matchstickStatus" class="mt-2 text-xs text-amber-300 font-semibold bg-amber-950/40 px-3 py-1.5 rounded-lg border border-amber-800/40 text-center w-full font-mono">
            🪵 2 Connected Squares: 7 Matchsticks (6 Outer + 1 Shared Wall). Saved 1 stick!
        </div>
    </div>

    <!-- Configuration Buttons -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button onclick="setMatchstickModel('sq1')" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            1 Square (4)
        </button>
        <button onclick="setMatchstickModel('sq2')" class="px-2 py-1.5 bg-amber-600 hover:bg-amber-500 text-white rounded-lg text-xs font-bold transition">
            2 Squares (7)
        </button>
        <button onclick="setMatchstickModel('sq3')" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            3 Squares (10)
        </button>
        <button onclick="setMatchstickModel('tri2')" class="px-2 py-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-lg text-xs font-bold transition">
            2 Triangles (5)
        </button>
    </div>
</div>

<script>
window.setMatchstickModel = function(model) {
    const grp = document.getElementById('matchstickDrawGroup');
    const st = document.getElementById('matchstickStatus');
    if (!grp) return;

    if (model === 'sq1') {
        grp.innerHTML = `
            <line x1="135" y1="45" x2="205" y2="45" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="135" y1="115" x2="205" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="135" y1="45" x2="135" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="205" y1="45" x2="205" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <text x="170" y="85" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Single Square</text>
        `;
        st.innerText = "🪵 1 Standalone Square: Exactly 4 matchsticks needed (4 boundary edges).";
    } else if (model === 'sq2') {
        grp.innerHTML = `
            <line x1="90" y1="45" x2="160" y2="45" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="160" y1="45" x2="230" y2="45" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="90" y1="115" x2="160" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="160" y1="115" x2="230" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="90" y1="45" x2="90" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="230" y1="45" x2="230" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="160" y1="45" x2="160" y2="115" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>
            <text x="125" y="85" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Square 1</text>
            <text x="195" y="85" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">Square 2</text>
            <text x="160" y="32" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Shared Wall ⭐</text>
        `;
        st.innerText = "🪵 2 Connected Squares: 7 Matchsticks (4 + 3). The 1 shared wall saves a matchstick!";
    } else if (model === 'sq3') {
        grp.innerHTML = `
            <line x1="60" y1="45" x2="130" y2="45" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="130" y1="45" x2="200" y2="45" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="200" y1="45" x2="270" y2="45" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="60" y1="115" x2="130" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="130" y1="115" x2="200" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="200" y1="115" x2="270" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="60" y1="45" x2="60" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="270" y1="45" x2="270" y2="115" stroke="#06b6d4" stroke-width="4" stroke-linecap="round"/>
            <line x1="130" y1="45" x2="130" y2="115" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
            <line x1="200" y1="45" x2="200" y2="115" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
            <text x="95" y="85" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Sq 1</text>
            <text x="165" y="85" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Sq 2</text>
            <text x="235" y="85" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">Sq 3</text>
        `;
        st.innerText = "🪵 3 Connected Squares: 10 Matchsticks (4 + 3 + 3). Two shared walls save 2 sticks!";
    } else if (model === 'tri2') {
        grp.innerHTML = `
            <line x1="180" y1="25" x2="120" y2="135" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
            <line x1="180" y1="25" x2="240" y2="135" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
            <line x1="120" y1="135" x2="180" y2="135" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
            <line x1="180" y1="135" x2="240" y2="135" stroke="#10b981" stroke-width="4" stroke-linecap="round"/>
            <line x1="180" y1="25" x2="180" y2="135" stroke="#f59e0b" stroke-width="5" stroke-linecap="round"/>
            <text x="150" y="105" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Tri 1</text>
            <text x="210" y="105" fill="#34d399" font-size="10" font-weight="bold" text-anchor="middle">Tri 2</text>
            <text x="180" y="155" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">Shared Center Seam (5 sticks total)</text>
        `;
        st.innerText = "🪵 2 Connected Triangles: 5 Matchsticks total (3 + 2). Shared center spine saves 1 stick!";
    }
};
</script>
"""

# 12. Square Corner Angles
simulators_part2['sim_square_corner_angles'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 12</span>
            <h3 class="text-lg font-bold text-slate-100">Square Corner Angle Tester</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold border border-emerald-500/30">90° Right Angle Tester</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Place the folded paper corner tester against various angles to classify them as equal to, less than, or greater than a square corner!
    </p>

    <!-- Angle Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="angleTesterSvg" viewBox="0 0 360 170" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <!-- Test Angle Rays -->
            <line x1="160" y1="130" x2="280" y2="130" stroke="#94a3b8" stroke-width="4" stroke-linecap="round"/>
            <line id="testRaySlant" x1="160" y1="130" x2="160" y2="20" stroke="#94a3b8" stroke-width="4" stroke-linecap="round" class="transition-all duration-300"/>

            <!-- Folded Paper 90-degree Tester Overlay -->
            <polygon points="160,130 160,50 240,130" fill="rgba(245, 158, 11, 0.25)" stroke="#f59e0b" stroke-width="2" stroke-dasharray="3 3"/>
            <text x="180" y="105" fill="#fbbf24" font-size="10" font-weight="bold">Paper Tester (90°)</text>

            <!-- Angle Arc -->
            <path id="angleArc" d="M 190 130 A 30 30 0 0 0 160 100" fill="none" stroke="#10b981" stroke-width="3"/>

            <circle cx="160" cy="130" r="5" fill="#f59e0b"/>
        </svg>

        <div id="angleClassification" class="mt-2 text-xs text-emerald-300 font-semibold bg-emerald-950/40 px-3 py-1.5 rounded-lg border border-emerald-800/40 text-center w-full font-mono">
            📐 Perfect Fit: Exactly EQUAL to a Square Corner (90° Right Angle).
        </div>
    </div>

    <!-- Tester Buttons -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setTestAngle('equal')" class="px-3 py-2 bg-emerald-600 hover:bg-emerald-500 rounded-xl text-xs font-bold transition">
            1. Equal (90° Book Corner)
        </button>
        <button onclick="setTestAngle('less')" class="px-3 py-2 bg-blue-600 hover:bg-blue-500 rounded-xl text-xs font-bold transition">
            2. Less Than (Scissors 45°)
        </button>
        <button onclick="setTestAngle('greater')" class="px-3 py-2 bg-amber-600 hover:bg-amber-500 rounded-xl text-xs font-bold transition">
            3. Greater Than (Clock 130°)
        </button>
    </div>
</div>

<script>
window.setTestAngle = function(type) {
    const ray = document.getElementById('testRaySlant');
    const arc = document.getElementById('angleArc');
    const cls = document.getElementById('angleClassification');
    if (!ray) return;

    if (type === 'equal') {
        ray.setAttribute('x2', '160');
        ray.setAttribute('y2', '20');
        if (arc) arc.setAttribute('d', 'M 190 130 A 30 30 0 0 0 160 100');
        cls.innerText = "📐 Perfect Fit: Exactly EQUAL to a Square Corner (Book cover, doorway, picture frame).";
    } else if (type === 'less') {
        ray.setAttribute('x2', '230');
        ray.setAttribute('y2', '55');
        if (arc) arc.setAttribute('d', 'M 190 130 A 30 30 0 0 0 185 105');
        cls.innerText = "✂️ Narrow Opening: LESS than a Square Corner (Acute angle, scissor tips, samosa points).";
    } else if (type === 'greater') {
        ray.setAttribute('x2', '80');
        ray.setAttribute('y2', '60');
        if (arc) arc.setAttribute('d', 'M 190 130 A 30 30 0 0 0 135 110');
        cls.innerText = "🛋️ Wide Opening: GREATER than a Square Corner (Obtuse angle, reclining chair, clock at 4 o'clock).";
    }
};
</script>
"""

# 13. Triangle Pattern Counts
simulators_part2['sim_triangle_pattern_counts'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 13</span>
            <h3 class="text-lg font-bold text-slate-100">Nested Triangle Pattern Counter</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-teal-500/20 text-teal-300 font-semibold border border-teal-500/30">Scale-Tiered Counting</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Count triangles systematically by size across this geometric star: single small units, composite groups, and the grand master triangle!
    </p>

    <!-- Star Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="triCountSvg" viewBox="0 0 360 180" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <!-- Master Triangle -->
            <polygon id="masterTri" points="180,20 100,160 260,160" fill="rgba(20, 184, 166, 0.1)" stroke="#0d9488" stroke-width="2"/>

            <!-- Internal Sub-Triangles -->
            <!-- Top Unit 1 -->
            <polygon id="unitTri1" points="180,20 140,90 220,90" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6" stroke-width="2"/>
            <text x="180" y="65" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">1</text>

            <!-- Bottom Left Unit 2 -->
            <polygon id="unitTri2" points="140,90 100,160 180,160" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6" stroke-width="2"/>
            <text x="140" y="135" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">2</text>

            <!-- Bottom Right Unit 3 -->
            <polygon id="unitTri3" points="220,90 180,160 260,160" fill="rgba(59, 130, 246, 0.2)" stroke="#3b82f6" stroke-width="2"/>
            <text x="220" y="135" fill="#93c5fd" font-size="11" font-weight="bold" text-anchor="middle">3</text>

            <!-- Center Inverted Unit 4 -->
            <polygon id="unitTri4" points="140,90 220,90 180,160" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="2"/>
            <text x="180" y="120" fill="#fde68a" font-size="11" font-weight="bold" text-anchor="middle">4 (Inverted)</text>
        </svg>

        <div id="triCountNotice" class="mt-2 text-xs text-teal-300 font-semibold bg-teal-950/40 px-3 py-1.5 rounded-lg border border-teal-800/40 text-center w-full font-mono">
            🔺 Total Triangles = 4 Small Units (3 upright + 1 inverted) + 1 Grand Master Triangle = 5 Triangles
        </div>
    </div>

    <!-- Tier Buttons -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="highlightTriTier('units')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            1. Small Units (4)
        </button>
        <button onclick="highlightTriTier('master')" class="px-3 py-2 bg-teal-600 hover:bg-teal-500 rounded-xl text-xs font-bold transition">
            2. Grand Master (1)
        </button>
        <button onclick="highlightTriTier('all')" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            3. Show All (5)
        </button>
    </div>
</div>

<script>
window.highlightTriTier = function(tier) {
    const notice = document.getElementById('triCountNotice');
    const mt = document.getElementById('masterTri');
    if (!notice || !mt) return;

    if (tier === 'units') {
        mt.setAttribute('stroke-width', '1');
        notice.innerText = "🔺 Small Units: 4 single-unit triangles (3 pointing upward, 1 inverted in the center).";
    } else if (tier === 'master') {
        mt.setAttribute('stroke-width', '5');
        mt.setAttribute('stroke', '#f59e0b');
        notice.innerText = "⭐ Grand Master: 1 overarching triangle enclosing all four smaller unit triangles.";
    } else {
        mt.setAttribute('stroke-width', '2');
        mt.setAttribute('stroke', '#0d9488');
        notice.innerText = "🔺 Complete Count: 4 Small Units + 1 Grand Master Triangle = 5 Triangles in Total!";
    }
};
</script>
"""

# 14. Paper Circle Center
simulators_part2['sim_paper_circle_center'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 14</span>
            <h3 class="text-lg font-bold text-slate-100">Paper Plate Circle Center Discovery</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-rose-500/20 text-rose-300 font-semibold border border-rose-500/30">Crease Intersection</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Fold a circular paper disc in half twice along different directions to find its exact rotational balance center!
    </p>

    <!-- Circle Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="circleCenterSvg" viewBox="0 0 360 180" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <!-- Circular Paper Disc -->
            <circle cx="180" cy="90" r="70" fill="rgba(244, 63, 94, 0.15)" stroke="#f43f5e" stroke-width="3"/>

            <!-- Crease Line 1 (Vertical Diameter) -->
            <line id="crease1" x1="180" y1="20" x2="180" y2="160" stroke="#fb7185" stroke-width="2.5" stroke-dasharray="4 3" class="transition-all duration-300"/>

            <!-- Crease Line 2 (Horizontal Diameter) -->
            <line id="crease2" x1="110" y1="90" x2="250" y2="90" stroke="#fb7185" stroke-width="2.5" stroke-dasharray="4 3" class="transition-all duration-300"/>

            <!-- Center Intersection Dot -->
            <circle id="centerDot" cx="180" cy="90" r="6" fill="#facc15" stroke="#eab308" stroke-width="2" class="transition-all duration-300"/>
            <text id="centerDotLabel" x="180" y="115" fill="#fde047" font-size="11" font-weight="bold" text-anchor="middle">Center Point ⭐</text>
        </svg>

        <div id="circleCenterNotice" class="mt-2 text-xs text-rose-300 font-semibold bg-rose-950/40 px-3 py-1.5 rounded-lg border border-rose-800/40 text-center w-full font-mono">
            🎯 Both diameter creases intersect at one single point: the exact rotational center of the circle!
        </div>
    </div>

    <!-- Fold Actions -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setCircleFoldStep(1)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            1. First Fold (Crease 1)
        </button>
        <button onclick="setCircleFoldStep(2)" class="px-3 py-2 bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 rounded-xl text-xs font-bold transition">
            2. Second Fold (Crease 2)
        </button>
        <button onclick="setCircleFoldStep(3)" class="px-3 py-2 bg-rose-600 hover:bg-rose-500 rounded-xl text-xs font-bold transition">
            3. Intersection Center
        </button>
    </div>
</div>

<script>
window.setCircleFoldStep = function(step) {
    const c1 = document.getElementById('crease1');
    const c2 = document.getElementById('crease2');
    const dot = document.getElementById('centerDot');
    const lbl = document.getElementById('centerDotLabel');
    const notice = document.getElementById('circleCenterNotice');

    if (step === 1) {
        if (c1) c1.style.opacity = '1';
        if (c2) c2.style.opacity = '0';
        if (dot) dot.style.opacity = '0';
        if (lbl) lbl.style.opacity = '0';
        notice.innerText = "📄 Step 1: Folding the disc in half creates Crease 1 (a straight diameter dividing circle into 2 semicircles).";
    } else if (step === 2) {
        if (c1) c1.style.opacity = '1';
        if (c2) c2.style.opacity = '1';
        if (dot) dot.style.opacity = '0';
        if (lbl) lbl.style.opacity = '0';
        notice.innerText = "📄 Step 2: Folding in half again in a different direction creates Crease 2 (another diameter).";
    } else {
        if (c1) c1.style.opacity = '1';
        if (c2) c2.style.opacity = '1';
        if (dot) dot.style.opacity = '1';
        if (lbl) lbl.style.opacity = '1';
        notice.innerText = "🎯 Step 3: Unfolding flat reveals that the two diameters intersect at the exact center point!";
    }
};
</script>
"""

# 15. Polygon Side Counters
simulators_part2['sim_polygon_side_counters'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 15</span>
            <h3 class="text-lg font-bold text-slate-100">Polygon Side & Corner Transformer</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-cyan-500/20 text-cyan-300 font-semibold border border-cyan-500/30">Sides = Corners Law</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Slide the polygon dial from 3 to 10 sides to watch how regular polygons transform and confirm the law: Sides = Corners!
    </p>

    <!-- Polygon Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="polySvg" viewBox="0 0 360 180" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <polygon id="polyShape" points="" fill="rgba(6, 182, 212, 0.2)" stroke="#06b6d4" stroke-width="3" class="transition-all duration-300"/>
            <text id="polyNameTxt" x="180" y="100" fill="#22d3ee" font-size="14" font-weight="bold" text-anchor="middle">Hexagon</text>
        </svg>

        <div id="polyStatsBanner" class="mt-2 text-xs text-cyan-300 font-semibold bg-cyan-950/40 px-3 py-1.5 rounded-lg border border-cyan-800/40 text-center w-full font-mono">
            🔷 Hexagon: 6 Straight Sides = 6 Sharp Corners (Honeycomb Cell)
        </div>
    </div>

    <!-- Slider -->
    <div class="space-y-2 pt-1">
        <div class="flex justify-between text-xs font-mono">
            <span class="text-slate-400">Number of Sides & Corners:</span>
            <span id="polyDialLabel" class="text-cyan-400 font-bold">6 Sides (Hexagon)</span>
        </div>
        <input type="range" min="3" max="10" value="6" id="polyDialRange" oninput="updatePolygonDial(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-cyan-500">
        <div class="flex justify-between text-[11px] text-slate-500 font-mono">
            <span>3 (Triangle)</span>
            <span>5 (Pentagon)</span>
            <span>8 (Octagon)</span>
            <span>10 (Decagon)</span>
        </div>
    </div>
</div>

<script>
window.polyNames = {
    3: { name: "Triangle", desc: "3 Straight Sides = 3 Corners (Samosa, traffic warning sign)" },
    4: { name: "Quadrilateral (Square)", desc: "4 Straight Sides = 4 Corners (Chessboard tile)" },
    5: { name: "Pentagon", desc: "5 Straight Sides = 5 Corners (Signpost, school banner)" },
    6: { name: "Hexagon", desc: "6 Straight Sides = 6 Corners (Bee honeycomb cell, pencil cross-section)" },
    7: { name: "Heptagon", desc: "7 Straight Sides = 7 Corners (Decorative palace tile)" },
    8: { name: "Octagon", desc: "8 Straight Sides = 8 Corners (Red road STOP sign)" },
    9: { name: "Nonagon", desc: "9 Straight Sides = 9 Corners (9-pointed floral rangoli)" },
    10: { name: "Decagon", desc: "10 Straight Sides = 10 Corners (Star mandala perimeter)" }
};

window.updatePolygonDial = function(nStr) {
    const n = parseInt(nStr);
    const shape = document.getElementById('polyShape');
    const nameTxt = document.getElementById('polyNameTxt');
    const banner = document.getElementById('polyStatsBanner');
    const lbl = document.getElementById('polyDialLabel');

    if (!shape) return;

    lbl.innerText = n + " Sides (" + window.polyNames[n].name + ")";
    nameTxt.innerText = window.polyNames[n].name;
    banner.innerText = "🔷 " + window.polyNames[n].name + ": " + window.polyNames[n].desc;

    // Calculate regular polygon points
    const cx = 180, cy = 90, r = 65;
    let pts = [];
    for (let i = 0; i < n; i++) {
        const angle = (i * 2 * Math.PI / n) - (Math.PI / 2);
        const x = cx + r * Math.cos(angle);
        const y = cy + r * Math.sin(angle);
        pts.push(x.toFixed(1) + "," + y.toFixed(1));
    }
    shape.setAttribute('points', pts.join(" "));
};

// Init
setTimeout(function() { if (window.updatePolygonDial) window.updatePolygonDial(6); }, 100);
</script>
"""

# 16. Tangram Puzzle Assembly
simulators_part2['sim_tangram_puzzle_assembly'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 16</span>
            <h3 class="text-lg font-bold text-slate-100">Classic 7-Piece Tangram Assembly</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold border border-emerald-500/30">7 Geometric Tans</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Click presets to assemble all 7 classic tangram pieces into a square, a sailing boat, or a flying bird silhouette!
    </p>

    <!-- Tangram Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="tangramSvg" viewBox="0 0 360 180" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <g id="tangramPiecesGroup">
                <!-- Master Square Arrangement (Default) -->
                <!-- Big Tri 1 (Cyan) -->
                <polygon points="120,30 240,30 180,90" fill="#06b6d4" stroke="#0891b2" stroke-width="1.5"/>
                <!-- Big Tri 2 (Blue) -->
                <polygon points="120,30 120,150 180,90" fill="#3b82f6" stroke="#2563eb" stroke-width="1.5"/>
                <!-- Medium Tri (Purple) -->
                <polygon points="240,30 240,90 210,60" fill="#a855f7" stroke="#9333ea" stroke-width="1.5"/>
                <!-- Small Tri 1 (Green) -->
                <polygon points="180,90 210,60 210,120" fill="#10b981" stroke="#059669" stroke-width="1.5"/>
                <!-- Square (Yellow) -->
                <polygon points="210,60 240,90 210,120 180,90" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
                <!-- Small Tri 2 (Red) -->
                <polygon points="120,150 180,150 150,120" fill="#ef4444" stroke="#dc2626" stroke-width="1.5"/>
                <!-- Parallelogram (Amber) -->
                <polygon points="180,150 240,150 210,120 150,120" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            </g>
        </svg>

        <div id="tangramSilhouetteNotice" class="mt-2 text-xs text-emerald-300 font-semibold bg-emerald-950/40 px-3 py-1.5 rounded-lg border border-emerald-800/40 text-center w-full font-mono">
            🧩 Master Square Silhouette: All 7 tans (5 Triangles + 1 Square + 1 Parallelogram) united into one master square.
        </div>
    </div>

    <!-- Presets -->
    <div class="grid grid-cols-3 gap-2 pt-1">
        <button onclick="setTangramPreset('square')" class="px-3 py-2 bg-emerald-600 hover:bg-emerald-500 rounded-xl text-xs font-bold transition">
            ■ Master Square
        </button>
        <button onclick="setTangramPreset('boat')" class="px-3 py-2 bg-blue-600 hover:bg-blue-500 rounded-xl text-xs font-bold transition">
            ⛵ Sailing Boat
        </button>
        <button onclick="setTangramPreset('rocket')" class="px-3 py-2 bg-purple-600 hover:bg-purple-500 rounded-xl text-xs font-bold transition">
            🚀 Soaring Rocket
        </button>
    </div>
</div>

<script>
window.setTangramPreset = function(preset) {
    const grp = document.getElementById('tangramPiecesGroup');
    const notice = document.getElementById('tangramSilhouetteNotice');
    if (!grp) return;

    if (preset === 'square') {
        grp.innerHTML = `
            <polygon points="120,30 240,30 180,90" fill="#06b6d4" stroke="#0891b2" stroke-width="1.5"/>
            <polygon points="120,30 120,150 180,90" fill="#3b82f6" stroke="#2563eb" stroke-width="1.5"/>
            <polygon points="240,30 240,90 210,60" fill="#a855f7" stroke="#9333ea" stroke-width="1.5"/>
            <polygon points="180,90 210,60 210,120" fill="#10b981" stroke="#059669" stroke-width="1.5"/>
            <polygon points="210,60 240,90 210,120 180,90" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
            <polygon points="120,150 180,150 150,120" fill="#ef4444" stroke="#dc2626" stroke-width="1.5"/>
            <polygon points="180,150 240,150 210,120 150,120" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
        `;
        notice.innerText = "🧩 Master Square Silhouette: All 7 pieces perfectly fit inside the original dissection square!";
    } else if (preset === 'boat') {
        grp.innerHTML = `
            <polygon points="180,20 180,90 250,90" fill="#06b6d4" stroke="#0891b2" stroke-width="1.5"/>
            <polygon points="170,35 170,90 120,90" fill="#3b82f6" stroke="#2563eb" stroke-width="1.5"/>
            <polygon points="180,90 210,90 195,110" fill="#10b981" stroke="#059669" stroke-width="1.5"/>
            <polygon points="70,110 290,110 250,150 110,150" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <polygon points="130,110 160,110 160,135 130,135" fill="#facc15" stroke="#eab308" stroke-width="1.5"/>
        `;
        notice.innerText = "⛵ Sailing Boat Silhouette: 7 tans rearranged to form tall billowing sails and a floating hull!";
    } else if (preset === 'rocket') {
        grp.innerHTML = `
            <polygon points="180,15 150,55 210,55" fill="#ef4444" stroke="#dc2626" stroke-width="1.5"/>
            <polygon points="150,55 210,55 210,105 150,105" fill="#3b82f6" stroke="#2563eb" stroke-width="1.5"/>
            <polygon points="150,105 180,105 165,130" fill="#10b981" stroke="#059669" stroke-width="1.5"/>
            <polygon points="180,105 210,105 195,130" fill="#06b6d4" stroke="#0891b2" stroke-width="1.5"/>
            <polygon points="150,70 120,120 150,105" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
            <polygon points="210,70 240,120 210,105" fill="#a855f7" stroke="#9333ea" stroke-width="1.5"/>
        `;
        notice.innerText = "🚀 Soaring Rocket Silhouette: Dissection tans transformed into an aerodynamic space cruiser!";
    }
};
</script>
"""
