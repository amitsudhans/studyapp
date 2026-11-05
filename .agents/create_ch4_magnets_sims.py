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
        <span class="text-xs font-bold text-indigo-400">🌊 Kerala Spice Ship Navigation</span>
        <button id="toggleWeatherBtn" onclick="toggleSim1Weather()" class="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-semibold rounded-lg shadow transition">
            Toggle Storm Clouds
        </button>
    </div>
    <div id="sim1Sky" class="relative w-full h-48 rounded-lg overflow-hidden border border-slate-700 transition-all duration-700 bg-slate-950 flex flex-col justify-between p-3">
        <!-- Sky view with stars or clouds -->
        <div id="sim1Stars" class="absolute inset-0 transition-opacity duration-700">
            <div class="absolute top-4 left-1/4 w-1.5 h-1.5 bg-white rounded-full animate-ping"></div>
            <div class="absolute top-8 left-1/2 w-2.5 h-2.5 bg-amber-200 rounded-full shadow-[0_0_8px_#fde68a]"></div>
            <span class="absolute top-3 left-1/2 ml-4 text-[10px] text-amber-300 font-bold">★ Pole Star (North)</span>
            <div class="absolute top-6 right-1/4 w-1 h-1 bg-white rounded-full"></div>
            <div class="absolute top-12 left-10 w-1.5 h-1.5 bg-white rounded-full"></div>
        </div>
        <div id="sim1Clouds" class="absolute inset-0 bg-slate-800/95 transition-opacity duration-700 opacity-0 flex flex-col items-center justify-center pointer-events-none p-4">
            <div class="text-2xl mb-1">⛈️ ☁️ 🌩️</div>
            <div class="text-xs text-amber-300 font-bold text-center">Dense Overcast Storm! Stars & Sun are Completely Invisible!</div>
        </div>
        <!-- Ship and Sea -->
        <div class="relative z-10 flex justify-between items-end mt-auto w-full pt-16">
            <div class="text-3xl animate-bounce">⛵</div>
            <div class="bg-slate-900/90 p-2 rounded-lg border border-slate-700 flex items-center gap-3">
                <div id="sim1CompassNeedle" class="w-10 h-10 rounded-full border-2 border-amber-500/60 relative flex items-center justify-center bg-slate-950 transition-transform duration-700">
                    <div class="w-1 h-8 bg-gradient-to-t from-blue-500 via-slate-400 to-red-500 rounded-full"></div>
                    <div class="absolute w-2 h-2 bg-amber-400 rounded-full"></div>
                </div>
                <div class="text-[11px] text-slate-300">
                    <span class="font-bold text-amber-400">Magnetic Compass:</span><br>
                    <span id="sim1StatusText">Stars visible. Ship steering North.</span>
                </div>
            </div>
        </div>
    </div>
</div>
""",
    2: """
<div class="bg-slate-900 p-4 rounded-xl border border-sky-500/30 flex flex-col items-center">
    <div class="flex flex-wrap gap-2 justify-center mb-3">
        <button onclick="setSim2Magnet('bar')" id="btnMagBar" class="px-2.5 py-1 bg-sky-600 text-white text-xs font-bold rounded-lg shadow">Bar Magnet</button>
        <button onclick="setSim2Magnet('horseshoe')" id="btnMagHorse" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold rounded-lg border border-slate-700">Horseshoe (U-Shape)</button>
        <button onclick="setSim2Magnet('ring')" id="btnMagRing" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold rounded-lg border border-slate-700">Ring / Disc</button>
        <button onclick="setSim2Magnet('needle')" id="btnMagNeedle" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold rounded-lg border border-slate-700">Compass Needle</button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 flex items-center justify-center relative p-2 overflow-hidden">
        <div id="sim2Display" class="flex flex-col items-center justify-center">
            <!-- Rendered dynamically by JS -->
        </div>
    </div>
    <div id="sim2Description" class="mt-2 text-xs text-center text-slate-300">
        Bar Magnet: Rectangular bar with North and South poles at opposite ends.
    </div>
</div>
""",
    3: """
