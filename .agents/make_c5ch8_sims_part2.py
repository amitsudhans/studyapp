"""
Simulators 9 to 16 for NCERT Class 5 Science Chapter 8: Clothes - How Things are Made
Zero raw LaTeX! Clean Unicode symbols.
"""

import sys

SIMS = {}

# SIM 9: Running Stitch Master (Activity 7 & 8)
SIMS[9] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-sky-400 uppercase tracking-wider block mb-1">Running Stitch Master (Kaccha Tanka)</span>
        <p class="text-[11px] text-slate-400">Master the rhythmic in-and-out needle motion joining tailor scrap patches into a durable coaster or mat.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Two Fabric Scrap Layers Overlapping -->
            <!-- Patch A: Teal -->
            <polygon points="50,40 220,40 200,200 50,200" fill="#0f766e" stroke="#14b8a6" stroke-width="2"/>
            <text x="110" y="70" fill="#99f6e4" font-size="10" font-weight="bold">Patch A (Cotton)</text>

            <!-- Patch B: Purple (Overlapping) -->
            <polygon points="180,40 350,40 350,200 160,200" fill="#6b21a8" stroke="#a855f7" stroke-width="2" opacity="0.9"/>
            <text x="270" y="70" fill="#e9d5ff" font-size="10" font-weight="bold">Patch B (Linen)</text>

            <!-- Running Stitch Seam (Vertical overlap line) -->
            <g id="runningStitchPathGroup">
                <!-- Seam baseline -->
                <line x1="190" y1="50" x2="190" y2="190" stroke="#334155" stroke-width="1" stroke-dasharray="2,2"/>
                <!-- Running stitches (Alternating in and out dashes) -->
                <line id="stitchSeg1" x1="190" y1="55" x2="190" y2="75" stroke="#fef08a" stroke-width="3.5" stroke-linecap="round"/>
                <line id="stitchSeg2" x1="190" y1="85" x2="190" y2="105" stroke="#fef08a" stroke-width="3.5" stroke-linecap="round"/>
                <line id="stitchSeg3" x1="190" y1="115" x2="190" y2="135" stroke="#fef08a" stroke-width="3.5" stroke-linecap="round"/>
                <line id="stitchSeg4" x1="190" y1="145" x2="190" y2="165" stroke="#fef08a" stroke-width="3.5" stroke-linecap="round"/>
            </g>

            <!-- Active Needle and Thread -->
            <g id="activeNeedle" transform="translate(190, 165)">
                <!-- Golden Needle pointing down -->
                <line x1="0" y1="0" x2="15" y2="25" stroke="#e2e8f0" stroke-width="2.5" stroke-linecap="round"/>
                <circle cx="0" cy="0" r="1.5" fill="#0f172a"/>
                <!-- Yellow Thread trailing from eye -->
                <path d="M 0,0 Q -15,-15 -10,-35" stroke="#fef08a" stroke-width="2" fill="none"/>
            </g>

            <!-- Live Stitch Counter -->
            <rect x="250" y="160" width="130" height="42" rx="6" fill="#020617" stroke="#334155" opacity="0.9"/>
            <text x="260" y="174" fill="#94a3b8" font-size="8">STITCH RHYTHM</text>
            <text id="stitchCountText" x="260" y="192" fill="#38bdf8" font-size="11" font-weight="bold">In - Out - In - Out</text>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="advanceRunningStitch()" class="flex-1 p-2 bg-teal-600 hover:bg-teal-500 rounded-lg text-xs font-bold text-white">
            Drive Needle (In & Out Stitch)
        </button>
        <button onclick="resetRunningStitch()" class="p-2 bg-slate-800 hover:bg-slate-700 rounded-lg text-xs font-semibold text-slate-300">
            Reset Seam
        </button>
    </div>
    <div id="sim9Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        In-and-out rhythm: Passing the needle straight through both fabric layers binds scrap pieces into a strong, uniform composite mat.
    </div>
