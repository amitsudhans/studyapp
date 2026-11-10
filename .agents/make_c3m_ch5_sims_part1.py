# -*- coding: utf-8 -*-
"""Simulators 1 to 8 for Class 3 Mathematics Chapter 5: Fun with Shapes."""

simulators_part1 = {}

# 1. Rangoli Dot Grid
simulators_part1['sim_rangoli_dot_grid'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 1</span>
            <h3 class="text-lg font-bold text-slate-100">Courtyard Rangoli Dot Grid</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Dot Grid Geometry</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Connect evenly spaced dots on this traditional courtyard floor to construct squares, triangles, and smooth circular loops!
    </p>

    <!-- Canvas Container -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="rangoliSvg" viewBox="0 0 360 220" class="w-full max-w-[420px] h-48 select-none bg-radial from-slate-900 to-slate-950 rounded-lg shadow-inner">
            <!-- Background grid lines -->
            <defs>
                <pattern id="dotPattern" width="40" height="40" patternUnits="userSpaceOnUse">
                    <circle cx="20" cy="20" r="2.5" fill="#64748b" opacity="0.6"/>
                </pattern>
            </defs>
            <rect width="360" height="220" fill="url(#dotPattern)" />

            <!-- Dynamic Shapes Group -->
            <g id="rangoliShapesGroup">
                <!-- Squares -->
                <rect id="rgSquare" x="60" y="60" width="80" height="80" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="3" stroke-dasharray="0" class="transition-all duration-300"/>
                <!-- Triangles -->
                <polygon id="rgTriangle" points="260,60 220,140 300,140" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="3" class="transition-all duration-300"/>
                <!-- Circular Loops -->
                <circle id="rgCircle" cx="180" cy="100" r="35" fill="rgba(59, 130, 246, 0.15)" stroke="#3b82f6" stroke-width="3" stroke-dasharray="4 2" class="transition-all duration-300"/>
            </g>

            <!-- Guide Labels -->
            <text id="rgSqLabel" x="100" y="105" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">Square</text>
            <text id="rgTriLabel" x="260" y="115" fill="#34d399" font-size="11" font-weight="bold" text-anchor="middle">Triangle</text>
            <text id="rgCirLabel" x="180" y="105" fill="#60a5fa" font-size="11" font-weight="bold" text-anchor="middle">Circle Loop</text>
        </svg>

        <div id="rangoliShapeInfo" class="mt-2 text-xs text-amber-300 font-semibold bg-amber-950/40 px-3 py-1.5 rounded-lg border border-amber-800/40 text-center w-full">
            ✨ Showing all foundational rangoli elements: 1 Square (4 straight sides), 1 Triangle (3 straight sides), and 1 Circular Arc (continuous curve).
        </div>
    </div>

    <!-- Controls -->
    <div class="grid grid-cols-2 sm:grid-cols-4 gap-2 pt-1">
        <button onclick="toggleRangoliElement('square')" class="px-3 py-2 rounded-xl bg-amber-500/20 hover:bg-amber-500/30 text-amber-300 border border-amber-500/40 text-xs font-bold transition flex items-center justify-center gap-1.5">
            <span>■ Square (4 Sides)</span>
        </button>
        <button onclick="toggleRangoliElement('triangle')" class="px-3 py-2 rounded-xl bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/40 text-xs font-bold transition flex items-center justify-center gap-1.5">
            <span>▲ Triangle (3 Sides)</span>
        </button>
        <button onclick="toggleRangoliElement('circle')" class="px-3 py-2 rounded-xl bg-blue-500/20 hover:bg-blue-500/30 text-blue-300 border border-blue-500/40 text-xs font-bold transition flex items-center justify-center gap-1.5">
            <span>● Circle (Curve)</span>
        </button>
        <button onclick="resetRangoliElements()" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 border border-slate-700 text-xs font-bold transition flex items-center justify-center gap-1.5">
            <span>🔄 Show All</span>
        </button>
    </div>
</div>

<script>
window.rgState = { square: true, triangle: true, circle: true };

window.toggleRangoliElement = function(type) {
    window.rgState[type] = !window.rgState[type];
    updateRangoliDisplay();
};

window.resetRangoliElements = function() {
    window.rgState = { square: true, triangle: true, circle: true };
    updateRangoliDisplay();
};

function updateRangoliDisplay() {
    const sq = document.getElementById('rgSquare');
    const sql = document.getElementById('rgSqLabel');
    const tr = document.getElementById('rgTriangle');
    const trl = document.getElementById('rgTriLabel');
    const cr = document.getElementById('rgCircle');
    const crl = document.getElementById('rgCirLabel');
    const info = document.getElementById('rangoliShapeInfo');

    if (sq) sq.style.display = window.rgState.square ? 'block' : 'none';
    if (sql) sql.style.display = window.rgState.square ? 'block' : 'none';
    if (tr) tr.style.display = window.rgState.triangle ? 'block' : 'none';
    if (trl) trl.style.display = window.rgState.triangle ? 'block' : 'none';
    if (cr) cr.style.display = window.rgState.circle ? 'block' : 'none';
    if (crl) crl.style.display = window.rgState.circle ? 'block' : 'none';

    let parts = [];
    if (window.rgState.square) parts.push('Square (4 equal sides, 4 corners)');
    if (window.rgState.triangle) parts.push('Triangle (3 straight sides, 3 corners)');
    if (window.rgState.circle) parts.push('Circle (smooth curved boundary, 0 corners)');

    if (parts.length === 0) {
        info.innerHTML = "Canvas cleared. Click any button above to draw geometric shapes on the dot grid!";
    } else {
        info.innerHTML = "Active Elements: " + parts.join(" • ");
    }
}
</script>
"""

# 2. Lines and Curves
simulators_part1['sim_lines_and_curves'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 2</span>
            <h3 class="text-lg font-bold text-slate-100">Straight Edges vs Curved Lines</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-emerald-500/20 text-emerald-300 font-semibold border border-emerald-500/30">Edge Classification</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Test everyday household objects to determine whether their boundaries are formed by straight edges, curved lines, or both!
    </p>

    <!-- Interactive Classification Stage -->
    <div class="grid grid-cols-1 md:grid-cols-3 gap-3">
        <!-- Pure Straight Category -->
        <div class="bg-slate-950/80 border border-indigo-500/40 rounded-xl p-3 flex flex-col items-center">
            <span class="text-xs font-bold uppercase text-indigo-400 tracking-wider mb-2">Straight Lines Only</span>
            <div id="straightItemsList" class="space-y-1.5 w-full min-h-[90px]">
                <div class="text-[11px] bg-indigo-950/60 border border-indigo-700/50 rounded-lg p-2 text-indigo-200 flex items-center justify-between">
                    <span>📏 Wooden Ruler</span>
                    <span class="text-[10px] text-indigo-400 font-mono">4 Straight</span>
                </div>
                <div class="text-[11px] bg-indigo-950/60 border border-indigo-700/50 rounded-lg p-2 text-indigo-200 flex items-center justify-between">
                    <span>🥪 Sandwich Slice</span>
                    <span class="text-[10px] text-indigo-400 font-mono">3 Straight</span>
                </div>
            </div>
            <span class="text-[10px] text-slate-400 mt-2 font-mono">Meet at Sharp Corners</span>
        </div>

        <!-- Pure Curved Category -->
        <div class="bg-slate-950/80 border border-emerald-500/40 rounded-xl p-3 flex flex-col items-center">
            <span class="text-xs font-bold uppercase text-emerald-400 tracking-wider mb-2">Curved Lines Only</span>
            <div id="curvedItemsList" class="space-y-1.5 w-full min-h-[90px]">
                <div class="text-[11px] bg-emerald-950/60 border border-emerald-700/50 rounded-lg p-2 text-emerald-200 flex items-center justify-between">
                    <span>⭕ Glass Bangle</span>
                    <span class="text-[10px] text-emerald-400 font-mono">0 Corners</span>
                </div>
                <div class="text-[11px] bg-emerald-950/60 border border-emerald-700/50 rounded-lg p-2 text-emerald-200 flex items-center justify-between">
                    <span>🪙 Rupee Coin</span>
                    <span class="text-[10px] text-emerald-400 font-mono">Continuous</span>
                </div>
            </div>
            <span class="text-[10px] text-slate-400 mt-2 font-mono">Zero Sharp Corners</span>
        </div>

        <!-- Hybrid Category -->
        <div class="bg-slate-950/80 border border-amber-500/40 rounded-xl p-3 flex flex-col items-center">
            <span class="text-xs font-bold uppercase text-amber-400 tracking-wider mb-2">Both Straight & Curved</span>
            <div id="bothItemsList" class="space-y-1.5 w-full min-h-[90px]">
                <div class="text-[11px] bg-amber-950/60 border border-amber-700/50 rounded-lg p-2 text-amber-200 flex items-center justify-between">
                    <span>🍦 Ice Cream Cone</span>
                    <span class="text-[10px] text-amber-400 font-mono">2 Slant + 1 Arc</span>
                </div>
                <div class="text-[11px] bg-amber-950/60 border border-amber-700/50 rounded-lg p-2 text-amber-200 flex items-center justify-between">
                    <span>🚪 Arched Doorway</span>
                    <span class="text-[10px] text-amber-400 font-mono">3 Flat + 1 Arch</span>
                </div>
            </div>
            <span class="text-[10px] text-slate-400 mt-2 font-mono">Composite Contours</span>
        </div>
    </div>

    <!-- Live Test Button -->
    <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col sm:flex-row items-center justify-between gap-3">
        <div class="flex items-center gap-2">
            <span class="text-xs text-slate-400">Current Test Item:</span>
            <span id="currentItemName" class="text-xs font-bold text-amber-300 bg-amber-500/10 px-2 py-0.5 rounded border border-amber-500/30">Matchbox (Cuboid Face)</span>
        </div>
        <div class="flex gap-2">
            <button onclick="cycleLineTestItem()" class="px-3 py-1.5 bg-indigo-600 hover:bg-indigo-500 rounded-lg text-xs font-bold transition">
                🔀 Test Next Item
            </button>
        </div>
    </div>
</div>

<script>
window.testItems = [
    { name: "Matchbox (Top Face)", category: "Straight Lines Only", desc: "4 straight segments meeting at 4 right angles." },
    { name: "Dinner Plate Rim", category: "Curved Lines Only", desc: "Smooth circular rim with zero vertices or corners." },
    { name: "Watermelon Slice", category: "Both Straight & Curved", desc: "2 straight radiating cuts meeting at a point + 1 curved rind arc." },
    { name: "Book Spine & Cover", category: "Straight Lines Only", desc: "Bounded by straight perpendicular edges." },
    { name: "Bicycle Wheel Rim", category: "Curved Lines Only", desc: "Pure circular curved boundary rolling without bumping." }
];
window.currItemIdx = 0;

window.cycleLineTestItem = function() {
    window.currItemIdx = (window.currItemIdx + 1) % window.testItems.length;
    const itm = window.testItems[window.currItemIdx];
    const lbl = document.getElementById('currentItemName');
    if (lbl) {
        lbl.innerText = itm.name + " (" + itm.category + ")";
    }
};
</script>
"""

# 3. Shape Cutout Art
simulators_part1['sim_shape_cutout_art'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 3</span>
            <h3 class="text-lg font-bold text-slate-100">Composite Shape Cutout Art</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-cyan-500/20 text-cyan-300 font-semibold border border-cyan-500/30">Composite Geometry</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Combine pre-cut squares, triangles, rectangles, and circles to assemble real-world figures without drawing lines!
    </p>

    <!-- Art Canvas Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="cutoutCanvasSvg" viewBox="0 0 360 180" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <g id="cutoutModelGroup">
                <!-- Cottage (Default) -->
                <!-- Roof: Green Triangle -->
                <polygon points="180,30 110,80 250,80" fill="#10b981" stroke="#059669" stroke-width="2"/>
                <!-- Wall: Red Square -->
                <rect x="125" y="80" width="110" height="80" fill="#ef4444" stroke="#dc2626" stroke-width="2"/>
                <!-- Door: Blue Rectangle -->
                <rect x="160" y="110" width="40" height="50" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
                <!-- Windows: Yellow Squares -->
                <rect x="135" y="95" width="20" height="20" fill="#facc15" stroke="#eab308" stroke-width="2"/>
                <rect x="205" y="95" width="20" height="20" fill="#facc15" stroke="#eab308" stroke-width="2"/>
                <!-- Chimney Smoke: Circles -->
                <circle cx="230" cy="35" r="8" fill="#94a3b8" opacity="0.7"/>
                <circle cx="238" cy="20" r="6" fill="#94a3b8" opacity="0.5"/>
            </g>
        </svg>

        <div id="cutoutStats" class="mt-2 text-xs text-cyan-300 font-semibold bg-cyan-950/40 px-3 py-1.5 rounded-lg border border-cyan-800/40 text-center w-full">
            🏡 Model: Village Cottage (1 Triangle + 3 Squares + 1 Rectangle + 2 Circles = 7 Cutouts)
        </div>
    </div>

    <!-- Preset Model Buttons -->
    <div class="grid grid-cols-3 gap-2">
        <button onclick="loadCutoutModel('cottage')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-bold transition">
            🏡 Cottage
        </button>
        <button onclick="loadCutoutModel('train')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-bold transition">
            🚂 Toy Train
        </button>
        <button onclick="loadCutoutModel('sailboat')" class="px-3 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-bold transition">
            ⛵ Sailboat
        </button>
    </div>
</div>

<script>
window.loadCutoutModel = function(model) {
    const grp = document.getElementById('cutoutModelGroup');
    const stats = document.getElementById('cutoutStats');
    if (!grp) return;

    if (model === 'cottage') {
        grp.innerHTML = `
            <polygon points="180,30 110,80 250,80" fill="#10b981" stroke="#059669" stroke-width="2"/>
            <rect x="125" y="80" width="110" height="80" fill="#ef4444" stroke="#dc2626" stroke-width="2"/>
            <rect x="160" y="110" width="40" height="50" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
            <rect x="135" y="95" width="20" height="20" fill="#facc15" stroke="#eab308" stroke-width="2"/>
            <rect x="205" y="95" width="20" height="20" fill="#facc15" stroke="#eab308" stroke-width="2"/>
            <circle cx="230" cy="35" r="8" fill="#94a3b8" opacity="0.7"/>
            <circle cx="238" cy="20" r="6" fill="#94a3b8" opacity="0.5"/>
        `;
        stats.innerText = "🏡 Model: Village Cottage (1 Triangle + 3 Squares + 1 Rectangle + 2 Circles = 7 Cutouts)";
    } else if (model === 'train') {
        grp.innerHTML = `
            <rect x="80" y="60" width="80" height="70" fill="#3b82f6" stroke="#2563eb" stroke-width="2"/>
            <rect x="160" y="90" width="120" height="40" fill="#ef4444" stroke="#dc2626" stroke-width="2"/>
            <rect x="95" y="70" width="25" height="25" fill="#facc15" stroke="#eab308" stroke-width="2"/>
            <rect x="240" y="70" width="20" height="20" fill="#10b981" stroke="#059669" stroke-width="2"/>
            <circle cx="105" cy="140" r="14" fill="#64748b" stroke="#334155" stroke-width="3"/>
            <circle cx="145" cy="140" r="14" fill="#64748b" stroke="#334155" stroke-width="3"/>
            <circle cx="190" cy="140" r="14" fill="#64748b" stroke="#334155" stroke-width="3"/>
            <circle cx="250" cy="140" r="14" fill="#64748b" stroke="#334155" stroke-width="3"/>
        `;
        stats.innerText = "🚂 Model: Toy Train (3 Rectangles + 1 Square + 4 Circular Wheels = 8 Cutouts)";
    } else if (model === 'sailboat') {
        grp.innerHTML = `
            <polygon points="170,25 170,110 240,110" fill="#10b981" stroke="#059669" stroke-width="2"/>
            <polygon points="160,40 160,110 110,110" fill="#06b6d4" stroke="#0891b2" stroke-width="2"/>
            <line x1="165" y1="20" x2="165" y2="115" stroke="#78350f" stroke-width="3"/>
            <polygon points="80,115 270,115 230,150 120,150" fill="#f59e0b" stroke="#d97706" stroke-width="2"/>
            <circle cx="175" cy="132" r="6" fill="#ffffff" stroke="#94a3b8" stroke-width="1.5"/>
        `;
        stats.innerText = "⛵ Model: Sailboat (2 Sail Triangles + 1 Trapezoid Hull + 1 Circular Porthole = 4 Shapes)";
    }
};
</script>
"""

# 4. Flattened Box Nets
simulators_part1['sim_flattened_box_nets'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 4</span>
            <h3 class="text-lg font-bold text-slate-100">Cardboard Box Net Unfolder</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-purple-500/20 text-purple-300 font-semibold border border-purple-500/30">3D to 2D Net</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Drag the unfold slider to flatten a 3D packaging carton into its 2D net of 6 connected rectangles!
    </p>

    <!-- Net Visualizer -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="boxNetSvg" viewBox="0 0 360 210" class="w-full max-w-[420px] h-48 bg-slate-900 rounded-lg shadow-inner">
            <!-- 2D Net Representation -->
            <!-- Central Column: Top (Face 1), Back (Face 2), Bottom (Face 3), Front (Face 4) -->
            <!-- Left Wing: Left Face 5 | Right Wing: Right Face 6 -->
            <g id="netRectangles" class="transition-all duration-300">
                <!-- Face 1: Top -->
                <rect x="140" y="15" width="80" height="40" fill="#a855f7" stroke="#9333ea" stroke-width="2" rx="2"/>
                <text x="180" y="38" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">1. Top</text>

                <!-- Face 2: Back -->
                <rect x="140" y="60" width="80" height="40" fill="#3b82f6" stroke="#2563eb" stroke-width="2" rx="2"/>
                <text x="180" y="83" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">2. Back</text>

                <!-- Face 5: Left Flap -->
                <rect id="leftFlap" x="55" y="60" width="80" height="40" fill="#10b981" stroke="#059669" stroke-width="2" rx="2"/>
                <text id="leftFlapTxt" x="95" y="83" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">5. Left</text>

                <!-- Face 6: Right Flap -->
                <rect id="rightFlap" x="225" y="60" width="80" height="40" fill="#10b981" stroke="#059669" stroke-width="2" rx="2"/>
                <text id="rightFlapTxt" x="265" y="83" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">6. Right</text>

                <!-- Face 3: Bottom Base -->
                <rect x="140" y="105" width="80" height="40" fill="#f59e0b" stroke="#d97706" stroke-width="2" rx="2"/>
                <text x="180" y="128" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">3. Bottom</text>

                <!-- Face 4: Front -->
                <rect x="140" y="150" width="80" height="40" fill="#ef4444" stroke="#dc2626" stroke-width="2" rx="2"/>
                <text x="180" y="173" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">4. Front</text>

                <!-- Dashed Fold Creases -->
                <line x1="140" y1="58" x2="220" y2="58" stroke="#cbd5e1" stroke-dasharray="3 3" stroke-width="1.5"/>
                <line x1="140" y1="102" x2="220" y2="102" stroke="#cbd5e1" stroke-dasharray="3 3" stroke-width="1.5"/>
                <line x1="140" y1="148" x2="220" y2="148" stroke="#cbd5e1" stroke-dasharray="3 3" stroke-width="1.5"/>
                <line x1="138" y1="60" x2="138" y2="100" stroke="#cbd5e1" stroke-dasharray="3 3" stroke-width="1.5"/>
                <line x1="222" y1="60" x2="222" y2="100" stroke="#cbd5e1" stroke-dasharray="3 3" stroke-width="1.5"/>
            </g>
        </svg>

        <div id="netStatus" class="mt-2 text-xs text-purple-300 font-semibold bg-purple-950/40 px-3 py-1.5 rounded-lg border border-purple-800/40 text-center w-full">
            📦 Unfolded Net: 6 Rectangular Faces (Top, Bottom, Front, Back, Left, Right)
        </div>
    </div>

    <!-- Unfold Slider Controls -->
    <div class="space-y-2 pt-1">
        <div class="flex justify-between text-xs font-mono">
            <span class="text-slate-400">Box Folding State:</span>
            <span id="unfoldPctLabel" class="text-purple-400 font-bold">100% (Completely Flat Net)</span>
        </div>
        <input type="range" min="0" max="100" value="100" id="unfoldRange" oninput="updateBoxNetUnfold(this.value)" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-purple-500">
        <div class="flex justify-between text-[11px] text-slate-500">
            <span>0% (Assembled 3D Box)</span>
            <span>50% (Partially Open)</span>
            <span>100% (Flat 2D Net)</span>
        </div>
    </div>
</div>

<script>
window.updateBoxNetUnfold = function(val) {
    const lbl = document.getElementById('unfoldPctLabel');
    const lf = document.getElementById('leftFlap');
    const rf = document.getElementById('rightFlap');
    const lft = document.getElementById('leftFlapTxt');
    const rft = document.getElementById('rightFlapTxt');
    const st = document.getElementById('netStatus');
    const pct = parseInt(val);

    if (lbl) lbl.innerText = pct + "% " + (pct === 100 ? "(Completely Flat Net)" : pct === 0 ? "(Closed 3D Box)" : "(Folding Creases)");

    // Scale the wings to simulate 3D folding
    const factor = pct / 100;
    if (lf && rf) {
        lf.setAttribute('width', (80 * factor).toString());
        lf.setAttribute('x', (140 - (80 * factor) - 5).toString());
        rf.setAttribute('width', (80 * factor).toString());
        if (lft) lft.setAttribute('x', (140 - (40 * factor) - 5).toString());
        if (rft) rft.setAttribute('x', (225 + (40 * factor)).toString());
    }

    if (st) {
        if (pct === 100) {
            st.innerText = "📦 Unfolded Net: Exactly 6 rectangular faces laid flat along straight fold seams.";
        } else if (pct === 0) {
            st.innerText = "📦 Closed Box: Flaps join at right angles to enclose a hollow 3D volume.";
        } else {
            st.innerText = "📦 Transition: Flaps folding along crease lines to transform 2D into 3D.";
        }
    }
};
</script>
"""

# 5. Paper Fold Envelope
simulators_part1['sim_paper_fold_envelope'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 5</span>
            <h3 class="text-lg font-bold text-slate-100">Origami Greeting Card Envelope</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-pink-500/20 text-pink-300 font-semibold border border-pink-500/30">Step-by-Step Folding</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Follow the sequential origami steps to transform a square sheet of craft paper into a functional greeting envelope!
    </p>

    <!-- Origami Visualizer -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="origamiSvg" viewBox="0 0 360 180" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <g id="origamiStepGroup">
                <!-- Step 1: Flat Square Sheet -->
                <rect x="110" y="20" width="140" height="140" fill="#f43f5e" stroke="#e11d48" stroke-width="2" rx="3"/>
                <line x1="110" y1="20" x2="250" y2="160" stroke="#fecdd3" stroke-dasharray="4 3" stroke-width="1.5"/>
                <text x="180" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Square Sheet (4 Equal Sides)</text>
            </g>
        </svg>

        <div id="origamiExplanation" class="mt-2 text-xs text-pink-300 font-semibold bg-pink-950/40 px-3 py-1.5 rounded-lg border border-pink-800/40 text-center w-full">
            📄 Step 1 of 4: Start with a crisp square sheet of craft paper with 4 equal sides and 4 square corners.
        </div>
    </div>

    <!-- Stepper Controls -->
    <div class="flex items-center justify-between gap-3 pt-1">
        <button onclick="changeOrigamiStep(-1)" class="px-4 py-2 bg-slate-800 hover:bg-slate-700 rounded-xl text-xs font-bold transition flex items-center gap-1">
            <span>◀ Previous Fold</span>
        </button>
        <span id="origamiStepBadge" class="text-xs font-mono font-bold text-amber-400">Step 1 / 4</span>
        <button onclick="changeOrigamiStep(1)" class="px-4 py-2 bg-pink-600 hover:bg-pink-500 rounded-xl text-xs font-bold transition flex items-center gap-1">
            <span>Next Fold ▶</span>
        </button>
    </div>
</div>

<script>
window.currOrigamiStep = 1;

window.changeOrigamiStep = function(delta) {
    window.currOrigamiStep += delta;
    if (window.currOrigamiStep < 1) window.currOrigamiStep = 1;
    if (window.currOrigamiStep > 4) window.currOrigamiStep = 4;
    renderOrigami();
};

function renderOrigami() {
    const grp = document.getElementById('origamiStepGroup');
    const exp = document.getElementById('origamiExplanation');
    const badge = document.getElementById('origamiStepBadge');
    if (!grp) return;

    badge.innerText = "Step " + window.currOrigamiStep + " / 4";

    if (window.currOrigamiStep === 1) {
        grp.innerHTML = `
            <rect x="110" y="20" width="140" height="140" fill="#f43f5e" stroke="#e11d48" stroke-width="2" rx="3"/>
            <line x1="110" y1="20" x2="250" y2="160" stroke="#fecdd3" stroke-dasharray="4 3" stroke-width="1.5"/>
            <text x="180" y="95" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Square Sheet (4 Equal Sides)</text>
        `;
        exp.innerText = "📄 Step 1 of 4: Start with a crisp square sheet of craft paper with 4 equal sides and 4 square corners.";
    } else if (window.currOrigamiStep === 2) {
        grp.innerHTML = `
            <polygon points="110,20 250,160 110,160" fill="#f43f5e" stroke="#e11d48" stroke-width="2"/>
            <line x1="110" y1="20" x2="250" y2="160" stroke="#ffffff" stroke-width="2"/>
            <text x="155" y="115" fill="#ffffff" font-size="11" font-weight="bold" text-anchor="middle">Diagonal Fold (2 Equal Triangles)</text>
        `;
        exp.innerText = "📐 Step 2 of 4: Crease diagonally across opposite corners to split the square into two symmetrical right triangles.";
    } else if (window.currOrigamiStep === 3) {
        grp.innerHTML = `
            <rect x="110" y="60" width="140" height="90" fill="#be123c" stroke="#9f1239" stroke-width="2"/>
            <polygon points="110,60 150,100 110,140" fill="#fb7185" stroke="#f43f5e" stroke-width="1.5"/>
            <polygon points="250,60 210,100 250,140" fill="#fb7185" stroke="#f43f5e" stroke-width="1.5"/>
            <polygon points="110,150 180,100 250,150" fill="#e11d48" stroke="#be123c" stroke-width="2"/>
            <text x="180" y="135" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Bottom Pocket + Side Flaps</text>
        `;
        exp.innerText = "✉️ Step 3 of 4: Fold side corners inward to center, then fold bottom flap upward to create a secure pocket.";
    } else if (window.currOrigamiStep === 4) {
        grp.innerHTML = `
            <rect x="110" y="60" width="140" height="90" fill="#be123c" stroke="#9f1239" stroke-width="2" rx="3"/>
            <polygon points="110,60 180,115 250,60" fill="#fb7185" stroke="#f43f5e" stroke-width="2"/>
            <circle cx="180" cy="115" r="5" fill="#facc15" stroke="#eab308" stroke-width="1"/>
            <text x="180" y="145" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">Completed Envelope (Sealed Flap)</text>
        `;
        exp.innerText = "💌 Step 4 of 4: Fold the top pointed triangular flap downward to seal your handsome greeting card envelope!";
    }
}
</script>
"""

# 6. Biscuit Tray Arrays
simulators_part1['sim_biscuit_tray_arrays'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 6</span>
            <h3 class="text-lg font-bold text-slate-100">Bakery Biscuit Tray Array</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-amber-500/20 text-amber-300 font-semibold border border-amber-500/30">Rows × Columns Array</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Adjust rows and columns on this metallic baking tray to see how identical biscuits pack into regular rectangular grids!
    </p>

    <!-- Baking Tray Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <div id="biscuitTrayGrid" class="bg-gradient-to-b from-stone-800 to-stone-900 border-4 border-stone-600 rounded-xl p-3 shadow-2xl flex flex-col gap-2 items-center justify-center min-h-[170px] w-full max-w-[400px]">
            <!-- Dynamic rows of biscuits -->
        </div>

        <div id="trayMathBanner" class="mt-2 text-xs text-amber-300 font-semibold bg-amber-950/40 px-3 py-1.5 rounded-lg border border-amber-800/40 text-center w-full font-mono">
            🧮 3 Rows × 4 Columns = 12 Delicious Golden Biscuits
        </div>
    </div>

    <!-- Sliders -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
        <div class="space-y-1">
            <div class="flex justify-between text-xs font-mono">
                <span class="text-slate-400">Horizontal Rows:</span>
                <span id="trayRowsLbl" class="text-amber-400 font-bold">3 Rows</span>
            </div>
            <input type="range" min="1" max="5" value="3" id="trayRowsRange" oninput="updateBiscuitTray()" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>

        <div class="space-y-1">
            <div class="flex justify-between text-xs font-mono">
                <span class="text-slate-400">Vertical Columns:</span>
                <span id="trayColsLbl" class="text-amber-400 font-bold">4 Columns</span>
            </div>
            <input type="range" min="1" max="6" value="4" id="trayColsRange" oninput="updateBiscuitTray()" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-amber-500">
        </div>
    </div>
</div>

<script>
window.updateBiscuitTray = function() {
    const rInput = document.getElementById('trayRowsRange');
    const cInput = document.getElementById('trayColsRange');
    const rLbl = document.getElementById('trayRowsLbl');
    const cLbl = document.getElementById('trayColsLbl');
    const grid = document.getElementById('biscuitTrayGrid');
    const banner = document.getElementById('trayMathBanner');

    if (!rInput || !cInput || !grid) return;

    const rows = parseInt(rInput.value);
    const cols = parseInt(cInput.value);
    const total = rows * cols;

    rLbl.innerText = rows + " Rows";
    cLbl.innerText = cols + " Columns";
    banner.innerText = "🧮 " + rows + " Rows × " + cols + " Columns = " + total + " Delicious Golden Biscuits";

    grid.innerHTML = "";
    for (let r = 0; r < rows; r++) {
        const rowDiv = document.createElement('div');
        rowDiv.className = "flex gap-2 justify-center w-full";
        for (let c = 0; c < cols; c++) {
            const b = document.createElement('div');
            b.className = "w-9 h-7 rounded bg-amber-400 border border-amber-600 shadow-md flex items-center justify-center text-[10px] font-bold text-amber-950";
            b.innerText = "🍪";
            rowDiv.appendChild(b);
        }
        grid.appendChild(rowDiv);
    }
};
// Initialize on load
setTimeout(function() { if (window.updateBiscuitTray) window.updateBiscuitTray(); }, 100);
</script>
"""

# 7. Tracing Cuboid Faces
simulators_part1['sim_tracing_cuboid_faces'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 7</span>
            <h3 class="text-lg font-bold text-slate-100">Tracing Cuboid 3D Faces</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-orange-500/20 text-orange-300 font-semibold border border-orange-500/30">3D to 2D Tracing</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Orient a wooden matchbox block on paper and trace its perimeter to reveal its three pairs of rectangular faces!
    </p>

    <!-- Tracing Paper Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="tracingSvg" viewBox="0 0 360 170" class="w-full max-w-[420px] h-44 bg-amber-50/10 rounded-lg border border-slate-800 shadow-inner">
            <!-- Paper Sheet Background -->
            <rect x="20" y="15" width="320" height="140" fill="#f8fafc" rx="4"/>

            <!-- Traced Outlines -->
            <!-- Large Face (Base) -->
            <rect id="traceBase" x="40" y="35" width="90" height="60" fill="rgba(249, 115, 22, 0.2)" stroke="#ea580c" stroke-width="2" stroke-dasharray="3 3"/>
            <text x="85" y="70" fill="#9a3412" font-size="9" font-weight="bold" text-anchor="middle">Base Face (9×6)</text>

            <!-- Medium Face (Side Wall) -->
            <rect id="traceSide" x="150" y="35" width="90" height="30" fill="rgba(59, 130, 246, 0.2)" stroke="#2563eb" stroke-width="2" stroke-dasharray="3 3"/>
            <text x="195" y="53" fill="#1e40af" font-size="9" font-weight="bold" text-anchor="middle">Side Wall (9×3)</text>

            <!-- Small Face (End Cap) -->
            <rect id="traceEnd" x="260" y="35" width="60" height="30" fill="rgba(16, 185, 129, 0.2)" stroke="#059669" stroke-width="2" stroke-dasharray="3 3"/>
            <text x="290" y="53" fill="#065f46" font-size="9" font-weight="bold" text-anchor="middle">End Face (6×3)</text>

            <text x="180" y="125" fill="#475569" font-size="10" font-weight="bold" text-anchor="middle">A cuboid has 6 total faces: 3 pairs of matching rectangles!</text>
        </svg>

        <div id="tracingResultNotice" class="mt-2 text-xs text-orange-300 font-semibold bg-orange-950/40 px-3 py-1.5 rounded-lg border border-orange-800/40 text-center w-full">
            ✏️ Current Orientation: Wide Base resting flat on paper, generating a 9 cm × 6 cm rectangle footprint.
        </div>
    </div>

    <!-- Orientation Switcher -->
    <div class="grid grid-cols-3 gap-2">
        <button onclick="setTraceOrientation('base')" class="px-3 py-2 bg-orange-500/20 hover:bg-orange-500/30 text-orange-300 border border-orange-500/40 rounded-xl text-xs font-bold transition">
            1. Broad Base Face
        </button>
        <button onclick="setTraceOrientation('side')" class="px-3 py-2 bg-blue-500/20 hover:bg-blue-500/30 text-blue-300 border border-blue-500/40 rounded-xl text-xs font-bold transition">
            2. Long Side Edge
        </button>
        <button onclick="setTraceOrientation('end')" class="px-3 py-2 bg-emerald-500/20 hover:bg-emerald-500/30 text-emerald-300 border border-emerald-500/40 rounded-xl text-xs font-bold transition">
            3. Narrow End Cap
        </button>
    </div>
</div>

<script>
window.setTraceOrientation = function(ori) {
    const notice = document.getElementById('tracingResultNotice');
    const tb = document.getElementById('traceBase');
    const ts = document.getElementById('traceSide');
    const te = document.getElementById('traceEnd');

    if (ori === 'base') {
        if (tb) tb.setAttribute('stroke-width', '4');
        if (ts) ts.setAttribute('stroke-width', '1');
        if (te) te.setAttribute('stroke-width', '1');
        notice.innerText = "✏️ Broad Base: Large rectangular footprint (top and bottom matching pair).";
    } else if (ori === 'side') {
        if (tb) tb.setAttribute('stroke-width', '1');
        if (ts) ts.setAttribute('stroke-width', '4');
        if (te) te.setAttribute('stroke-width', '1');
        notice.innerText = "✏️ Long Side: Medium elongated rectangle (front and back matching pair).";
    } else if (ori === 'end') {
        if (tb) tb.setAttribute('stroke-width', '1');
        if (ts) ts.setAttribute('stroke-width', '1');
        if (te) te.setAttribute('stroke-width', '4');
        notice.innerText = "✏️ Narrow End: Small compact rectangle (left and right matching pair).";
    }
};
</script>
"""

# 8. Dot Grid Rectangles
simulators_part1['sim_dot_grid_rectangles'] = """
<div class="bg-slate-900 border border-slate-800 rounded-2xl p-4 sm:p-5 text-white space-y-4">
    <div class="flex flex-col sm:flex-row sm:items-center justify-between gap-2 border-b border-slate-800 pb-3">
        <div>
            <span class="text-xs font-bold uppercase tracking-wider text-amber-400">Interactive Lab 8</span>
            <h3 class="text-lg font-bold text-slate-100">Dot Grid Rectangle Dimension Explorer</h3>
        </div>
        <div class="flex items-center gap-2">
            <span class="text-xs px-2.5 py-1 rounded-full bg-teal-500/20 text-teal-300 font-semibold border border-teal-500/30">Opposite Equal Sides</span>
        </div>
    </div>
    
    <p class="text-sm text-slate-300">
        Adjust width and height sliders to construct rectangles on the coordinate dot grid and observe opposite equal lengths!
    </p>

    <!-- Grid Stage -->
    <div class="bg-slate-950 border border-slate-800 rounded-xl p-3 flex flex-col items-center">
        <svg id="rectGridSvg" viewBox="0 0 360 190" class="w-full max-w-[420px] h-44 bg-slate-900 rounded-lg shadow-inner">
            <!-- Dot Matrix Background -->
            <defs>
                <pattern id="matrixPattern" width="30" height="30" patternUnits="userSpaceOnUse">
                    <circle cx="15" cy="15" r="2" fill="#475569"/>
                </pattern>
            </defs>
            <rect width="360" height="190" fill="url(#matrixPattern)" />

            <!-- Dynamic Rectangle -->
            <rect id="dynRect" x="60" y="30" width="150" height="90" fill="rgba(20, 184, 166, 0.2)" stroke="#14b8a6" stroke-width="3" rx="2" class="transition-all duration-200"/>

            <!-- Dimension Lines & Text -->
            <text id="topLenTxt" x="135" y="24" fill="#2dd4bf" font-size="11" font-weight="bold" text-anchor="middle">Top: 5 Units</text>
            <text id="botLenTxt" x="135" y="135" fill="#2dd4bf" font-size="11" font-weight="bold" text-anchor="middle">Bottom: 5 Units</text>
            <text id="leftLenTxt" x="42" y="80" fill="#2dd4bf" font-size="11" font-weight="bold" text-anchor="middle">Left: 3</text>
            <text id="rightLenTxt" x="225" y="80" fill="#2dd4bf" font-size="11" font-weight="bold" text-anchor="middle">Right: 3</text>
        </svg>

        <div id="rectPropsBanner" class="mt-2 text-xs text-teal-300 font-semibold bg-teal-950/40 px-3 py-1.5 rounded-lg border border-teal-800/40 text-center w-full font-mono">
            📏 Width = 5 Units | Height = 3 Units | Opposite Sides: Top = Bottom (5), Left = Right (3)
        </div>
    </div>

    <!-- Sliders -->
    <div class="grid grid-cols-1 sm:grid-cols-2 gap-3 pt-1">
        <div class="space-y-1">
            <div class="flex justify-between text-xs font-mono">
                <span class="text-slate-400">Horizontal Width:</span>
                <span id="rectWidthLbl" class="text-teal-400 font-bold">5 Units</span>
            </div>
            <input type="range" min="2" max="8" value="5" id="rectWidthRange" oninput="updateDynRect()" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-teal-500">
        </div>

        <div class="space-y-1">
            <div class="flex justify-between text-xs font-mono">
                <span class="text-slate-400">Vertical Height:</span>
                <span id="rectHeightLbl" class="text-teal-400 font-bold">3 Units</span>
            </div>
            <input type="range" min="2" max="4" value="3" id="rectHeightRange" oninput="updateDynRect()" class="w-full h-2 bg-slate-800 rounded-lg appearance-none cursor-pointer accent-teal-500">
        </div>
    </div>
</div>

<script>
window.updateDynRect = function() {
    const wInput = document.getElementById('rectWidthRange');
    const hInput = document.getElementById('rectHeightRange');
    const wLbl = document.getElementById('rectWidthLbl');
    const hLbl = document.getElementById('rectHeightLbl');
    const rect = document.getElementById('dynRect');
    const topT = document.getElementById('topLenTxt');
    const botT = document.getElementById('botLenTxt');
    const leftT = document.getElementById('leftLenTxt');
    const rightT = document.getElementById('rightLenTxt');
    const banner = document.getElementById('rectPropsBanner');

    if (!wInput || !hInput || !rect) return;

    const w = parseInt(wInput.value);
    const h = parseInt(hInput.value);
    const pixelW = w * 30;
    const pixelH = h * 30;

    wLbl.innerText = w + " Units";
    hLbl.innerText = h + " Units";

    rect.setAttribute('width', pixelW.toString());
    rect.setAttribute('height', pixelH.toString());

    if (topT) {
        topT.setAttribute('x', (60 + pixelW / 2).toString());
        topT.innerText = "Top: " + w + " Units";
    }
    if (botT) {
        botT.setAttribute('x', (60 + pixelW / 2).toString());
        botT.setAttribute('y', (30 + pixelH + 15).toString());
        botT.innerText = "Bottom: " + w + " Units";
    }
    if (leftT) {
        leftT.setAttribute('y', (30 + pixelH / 2).toString());
        leftT.innerText = "Left: " + h;
    }
    if (rightT) {
        rightT.setAttribute('x', (60 + pixelW + 15).toString());
        rightT.setAttribute('y', (30 + pixelH / 2).toString());
        rightT.innerText = "Right: " + h;
    }

    if (banner) {
        if (w === h) {
            banner.innerText = "⭐ Special Case: All 4 Sides Equal (" + w + " × " + h + ") — This is a Square!";
        } else {
            banner.innerText = "📏 Width = " + w + " | Height = " + h + " | Opposite Sides Equal (Top=Bottom=" + w + ", Left=Right=" + h + ")";
        }
    }
};
</script>
"""