<div class="bg-slate-900 p-4 rounded-xl border border-emerald-500/30 flex flex-col items-center">
    <div class="text-xs text-emerald-400 font-bold mb-2">Click Any Material to Bring Magnet Close</div>
    <div class="grid grid-cols-3 gap-2 w-full mb-3">
        <button onclick="testSim3Material('iron')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg border border-slate-700 text-center transition">
            <div class="text-xl">🪛</div>
            <div class="text-[11px] font-bold text-slate-200">Iron Nail</div>
        </button>
        <button onclick="testSim3Material('wood')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg border border-slate-700 text-center transition">
            <div class="text-xl">✏️</div>
            <div class="text-[11px] font-bold text-slate-200">Wooden Pencil</div>
        </button>
        <button onclick="testSim3Material('steel')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg border border-slate-700 text-center transition">
            <div class="text-xl">📎</div>
            <div class="text-[11px] font-bold text-slate-200">Steel Clip</div>
        </button>
        <button onclick="testSim3Material('copper')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg border border-slate-700 text-center transition">
            <div class="text-xl">🪙</div>
            <div class="text-[11px] font-bold text-slate-200">Copper Coin</div>
        </button>
        <button onclick="testSim3Material('plastic')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg border border-slate-700 text-center transition">
            <div class="text-xl">📏</div>
            <div class="text-[11px] font-bold text-slate-200">Plastic Scale</div>
        </button>
        <button onclick="testSim3Material('nickel')" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg border border-slate-700 text-center transition">
            <div class="text-xl">🔩</div>
            <div class="text-[11px] font-bold text-slate-200">Nickel Bolt</div>
        </button>
    </div>
    <div id="sim3ResultBox" class="w-full p-2.5 bg-slate-950 rounded-lg border border-slate-800 text-xs text-center text-slate-300 min-h-[50px] flex items-center justify-center">
        Select an object above to test its magnetic properties with the bar magnet.
    </div>
</div>
""",
    4: """
<div class="bg-slate-900 p-4 rounded-xl border border-amber-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-amber-400">🏗️ Industrial Scrap Crane Electromagnet</span>
        <button id="sim4CraneBtn" onclick="toggleSim4Electromagnet()" class="px-3 py-1 bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold rounded-lg shadow">
            Turn Electromagnet ON
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col justify-between p-3 overflow-hidden">
        <!-- Electromagnet head -->
        <div id="sim4CraneHead" class="mx-auto w-32 h-8 bg-slate-700 rounded-lg border-2 border-slate-500 flex items-center justify-center text-xs font-bold text-slate-300 transition-all duration-500">
            🧲 CRANE HEAD (OFF)
        </div>
        <!-- Scrap pile -->
        <div class="flex justify-around items-end pt-8">
            <div id="scrapIron" class="flex flex-col items-center transition-all duration-700">
                <span class="text-2xl">⚙️🔩</span>
                <span class="text-[10px] text-emerald-400 font-bold">Iron Scrap</span>
            </div>
            <div id="scrapSteel" class="flex flex-col items-center transition-all duration-700">
                <span class="text-2xl">🚗🔧</span>
                <span class="text-[10px] text-emerald-400 font-bold">Steel Cars</span>
            </div>
            <div id="scrapAlum" class="flex flex-col items-center">
                <span class="text-2xl">🥫</span>
                <span class="text-[10px] text-rose-400 font-bold">Aluminium Cans</span>
            </div>
            <div id="scrapPlastic" class="flex flex-col items-center">
                <span class="text-2xl">🧴</span>
                <span class="text-[10px] text-rose-400 font-bold">Plastic Bottles</span>
            </div>
        </div>
    </div>
    <div id="sim4Status" class="mt-2 text-xs text-center text-slate-300">
        Electromagnet is currently OFF. Both magnetic and non-magnetic materials sit mixed on the floor.
    </div>
</div>
""",
    5: """