</div>
"""

# SIM 10: Lucknow Chikankari & Banjara Mirror Studio
SIMS[10] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-pink-400 uppercase tracking-wider block mb-1">Chikankari & Banjara Mirror Studio</span>
        <p class="text-[11px] text-slate-400">Toggle between Lucknow translucent shadow-work (Bakhiya) and vibrant Rajasthani Banjara mirror embroidery.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Studio Display Stage -->
            <g id="craftStudioContent">
                <!-- Mode A: Lucknow Chikankari (Default) -->
                <!-- Sheer Muslin Cloth background -->
                <rect x="70" y="25" width="260" height="190" rx="8" fill="#1e293b" stroke="#e2e8f0" stroke-width="1.5"/>
                <rect x="75" y="30" width="250" height="180" rx="6" fill="#f8fafc" opacity="0.15"/>

                <!-- Paisley / Floral Shadow-Work Motif -->
                <path d="M 200,60 C 160,80 160,140 200,165 C 240,140 240,80 200,60 Z" fill="#ffffff" opacity="0.3" stroke="#ffffff" stroke-width="2"/>
                <!-- Crisscross Herringbone Bakhiya Stitches on reverse -->
                <path d="M 180,90 L 220,110 M 180,110 L 220,90 M 180,110 L 220,130 M 180,130 L 220,110 M 185,130 L 215,150 M 185,150 L 215,130" stroke="#f8fafc" stroke-width="2.5" opacity="0.6"/>
                <!-- Tiny knot stitches (Murri) in center -->
                <circle cx="200" cy="110" r="3" fill="#ffffff"/>
                <circle cx="200" cy="125" r="3" fill="#ffffff"/>

                <text x="200" y="195" fill="#f8fafc" font-size="10" font-weight="bold" text-anchor="middle">Lucknow Chikankari: Bakhiya Shadow Work</text>
            </g>

            <!-- Mode Tag -->
            <rect x="25" y="20" width="120" height="30" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="craftStudioTag" x="85" y="39" fill="#f472b6" font-size="9" font-weight="bold" text-anchor="middle">CHIKANKARI MODE</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="switchCraftMode('chikankari')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-pink-500/50 text-xs font-semibold text-pink-300">
            Lucknow Chikankari
        </button>
        <button onclick="switchCraftMode('banjara')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-amber-500/50 text-xs font-semibold text-amber-300">
            Banjara Mirror Work
        </button>
    </div>
    <div id="sim10Description" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Bakhiya (Shadow Stitch):</strong> Worked in a crisscross herringbone pattern on the reverse side of fine muslin, casting a delicate translucent shadow motif on the front.
    </div>
</div>
"""

# SIM 11: Kantha Quilt Storyteller & Gota Patti
SIMS[11] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Kantha Quilt & Gota Patti Studio</span>
        <p class="text-[11px] text-slate-400">Discover how layered sarees form ripple-quilted Kantha, and how gold ribbon petals form Gota Patti applique.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <g id="sim11Canvas">
                <!-- 5 Layered Old Sarees stacked -->
                <rect x="50" y="40" width="200" height="150" fill="#dc2626" opacity="0.3" transform="rotate(-3 150 115)"/>
                <rect x="50" y="40" width="200" height="150" fill="#2563eb" opacity="0.4" transform="rotate(2 150 115)"/>
                <rect x="50" y="40" width="200" height="150" fill="#f59e0b" opacity="0.5"/>

                <!-- Thousands of tiny rippling running stitches -->
                <path d="M 60,60 Q 150,55 240,60 M 60,75 Q 150,70 240,75 M 60,90 Q 150,85 240,90 M 60,105 Q 150,100 240,105 M 60,120 Q 150,115 240,120 M 60,135 Q 150,130 240,135 M 60,150 Q 150,145 240,150 M 60,165 Q 150,160 240,165" stroke="#fef08a" stroke-width="1.8" stroke-dasharray="5,4" fill="none"/>

                <!-- Folk Lotus / Fish Motif in Center of Quilt -->
                <path d="M 150,115 C 135,95 165,95 150,115 Z M 130,115 C 120,100 140,100 135,115 Z M 170,115 C 180,100 160,100 165,115 Z" fill="#ffffff" stroke="#e11d48" stroke-width="1.5"/>
            </g>

            <!-- Layer Count Inspector (Right) -->
            <rect x="270" y="30" width="115" height="100" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="280" y="46" fill="#94a3b8" font-size="8">KANTHA COMPOSITE</text>
            <text x="280" y="62" fill="#f59e0b" font-size="11" font-weight="bold">5 Layers Stacked</text>
            <text x="280" y="76" fill="#cbd5e1" font-size="7.5">Soft Worn Cotton</text>
            <text x="280" y="88" fill="#94a3b8" font-size="7.5">Air-Trapping Ripples</text>
            <text x="280" y="100" fill="#4ade80" font-size="7.5">Tensile Composite</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="switchSim11('kantha')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-amber-500/50 text-xs font-semibold text-amber-300">
            Kantha Quilt (Bengal/Odisha)
        </button>
        <button onclick="switchSim11('gotapatti')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-yellow-500/50 text-xs font-semibold text-yellow-300">
            Gota Patti (Rajasthan)
        </button>
    </div>
    <div id="sim11Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Kantha:</strong> Women layer soft, discarded cotton sarees, sewing them together with thousands of rippling running stitches using unravelled border threads.
    </div>
