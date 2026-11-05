import re
import sys

def verify_no_latex(text, context=""):
    matches = re.findall(r'\\[a-zA-Z]+', text)
    if matches:
        print(f"ERROR: Raw LaTeX found in {context}: {matches[:10]}")
        sys.exit(1)

SIMULATORS = {
    1: """
<div class="bg-slate-900 p-4 rounded-xl border border-indigo-500/30 shadow-inner flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-3">
        <span class="text-xs font-bold text-indigo-400">✂️ Tailor Shop: Tape vs Char Angula</span>
        <button id="sim1ModeBtn" onclick="toggleSim1Tool()" class="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg shadow transition">
            Switch to Flexible Tape
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col justify-around p-3 overflow-hidden">
        <!-- Uniform sleeve to measure -->
        <div class="flex items-center justify-between px-4">
            <span class="text-xs text-slate-400 font-bold">Shoulder</span>
            <div class="w-64 h-8 bg-blue-900/60 rounded border border-blue-500/40 relative flex items-center justify-center">
                <span class="text-[11px] text-blue-200 font-bold">Uniform Sleeve (Physical Length = 45.0 cm)</span>
            </div>
            <span class="text-xs text-slate-400 font-bold">Cuff</span>
        </div>
        <!-- Measuring device overlay -->
        <div id="sim1ToolVisual" class="w-full flex items-center justify-center">
            <!-- Dynamically rendered by JS -->
        </div>
    </div>
    <div id="sim1Status" class="mt-2 text-xs text-center text-slate-300">
        Using <strong>Char Angula</strong> (four fingers). Width varies by hand size! Click switch to test tailor's tape.
    </div>
</div>
""",
    2: """
<div class="bg-slate-900 p-4 rounded-xl border border-sky-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-sky-400">Activity 5.1: Handspan Table Test</span>
        <div class="flex gap-1.5">
            <button onclick="setSim2Student('tall')" id="btnStudTall" class="px-2 py-1 bg-sky-600 text-white text-xs font-bold rounded shadow">Tall (20cm)</button>
            <button onclick="setSim2Student('med')" id="btnStudMed" class="px-2 py-1 bg-slate-800 text-slate-300 text-xs font-bold rounded border border-slate-700">Med (15cm)</button>
            <button onclick="setSim2Student('short')" id="btnStudShort" class="px-2 py-1 bg-slate-800 text-slate-300 text-xs font-bold rounded border border-slate-700">Small (12cm)</button>
        </div>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col justify-around p-2 overflow-hidden">
        <!-- Desk -->
        <div class="w-full h-12 bg-amber-900/40 rounded-lg border border-amber-600/50 flex items-center justify-center">
            <span class="text-xs font-bold text-amber-300">Classroom Teacher's Desk (True Length: 120 cm)</span>
        </div>
        <!-- Handspans container -->
        <div id="sim2HandsContainer" class="flex items-center justify-start gap-1 overflow-x-auto py-2">
            <!-- Rendered by JS -->
        </div>
    </div>
    <div id="sim2Status" class="mt-2 text-xs text-center text-slate-300">
        Tall Student (Handspan = 20 cm): Table measures exactly <strong>6 handspans</strong>.
    </div>
</div>
""",
    3: """
<div class="bg-slate-900 p-4 rounded-xl border border-amber-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-amber-400">🏛️ Lothal 2400 BCE Ivory Scale & Units</span>
        <button onclick="toggleSim3Zoom()" id="sim3ZoomBtn" class="px-3 py-1 bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold rounded shadow">
            Zoom 1.7 mm Divisions 🔍
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-center p-2 overflow-hidden">
        <!-- Ivory scale SVG -->
        <div id="sim3ScaleGraphic" class="transition-all duration-500 flex flex-col items-center">
            <div class="w-64 h-10 bg-amber-100 rounded shadow border border-amber-400 flex items-center justify-between px-2 text-slate-900 font-mono font-bold text-xs relative">
                <span class="absolute top-0 left-0 right-0 h-4 border-b border-amber-700 flex justify-between px-1 text-[8px]">
                    | | | | | | | | | | | | | | | | | | | | | | | | | | | | | |
                </span>
                <span class="mt-4 text-[9px] text-amber-900">LOTHAL HARAPPAN IVORY SCALE (c. 2400 BCE)</span>
            </div>
        </div>
        <!-- Units hierarchy row -->
        <div class="grid grid-cols-4 gap-1.5 w-full mt-3 text-[10px] text-center">
            <div class="p-1.5 bg-slate-900 rounded border border-slate-800"><strong class="text-amber-400">Angula</strong><br>~1.7 cm</div>
            <div class="p-1.5 bg-slate-900 rounded border border-slate-800"><strong class="text-amber-400">Hasta</strong><br>~45 cm</div>
            <div class="p-1.5 bg-slate-900 rounded border border-slate-800"><strong class="text-amber-400">Dhanusa</strong><br>~1.8 m</div>
            <div class="p-1.5 bg-slate-900 rounded border border-slate-800"><strong class="text-amber-400">Yojana</strong><br>~12-15 km</div>
        </div>
    </div>
    <div id="sim3Status" class="mt-2 text-xs text-center text-slate-300">
        Lothal ivory scale: Precision divisions of ~1.7 mm prove Harappan standard calibration.
    </div>
</div>
""",
    4: """
<div class="bg-slate-900 p-4 rounded-xl border border-cyan-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-cyan-400">🌐 The Global Metric SI Metre</span>
        <span class="text-xs font-mono text-cyan-300 font-bold">1 Metre = 100 cm</span>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-around p-3 overflow-hidden">
        <!-- Standard Metre Bar -->
        <div class="w-72 h-8 bg-gradient-to-r from-slate-300 via-slate-100 to-slate-400 rounded-lg shadow-xl border border-white flex items-center justify-between px-3 text-slate-900 font-bold text-xs font-mono">
            <span>0 m</span>
            <span class="text-indigo-600 font-extrabold tracking-wider">STANDARD SI METRE (1.000 m)</span>
            <span>1 m</span>
        </div>
        <!-- Light Speed Definition Card -->
        <div class="p-2.5 bg-indigo-950/60 rounded-lg border border-indigo-500/30 text-xs text-indigo-200 text-center w-full max-w-md">
            <strong>Laser Speed of Light Standard:</strong> Length of path traveled by light in vacuum in 1 / 299,792,458 of a second. Identical across all galaxies!
        </div>
    </div>
    <div class="mt-2 text-xs text-center text-slate-300">
        Universal SI standard adopted globally so 1 metre means the exact same length in every country.
    </div>
</div>
""",
    5: """
<div class="bg-slate-900 p-4 rounded-xl border border-emerald-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-emerald-400">Metric Multiples & Subunits Zoomer</span>
        <span id="sim5ScaleDisplay" class="text-xs font-mono font-bold text-amber-400">Scale: Centimetre (cm)</span>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-center p-3 overflow-hidden">
        <div id="sim5ZoomGraphic" class="w-full flex flex-col items-center justify-center transition-all duration-300">
            <!-- Rendered by JS -->
        </div>
    </div>
    <div class="flex items-center gap-3 w-full mt-2">
        <span class="text-[11px] text-slate-400 shrink-0">Zoom Level:</span>
        <input type="range" min="1" max="4" value="2" id="sim5Slider" oninput="setSim5Zoom(this.value)" class="w-full accent-emerald-500">
    </div>
    <div id="sim5Status" class="mt-1 text-xs text-center text-slate-300">
        Centimetre (cm): 1 m = 100 cm. Ideal for textbooks, pens, and shoes.
    </div>
</div>
""",
    6: """
<div class="bg-slate-900 p-4 rounded-xl border border-teal-500/30 flex flex-col items-center">
    <div class="text-xs text-teal-400 font-bold mb-2">Select an Object to Choose the Best Measuring Tool</div>
    <div class="grid grid-cols-4 gap-2 w-full mb-2">
        <button onclick="testSim6Tool('pencil')" class="p-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded border border-slate-700">✏️ Pencil</button>
        <button onclick="testSim6Tool('tree')" class="p-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded border border-slate-700">🌳 Tree Girth</button>
        <button onclick="testSim6Tool('cloth')" class="p-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded border border-slate-700">🧵 Cloth Roll</button>
        <button onclick="testSim6Tool('track')" class="p-1.5 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded border border-slate-700">🏃 100m Track</button>
    </div>
    <div id="sim6ResultBox" class="w-full h-36 bg-slate-950 rounded-lg border border-slate-800 p-3 flex flex-col items-center justify-center text-xs text-center text-slate-300">
        Click an object above to match it with the correct measuring instrument.
    </div>
</div>
""",
    7: """
<div class="bg-slate-900 p-4 rounded-xl border border-amber-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-amber-400">Activity 5.3: Parallax Error Viewer</span>
        <div class="flex gap-1.5">
            <button onclick="setSim7Angle('A')" id="btnAngleA" class="px-2 py-1 bg-slate-800 text-slate-300 text-xs font-bold rounded border border-slate-700">Left (A)</button>
            <button onclick="setSim7Angle('B')" id="btnAngleB" class="px-2 py-1 bg-emerald-600 text-white text-xs font-bold rounded shadow">Above 90° (B)</button>
            <button onclick="setSim7Angle('C')" id="btnAngleC" class="px-2 py-1 bg-slate-800 text-slate-300 text-xs font-bold rounded border border-slate-700">Right (C)</button>
        </div>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-between p-3 overflow-hidden">
        <!-- Eye ray representation -->
        <div id="sim7EyeRay" class="flex flex-col items-center transition-all duration-300">
            <span class="text-2xl">👁️</span>
            <div id="sim7RayLine" class="w-0.5 h-12 bg-emerald-400"></div>
        </div>
        <!-- Scale with pencil -->
        <div class="w-64 h-8 bg-amber-200 rounded border border-amber-500 relative flex items-center justify-between px-2 text-slate-900 font-mono text-[10px] font-bold">
            <span>5 cm</span>
            <span>6 cm</span>
            <span class="text-red-600 font-extrabold">6.5 cm</span>
            <span>7 cm</span>
            <span>8 cm</span>
        </div>
    </div>
    <div id="sim7Status" class="mt-2 text-xs text-center text-emerald-300 font-bold">
        Position B: Eye directly perpendicular at 90°. True Reading: 6.5 cm (Zero Parallax!).
    </div>
</div>
""",
    8: """
<div class="bg-slate-900 p-4 rounded-xl border border-indigo-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-indigo-400">Broken Zero Scale Offset Calculator</span>
        <span id="sim8Formula" class="text-xs font-mono text-amber-400 font-bold">Length = 7.4 - 1.0 = 6.4 cm</span>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col justify-around p-3 overflow-hidden">
        <!-- Broken Scale graphic -->
        <div class="w-full h-10 bg-slate-800 rounded relative flex items-center border border-slate-700 overflow-hidden font-mono text-xs">
            <!-- Chipped 0 end -->
            <div class="w-8 h-full bg-rose-950/80 border-r border-rose-500 flex items-center justify-center text-[9px] text-rose-300 font-bold">BROKEN</div>
            <div class="flex-1 flex justify-around text-slate-300">
                <span class="text-amber-400 font-bold">| 1.0 cm</span>
                <span>| 2.0</span>
                <span>| 3.0</span>
                <span>| 4.0</span>
                <span>| 5.0</span>
                <span>| 6.0</span>
                <span class="text-emerald-400 font-bold">| 7.4 cm</span>
            </div>
        </div>
        <!-- Pencil being measured -->
        <div class="flex justify-center">
            <div class="w-56 h-4 bg-amber-500 rounded-r-full border border-amber-300 relative flex items-center justify-center text-[9px] text-slate-900 font-bold">
                Pencil (Aligned 1.0 cm to 7.4 cm)
            </div>
        </div>
    </div>
    <div id="sim8Status" class="mt-2 text-xs text-center text-slate-300">
        Start at 1.0 cm. End at 7.4 cm. True Length = Final (7.4 cm) - Initial (1.0 cm) = <strong>6.4 cm</strong>!
    </div>
</div>
""",
    9: """
<div class="bg-slate-900 p-4 rounded-xl border border-purple-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-purple-400">SI Notation Grammar & Tactile Rulers</span>
        <button onclick="toggleSim9Tactile()" id="sim9TactileBtn" class="px-3 py-1 bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold rounded shadow">
            Show Tactile Braille Scale 🦯
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-around p-3 overflow-hidden">
        <div id="sim9ScaleVisual" class="w-64 h-12 bg-slate-800 rounded border border-slate-600 flex items-center justify-around text-xs font-mono">
            <span>1 cm</span><span>2 cm</span><span>3 cm</span><span>4 cm</span><span>5 cm</span>
        </div>
        <div class="grid grid-cols-2 gap-2 w-full text-[11px]">
            <div class="p-2 bg-emerald-950/40 rounded border border-emerald-500/30 text-emerald-300">
                <strong>✓ Correct:</strong> <code>15 cm</code> (with space, lowercase, no 's')
            </div>
            <div class="p-2 bg-rose-950/40 rounded border border-rose-500/30 text-rose-300">
                <strong>✗ Incorrect:</strong> <code>15cms.</code>, <code>15cm</code>, <code>15 ms</code>
            </div>
        </div>
    </div>
    <div id="sim9Status" class="mt-2 text-xs text-center text-slate-300">
        Symbols never take plural 's' or trailing periods. Tactile scales use embossed dots for touch.
    </div>
</div>
""",
    10: """
<div class="bg-slate-900 p-4 rounded-xl border border-teal-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-teal-400">Activity 5.4: Curved Line Thread Lab</span>
        <button onclick="straightenSim10Thread()" id="sim10ThreadBtn" class="px-3 py-1 bg-teal-600 hover:bg-teal-500 text-white text-xs font-bold rounded shadow">
            Straighten Thread on Scale 📏
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-3 overflow-hidden">
        <!-- SVG Canvas for curve / straight thread -->
        <div id="sim10Display" class="w-full h-full flex items-center justify-center">
            <!-- Rendered by JS -->
        </div>
    </div>
    <div id="sim10Status" class="mt-2 text-xs text-center text-slate-300">
        Thread conforms to the winding curved line from A to B. Click to straighten across the centimetre ruler!
    </div>
</div>
""",
    11: """
<div class="bg-slate-900 p-4 rounded-xl border border-blue-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-blue-400">📍 Reference Points & Highway Milestones</span>
        <button onclick="toggleSim11Origin()" id="sim11OriginBtn" class="px-3 py-1 bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold rounded shadow">
            Change Reference Origin
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col justify-around p-3 overflow-hidden">
        <!-- Road with car and milestones -->
        <div class="w-full h-10 bg-slate-800 rounded relative flex items-center justify-between px-6 border border-slate-700">
            <span class="text-xs font-bold text-amber-400">🏙️ Delhi (0 km)</span>
            <div id="sim11Car" class="text-2xl transition-all duration-700 transform translate-x-12">🚗</div>
            <span class="text-xs font-bold text-sky-400">🏙️ Chandigarh (250 km)</span>
        </div>
        <!-- Milestone stone graphic -->
        <div class="flex justify-center">
            <div id="sim11Milestone" class="w-28 h-12 bg-amber-400 rounded-t-2xl border border-amber-600 flex flex-col items-center justify-center text-slate-900 font-extrabold text-[11px] shadow-lg">
                <span>DELHI</span>
                <span class="text-xs">120 km</span>
            </div>
        </div>
    </div>
    <div id="sim11Status" class="mt-2 text-xs text-center text-slate-300">
        Reference Point: <strong>Delhi</strong>. The milestone indicates the car is 120 km from Delhi.
    </div>
</div>
""",
    12: """
<div class="bg-slate-900 p-4 rounded-xl border border-emerald-500/30 flex flex-col items-center">
    <div class="text-xs text-emerald-400 font-bold mb-2">Classroom Observation: Rest vs Motion Over Time</div>
    <div class="grid grid-cols-3 gap-2 w-full mb-2">
        <button onclick="testSim12Object('board')" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 rounded border border-slate-700">🏫 Blackboard</button>
        <button onclick="testSim12Object('student')" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 rounded border border-slate-700">🚶 Walking Student</button>
        <button onclick="testSim12Object('clock')" class="p-2 bg-slate-800 hover:bg-slate-700 text-xs font-bold text-slate-200 rounded border border-slate-700">⏰ Clock Hands</button>
    </div>
    <div id="sim12ResultBox" class="w-full h-36 bg-slate-950 rounded-lg border border-slate-800 p-3 flex flex-col items-center justify-center text-xs text-center text-slate-300">
        Select an object above to observe its position change relative to the classroom walls.
    </div>
</div>
""",
    13: """
<div class="bg-slate-900 p-4 rounded-xl border border-purple-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-purple-400">The Moving Bus Paradox: Relative Motion</span>
        <button onclick="toggleSim13Observer()" id="sim13ObsBtn" class="px-3 py-1 bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold rounded shadow">
            Switch to Roadside Observer 🌲
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-3 overflow-hidden">
        <div id="sim13Scene" class="w-full flex flex-col items-center justify-center">
            <!-- Rendered by JS -->
        </div>
    </div>
    <div id="sim13Status" class="mt-2 text-xs text-center text-slate-300">
        Inside Bus View: Deepa and friend sit side by side. <strong>Relative Speed = 0 km/h (At Rest!).</strong>
    </div>
</div>
""",
    14: """
<div class="bg-slate-900 p-4 rounded-xl border border-cyan-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-cyan-400">Linear (Rectilinear) Motion Laboratory</span>
        <button onclick="dropSim14Mango()" class="px-3 py-1 bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold rounded shadow">
            Drop Mango from Tree 🥭
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-between px-8 overflow-hidden">
        <!-- Tree top -->
        <div class="flex flex-col items-center">
            <span class="text-3xl">🌳</span>
            <div id="sim14Mango" class="text-2xl transition-all duration-700 transform translate-y-0">🥭</div>
        </div>
        <!-- Straight line path visual -->
        <div class="w-0.5 h-32 border-l-2 border-dashed border-cyan-400/60 flex items-center justify-center">
            <span class="text-[9px] text-cyan-300 font-bold -rotate-90 bg-slate-950 px-1">STRAIGHT VERTICAL PATH</span>
        </div>
        <div class="text-xs text-slate-400 text-center">
            <span class="text-2xl">🌱</span><br>Ground
        </div>
    </div>
    <div id="sim14Status" class="mt-2 text-xs text-center text-slate-300">
        Click drop: Mango falls straight down under gravity with zero turning—pure linear motion!
    </div>
</div>
""",
    15: """
<div class="bg-slate-900 p-4 rounded-xl border border-emerald-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-emerald-400">Circular Motion: Constant Radial Distance</span>
        <button onclick="spinSim15String()" class="px-3 py-1 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold rounded shadow">
            Whirl Stone on String 🔄
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-3 overflow-hidden">
        <!-- Circular path ring -->
        <div class="w-32 h-32 rounded-full border border-dashed border-emerald-500/50 flex items-center justify-center relative">
            <div class="w-2 h-2 rounded-full bg-amber-400"></div>
            <!-- String & stone rotating -->
            <div id="sim15StoneArm" class="absolute w-16 h-0.5 bg-slate-400 origin-left transition-transform duration-1000 ease-linear flex items-center justify-end" style="left: 64px;">
                <div class="w-3.5 h-3.5 rounded-full bg-emerald-400 border border-white shadow"></div>
            </div>
            <span class="absolute top-1 text-[9px] text-emerald-300 font-bold">Radius r = Constant</span>
        </div>
    </div>
    <div id="sim15Status" class="mt-2 text-xs text-center text-slate-300">
        In circular motion, distance from the central pivot stays constant as the object revolves.
    </div>
</div>
""",
    16: """
<div class="bg-slate-900 p-4 rounded-xl border border-purple-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-purple-400">Oscillatory & Periodic Motion: Pendulum</span>
        <button onclick="swingSim16Pendulum()" class="px-3 py-1 bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold rounded shadow">
            Release Swing ⏱️
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-between p-3 overflow-hidden">
        <div class="w-16 h-1 bg-slate-600 rounded"></div>
        <!-- Pendulum rod & bob -->
        <div id="sim16PendulumArm" class="origin-top transition-transform duration-700 ease-in-out flex flex-col items-center" style="transform: rotate(-30deg);">
            <div class="w-0.5 h-24 bg-purple-400"></div>
            <div class="w-5 h-5 rounded-full bg-gradient-to-br from-amber-400 to-yellow-600 border border-white shadow-lg"></div>
        </div>
        <!-- Mean position marker -->
        <div class="text-[10px] text-slate-400 flex justify-between w-full px-12">
            <span>Extreme Left</span>
            <span class="text-amber-400 font-bold">Mean Center</span>
            <span>Extreme Right</span>
        </div>
    </div>
    <div id="sim16Status" class="mt-2 text-xs text-center text-slate-300">
        Oscillatory motion: To-and-fro swing across the mean position. Periodic because each cycle repeats in equal time.
    </div>
</div>
"""
}

# Verify no latex in simulators
for sim_id, sim_code in SIMULATORS.items():
    verify_no_latex(sim_code, f"Simulator {sim_id}")

print(f"Verified {len(SIMULATORS)} bespoke simulators with zero raw LaTeX.")

with open('.agents/class6_science_ch5_sims.py', 'w') as f:
    f.write('"""\nBespoke Interactive Simulators for NCERT Class 6 Science - Chapter 5\n"""\n\nSIMULATORS = ' + repr(SIMULATORS) + '\n')

print("Created .agents/class6_science_ch5_sims.py successfully!")