<div class="bg-slate-900 p-4 rounded-xl border border-cyan-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-cyan-400">Activity 4.2: Iron Filings Density</span>
        <button onclick="sprinkleSim5Filings()" class="px-3 py-1 bg-cyan-600 hover:bg-cyan-500 text-white text-xs font-bold rounded-lg shadow">
            Sprinkle Iron Filings
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-2 overflow-hidden">
        <!-- Bar Magnet -->
        <div class="flex shadow-lg rounded overflow-hidden z-10">
            <div class="w-24 h-10 bg-red-600 flex items-center justify-center font-bold text-white text-sm">N</div>
            <div class="w-24 h-10 bg-blue-600 flex items-center justify-center font-bold text-white text-sm">S</div>
        </div>
        <!-- Filings layers -->
        <div id="sim5FilingsContainer" class="absolute inset-0 pointer-events-none opacity-0 transition-opacity duration-700 flex justify-between items-center px-6">
            <div class="text-slate-400 text-xl font-bold tracking-tighter">░▒▓█▓▒░<br>███████<br>░▒▓█▓▒░</div>
            <div class="text-slate-600 text-xs">· · ·</div>
            <div class="text-slate-400 text-xl font-bold tracking-tighter">░▒▓█▓▒░<br>███████<br>░▒▓█▓▒░</div>
        </div>
    </div>
    <div id="sim5Status" class="mt-2 text-xs text-center text-slate-300">
        Clean bar magnet. Click "Sprinkle Iron Filings" to test where magnetic attraction is strongest.
    </div>
</div>
""",
    6: """
<div class="bg-slate-900 p-4 rounded-xl border border-violet-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-violet-400">Dipole Slicer: Inseparable Poles</span>
        <button id="sim6CutBtn" onclick="cutSim6Magnet()" class="px-3 py-1 bg-violet-600 hover:bg-violet-500 text-white text-xs font-bold rounded-lg shadow">
            Cut Magnet in Half ✂️
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-2 overflow-hidden">
        <div id="sim6MagnetsContainer" class="flex flex-col gap-3 items-center justify-center w-full transition-all duration-500">
            <!-- Generated dynamically by JS -->
        </div>
    </div>
    <div id="sim6Status" class="mt-2 text-xs text-center text-slate-300">
        One full bar magnet with North (N) and South (S) poles. Click Cut to test if you can isolate a pole!
    </div>
</div>
""",
    7: """
<div class="bg-slate-900 p-4 rounded-xl border border-teal-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-teal-400">Activity 4.3: Freely Suspended Magnet</span>
        <button onclick="spinSim7Magnet()" class="px-3 py-1 bg-teal-600 hover:bg-teal-500 text-white text-xs font-bold rounded-lg shadow">
            Spin Magnet 🔄
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-between p-3 overflow-hidden">
        <!-- Stand string -->
        <div class="w-0.5 h-10 bg-amber-400/80"></div>
        <!-- Magnet -->
        <div id="sim7Magnet" class="flex shadow-xl rounded overflow-hidden transition-transform duration-1000 ease-out origin-center">
            <div class="w-20 h-8 bg-red-600 flex items-center justify-center font-bold text-white text-xs">N (North)</div>
            <div class="w-20 h-8 bg-blue-600 flex items-center justify-center font-bold text-white text-xs">S (South)</div>
        </div>
        <!-- Compass dial backdrop -->
        <div class="text-[11px] text-slate-400 flex justify-between w-full px-8">
            <span>WEST</span>
            <span class="text-amber-400 font-bold">NORTH ⬆️</span>
            <span>EAST</span>
        </div>
    </div>
    <div id="sim7Status" class="mt-2 text-xs text-center text-slate-300">
        The suspended magnet is at rest, pointing directly along the North-South axis.
    </div>
</div>
""",
    8: """