</div>
"""

# SIM 12: Punjab Phulkari & Nilgiri Toda Shawl
SIMS[12] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-rose-400 uppercase tracking-wider block mb-1">Phulkari & Toda Geometry Studio</span>
        <p class="text-[11px] text-slate-400">Compare Punjab's silk floss darning stitch (Phulkari) with the Toda tribe's counted-thread red & black buffalo motifs.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <g id="sim12Canvas">
                <!-- Default: Punjab Phulkari -->
                <!-- Coarse dark khaddar base cloth -->
                <rect x="60" y="25" width="280" height="190" rx="8" fill="#451a03" stroke="#78350f" stroke-width="2"/>

                <!-- Vibrant geometric floral darning stitches (Pat silk floss) -->
                <!-- Center large diamond flower -->
                <polygon points="200,60 250,120 200,180 150,120" fill="#f59e0b" stroke="#ea580c" stroke-width="2"/>
                <polygon points="200,80 230,120 200,160 170,120" fill="#e11d48" stroke="#be123c" stroke-width="1.5"/>
                <polygon points="200,100 215,120 200,140 185,120" fill="#fde047"/>

                <!-- Corner floral triangles -->
                <polygon points="70,35 110,35 70,75" fill="#059669"/>
                <polygon points="330,35 290,35 330,75" fill="#059669"/>
                <polygon points="70,205 110,205 70,165" fill="#059669"/>
                <polygon points="330,205 290,205 330,165" fill="#059669"/>

                <text x="200" y="200" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">Punjab Phulkari: Reverse Darning Stitch (Bagh)</text>
            </g>

            <!-- Mode Selector Tag -->
            <rect x="25" y="20" width="110" height="28" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="sim12ModeTag" x="80" y="38" fill="#fb7185" font-size="9" font-weight="bold" text-anchor="middle">PHULKARI</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="switchSim12('phulkari')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-amber-500/50 text-xs font-semibold text-amber-300">
            Punjab Phulkari
        </button>
        <button onclick="switchSim12('toda')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-red-500/50 text-xs font-semibold text-red-300">
            Nilgiri Toda Shawl
        </button>
    </div>
    <div id="sim12Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Phulkari:</strong> Stitched with untwisted silk floss (pat) from the back of coarse handspun cotton cloth, creating a lustrous floral tapestry.
    </div>
</div>
"""

