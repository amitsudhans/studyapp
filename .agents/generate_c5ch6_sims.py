"""
Generator for 16 bespoke SVG/HTML simulators for NCERT Class 5 Science Chapter 6: Some Unique Places.
Zero raw LaTeX! Clean Unicode symbols.
"""

import sys

SIMULATORS = {}

# Sim 1: Island Explorer & Indira Point Compass
SIMULATORS[1] = """
<div class="space-y-3">
    <div class="p-3 bg-slate-950 rounded-xl border border-slate-800 text-center">
        <span class="text-xs font-bold text-cyan-400 uppercase tracking-wider block mb-1">Island Explorer & Indira Point Compass</span>
        <p class="text-[11px] text-slate-400">An island is land completely surrounded by water on all four sides. Locate India's southernmost tip!</p>
    </div>
    <div class="relative h-60 bg-gradient-to-b from-slate-950 via-cyan-950/30 to-slate-950 rounded-xl border border-slate-800 overflow-hidden p-2 flex items-center justify-center">
        <svg viewBox="0 0 400 240" class="w-full h-full">
            <!-- Ocean Water Background with subtle waves -->
            <rect x="0" y="0" width="400" height="240" fill="#082f49"/>
            <path d="M 0,40 Q 50,35 100,40 T 200,40 T 300,40 T 400,40 L 400,240 L 0,240 Z" fill="#0c4a6e" opacity="0.6"/>
            <path d="M 0,120 Q 50,115 100,120 T 200,120 T 300,120 T 400,120 L 400,240 L 0,240 Z" fill="#075985" opacity="0.4"/>

            <!-- Mainland India Outline (South Tip) on West -->
            <path d="M 40,0 L 40,60 Q 60,110 90,140 Q 110,160 120,180 L 100,190 Q 70,160 50,110 L 30,50 Z" fill="#334155" stroke="#64748b" stroke-width="1.5"/>
            <text x="50" y="40" fill="#94a3b8" font-size="9" font-weight="bold">Indian Mainland</text>
            <text x="55" y="52" fill="#64748b" font-size="8">(Peninsula: 3 sides water)</text>

            <!-- Andaman & Nicobar Chain (East) -->
            <!-- North Andaman -->
            <ellipse cx="250" cy="50" rx="14" ry="24" fill="#059669" stroke="#10b981" stroke-width="1.5"/>
            <text x="270" y="52" fill="#a7f3d0" font-size="8">North & Middle Andaman</text>

            <!-- South & Little Andaman -->
            <ellipse cx="254" cy="105" rx="12" ry="18" fill="#059669" stroke="#10b981" stroke-width="1.5"/>
            <ellipse cx="256" cy="138" rx="9" ry="10" fill="#059669" stroke="#10b981" stroke-width="1.5"/>
            <text x="272" y="108" fill="#a7f3d0" font-size="8">South Andaman (Port Blair)</text>

            <!-- Ten Degree Channel -->
            <line x1="220" y1="156" x2="330" y2="156" stroke="#38bdf8" stroke-dasharray="3,3" stroke-width="1"/>
            <text x="275" y="154" fill="#38bdf8" font-size="7">10° Channel</text>

            <!-- Nicobar Group -->
            <ellipse cx="260" cy="172" rx="10" ry="8" fill="#047857" stroke="#10b981" stroke-width="1.5"/>
            <!-- Great Nicobar -->
            <ellipse cx="265" cy="202" rx="14" ry="16" fill="#047857" stroke="#34d399" stroke-width="1.5"/>
            <text x="284" y="196" fill="#6ee7b7" font-size="8" font-weight="bold">Great Nicobar</text>

            <!-- Indira Point Lighthouse Marker -->
            <g id="indiraMarker" class="cursor-pointer" transform="translate(268, 214)">
                <circle cx="0" cy="0" r="6" fill="#ef4444" opacity="0.8">
                    <animate attributeName="r" values="4;8;4" dur="2s" repeatCount="indefinite"/>
                </circle>
                <circle cx="0" cy="0" r="3" fill="#ffffff"/>
                <polygon points="0,-14 -3,-3 3,-3" fill="#f59e0b"/>
                <rect x="-2" y="-18" width="4" height="4" fill="#ef4444"/>
            </g>
            <text x="280" y="222" fill="#f87171" font-size="9" font-weight="bold">Indira Point (6°45' N)</text>

            <!-- Water Encirclement Indicators (revealed on button click) -->
            <g id="waterFlowArrows" class="opacity-0 transition-opacity duration-300">
                <!-- North, South, East, West water surround labels -->
                <circle cx="265" cy="100" r="45" fill="none" stroke="#38bdf8" stroke-dasharray="4,4" stroke-width="1.5"/>
                <text x="265" y="45" text-anchor="middle" fill="#7dd3fc" font-size="8">▲ North: Bay of Bengal</text>
                <text x="265" y="165" text-anchor="middle" fill="#7dd3fc" font-size="8">▼ South: Indian Ocean</text>
                <text x="325" y="105" fill="#7dd3fc" font-size="8">▶ East: Andaman Sea</text>
                <text x="180" y="105" fill="#7dd3fc" font-size="8">◀ West: Bay of Bengal</text>
            </g>

            <!-- Compass Rose Top Right -->
            <g transform="translate(365, 35)">
                <circle cx="0" cy="0" r="16" fill="#0f172a" stroke="#475569" stroke-width="1"/>
                <line x1="0" y1="-14" x2="0" y2="14" stroke="#94a3b8" stroke-width="1"/>
                <line x1="-14" y1="0" x2="14" y2="0" stroke="#94a3b8" stroke-width="1"/>
                <polygon points="0,-13 -3,0 3,0" fill="#ef4444"/>
                <polygon points="0,13 -3,0 3,0" fill="#cbd5e1"/>
                <text x="0" y="-15" text-anchor="middle" fill="#ef4444" font-size="8" font-weight="bold">N</text>
                <text x="0" y="23" text-anchor="middle" fill="#94a3b8" font-size="7">S</text>
            </g>
        </svg>
    </div>
    <div class="grid grid-cols-2 gap-2">
        <button onclick="toggleIslandWaterCheck()" id="sim1WaterBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition flex items-center justify-center space-x-1">
            <span>Verify Water Surround</span>
        </button>
        <button onclick="zoomIndiraPoint()" id="sim1IndiraBtn" class="py-2 px-3 rounded-xl text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 transition flex items-center justify-center space-x-1">
            <span>Locate Indira Point (6°45' N)</span>
        </button>
    </div>
    <div id="sim1Status" class="p-2.5 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-300">
        <span class="text-cyan-400 font-bold">Island Fact:</span> An island has 360° water boundaries. India's mainland is a peninsula (water on 3 sides), while the Andaman & Nicobar group is a true island archipelago!
    </div>
</div>
"""

print("Sim 1 generated")