<div class="bg-slate-900 p-4 rounded-xl border border-blue-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-blue-400">Geodynamo & Earth's Inner Magnet</span>
        <button onclick="toggleSim8Poles()" class="px-3 py-1 bg-blue-600 hover:bg-blue-500 text-white text-xs font-bold rounded-lg shadow">
            Toggle Magnetic Dipole
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-2 overflow-hidden">
        <!-- Earth circle -->
        <div class="w-32 h-32 rounded-full border-2 border-emerald-500/40 bg-gradient-to-br from-blue-900 via-emerald-950 to-slate-950 relative flex items-center justify-center shadow-[0_0_20px_rgba(59,130,246,0.3)]">
            <span class="text-3xl">🌍</span>
            <!-- Inner core magnet overlay -->
            <div id="sim8Dipole" class="absolute flex flex-col rounded overflow-hidden shadow-lg border border-amber-400 opacity-90 transition-opacity duration-500">
                <div class="w-8 h-8 bg-blue-600 text-white font-bold text-[10px] flex items-center justify-center">S</div>
                <div class="w-8 h-8 bg-red-600 text-white font-bold text-[10px] flex items-center justify-center">N</div>
            </div>
            <span class="absolute -top-5 text-[10px] font-bold text-amber-300">Geographic North</span>
            <span class="absolute -bottom-5 text-[10px] font-bold text-slate-400">Geographic South</span>
        </div>
    </div>
    <div id="sim8Status" class="mt-2 text-xs text-center text-slate-300">
        Earth acts like a giant magnet! Note: Earth's internal <strong>magnetic South</strong> resides near geographic North!
    </div>
</div>
""",
    9: """
<div class="bg-slate-900 p-4 rounded-xl border border-sky-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-sky-400">🧭 Interactive 360° Magnetic Compass</span>
        <span id="sim9AngleDisplay" class="text-xs font-mono font-bold text-amber-400">Dial: 0° (North)</span>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-2 overflow-hidden">
        <!-- Compass Outer Housing -->
        <div id="sim9Dial" class="w-36 h-36 rounded-full border-4 border-amber-600/70 bg-slate-900 relative flex items-center justify-center shadow-inner transition-transform duration-300">
            <span class="absolute top-1 text-xs font-bold text-amber-300">N</span>
            <span class="absolute bottom-1 text-xs font-bold text-slate-400">S</span>
            <span class="absolute right-1 text-xs font-bold text-slate-400">E</span>
            <span class="absolute left-1 text-xs font-bold text-slate-400">W</span>
            <!-- Magnetic needle locked to Earth's North -->
            <div class="w-1.5 h-28 bg-gradient-to-t from-blue-500 via-slate-300 to-red-500 rounded-full shadow-lg relative flex items-center justify-center pointer-events-none">
                <div class="w-3 h-3 bg-amber-400 rounded-full border border-slate-950"></div>
            </div>
        </div>
    </div>
    <div class="flex items-center gap-3 w-full mt-2">
        <span class="text-[11px] text-slate-400 shrink-0">Rotate Box:</span>
        <input type="range" min="0" max="360" value="0" id="sim9Slider" oninput="rotateSim9Compass(this.value)" class="w-full accent-amber-500">
    </div>
</div>
""",
    10: """
<div class="bg-slate-900 p-4 rounded-xl border border-amber-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-amber-400">🐟 Ancient Matsya-Yantra (Oil Flotation)</span>
        <button onclick="stirSim10Oil()" class="px-3 py-1 bg-amber-600 hover:bg-amber-500 text-white text-xs font-bold rounded-lg shadow">
            Rock Vessel / Stir Oil 🌊
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-2 overflow-hidden">
        <!-- Brass bowl -->
        <div class="w-40 h-40 rounded-full border-4 border-yellow-600/80 bg-gradient-to-br from-amber-900/60 via-yellow-950/40 to-slate-950 relative flex items-center justify-center shadow-2xl">
            <!-- Oil surface indicator -->
            <div class="absolute inset-2 rounded-full border border-amber-500/30 bg-amber-500/10 flex items-center justify-center">
                <!-- Magnetized iron fish -->
                <div id="sim10Fish" class="transition-transform duration-1000 ease-out flex items-center justify-center">
                    <span class="text-4xl filter drop-shadow-[0_2px_4px_rgba(0,0,0,0.8)] -rotate-90">🐟</span>
                </div>
            </div>
            <span class="absolute top-1 text-[10px] font-bold text-amber-400">NORTH (Target)</span>
        </div>
    </div>
    <div id="sim10Status" class="mt-2 text-xs text-center text-slate-300">
        The magnetized iron fish floats upon viscous oil, pointing its head reliably towards the North.
    </div>