# SIM 13: Kashmiri Kashida & Meghalaya Khneng
SIMS[13] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-teal-400 uppercase tracking-wider block mb-1">Kashmiri Kashida & Meghalaya Khneng</span>
        <p class="text-[11px] text-slate-400">Witness the rich diversity of Indian needlecraft: Kashmir's Chinar leaf crewel work vs Meghalaya's river fish-bone stitch.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <g id="sim13Canvas">
                <!-- Kashmiri Kashida: Warm Woollen Shawl with Chinar Leaf -->
                <rect x="60" y="25" width="280" height="190" rx="8" fill="#1e1b4b" stroke="#4338ca" stroke-width="2"/>

                <!-- Graceful Chinar Leaf Motif (Crewel chain stitch) -->
                <path d="M 200,60 C 190,80 160,85 155,105 C 170,115 160,135 150,150 C 170,150 185,160 195,175 C 200,165 205,165 205,175 C 215,160 230,150 250,150 C 240,135 230,115 245,105 C 240,85 210,80 200,60 Z" fill="#b45309" stroke="#f59e0b" stroke-width="2.5"/>
                <!-- Central Leaf Vein -->
                <line x1="200" y1="65" x2="200" y2="175" stroke="#fef08a" stroke-width="2"/>
                <line x1="200" y1="100" x2="170" y2="120" stroke="#fde047" stroke-width="1.5"/>
                <line x1="200" y1="100" x2="230" y2="120" stroke="#fde047" stroke-width="1.5"/>
                <line x1="200" y1="130" x2="175" y2="145" stroke="#fde047" stroke-width="1.5"/>
                <line x1="200" y1="130" x2="225" y2="145" stroke="#fde047" stroke-width="1.5"/>

                <text x="200" y="200" fill="#fde047" font-size="10" font-weight="bold" text-anchor="middle">Kashmiri Kashida: Chinar Autumn Leaf Motif</text>
            </g>

            <rect x="25" y="20" width="115" height="28" rx="5" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text id="sim13ModeTag" x="82" y="38" fill="#2dd4bf" font-size="9" font-weight="bold" text-anchor="middle">KASHIDA</text>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="switchSim13('kashida')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-amber-500/50 text-xs font-semibold text-amber-300">
            Kashmiri Kashida
        </button>
        <button onclick="switchSim13('khneng')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-teal-500/50 text-xs font-semibold text-teal-300">
            Meghalaya Khneng
        </button>
    </div>
    <div id="sim13Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        <strong>Kashida (Kashmir):</strong> Uses single-strand chain stitch with jewel-toned threads to replicate Kashmir's famous autumn Chinar leaves and singing nightingales.
    </div>
</div>
"""

# SIM 14: Circular Textile Upcycling Wheel
SIMS[14] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Zero-Waste Circular Textile Wheel</span>
        <p class="text-[11px] text-slate-400">Step through the 5 stages of an Indian cotton garment's life cycle from new attire to organic soil compost.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Circular Flow Orbit -->
            <circle cx="200" cy="120" r="75" fill="none" stroke="#334155" stroke-width="3" stroke-dasharray="6,4"/>

            <!-- Central Hub -->
            <circle cx="200" cy="120" r="30" fill="#0f172a" stroke="#22c55e" stroke-width="2"/>
            <text x="200" y="117" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">ZERO</text>
            <text x="200" y="128" fill="#cbd5e1" font-size="8" text-anchor="middle">WASTE</text>

            <!-- 5 Node Circles along circumference -->
            <!-- Node 1: New Clothes (Top) -->
            <g id="nodeUpcycle1" class="cursor-pointer" onclick="setUpcycleStage(1)">
                <circle cx="200" cy="45" r="16" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
                <text x="200" y="49" font-size="12" text-anchor="middle">👕</text>
            </g>

            <!-- Node 2: Sibling Hand-Me-Down (Right Top) -->
            <g id="nodeUpcycle2" class="cursor-pointer" onclick="setUpcycleStage(2)">
                <circle cx="270" cy="95" r="16" fill="#1e293b" stroke="#a855f7" stroke-width="2"/>
                <text x="270" y="99" font-size="12" text-anchor="middle">🧒</text>
            </g>

            <!-- Node 3: Godhari Quilt / Toy (Right Bottom) -->
            <g id="nodeUpcycle3" class="cursor-pointer" onclick="setUpcycleStage(3)">
                <circle cx="245" cy="175" r="16" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                <text x="245" y="179" font-size="12" text-anchor="middle">🛏️</text>
            </g>

            <!-- Node 4: Cleaning Mop / Duster (Left Bottom) -->
            <g id="nodeUpcycle4" class="cursor-pointer" onclick="setUpcycleStage(4)">
                <circle cx="155" cy="175" r="16" fill="#1e293b" stroke="#f43f5e" stroke-width="2"/>
                <text x="155" y="179" font-size="12" text-anchor="middle">🧹</text>
            </g>

            <!-- Node 5: Soil Compost (Left Top) -->
            <g id="nodeUpcycle5" class="cursor-pointer" onclick="setUpcycleStage(5)">
                <circle cx="130" cy="95" r="16" fill="#1e293b" stroke="#22c55e" stroke-width="2"/>
                <text x="130" y="99" font-size="12" text-anchor="middle">🌱</text>
            </g>

            <!-- Current Stage Readout -->
            <rect x="25" y="20" width="135" height="38" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="35" y="34" fill="#94a3b8" font-size="8">LIFECYCLE STAGE</text>
            <text id="upcycleStageName" x="35" y="48" fill="#4ade80" font-size="10" font-weight="bold">1. New Garment</text>
        </svg>
    </div>
    <div class="grid grid-cols-5 gap-1">
        <button onclick="setUpcycleStage(1)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-sky-500/50 text-[10px] font-semibold text-sky-300">1. New</button>
        <button onclick="setUpcycleStage(2)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-purple-500/50 text-[10px] font-semibold text-purple-300">2. Sibling</button>
        <button onclick="setUpcycleStage(3)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-amber-500/50 text-[10px] font-semibold text-amber-300">3. Quilt</button>
        <button onclick="setUpcycleStage(4)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-rose-500/50 text-[10px] font-semibold text-rose-300">4. Mop</button>
        <button onclick="setUpcycleStage(5)" class="p-1.5 bg-slate-900 hover:bg-slate-800 rounded border border-emerald-500/50 text-[10px] font-semibold text-emerald-300">5. Soil</button>
    </div>
    <div id="sim14Explanation" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        Stage 1: A freshly spun and handwoven cotton kurta is worn for festive occasions and daily school.
    </div>
</div>
"""