</div>
""",
    11: """
<div class="bg-slate-900 p-4 rounded-xl border border-emerald-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-emerald-400">Activity 4.4: Magnetize a Needle</span>
        <span id="sim11StrokeCounter" class="text-xs font-mono font-bold text-amber-400">Strokes: 0 / 30</span>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-around p-3 overflow-hidden">
        <!-- Needle on table -->
        <div class="flex items-center gap-2">
            <span class="text-xs font-bold text-slate-400">Eye</span>
            <div id="sim11Needle" class="w-48 h-2 bg-slate-400 rounded-full transition-all duration-300"></div>
            <span class="text-xs font-bold text-slate-400">Tip</span>
        </div>
        <!-- Stroking bar magnet -->
        <div id="sim11Magnet" class="flex shadow-md rounded overflow-hidden transition-all duration-300">
            <div class="w-16 h-6 bg-red-600 text-[10px] font-bold text-white flex items-center justify-center">N</div>
            <div class="w-16 h-6 bg-blue-600 text-[10px] font-bold text-white flex items-center justify-center">S</div>
        </div>
        <button id="sim11StrokeBtn" onclick="performSim11Stroke()" class="px-4 py-1.5 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold rounded-lg shadow">
            Stroke Magnet in One Direction ➡️
        </button>
    </div>
    <div id="sim11Status" class="mt-2 text-xs text-center text-slate-300">
        Click stroke to rub the magnet along the needle from eye to tip in a single direction.
    </div>
</div>
""",
    12: """
<div class="bg-slate-900 p-4 rounded-xl border border-indigo-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-indigo-400">Activity 4.5: Pencil Rollers Lab</span>
        <button onclick="flipSim12HandMagnet()" class="px-3 py-1 bg-indigo-600 hover:bg-indigo-500 text-white text-xs font-bold rounded-lg shadow">
            Flip Hand Magnet 🔄
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-around p-3 overflow-hidden">
        <!-- Roller magnet -->
        <div id="sim12RollerMagnet" class="flex flex-col items-center transition-all duration-700">
            <div class="flex rounded overflow-hidden shadow-lg border border-slate-700">
                <div class="w-16 h-8 bg-red-600 text-xs font-bold text-white flex items-center justify-center">N</div>
                <div class="w-16 h-8 bg-blue-600 text-xs font-bold text-white flex items-center justify-center">S</div>
            </div>
            <!-- Pencils underneath -->
            <div class="flex gap-4 mt-2">
                <div class="w-2 h-4 bg-amber-600 rounded"></div>
                <div class="w-2 h-4 bg-amber-600 rounded"></div>
                <div class="w-2 h-4 bg-amber-600 rounded"></div>
            </div>
            <span class="text-[10px] text-slate-400 mt-1">Free on Rollers</span>
        </div>
        <!-- Approaching Hand Magnet -->
        <div id="sim12HandMagnet" class="flex rounded overflow-hidden shadow-lg border border-slate-700 transition-all duration-300">
            <div id="sim12HandLeft" class="w-16 h-8 bg-red-600 text-xs font-bold text-white flex items-center justify-center">N</div>
            <div id="sim12HandRight" class="w-16 h-8 bg-blue-600 text-xs font-bold text-white flex items-center justify-center">S</div>
        </div>
    </div>
    <div id="sim12Status" class="mt-2 text-xs text-center text-slate-300">
        Unlike poles face each other (S faces N): Attraction draws the roller magnet forward!
    </div>
</div>
""",
    13: """