# SIM 15: Forensic Flame Burn Test Laboratory
SIMS[15] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-amber-400 uppercase tracking-wider block mb-1">Forensic Fibre Burn Test Laboratory</span>
        <p class="text-[11px] text-slate-400">Scientifically identify mystery fabrics by observing their flame reaction, smoke odor, and ash residue.</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Lab burner bench -->
            <rect x="50" y="190" width="300" height="15" rx="3" fill="#1e293b" stroke="#334155" stroke-width="1.5"/>

            <!-- Spirit Lamp / Bunsen Burner -->
            <rect x="185" y="150" width="30" height="40" rx="4" fill="#64748b" stroke="#94a3b8" stroke-width="1.5"/>
            <polygon points="195,150 205,150 203,142 197,142" fill="#cbd5e1"/>
            <!-- Active Flame -->
            <path d="M 200,142 Q 192,125 200,105 Q 208,125 200,142" fill="#f59e0b">
                <animate attributeName="d" values="M 200,142 Q 192,125 200,105 Q 208,125 200,142; M 200,142 Q 188,120 200,100 Q 212,120 200,142; M 200,142 Q 192,125 200,105 Q 208,125 200,142" dur="1s" repeatCount="indefinite"/>
            </path>
            <path d="M 200,142 Q 196,132 200,118 Q 204,132 200,142" fill="#38bdf8"/>

            <!-- Tweezer holding mystery yarn strand -->
            <line x1="120" y1="85" x2="190" y2="115" stroke="#94a3b8" stroke-width="3"/>
            <circle cx="190" cy="115" r="3" fill="#64748b"/>

            <!-- Reaction Diagnostics Card -->
            <rect x="250" y="25" width="135" height="110" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="260" y="42" fill="#94a3b8" font-size="8">BURN TEST SIGNATURE</text>
            <text id="burnSampleName" x="260" y="58" fill="#38bdf8" font-size="10" font-weight="bold">Cotton Sample</text>
            <text id="burnOdorText" x="260" y="74" fill="#cbd5e1" font-size="8">Odor: Burning paper</text>
            <text id="burnAshText" x="260" y="90" fill="#cbd5e1" font-size="8">Ash: Light powdery grey</text>
            <text id="burnVerdict" x="260" y="112" fill="#4ade80" font-size="8.5" font-weight="bold">Natural Plant Cellulose</text>
        </svg>
    </div>
    <div class="grid grid-cols-3 gap-2">
        <button onclick="burnSample('cotton')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-sky-500/50 text-xs font-semibold text-sky-300">Test Cotton</button>
        <button onclick="burnSample('wool')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-amber-500/50 text-xs font-semibold text-amber-300">Test Wool / Silk</button>
        <button onclick="burnSample('polyester')" class="p-2 bg-slate-900 hover:bg-slate-800 rounded-lg border border-rose-500/50 text-xs font-semibold text-rose-300">Test Polyester</button>
    </div>
    <div id="sim15Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        Cotton burns with a steady flame, smells like burning paper (cellulose), and leaves soft, harmless grey ash.
    </div>