<div class="bg-slate-900 p-4 rounded-xl border border-amber-500/30 flex flex-col items-center">
    <div class="text-xs text-amber-400 font-bold mb-2">Mystery Bar Identifier: Which is the Real Magnet?</div>
    <div class="flex gap-3 mb-2">
        <button onclick="testSim13Bar('barA')" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded-lg border border-slate-700">Test Bar A</button>
        <button onclick="testSim13Bar('barB')" class="px-3 py-1 bg-slate-800 hover:bg-slate-700 text-slate-200 text-xs font-bold rounded-lg border border-slate-700">Test Bar B</button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-around p-3 overflow-hidden">
        <!-- Known Test Magnet -->
        <div class="flex flex-col items-center">
            <span class="text-[10px] text-emerald-400 font-bold mb-1">Known Test Magnet</span>
            <div class="flex rounded overflow-hidden shadow">
                <div class="w-14 h-7 bg-red-600 text-xs font-bold text-white flex items-center justify-center">N</div>
                <div class="w-14 h-7 bg-blue-600 text-xs font-bold text-white flex items-center justify-center">S</div>
            </div>
        </div>
        <!-- Mystery Bar -->
        <div id="sim13MysteryBar" class="flex flex-col items-center transition-all duration-500">
            <span id="sim13MysteryLabel" class="text-[10px] text-amber-400 font-bold mb-1">Select a Mystery Bar</span>
            <div id="sim13BarVisual" class="w-28 h-7 bg-slate-600 rounded flex items-center justify-around text-xs font-bold text-slate-300 border border-slate-500">
                <span>End 1</span>
                <span>End 2</span>
            </div>
        </div>
    </div>
    <div id="sim13Status" class="mt-2 text-xs text-center text-slate-300">
        Click Test Bar A or Bar B to bring the test North pole to both ends and observe attraction vs repulsion.
    </div>
</div>
""",
    14: """
<div class="bg-slate-900 p-4 rounded-xl border border-teal-500/30 flex flex-col items-center">
    <div class="flex flex-wrap gap-2 justify-center mb-2">
        <button onclick="setSim14Barrier('cardboard')" class="px-2.5 py-1 bg-teal-600 text-white text-xs font-bold rounded-lg shadow">Cardboard</button>
        <button onclick="setSim14Barrier('glass')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold rounded-lg border border-slate-700">Glass Plate</button>
        <button onclick="setSim14Barrier('water')" class="px-2.5 py-1 bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-bold rounded-lg border border-slate-700">Water Tumbler</button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col items-center justify-between p-3 overflow-hidden">
        <!-- Paper clip top -->
        <div id="sim14Clip" class="text-2xl transition-all duration-300 transform">📎</div>
        <!-- Barrier -->
        <div id="sim14BarrierVisual" class="w-full h-4 bg-amber-700/80 rounded border border-amber-600 text-[10px] text-center font-bold text-amber-200">
            Cardboard Sheet
        </div>
        <!-- Magnet below -->
        <div id="sim14Magnet" class="flex shadow rounded overflow-hidden transition-all duration-300">
            <div class="w-16 h-7 bg-red-600 text-xs font-bold text-white flex items-center justify-center">N</div>
            <div class="w-16 h-7 bg-blue-600 text-xs font-bold text-white flex items-center justify-center">S</div>
        </div>
    </div>
    <div class="flex items-center gap-3 w-full mt-2">
        <span class="text-[11px] text-slate-400 shrink-0">Slide Magnet:</span>
        <input type="range" min="-80" max="80" value="0" id="sim14Slider" oninput="moveSim14Magnet(this.value)" class="w-full accent-teal-500">
    </div>
</div>
""",
    15: """