</div>
"""

# SIM 16: Textile Guardian Workshop & 20 km Thread Meter
SIMS[16] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-emerald-400 uppercase tracking-wider block mb-1">Textile Guardian Workshop</span>
        <p class="text-[11px] text-slate-400">Discover the 20 km of thread woven into a single shirt, mend a loose button, and earn your Textile Guardian badge!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-slate-900 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Cotton Shirt Outline -->
            <path d="M 160,50 L 130,70 L 90,85 L 110,135 L 140,120 L 140,210 L 260,210 L 260,120 L 290,135 L 310,85 L 270,70 L 240,50 Q 200,75 160,50 Z" fill="#1e293b" stroke="#38bdf8" stroke-width="2"/>
            <!-- Collar & Placket -->
            <path d="M 160,50 L 200,75 L 240,50" fill="none" stroke="#38bdf8" stroke-width="2"/>
            <line x1="200" y1="75" x2="200" y2="210" stroke="#475569" stroke-width="2"/>

            <!-- Buttons on placket -->
            <circle cx="200" cy="100" r="5" fill="#f8fafc" stroke="#64748b"/>
            <!-- Loose button (Stage 2 mending target) -->
            <g id="looseButton" class="cursor-pointer" onclick="mendButton()">
                <circle cx="200" cy="135" r="5" fill="#fef08a" stroke="#ca8a04" stroke-width="1.5"/>
                <line x1="198" y1="133" x2="202" y2="137" stroke="#020617"/>
                <line x1="198" y1="137" x2="202" y2="133" stroke="#020617"/>
            </g>
            <circle cx="200" cy="170" r="5" fill="#f8fafc" stroke="#64748b"/>

            <!-- 20 km Thread Meter (Left) -->
            <rect x="20" y="25" width="95" height="75" rx="6" fill="#020617" stroke="#334155" opacity="0.95"/>
            <text x="28" y="40" fill="#94a3b8" font-size="8">SHIRT THREAD SPAN</text>
            <text id="threadSpanNumber" x="28" y="60" fill="#38bdf8" font-size="14" font-weight="bold">21.4 km</text>
            <text x="28" y="74" fill="#cbd5e1" font-size="7.5">Enough yarn to link</text>
            <text x="28" y="86" fill="#4ade80" font-size="7.5">two nearby towns!</text>

            <!-- Guardian Badge (Right) -->
            <g id="guardianBadgeGroup" transform="translate(290, 30)">
                <circle cx="45" cy="45" r="38" fill="#0f172a" stroke="#eab308" stroke-width="2"/>
                <polygon points="45,15 53,35 75,35 57,48 64,68 45,55 26,68 33,48 15,35 37,35" fill="#eab308"/>
                <text x="45" y="74" fill="#fef08a" font-size="7" font-weight="bold" text-anchor="middle">GUARDIAN</text>
            </g>
        </svg>
    </div>
    <div class="flex items-center gap-2">
        <button onclick="mendButton()" class="flex-1 p-2 bg-emerald-600 hover:bg-emerald-500 rounded-lg text-xs font-bold text-white">
            Mend Loose Button (Needle & Thread)
        </button>
        <button onclick="pledgeGuardian()" class="flex-1 p-2 bg-amber-600 hover:bg-amber-500 rounded-lg text-xs font-bold text-white">
            Sign Textile Guardian Pledge
        </button>
    </div>
    <div id="sim16Status" class="p-2 bg-slate-900/60 rounded-lg border border-slate-800 text-[11px] text-slate-300">
        One shirt contains over 20 kilometres of fine spun yarn. Caring for and mending small tears honours the tremendous labour of farmers and weavers.
    </div>
</div>
"""

print("Simulators 9 to 16 defined.")