<div class="bg-slate-900 p-4 rounded-xl border border-emerald-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-emerald-400">Proper Storage: Keepers & Spacers</span>
        <button onclick="resetSim15Storage()" class="px-3 py-1 bg-emerald-600 hover:bg-emerald-500 text-white text-xs font-bold rounded-lg shadow">
            Reset Box 📦
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex items-center justify-center p-3 overflow-hidden">
        <div class="flex items-center">
            <!-- Left Soft Iron Keeper -->
            <div id="sim15LeftKeeper" class="w-3 h-28 bg-slate-400 rounded-l border border-slate-300 flex items-center justify-center text-[9px] font-bold text-slate-900 -rotate-90">KEEPER</div>
            <!-- Bar magnets & wooden spacer -->
            <div class="flex flex-col gap-2 mx-1">
                <div class="flex rounded overflow-hidden shadow">
                    <div class="w-20 h-8 bg-red-600 text-xs font-bold text-white flex items-center justify-center">N</div>
                    <div class="w-20 h-8 bg-blue-600 text-xs font-bold text-white flex items-center justify-center">S</div>
                </div>
                <!-- Wooden spacer -->
                <div class="w-40 h-3 bg-amber-700 rounded text-[9px] text-center font-bold text-amber-200">WOODEN SPACER</div>
                <div class="flex rounded overflow-hidden shadow">
                    <div class="w-20 h-8 bg-blue-600 text-xs font-bold text-white flex items-center justify-center">S</div>
                    <div class="w-20 h-8 bg-red-600 text-xs font-bold text-white flex items-center justify-center">N</div>
                </div>
            </div>
            <!-- Right Soft Iron Keeper -->
            <div id="sim15RightKeeper" class="w-3 h-28 bg-slate-400 rounded-r border border-slate-300 flex items-center justify-center text-[9px] font-bold text-slate-900 rotate-90">KEEPER</div>
        </div>
    </div>
    <div id="sim15Status" class="mt-2 text-xs text-center text-slate-300">
        Properly stored: Unlike poles opposite, wooden spacer between bars, and soft iron keepers completing the magnetic loop!
    </div>
</div>
""",
    16: """
<div class="bg-slate-900 p-4 rounded-xl border border-purple-500/30 flex flex-col items-center">
    <div class="flex justify-between w-full items-center mb-2">
        <span class="text-xs font-bold text-purple-400">🚄 High-Speed Maglev Train Levitation</span>
        <button id="sim16MaglevBtn" onclick="toggleSim16Maglev()" class="px-3 py-1 bg-purple-600 hover:bg-purple-500 text-white text-xs font-bold rounded-lg shadow">
            Activate Levitation
        </button>
    </div>
    <div class="w-full h-44 bg-slate-950 rounded-lg border border-slate-800 relative flex flex-col justify-between p-3 overflow-hidden">
        <!-- Speedometer -->
        <div class="flex justify-between text-xs text-slate-400">
            <span>Levitation Gap: <strong id="sim16Gap" class="text-amber-400">0 mm (Resting on track)</strong></span>
            <span>Speed: <strong id="sim16Speed" class="text-emerald-400">0 km/h</strong></span>
        </div>
        <!-- Maglev Train carriage -->
        <div id="sim16Train" class="mx-auto w-48 h-14 bg-gradient-to-r from-indigo-700 via-purple-600 to-pink-600 rounded-xl shadow-2xl border border-white/20 flex items-center justify-around text-white font-bold text-sm transition-all duration-700">
            <span>🚅 MAGLEV</span>
            <span class="text-xs font-normal">Repelling Coils</span>
        </div>
        <!-- Track guideway -->
        <div class="w-full h-4 bg-slate-800 rounded border border-slate-600 flex justify-around items-center">
            <div class="w-8 h-2 bg-purple-500 rounded-full"></div>
            <div class="w-8 h-2 bg-purple-500 rounded-full"></div>
            <div class="w-8 h-2 bg-purple-500 rounded-full"></div>
        </div>
    </div>
    <div id="sim16Status" class="mt-2 text-xs text-center text-slate-300">
        Train is resting mechanically on the track. Activate electromagnets to achieve magnetic levitation!
    </div>
</div>
"""
}

# Verify no latex in simulators
for sim_id, sim_code in SIMULATORS.items():
    verify_no_latex(sim_code, f"Simulator {sim_id}")

print(f"Verified {len(SIMULATORS)} bespoke simulators with zero raw LaTeX.")

with open('.agents/class6_science_ch4_sims.py', 'w') as f:
    f.write('"""\nBespoke Interactive Simulators for NCERT Class 6 Science - Chapter 4\n"""\n\nSIMULATORS = ' + repr(SIMULATORS) + '\n')

print("Created .agents/class6_science_ch4_sims.py successfully!")
