<!-- GEOMETRIC DRAWING & SHAPE BOARD MODAL -->
<div id="drawToolModal" style="z-index: 99999;" class="hidden fixed inset-0 bg-black/85 backdrop-blur-md overflow-y-auto p-2 sm:p-4 flex justify-center items-start">
    <div class="bg-slate-900 border border-slate-700/80 rounded-2xl sm:rounded-3xl w-full max-w-5xl max-h-[96vh] flex flex-col overflow-hidden shadow-2xl my-1 sm:my-2">
        <!-- Modal Header -->
        <div class="px-4 sm:px-6 py-3 border-b border-slate-800 flex items-center justify-between bg-slate-950/90 shrink-0">
            <div class="flex items-center space-x-3">
                <div class="w-10 h-10 rounded-2xl bg-gradient-to-br from-emerald-500/20 to-teal-500/20 border border-emerald-500/40 text-emerald-400 flex items-center justify-center font-bold text-lg shadow-inner shrink-0">
                    <span>📐</span>
                </div>
                <div>
                    <div class="flex items-center space-x-2 flex-wrap">
                        <h3 class="text-sm sm:text-base font-bold text-white tracking-tight">Draw Tool — Geometry & Shapes</h3>
                        <span class="px-2 py-0.5 rounded-full text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30">Triangle • Square • Circle • 3D Solids</span>
                    </div>
                    <p class="text-[11px] text-slate-400">Draw or stamp geometric diagrams with measurements, and insert directly into your question prompt.</p>
                </div>
            </div>
            <button type="button" onclick="closeDrawToolModal()" class="w-8 h-8 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-400 hover:text-white flex items-center justify-center transition-all cursor-pointer border border-slate-700">
                <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg>
            </button>
        </div>

        <!-- Toolbars & Controls Area -->
        <div class="p-3 bg-slate-950/60 border-b border-slate-800 space-y-2.5 shrink-0">
            <!-- Row 1: Categories & Primary Tools -->
            <div class="flex items-center justify-between gap-2 flex-wrap">
                <!-- Tool Category Tabs -->
                <div class="flex items-center space-x-1 bg-slate-900 p-1 rounded-xl border border-slate-800 text-xs">
                    <button type="button" onclick="selectDrawCategory('shapes', this)" class="draw-cat-btn active px-2.5 py-1 rounded-lg bg-indigo-600 text-white font-semibold transition-all">
                        📐 Shapes
                    </button>
                    <button type="button" onclick="selectDrawCategory('presets', this)" class="draw-cat-btn px-2.5 py-1 rounded-lg hover:bg-slate-800 text-slate-300 font-medium transition-all">
                        ⚡ Quick Presets
                    </button>
                    <button type="button" onclick="selectDrawCategory('freehand', this)" class="draw-cat-btn px-2.5 py-1 rounded-lg hover:bg-slate-800 text-slate-300 font-medium transition-all">
                        ✏️ Freehand & Labels
                    </button>
                </div>

                <!-- Secondary Global Actions -->
                <div class="flex items-center space-x-1.5 ml-auto">
                    <input type="file" id="draw_image_file_input" accept="image/*" class="hidden" onchange="handleDrawImageUpload(this)">
                    <button type="button" onclick="document.getElementById('draw_image_file_input').click()" title="Upload or Paste (Ctrl+V) Textbook Diagram" class="px-2.5 py-1 rounded-lg bg-sky-600/20 hover:bg-sky-600/30 text-sky-300 border border-sky-500/30 text-xs font-semibold flex items-center space-x-1 cursor-pointer transition-colors">
                        <span>📁</span>
                        <span class="hidden sm:inline">Upload Image</span>
                        <span class="text-[10px] text-sky-400 font-mono">(Ctrl+V)</span>
                    </button>
                    <button type="button" onclick="undoDraw()" title="Undo (Ctrl+Z)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center space-x-1 cursor-pointer transition-colors">
                        <span>↩️</span>
                        <span class="hidden sm:inline">Undo</span>
                    </button>
                    <button type="button" onclick="redoDraw()" title="Redo (Ctrl+Y)" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-200 border border-slate-700 text-xs font-semibold flex items-center space-x-1 cursor-pointer transition-colors">
                        <span>↪️</span>
                        <span class="hidden sm:inline">Redo</span>
                    </button>
                    <button type="button" onclick="clearDrawCanvas()" title="Clear Canvas" class="px-2.5 py-1 rounded-lg bg-rose-500/10 hover:bg-rose-500/20 text-rose-300 border border-rose-500/30 text-xs font-semibold flex items-center space-x-1 cursor-pointer transition-colors">
                        <span>🗑️</span>
                        <span class="hidden sm:inline">Clear</span>
                    </button>
                </div>
            </div>

            <!-- Row 2: Sub-tools based on selected category -->
            <!-- 1. Shapes Sub-toolbar -->
            <div id="draw_tools_shapes" class="flex items-center gap-1.5 flex-wrap overflow-x-auto pb-1 text-xs scrollbar-thin">
                <span class="text-[10px] uppercase font-bold text-slate-500 mr-1 shrink-0">Triangles:</span>
                <button type="button" onclick="setDrawTool('right_triangle', this)" class="shape-tool-btn active px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">⊿</span>
                    <span>Right △ (90°)</span>
                </button>
                <button type="button" onclick="setDrawTool('triangle', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">△</span>
                    <span>Triangle</span>
                </button>
                <button type="button" onclick="setDrawTool('isosceles', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">◬</span>
                    <span>Isosceles △</span>
                </button>
                <button type="button" onclick="setDrawTool('polyline', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0" title="Click point by point to draw any scalene triangle or custom polygon">
                    <span class="font-bold">☡</span>
                    <span>Connected Lines (Arbitrary △)</span>
                </button>
                <button id="draw_finish_polyline_btn" type="button" onclick="finishPolyline()" class="hidden px-2.5 py-1 rounded-lg bg-emerald-600 hover:bg-emerald-500 text-white font-bold text-xs shrink-0 animate-pulse">
                    ✓ Finish Shape
                </button>

                <span class="text-slate-700 mx-0.5">|</span>
                <span class="text-[10px] uppercase font-bold text-slate-500 mr-1 shrink-0">Quadrilaterals:</span>
                <button type="button" onclick="setDrawTool('square', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">□</span>
                    <span>Square</span>
                </button>
                <button type="button" onclick="setDrawTool('rectangle', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">▭</span>
                    <span>Rectangle</span>
                </button>
                <button type="button" onclick="setDrawTool('parallelogram', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">▱</span>
                    <span>Parallelogram</span>
                </button>
                <button type="button" onclick="setDrawTool('trapezoid', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">⏢</span>
                    <span>Trapezoid</span>
                </button>
                <button type="button" onclick="setDrawTool('rhombus', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">◇</span>
                    <span>Rhombus</span>
                </button>

                <span class="text-slate-700 mx-0.5">|</span>
                <span class="text-[10px] uppercase font-bold text-slate-500 mr-1 shrink-0">Circles & 3D:</span>
                <button type="button" onclick="setDrawTool('circle', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">○</span>
                    <span>Circle</span>
                </button>
                <button type="button" onclick="setDrawTool('circle_radius', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">⊙</span>
                    <span>Circle + Radius</span>
                </button>
                <button type="button" onclick="setDrawTool('cylinder', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span>🛢️</span>
                    <span>Cylinder</span>
                </button>
                <button type="button" onclick="setDrawTool('cone', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span>🍦</span>
                    <span>Cone</span>
                </button>
                <button type="button" onclick="setDrawTool('cube', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span>📦</span>
                    <span>Cube 3D</span>
                </button>

                <span class="text-slate-700 mx-0.5">|</span>
                <span class="text-[10px] uppercase font-bold text-slate-500 mr-1 shrink-0">Lines & Axes:</span>
                <button type="button" onclick="setDrawTool('line', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">―</span>
                    <span>Line</span>
                </button>
                <button type="button" onclick="setDrawTool('arrow', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">⟶</span>
                    <span>Arrow / Ray</span>
                </button>
                <button type="button" onclick="setDrawTool('double_arrow', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">⟷</span>
                    <span>Dimension</span>
                </button>
                <button type="button" onclick="setDrawTool('axes', this)" class="shape-tool-btn px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1 shrink-0">
                    <span class="font-bold">┼</span>
                    <span>X-Y Plane</span>
                </button>
            </div>

            <!-- 2. Presets Sub-toolbar -->
            <div id="draw_tools_presets" class="hidden flex items-center gap-2 flex-wrap overflow-x-auto pb-1 text-xs scrollbar-thin">
                <span class="text-[10px] uppercase font-bold text-amber-400 mr-1 shrink-0">One-Click Presets:</span>
                <button type="button" onclick="stampPreset('triangle_pqr_st')" class="px-3 py-1 rounded-lg bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white font-bold border border-emerald-400/50 shadow-md transition-all shrink-0">
                    ⭐ △ PQR with Line ST (20 cm)
                </button>
                <button type="button" onclick="stampPreset('right_triangle_abc')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    ⊿ Right △ (ABC with 90°)
                </button>
                <button type="button" onclick="stampPreset('equilateral_triangle')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    △ Equilateral △ (ABC + altitude h)
                </button>
                <button type="button" onclick="stampPreset('square_abcd')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    □ Square (ABCD + side s)
                </button>
                <button type="button" onclick="stampPreset('rectangle_abcd')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    ▭ Rectangle (ABCD + l, w)
                </button>
                <button type="button" onclick="stampPreset('circle_radius_r')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    ⊙ Circle (Center O + Radius r)
                </button>
                <button type="button" onclick="stampPreset('coordinate_plane')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    📊 Coordinate Axes (X, Y, O)
                </button>
                <button type="button" onclick="stampPreset('cylinder_rh')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    🛢️ Cylinder (r, h)
                </button>
                <button type="button" onclick="stampPreset('cone_rhl')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    🍦 Cone (r, h, l)
                </button>
                <button type="button" onclick="stampPreset('cube_3d')" class="px-2.5 py-1 rounded-lg bg-slate-800 hover:bg-emerald-600 text-slate-200 hover:text-white border border-slate-700 transition-all shrink-0">
                    📦 3D Cube / Cuboid
                </button>
            </div>

            <!-- 3. Freehand & Labels Sub-toolbar -->
            <div id="draw_tools_freehand" class="hidden flex items-center gap-2 flex-wrap pb-1 text-xs">
                <span class="text-[10px] uppercase font-bold text-slate-500 mr-1 shrink-0">Freehand & Text:</span>
                <button type="button" onclick="setDrawTool('pen', this)" class="shape-tool-btn px-3 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1.5 shrink-0">
                    <span>✏️</span>
                    <span>Freehand Pen</span>
                </button>
                <button type="button" onclick="setDrawTool('text', this)" class="shape-tool-btn px-3 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1.5 shrink-0">
                    <span>🔤</span>
                    <span>Add Text Label (Click Canvas)</span>
                </button>
                <button type="button" onclick="setDrawTool('eraser', this)" class="shape-tool-btn px-3 py-1 rounded-lg bg-slate-800 hover:bg-indigo-600/50 text-slate-200 border border-slate-700 flex items-center space-x-1.5 shrink-0">
                    <span>🧹</span>
                    <span>Eraser</span>
                </button>

                <span class="text-slate-700 mx-1">|</span>
                <span class="text-[10px] uppercase font-bold text-slate-500 mr-1 shrink-0">Quick Click-to-Stamp Labels:</span>
                <div class="flex items-center space-x-1 overflow-x-auto scrollbar-thin">
                    <button type="button" onclick="quickSelectLabel('P')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">P</button>
                    <button type="button" onclick="quickSelectLabel('Q')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">Q</button>
                    <button type="button" onclick="quickSelectLabel('R')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">R</button>
                    <button type="button" onclick="quickSelectLabel('S')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">S</button>
                    <button type="button" onclick="quickSelectLabel('T')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">T</button>
                    <button type="button" onclick="quickSelectLabel('20 cm')" class="px-2 py-0.5 rounded bg-emerald-900/60 hover:bg-emerald-600 text-emerald-300 hover:text-white border border-emerald-500/40 text-xs font-bold font-mono">20 cm</button>
                    <button type="button" onclick="quickSelectLabel('10 cm')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">10 cm</button>
                    <button type="button" onclick="quickSelectLabel('5 cm')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">5 cm</button>
                    <button type="button" onclick="quickSelectLabel('A')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">A</button>
                    <button type="button" onclick="quickSelectLabel('B')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">B</button>
                    <button type="button" onclick="quickSelectLabel('C')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">C</button>
                    <button type="button" onclick="quickSelectLabel('D')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">D</button>
                    <button type="button" onclick="quickSelectLabel('O')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">O</button>
                    <button type="button" onclick="quickSelectLabel('x')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">x</button>
                    <button type="button" onclick="quickSelectLabel('y')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">y</button>
                    <button type="button" onclick="quickSelectLabel('r')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">r</button>
                    <button type="button" onclick="quickSelectLabel('h')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">h</button>
                    <button type="button" onclick="quickSelectLabel('90°')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">90°</button>
                    <button type="button" onclick="quickSelectLabel('θ')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">θ</button>
                    <button type="button" onclick="quickSelectLabel('cm')" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-xs font-bold font-mono">cm</button>
                </div>
            </div>

            <!-- Row 3: Colors, Line Widths & Canvas Styles -->
            <div class="flex items-center justify-between gap-3 flex-wrap pt-1.5 border-t border-slate-800/80 text-xs">
                <!-- Color Swatches -->
                <div class="flex items-center space-x-1.5">
                    <span class="text-[10px] uppercase font-bold text-slate-500 mr-1">Color:</span>
                    <button type="button" onclick="setDrawColor('#0f172a', this)" class="draw-color-swatch active w-5 h-5 rounded-full bg-slate-900 border-2 border-white shadow-sm" title="Black / Dark Slate"></button>
                    <button type="button" onclick="setDrawColor('#3730a3', this)" class="draw-color-swatch w-5 h-5 rounded-full bg-indigo-700 border border-slate-600 shadow-sm" title="Indigo"></button>
                    <button type="button" onclick="setDrawColor('#0284c7', this)" class="draw-color-swatch w-5 h-5 rounded-full bg-sky-600 border border-slate-600 shadow-sm" title="Cyan / Sky Blue"></button>
                    <button type="button" onclick="setDrawColor('#c026d3', this)" class="draw-color-swatch w-5 h-5 rounded-full bg-fuchsia-600 border border-slate-600 shadow-sm" title="Magenta / Purple"></button>
                    <button type="button" onclick="setDrawColor('#059669', this)" class="draw-color-swatch w-5 h-5 rounded-full bg-emerald-600 border border-slate-600 shadow-sm" title="Emerald Green"></button>
                    <button type="button" onclick="setDrawColor('#e11d48', this)" class="draw-color-swatch w-5 h-5 rounded-full bg-rose-600 border border-slate-600 shadow-sm" title="Rose Red"></button>
                    <button type="button" onclick="setDrawColor('#d97706', this)" class="draw-color-swatch w-5 h-5 rounded-full bg-amber-600 border border-slate-600 shadow-sm" title="Amber"></button>
                    <button type="button" onclick="setDrawColor('#7c3aed', this)" class="draw-color-swatch w-5 h-5 rounded-full bg-purple-600 border border-slate-600 shadow-sm" title="Purple"></button>
                    <label class="relative cursor-pointer ml-1 inline-flex items-center" title="Custom Color">
                        <input type="color" id="draw_custom_color" value="#0f172a" onchange="setDrawColor(this.value, null)" class="w-5 h-5 rounded cursor-pointer opacity-0 absolute">
                        <span class="w-5 h-5 rounded-full bg-gradient-to-tr from-pink-500 via-amber-400 to-indigo-500 border border-slate-600 flex items-center justify-center text-[10px]">🎨</span>
                    </label>
                </div>

                <!-- Stroke Width -->
                <div class="flex items-center space-x-1.5">
                    <span class="text-[10px] uppercase font-bold text-slate-500 mr-1">Thickness:</span>
                    <button type="button" onclick="setDrawWidth(1, this)" class="draw-width-btn px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono text-[11px]">1px</button>
                    <button type="button" onclick="setDrawWidth(2, this)" class="draw-width-btn active px-2 py-0.5 rounded bg-indigo-600 text-white font-mono text-[11px]">2px</button>
                    <button type="button" onclick="setDrawWidth(3, this)" class="draw-width-btn px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono text-[11px]">3px</button>
                    <button type="button" onclick="setDrawWidth(5, this)" class="draw-width-btn px-2 py-0.5 rounded bg-slate-800 hover:bg-slate-700 text-slate-300 font-mono text-[11px]">5px</button>
                </div>

                <!-- Dash & Fill Options -->
                <div class="flex items-center space-x-3">
                    <label class="inline-flex items-center space-x-1.5 cursor-pointer text-slate-300">
                        <input type="checkbox" id="draw_dashed_stroke" onchange="toggleDashedStroke(this.checked)" class="rounded bg-slate-900 border-slate-700 text-indigo-500 focus:ring-indigo-500">
                        <span class="text-[11px] font-medium">Dashed Line</span>
                    </label>

                    <label class="inline-flex items-center space-x-1.5 cursor-pointer text-slate-300">
                        <input type="checkbox" id="draw_fill_shape" onchange="toggleFillShape(this.checked)" class="rounded bg-slate-900 border-slate-700 text-indigo-500 focus:ring-indigo-500">
                        <span class="text-[11px] font-medium">Soft Fill</span>
                    </label>

                    <label class="inline-flex items-center space-x-1.5 cursor-pointer text-slate-300">
                        <input type="checkbox" id="draw_grid_toggle" checked onchange="toggleGridBackground(this.checked)" class="rounded bg-slate-900 border-slate-700 text-indigo-500 focus:ring-indigo-500">
                        <span class="text-[11px] font-medium">Grid Paper</span>
                    </label>
                </div>
            </div>
        </div>

        <!-- Canvas Drawing Surface -->
        <div class="p-3 sm:p-5 bg-slate-950 flex-1 flex flex-col items-center justify-center overflow-auto relative">
            <!-- Quick Type Length / Side Label Bar -->
            <div class="w-full max-w-[760px] mb-2 flex items-center justify-between gap-2 flex-wrap bg-slate-900/90 border border-slate-800 px-3 py-1.5 rounded-xl text-xs shadow-inner">
                <div class="flex items-center space-x-2 flex-wrap">
                    <span class="text-amber-400 font-bold flex items-center space-x-1">
                        <span>📏</span>
                        <span>Side Length / Label:</span>
                    </span>
                    <div class="flex items-center space-x-1">
                        <input type="text" id="quick_side_length_input" value="10 cms" placeholder="e.g. 10 cms, 5 cm"
                            class="w-24 px-2 py-0.5 rounded-lg bg-slate-950 border border-indigo-500/60 text-white font-mono text-xs focus:ring-1 focus:ring-indigo-400 focus:outline-none font-bold"
                            onkeydown="if(event.key==='Enter'){stampCustomLength(this.value);}">
                        <button type="button" onclick="stampCustomLength(document.getElementById('quick_side_length_input').value)"
                            class="px-2.5 py-0.5 rounded-lg bg-indigo-600 hover:bg-indigo-500 text-white font-bold text-xs shadow-md transition-all cursor-pointer">
                            Click to Place on Line
                        </button>
                    </div>
                </div>
                <!-- Quick Chip suggestions -->
                <div class="flex items-center space-x-1 overflow-x-auto scrollbar-thin">
                    <span class="text-[10px] text-slate-400">Presets:</span>
                    <button type="button" onclick="document.getElementById('quick_side_length_input').value='10 cms'; stampCustomLength('10 cms');" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-[11px] font-mono font-semibold cursor-pointer">10 cms</button>
                    <button type="button" onclick="document.getElementById('quick_side_length_input').value='10 cm'; stampCustomLength('10 cm');" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-[11px] font-mono font-semibold cursor-pointer">10 cm</button>
                    <button type="button" onclick="document.getElementById('quick_side_length_input').value='20 cm'; stampCustomLength('20 cm');" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-[11px] font-mono font-semibold cursor-pointer">20 cm</button>
                    <button type="button" onclick="document.getElementById('quick_side_length_input').value='5 cm'; stampCustomLength('5 cm');" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-[11px] font-mono font-semibold cursor-pointer">5 cm</button>
                    <button type="button" onclick="document.getElementById('quick_side_length_input').value='x cm'; stampCustomLength('x cm');" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-[11px] font-mono font-semibold cursor-pointer">x cm</button>
                    <button type="button" onclick="document.getElementById('quick_side_length_input').value='12 cm'; stampCustomLength('12 cm');" class="px-2 py-0.5 rounded bg-slate-800 hover:bg-indigo-600 text-slate-200 text-[11px] font-mono font-semibold cursor-pointer">12 cm</button>
                </div>
            </div>

            <div class="relative bg-white rounded-xl shadow-xl overflow-hidden border border-slate-300 max-w-full">
                <canvas id="geometryCanvas" width="760" height="460" class="block cursor-crosshair touch-none max-w-full"></canvas>

                <!-- Floating Inline Text Label Input -->
                <div id="draw_text_input_box" style="z-index: 100000;" class="hidden absolute p-2 rounded-xl bg-slate-900/95 border border-indigo-500 shadow-2xl backdrop-blur-sm space-y-1.5 w-60">
                    <div class="flex items-center justify-between text-[11px] text-slate-300">
                        <span class="font-bold">Add Label / Dimension:</span>
                        <button type="button" onclick="cancelTextPlacement()" class="text-slate-400 hover:text-white">✕</button>
                    </div>
                    <input type="text" id="draw_text_input_field" placeholder="e.g. A, 5 cm, 90°, x..." class="w-full px-2 py-1 rounded bg-slate-950 border border-slate-700 text-white text-xs focus:ring-1 focus:ring-indigo-500 focus:outline-none">
                    <div class="flex items-center justify-between pt-1">
                        <div class="flex items-center space-x-1">
                            <button type="button" onclick="appendInlineText('90°')" class="px-1.5 py-0.5 rounded bg-slate-800 text-[10px] text-slate-300 font-mono">90°</button>
                            <button type="button" onclick="appendInlineText('cm')" class="px-1.5 py-0.5 rounded bg-slate-800 text-[10px] text-slate-300 font-mono">cm</button>
                            <button type="button" onclick="appendInlineText('θ')" class="px-1.5 py-0.5 rounded bg-slate-800 text-[10px] text-slate-300 font-mono">θ</button>
                        </div>
                        <button type="button" onclick="confirmTextPlacement()" class="px-2.5 py-1 rounded bg-indigo-600 hover:bg-indigo-500 text-white text-[11px] font-bold shadow-md cursor-pointer">
                            Place Text
                        </button>
                    </div>
                </div>
            </div>

            <!-- Hint below canvas -->
            <div class="mt-2 flex items-center justify-between w-full max-w-[760px] text-[11px] text-slate-400 px-1">
                <span>Tip: Click &amp; drag on canvas to draw shapes, or click "⚡ Quick Presets" to place complete diagrams.</span>
                <span class="font-mono text-slate-500">760 × 460 px Canvas</span>
            </div>
        </div>

        <!-- Modal Footer -->
        <div class="px-4 sm:px-6 py-3 border-t border-slate-800 bg-slate-950 flex items-center justify-between gap-3 shrink-0">
            <div class="flex items-center space-x-3">
                <label class="inline-flex items-center space-x-1.5 cursor-pointer text-slate-300 text-xs">
                    <input type="checkbox" id="draw_auto_trim" checked class="rounded bg-slate-900 border-slate-700 text-emerald-500 focus:ring-emerald-500">
                    <span class="font-medium">Trim extra margin whitespace</span>
                </label>
                <button type="button" onclick="downloadDrawCanvas()" class="px-3 py-1.5 rounded-lg bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-medium border border-slate-700 transition-colors cursor-pointer hidden sm:inline-flex items-center space-x-1">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M4 16v1a3 3 0 003 3h10a3 3 0 003-3v-1m-4-4l-4 4m0 0l-4-4m4 4V4"/></svg>
                    <span>Download PNG</span>
                </button>
            </div>

            <div class="flex items-center space-x-2.5">
                <button type="button" onclick="closeDrawToolModal()" class="px-4 py-2 rounded-xl bg-slate-800 hover:bg-slate-700 text-slate-300 text-xs font-semibold border border-slate-700 transition-colors cursor-pointer">
                    Cancel
                </button>
                <button type="button" onclick="insertDrawingIntoQuestion()" class="px-5 py-2 rounded-xl bg-gradient-to-r from-emerald-600 to-teal-600 hover:from-emerald-500 hover:to-teal-500 text-white text-xs font-bold shadow-lg shadow-emerald-600/30 transition-all inline-flex items-center space-x-1.5 cursor-pointer active:scale-95">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                    <span>Insert into Question Prompt</span>
                </button>
            </div>
        </div>
    </div>
</div>

<script>
    (function() {
        let drawTargetPrefix = 'create';
        let currentDrawTool = 'right_triangle';
        let currentDrawColor = '#0f172a';
        let currentDrawWidth = 2;
        let isDashedStroke = false;
        let isFillShape = false;
        let isGridEnabled = true;

        let canvas = null;
        let ctx = null;
        let isDrawing = false;
        let startX = 0;
        let startY = 0;
        let lastX = 0;
        let lastY = 0;

        let canvasSnapshot = null;
        let undoStack = [];
        let redoStack = [];
        const MAX_STACK = 25;

        let pendingTextCoords = null;
        let activeStampText = null;
        let polylinePoints = [];
        let polylineBaseSnapshot = null;

        window.handleDrawImageUpload = function(input) {
            if (input && input.files && input.files[0]) {
                loadImageOntoCanvas(input.files[0]);
                input.value = '';
            }
        };

        function loadImageOntoCanvas(file) {
            if (!file || !file.type || !file.type.startsWith('image/')) return;
            const reader = new FileReader();
            reader.onload = function(e) {
                const img = new Image();
                img.onload = function() {
                    if (!ctx || !canvas) return;
                    clearCanvasInternal();
                    const maxW = canvas.width - 40;
                    const maxH = canvas.height - 40;
                    let scale = Math.min(maxW / img.width, maxH / img.height);
                    if (scale > 1) scale = 1;
                    const drawW = img.width * scale;
                    const drawH = img.height * scale;
                    const drawX = (canvas.width - drawW) / 2;
                    const drawY = (canvas.height - drawH) / 2;
                    ctx.drawImage(img, drawX, drawY, drawW, drawH);
                    pushUndoState();
                    showDrawToast('Image diagram loaded! You can annotate or insert it.');
                };
                img.src = e.target.result;
            };
            reader.readAsDataURL(file);
        }

        function getCanvasPoint(e) {
            if (!canvas) return { x: 0, y: 0 };
            const rect = canvas.getBoundingClientRect();
            const clientX = e.touches ? e.touches[0].clientX : e.clientX;
            const clientY = e.touches ? e.touches[0].clientY : e.clientY;
            const scaleX = canvas.width / rect.width;
            const scaleY = canvas.height / rect.height;
            return {
                x: (clientX - rect.left) * scaleX,
                y: (clientY - rect.top) * scaleY
            };
        }

        function initDrawCanvas() {
            canvas = document.getElementById('geometryCanvas');
            if (!canvas) return;
            ctx = canvas.getContext('2d', { willReadFrequently: true });

            // Setup events
            canvas.addEventListener('mousedown', onPointerDown);
            canvas.addEventListener('mousemove', onPointerMove);
            window.addEventListener('mouseup', onPointerUp);

            canvas.addEventListener('touchstart', onPointerDown, { passive: false });
            canvas.addEventListener('touchmove', onPointerMove, { passive: false });
            window.addEventListener('touchend', onPointerUp);

            // Double click to finish polyline
            canvas.addEventListener('dblclick', function(e) {
                if (currentDrawTool === 'polyline') {
                    finishPolyline();
                }
            });

            // Clipboard Paste listener (Ctrl+V)
            window.addEventListener('paste', function(e) {
                const modal = document.getElementById('drawToolModal');
                if (!modal || modal.classList.contains('hidden')) return;
                const clipboardData = e.clipboardData || window.clipboardData;
                if (!clipboardData) return;
                const items = clipboardData.items;
                if (!items) return;
                for (let i = 0; i < items.length; i++) {
                    if (items[i].type && items[i].type.indexOf('image') !== -1) {
                        const file = items[i].getAsFile();
                        loadImageOntoCanvas(file);
                        e.preventDefault();
                        break;
                    }
                }
            });

            // Handle keyboard shortcuts
            window.addEventListener('keydown', function(e) {
                const modal = document.getElementById('drawToolModal');
                if (!modal || modal.classList.contains('hidden')) return;

                if ((e.ctrlKey || e.metaKey) && e.key === 'z') {
                    e.preventDefault();
                    if (e.shiftKey) {
                        redoDraw();
                    } else {
                        undoDraw();
                    }
                } else if ((e.ctrlKey || e.metaKey) && e.key === 'y') {
                    e.preventDefault();
                    redoDraw();
                } else if (e.key === 'Escape') {
                    closeDrawToolModal();
                }
            });

            // Initial clear with white & grid
            clearCanvasInternal();
            pushUndoState();
        }

        function drawGridLines() {
            if (!isGridEnabled || !ctx || !canvas) return;
            ctx.save();
            ctx.strokeStyle = '#f1f5f9'; // Very light slate line
            ctx.lineWidth = 1;
            ctx.setLineDash([]);

            const step = 20;
            for (let x = 0; x <= canvas.width; x += step) {
                ctx.beginPath();
                ctx.moveTo(x, 0);
                ctx.lineTo(x, canvas.height);
                ctx.stroke();
            }
            for (let y = 0; y <= canvas.height; y += step) {
                ctx.beginPath();
                ctx.moveTo(0, y);
                ctx.lineTo(canvas.width, y);
                ctx.stroke();
            }
            ctx.restore();
        }

        function clearCanvasInternal() {
            if (!ctx || !canvas) return;
            ctx.save();
            ctx.fillStyle = '#ffffff';
            ctx.fillRect(0, 0, canvas.width, canvas.height);
            drawGridLines();
            ctx.restore();
        }

        function pushUndoState() {
            if (!ctx || !canvas) return;
            try {
                if (undoStack.length >= MAX_STACK) {
                    undoStack.shift();
                }
                undoStack.push(ctx.getImageData(0, 0, canvas.width, canvas.height));
                redoStack = []; // Clear redo on new action
            } catch (err) {
                console.warn('Canvas snapshot error:', err);
            }
        }

        window.undoDraw = function() {
            if (!ctx || !canvas || undoStack.length <= 1) return;
            const current = undoStack.pop();
            redoStack.push(current);
            const prev = undoStack[undoStack.length - 1];
            ctx.putImageData(prev, 0, 0);
        };

        window.redoDraw = function() {
            if (!ctx || !canvas || redoStack.length === 0) return;
            const next = redoStack.pop();
            undoStack.push(next);
            ctx.putImageData(next, 0, 0);
        };

        window.clearDrawCanvas = function() {
            if (!confirm('Are you sure you want to clear the drawing canvas?')) return;
            clearCanvasInternal();
            polylinePoints = [];
            polylineBaseSnapshot = null;
            document.getElementById('draw_finish_polyline_btn')?.classList.add('hidden');
            pushUndoState();
        };

        window.finishPolyline = function() {
            if (polylinePoints.length >= 2 && polylineBaseSnapshot) {
                ctx.putImageData(polylineBaseSnapshot, 0, 0);
                ctx.save();
                applyDrawStyles(true);
                ctx.beginPath();
                ctx.moveTo(polylinePoints[0].x, polylinePoints[0].y);
                for (let i = 1; i < polylinePoints.length; i++) {
                    ctx.lineTo(polylinePoints[i].x, polylinePoints[i].y);
                }
                if (isFillShape) ctx.fill();
                ctx.stroke();
                ctx.restore();
                pushUndoState();
            }
            polylinePoints = [];
            polylineBaseSnapshot = null;
            document.getElementById('draw_finish_polyline_btn')?.classList.add('hidden');
        };

        function onPointerDown(e) {
            const modal = document.getElementById('drawToolModal');
            if (!modal || modal.classList.contains('hidden')) return;

            const pt = getCanvasPoint(e);
            startX = pt.x;
            startY = pt.y;
            lastX = pt.x;
            lastY = pt.y;

            if (currentDrawTool === 'text') {
                openInlineTextInput(pt.x, pt.y);
                return;
            }

            if (currentDrawTool === 'stamp' && activeStampText) {
                ctx.save();
                ctx.font = 'bold 16px "Instrument Sans", sans-serif';
                // Crisp white halo so text placed directly on lines or triangle edges does not get obscured
                ctx.strokeStyle = '#ffffff';
                ctx.lineWidth = 6;
                ctx.lineJoin = 'round';
                ctx.strokeText(activeStampText, pt.x, pt.y);
                ctx.fillStyle = currentDrawColor;
                ctx.fillText(activeStampText, pt.x, pt.y);
                ctx.restore();
                pushUndoState();
                return;
            }

            if (currentDrawTool === 'polyline') {
                if (polylinePoints.length === 0) {
                    polylineBaseSnapshot = ctx.getImageData(0, 0, canvas.width, canvas.height);
                    document.getElementById('draw_finish_polyline_btn')?.classList.remove('hidden');
                    polylinePoints.push({ x: pt.x, y: pt.y });
                } else {
                    const distToFirst = Math.hypot(pt.x - polylinePoints[0].x, pt.y - polylinePoints[0].y);
                    if (polylinePoints.length >= 3 && distToFirst < 18) {
                        // Close loop as closed polygon (e.g. custom triangle)
                        ctx.putImageData(polylineBaseSnapshot, 0, 0);
                        ctx.save();
                        applyDrawStyles(true);
                        ctx.beginPath();
                        ctx.moveTo(polylinePoints[0].x, polylinePoints[0].y);
                        for (let i = 1; i < polylinePoints.length; i++) {
                            ctx.lineTo(polylinePoints[i].x, polylinePoints[i].y);
                        }
                        ctx.closePath();
                        if (isFillShape) ctx.fill();
                        ctx.stroke();
                        ctx.restore();
                        pushUndoState();
                        polylinePoints = [];
                        polylineBaseSnapshot = null;
                        document.getElementById('draw_finish_polyline_btn')?.classList.add('hidden');
                        return;
                    }
                    polylinePoints.push({ x: pt.x, y: pt.y });
                }

                // Render current polyline state
                ctx.putImageData(polylineBaseSnapshot, 0, 0);
                ctx.save();
                applyDrawStyles(false);
                ctx.beginPath();
                ctx.moveTo(polylinePoints[0].x, polylinePoints[0].y);
                for (let i = 1; i < polylinePoints.length; i++) {
                    ctx.lineTo(polylinePoints[i].x, polylinePoints[i].y);
                }
                ctx.stroke();
                // Draw vertex dots
                ctx.fillStyle = currentDrawColor;
                for (let p of polylinePoints) {
                    ctx.beginPath();
                    ctx.arc(p.x, p.y, 3.5, 0, Math.PI * 2);
                    ctx.fill();
                }
                ctx.restore();
                return;
            }

            isDrawing = true;
            canvasSnapshot = ctx.getImageData(0, 0, canvas.width, canvas.height);

            if (currentDrawTool === 'pen' || currentDrawTool === 'eraser') {
                ctx.save();
                ctx.beginPath();
                ctx.moveTo(pt.x, pt.y);
                ctx.strokeStyle = currentDrawTool === 'eraser' ? '#ffffff' : currentDrawColor;
                ctx.lineWidth = currentDrawTool === 'eraser' ? (currentDrawWidth * 6) : currentDrawWidth;
                ctx.lineCap = 'round';
                ctx.lineJoin = 'round';
                if (isDashedStroke && currentDrawTool !== 'eraser') {
                    ctx.setLineDash([6, 4]);
                } else {
                    ctx.setLineDash([]);
                }
            }

            if (e.cancelable) e.preventDefault();
        }

        function onPointerMove(e) {
            const pt = getCanvasPoint(e);

            if (currentDrawTool === 'polyline' && polylinePoints.length > 0 && polylineBaseSnapshot) {
                ctx.putImageData(polylineBaseSnapshot, 0, 0);
                ctx.save();
                applyDrawStyles(false);
                ctx.beginPath();
                ctx.moveTo(polylinePoints[0].x, polylinePoints[0].y);
                for (let i = 1; i < polylinePoints.length; i++) {
                    ctx.lineTo(polylinePoints[i].x, polylinePoints[i].y);
                }
                ctx.lineTo(pt.x, pt.y);
                ctx.stroke();

                // Highlight first point if hovering near it to close
                if (polylinePoints.length >= 2) {
                    const dist = Math.hypot(pt.x - polylinePoints[0].x, pt.y - polylinePoints[0].y);
                    ctx.beginPath();
                    ctx.arc(polylinePoints[0].x, polylinePoints[0].y, dist < 18 ? 7 : 3.5, 0, Math.PI * 2);
                    ctx.fillStyle = dist < 18 ? '#10b981' : currentDrawColor;
                    ctx.fill();
                }
                ctx.restore();
                return;
            }

            if (!isDrawing) return;

            if (currentDrawTool === 'pen' || currentDrawTool === 'eraser') {
                ctx.lineTo(pt.x, pt.y);
                ctx.stroke();
                lastX = pt.x;
                lastY = pt.y;
            } else {
                // Restore snapshot then preview shape
                ctx.putImageData(canvasSnapshot, 0, 0);
                drawShape(currentDrawTool, startX, startY, pt.x, pt.y, false);
            }

            if (e.cancelable) e.preventDefault();
        }

        function onPointerUp(e) {
            if (currentDrawTool === 'polyline') return;
            if (!isDrawing) return;
            isDrawing = false;

            if (currentDrawTool === 'pen' || currentDrawTool === 'eraser') {
                ctx.restore();
            } else {
                // Finalize shape
                const pt = (e && e.clientX !== undefined) ? getCanvasPoint(e) : { x: lastX, y: lastY };
                ctx.putImageData(canvasSnapshot, 0, 0);
                drawShape(currentDrawTool, startX, startY, pt.x, pt.y, true);
            }

            pushUndoState();
        }

        function applyDrawStyles(isFinal) {
            ctx.strokeStyle = currentDrawColor;
            ctx.lineWidth = currentDrawWidth;
            ctx.lineCap = 'round';
            ctx.lineJoin = 'round';

            if (isDashedStroke) {
                ctx.setLineDash([7, 5]);
            } else {
                ctx.setLineDash([]);
            }

            if (isFillShape) {
                // 15% opacity pastel tint of stroke color
                ctx.fillStyle = hexToRgba(currentDrawColor, 0.15);
            } else {
                ctx.fillStyle = 'transparent';
            }
        }

        function hexToRgba(hex, alpha) {
            let c;
            if (/^#([A-Fa-f0-9]{3}){1,2}$/.test(hex)) {
                c = hex.substring(1).split('');
                if (c.length === 3) {
                    c = [c[0], c[0], c[1], c[1], c[2], c[2]];
                }
                c = '0x' + c.join('');
                return `rgba(${[(c >> 16) & 255, (c >> 8) & 255, c & 255].join(',')},${alpha})`;
            }
            return `rgba(79, 70, 229, ${alpha})`;
        }

        function drawShape(tool, x1, y1, x2, y2, isFinal) {
            ctx.save();
            applyDrawStyles(isFinal);

            const dx = x2 - x1;
            const dy = y2 - y1;
            const w = Math.abs(dx);
            const h = Math.abs(dy);
            const minX = Math.min(x1, x2);
            const minY = Math.min(y1, y2);
            const maxX = Math.max(x1, x2);
            const maxY = Math.max(y1, y2);

            switch (tool) {
                case 'right_triangle': {
                    // Triangle vertices: (x1, y2) [Right angle], (x2, y2), (x1, y1)
                    ctx.beginPath();
                    ctx.moveTo(x1, y1);
                    ctx.lineTo(x1, y2);
                    ctx.lineTo(x2, y2);
                    ctx.closePath();
                    if (isFillShape) ctx.fill();
                    ctx.stroke();

                    // Right angle marker
                    const boxSize = Math.min(18, Math.min(w, h) * 0.25);
                    if (boxSize > 4) {
                        const signX = dx >= 0 ? 1 : -1;
                        const signY = dy >= 0 ? -1 : 1;
                        ctx.beginPath();
                        ctx.moveTo(x1, y2 + signY * boxSize);
                        ctx.lineTo(x1 + signX * boxSize, y2 + signY * boxSize);
                        ctx.lineTo(x1 + signX * boxSize, y2);
                        ctx.setLineDash([]);
                        ctx.stroke();
                    }
                    break;
                }

                case 'triangle': {
                    // Apex at top center
                    const apexX = x1 + dx / 2;
                    const apexY = y1;
                    ctx.beginPath();
                    ctx.moveTo(apexX, apexY);
                    ctx.lineTo(x1, y2);
                    ctx.lineTo(x2, y2);
                    ctx.closePath();
                    if (isFillShape) ctx.fill();
                    ctx.stroke();
                    break;
                }

                case 'isosceles': {
                    // Triangle with dashed altitude
                    const apexX = x1 + dx / 2;
                    const apexY = y1;
                    const midBaseX = apexX;
                    const midBaseY = y2;

                    ctx.beginPath();
                    ctx.moveTo(apexX, apexY);
                    ctx.lineTo(x1, y2);
                    ctx.lineTo(x2, y2);
                    ctx.closePath();
                    if (isFillShape) ctx.fill();
                    ctx.stroke();

                    // Altitude line
                    ctx.beginPath();
                    ctx.setLineDash([5, 4]);
                    ctx.moveTo(apexX, apexY);
                    ctx.lineTo(midBaseX, midBaseY);
                    ctx.stroke();

                    // Altitude right angle mark
                    const altBox = Math.min(12, h * 0.15);
                    if (altBox > 3) {
                        ctx.setLineDash([]);
                        ctx.strokeRect(midBaseX, midBaseY - altBox, altBox, altBox);
                    }
                    break;
                }

                case 'square': {
                    const side = Math.min(w, h);
                    const signX = dx >= 0 ? 1 : -1;
                    const signY = dy >= 0 ? 1 : -1;
                    const sqX = signX >= 0 ? x1 : x1 - side;
                    const sqY = signY >= 0 ? y1 : y1 - side;

                    ctx.beginPath();
                    ctx.rect(sqX, sqY, side, side);
                    if (isFillShape) ctx.fill();
                    ctx.stroke();
                    break;
                }

                case 'rectangle': {
                    ctx.beginPath();
                    ctx.rect(minX, minY, w, h);
                    if (isFillShape) ctx.fill();
                    ctx.stroke();
                    break;
                }

                case 'parallelogram': {
                    const skew = w * 0.25;
                    ctx.beginPath();
                    ctx.moveTo(minX + skew, minY);
                    ctx.lineTo(maxX, minY);
                    ctx.lineTo(maxX - skew, maxY);
                    ctx.lineTo(minX, maxY);
                    ctx.closePath();
                    if (isFillShape) ctx.fill();
                    ctx.stroke();
                    break;
                }

                case 'trapezoid': {
                    const inset = w * 0.2;
                    ctx.beginPath();
                    ctx.moveTo(minX + inset, minY);
                    ctx.lineTo(maxX - inset, minY);
                    ctx.lineTo(maxX, maxY);
                    ctx.lineTo(minX, maxY);
                    ctx.closePath();
                    if (isFillShape) ctx.fill();
                    ctx.stroke();
                    break;
                }

                case 'rhombus': {
                    const midX = minX + w / 2;
                    const midY = minY + h / 2;
                    ctx.beginPath();
                    ctx.moveTo(midX, minY);
                    ctx.lineTo(maxX, midY);
                    ctx.lineTo(midX, maxY);
                    ctx.lineTo(minX, midY);
                    ctx.closePath();
                    if (isFillShape) ctx.fill();
                    ctx.stroke();
                    break;
                }

                case 'circle': {
                    const radius = Math.hypot(dx, dy);
                    ctx.beginPath();
                    ctx.arc(x1, y1, radius, 0, Math.PI * 2);
                    if (isFillShape) ctx.fill();
                    ctx.stroke();
                    break;
                }

                case 'circle_radius': {
                    const radius = Math.hypot(dx, dy);
                    ctx.beginPath();
                    ctx.arc(x1, y1, radius, 0, Math.PI * 2);
                    if (isFillShape) ctx.fill();
                    ctx.stroke();

                    // Center dot
                    ctx.fillStyle = currentDrawColor;
                    ctx.beginPath();
                    ctx.arc(x1, y1, 3.5, 0, Math.PI * 2);
                    ctx.fill();

                    // Radius line
                    ctx.beginPath();
                    ctx.setLineDash([4, 3]);
                    ctx.moveTo(x1, y1);
                    ctx.lineTo(x2, y2);
                    ctx.stroke();

                    // Label 'r' and 'O'
                    if (isFinal && radius > 15) {
                        ctx.setLineDash([]);
                        ctx.font = 'bold 14px sans-serif';
                        ctx.fillStyle = currentDrawColor;
                        ctx.fillText('O', x1 - 14, y1 - 6);
                        const midX = (x1 + x2) / 2;
                        const midY = (y1 + y2) / 2;
                        ctx.fillText('r', midX + 6, midY - 6);
                    }
                    break;
                }

                case 'cylinder': {
                    const rx = w / 2;
                    const ry = Math.min(24, Math.max(8, h * 0.18));
                    const cx = minX + rx;
                    const topY = minY + ry;
                    const botY = maxY - ry;

                    // Top ellipse (complete)
                    ctx.beginPath();
                    ctx.ellipse(cx, topY, rx, ry, 0, 0, Math.PI * 2);
                    if (isFillShape) ctx.fill();
                    ctx.stroke();

                    // Vertical sides
                    ctx.beginPath();
                    ctx.moveTo(minX, topY);
                    ctx.lineTo(minX, botY);
                    ctx.moveTo(maxX, topY);
                    ctx.lineTo(maxX, botY);
                    ctx.stroke();

                    // Bottom ellipse front half (solid)
                    ctx.beginPath();
                    ctx.ellipse(cx, botY, rx, ry, 0, 0, Math.PI);
                    ctx.stroke();

                    // Bottom ellipse back half (dashed)
                    ctx.beginPath();
                    ctx.setLineDash([5, 4]);
                    ctx.ellipse(cx, botY, rx, ry, 0, Math.PI, Math.PI * 2);
                    ctx.stroke();
                    break;
                }

                case 'cone': {
                    const rx = w / 2;
                    const ry = Math.min(24, Math.max(8, h * 0.18));
                    const cx = minX + rx;
                    const apexY = minY;
                    const botY = maxY - ry;

                    // Slant sides
                    ctx.beginPath();
                    ctx.moveTo(cx, apexY);
                    ctx.lineTo(minX, botY);
                    ctx.moveTo(cx, apexY);
                    ctx.lineTo(maxX, botY);
                    ctx.stroke();

                    // Bottom ellipse front half (solid)
                    ctx.beginPath();
                    ctx.ellipse(cx, botY, rx, ry, 0, 0, Math.PI);
                    ctx.stroke();

                    // Bottom ellipse back half (dashed)
                    ctx.beginPath();
                    ctx.setLineDash([5, 4]);
                    ctx.ellipse(cx, botY, rx, ry, 0, Math.PI, Math.PI * 2);
                    ctx.stroke();

                    // Height dashed line
                    ctx.beginPath();
                    ctx.setLineDash([4, 4]);
                    ctx.moveTo(cx, apexY);
                    ctx.lineTo(cx, botY);
                    ctx.stroke();
                    break;
                }

                case 'cube': {
                    const cubeSide = Math.min(w, h) * 0.75;
                    const offset = cubeSide * 0.35;

                    const fx1 = minX;
                    const fy1 = minY + offset;
                    const fx2 = fx1 + cubeSide;
                    const fy2 = fy1 + cubeSide;

                    const bx1 = fx1 + offset;
                    const by1 = minY;
                    const bx2 = bx1 + cubeSide;
                    const by2 = by1 + cubeSide;

                    // Front face
                    ctx.beginPath();
                    ctx.rect(fx1, fy1, cubeSide, cubeSide);
                    ctx.stroke();

                    // Back face visible edges
                    ctx.beginPath();
                    ctx.moveTo(bx1, by1);
                    ctx.lineTo(bx2, by1);
                    ctx.lineTo(bx2, by2);
                    ctx.stroke();

                    // Connecting top and right edges
                    ctx.beginPath();
                    ctx.moveTo(fx1, fy1);
                    ctx.lineTo(bx1, by1);
                    ctx.moveTo(fx2, fy1);
                    ctx.lineTo(bx2, by1);
                    ctx.moveTo(fx2, fy2);
                    ctx.lineTo(bx2, by2);
                    ctx.stroke();

                    // Hidden dashed edges
                    ctx.beginPath();
                    ctx.setLineDash([5, 4]);
                    ctx.moveTo(fx1, fy2);
                    ctx.lineTo(bx1, by2);
                    ctx.lineTo(bx1, by1);
                    ctx.moveTo(bx1, by2);
                    ctx.lineTo(bx2, by2);
                    ctx.stroke();
                    break;
                }

                case 'line': {
                    ctx.beginPath();
                    ctx.moveTo(x1, y1);
                    ctx.lineTo(x2, y2);
                    ctx.stroke();
                    break;
                }

                case 'arrow': {
                    ctx.beginPath();
                    ctx.moveTo(x1, y1);
                    ctx.lineTo(x2, y2);
                    ctx.stroke();
                    drawArrowHead(x1, y1, x2, y2);
                    break;
                }

                case 'double_arrow': {
                    ctx.beginPath();
                    ctx.moveTo(x1, y1);
                    ctx.lineTo(x2, y2);
                    ctx.stroke();
                    drawArrowHead(x2, y2, x1, y1);
                    drawArrowHead(x1, y1, x2, y2);
                    break;
                }

                case 'axes': {
                    const midX = minX + w / 2;
                    const midY = minY + h / 2;

                    // X-axis
                    ctx.beginPath();
                    ctx.moveTo(minX, midY);
                    ctx.lineTo(maxX, midY);
                    ctx.stroke();
                    drawArrowHead(maxX - 10, midY, maxX, midY);
                    drawArrowHead(minX + 10, midY, minX, midY);

                    // Y-axis
                    ctx.beginPath();
                    ctx.moveTo(midX, maxY);
                    ctx.lineTo(midX, minY);
                    ctx.stroke();
                    drawArrowHead(midX, minY + 10, midX, minY);
                    drawArrowHead(midX, maxY - 10, midX, maxY);

                    // Origin and labels
                    if (isFinal) {
                        ctx.font = 'bold 13px sans-serif';
                        ctx.fillStyle = currentDrawColor;
                        ctx.fillText('X', maxX - 14, midY - 8);
                        ctx.fillText("X'", minX + 4, midY - 8);
                        ctx.fillText('Y', midX + 8, minY + 16);
                        ctx.fillText("Y'", midX + 8, maxY - 6);
                        ctx.fillText('O', midX - 14, midY + 16);
                    }
                    break;
                }
            }

            ctx.restore();
        }

        function drawArrowHead(fromX, fromY, toX, toY) {
            const headLen = 12;
            const angle = Math.atan2(toY - fromY, toX - fromX);
            ctx.save();
            ctx.fillStyle = currentDrawColor;
            ctx.strokeStyle = currentDrawColor;
            ctx.setLineDash([]);
            ctx.beginPath();
            ctx.moveTo(toX, toY);
            ctx.lineTo(toX - headLen * Math.cos(angle - Math.PI / 6), toY - headLen * Math.sin(angle - Math.PI / 6));
            ctx.lineTo(toX - headLen * Math.cos(angle + Math.PI / 6), toY - headLen * Math.sin(angle + Math.PI / 6));
            ctx.closePath();
            ctx.fill();
            ctx.stroke();
            ctx.restore();
        }

        // Inline Text Input Placement
        function openInlineTextInput(canvasX, canvasY) {
            pendingTextCoords = { x: canvasX, y: canvasY };
            const box = document.getElementById('draw_text_input_box');
            const input = document.getElementById('draw_text_input_field');
            if (!box || !canvas) return;

            const rect = canvas.getBoundingClientRect();
            const scaleX = rect.width / canvas.width;
            const scaleY = rect.height / canvas.height;

            const displayX = canvasX * scaleX;
            const displayY = canvasY * scaleY;

            box.style.left = Math.min(rect.width - 250, Math.max(10, displayX - 20)) + 'px';
            box.style.top = Math.min(rect.height - 90, Math.max(10, displayY - 10)) + 'px';
            box.classList.remove('hidden');

            if (input) {
                input.value = '';
                setTimeout(() => input.focus(), 60);
                input.onkeydown = function(e) {
                    if (e.key === 'Enter') {
                        confirmTextPlacement();
                    } else if (e.key === 'Escape') {
                        cancelTextPlacement();
                    }
                };
            }
        }

        window.cancelTextPlacement = function() {
            const box = document.getElementById('draw_text_input_box');
            if (box) box.classList.add('hidden');
            pendingTextCoords = null;
        };

        window.confirmTextPlacement = function() {
            const input = document.getElementById('draw_text_input_field');
            if (!input || !pendingTextCoords || !ctx) {
                cancelTextPlacement();
                return;
            }

            const text = input.value.trim();
            if (text.length > 0) {
                ctx.save();
                ctx.font = 'bold 16px "Instrument Sans", sans-serif';
                // Crisp white halo so text placed over lines/edges stays completely readable
                ctx.strokeStyle = '#ffffff';
                ctx.lineWidth = 6;
                ctx.lineJoin = 'round';
                ctx.strokeText(text, pendingTextCoords.x, pendingTextCoords.y);
                ctx.fillStyle = currentDrawColor;
                ctx.fillText(text, pendingTextCoords.x, pendingTextCoords.y);
                ctx.restore();
                pushUndoState();
            }

            cancelTextPlacement();
        };

        window.stampCustomLength = function(val) {
            const text = (val || '').trim();
            if (!text) return;
            currentDrawTool = 'stamp';
            activeStampText = text;
            document.querySelectorAll('.shape-tool-btn').forEach(b => {
                b.classList.remove('active', 'bg-indigo-600', 'text-white');
                b.classList.add('bg-slate-800', 'text-slate-200');
            });
            if (canvas) {
                canvas.className = 'block cursor-crosshair touch-none max-w-full';
            }
            showDrawToast('Click on any line or triangle side to place "' + text + '"');
        };

        window.appendInlineText = function(val) {
            const input = document.getElementById('draw_text_input_field');
            if (input) {
                input.value += val;
                input.focus();
            }
        };

        window.quickSelectLabel = function(label) {
            currentDrawTool = 'stamp';
            activeStampText = label;
            document.querySelectorAll('.shape-tool-btn').forEach(b => {
                b.classList.remove('active', 'bg-indigo-600', 'text-white');
                b.classList.add('bg-slate-800', 'text-slate-200');
            });
            if (canvas) {
                canvas.className = 'block cursor-crosshair touch-none max-w-full';
            }
            showDrawToast('Click anywhere on canvas to stamp "' + label + '"');
        };

        // UI Selectors
        window.selectDrawCategory = function(cat, btn) {
            document.querySelectorAll('.draw-cat-btn').forEach(b => {
                b.classList.remove('active', 'bg-indigo-600', 'text-white');
                b.classList.add('text-slate-300');
            });
            if (btn) {
                btn.classList.add('active', 'bg-indigo-600', 'text-white');
                btn.classList.remove('text-slate-300');
            }

            document.getElementById('draw_tools_shapes').classList.add('hidden');
            document.getElementById('draw_tools_presets').classList.add('hidden');
            document.getElementById('draw_tools_freehand').classList.add('hidden');

            if (cat === 'shapes') {
                document.getElementById('draw_tools_shapes').classList.remove('hidden');
            } else if (cat === 'presets') {
                document.getElementById('draw_tools_presets').classList.remove('hidden');
            } else if (cat === 'freehand') {
                document.getElementById('draw_tools_freehand').classList.remove('hidden');
            }
        };

        window.setDrawTool = function(tool, btn) {
            if (currentDrawTool === 'polyline' && tool !== 'polyline') {
                finishPolyline();
            }
            currentDrawTool = tool;
            activeStampText = null;
            document.querySelectorAll('.shape-tool-btn').forEach(b => {
                b.classList.remove('active', 'bg-indigo-600', 'text-white');
                b.classList.add('bg-slate-800', 'text-slate-200');
            });
            if (btn) {
                btn.classList.add('active', 'bg-indigo-600', 'text-white');
                btn.classList.remove('bg-slate-800', 'text-slate-200');
            }

            if (canvas) {
                if (tool === 'pen') {
                    canvas.className = 'block cursor-crosshair touch-none max-w-full';
                } else if (tool === 'text') {
                    canvas.className = 'block cursor-text touch-none max-w-full';
                } else if (tool === 'eraser') {
                    canvas.className = 'block cursor-cell touch-none max-w-full';
                } else {
                    canvas.className = 'block cursor-crosshair touch-none max-w-full';
                }
            }
        };

        window.setDrawColor = function(color, btn) {
            currentDrawColor = color;
            document.querySelectorAll('.draw-color-swatch').forEach(s => s.classList.remove('border-2', 'border-white', 'ring-2', 'ring-indigo-400'));
            if (btn) {
                btn.classList.add('border-2', 'border-white', 'ring-2', 'ring-indigo-400');
            }
        };

        window.setDrawWidth = function(width, btn) {
            currentDrawWidth = parseInt(width);
            document.querySelectorAll('.draw-width-btn').forEach(b => {
                b.classList.remove('active', 'bg-indigo-600', 'text-white');
                b.classList.add('bg-slate-800', 'text-slate-300');
            });
            if (btn) {
                btn.classList.add('active', 'bg-indigo-600', 'text-white');
                btn.classList.remove('bg-slate-800', 'text-slate-300');
            }
        };

        window.toggleDashedStroke = function(val) {
            isDashedStroke = Boolean(val);
        };

        window.toggleFillShape = function(val) {
            isFillShape = Boolean(val);
        };

        window.toggleGridBackground = function(val) {
            isGridEnabled = Boolean(val);
            // Redraw background & contents
            if (undoStack.length > 0) {
                const currentImg = undoStack[undoStack.length - 1];
                clearCanvasInternal();
                ctx.putImageData(currentImg, 0, 0);
            }
        };

        // Presets Library
        window.stampPreset = function(presetKey) {
            if (!ctx || !canvas) return;

            clearCanvasInternal();
            polylinePoints = [];
            polylineBaseSnapshot = null;
            document.getElementById('draw_finish_polyline_btn')?.classList.add('hidden');

            ctx.save();
            ctx.strokeStyle = '#0f172a';
            ctx.fillStyle = '#0f172a';
            ctx.lineWidth = 2.5;
            ctx.setLineDash([]);
            ctx.font = 'bold 16px sans-serif';

            switch (presetKey) {
                case 'triangle_pqr_st': {
                    // Coordinates for textbook diagram: Triangle PQR with transversal ST
                    const px = 120, py = 390;  // Vertex P (bottom-left)
                    const qx = 530, qy = 390;  // Vertex Q (bottom-right)
                    const rx = 640, ry = 80;   // Vertex R (top-right)

                    const sx = 330, sy = 390;  // S on PQ
                    const tx = 590, ty = 220;  // T on QR

                    // 1. Triangle PQR in Sky Blue
                    ctx.strokeStyle = '#0284c7';
                    ctx.lineWidth = 2.8;
                    ctx.lineJoin = 'round';
                    ctx.beginPath();
                    ctx.moveTo(px, py);
                    ctx.lineTo(qx, qy);
                    ctx.lineTo(rx, ry);
                    ctx.closePath();
                    ctx.stroke();

                    // 2. Transversal ST in Magenta
                    ctx.strokeStyle = '#c026d3';
                    ctx.lineWidth = 2.8;
                    ctx.beginPath();
                    ctx.moveTo(sx, sy);
                    ctx.lineTo(tx, ty);
                    ctx.stroke();

                    // 3. Vertex indicator dots
                    const pts = [
                        { x: px, y: py, color: '#0284c7' },
                        { x: qx, y: qy, color: '#0284c7' },
                        { x: rx, y: ry, color: '#0284c7' },
                        { x: sx, y: sy, color: '#c026d3' },
                        { x: tx, y: ty, color: '#c026d3' }
                    ];
                    for (const p of pts) {
                        ctx.fillStyle = p.color;
                        ctx.beginPath();
                        ctx.arc(p.x, p.y, 4, 0, Math.PI * 2);
                        ctx.fill();
                    }

                    // 4. Vertex Labels P, Q, R, S, T
                    ctx.fillStyle = '#0f172a';
                    ctx.font = 'bold 20px "Instrument Sans", sans-serif';
                    ctx.fillText('P', px - 28, py + 8);
                    ctx.fillText('Q', qx + 12, qy + 14);
                    ctx.fillText('R', rx + 10, ry + 4);
                    ctx.fillText('S', sx - 8, sy + 26);
                    ctx.fillText('T', tx + 14, ty + 6);

                    // 5. Dimension "20 cm" alongside side PR
                    ctx.font = 'bold 18px "Instrument Sans", sans-serif';
                    ctx.fillStyle = '#0f172a';
                    ctx.fillText('20 cm', 290, 220);
                    break;
                }

                case 'right_triangle_abc': {
                    const ax = 200, ay = 90;
                    const bx = 200, by = 360;
                    const cx = 560, cy = 360;

                    // Triangle
                    ctx.beginPath();
                    ctx.moveTo(ax, ay);
                    ctx.lineTo(bx, by);
                    ctx.lineTo(cx, cy);
                    ctx.closePath();
                    ctx.stroke();

                    // Right angle mark at B
                    ctx.strokeRect(bx, by - 24, 24, 24);

                    // Vertex Labels
                    ctx.fillText('A', ax - 24, ay + 6);
                    ctx.fillText('B', bx - 24, by + 16);
                    ctx.fillText('C', cx + 12, by + 16);

                    // Side Labels
                    ctx.font = 'italic bold 15px sans-serif';
                    ctx.fillText('height (h)', ax - 85, (ay + by) / 2);
                    ctx.fillText('base (b)', (bx + cx) / 2 - 25, by + 28);
                    ctx.fillText('hypotenuse (c)', (ax + cx) / 2 + 15, (ay + cy) / 2 - 15);
                    break;
                }

                case 'equilateral_triangle': {
                    const ax = 380, ay = 80;
                    const bx = 180, by = 370;
                    const cx = 580, cy = 370;
                    const mx = 380, my = 370;

                    // Triangle
                    ctx.beginPath();
                    ctx.moveTo(ax, ay);
                    ctx.lineTo(bx, by);
                    ctx.lineTo(cx, cy);
                    ctx.closePath();
                    ctx.stroke();

                    // Dashed altitude
                    ctx.beginPath();
                    ctx.setLineDash([6, 4]);
                    ctx.moveTo(ax, ay);
                    ctx.lineTo(mx, my);
                    ctx.stroke();
                    ctx.setLineDash([]);
                    ctx.strokeRect(mx, my - 16, 16, 16);

                    // Labels
                    ctx.fillText('A', ax - 6, ay - 14);
                    ctx.fillText('B', bx - 22, by + 16);
                    ctx.fillText('C', cx + 12, by + 16);
                    ctx.fillText('D', mx - 6, my + 24);
                    ctx.fillText('h', mx + 10, (ay + my) / 2);
                    ctx.fillText('a', (ax + bx) / 2 - 25, (ay + by) / 2);
                    ctx.fillText('a', (ax + cx) / 2 + 15, (ay + cy) / 2);
                    ctx.fillText('a', (bx + cx) / 2 - 4, by + 26);
                    break;
                }

                case 'square_abcd': {
                    const x = 240, y = 110, s = 260;

                    ctx.strokeRect(x, y, s, s);

                    // 4 Right angle marks
                    const m = 18;
                    ctx.strokeRect(x, y, m, m);
                    ctx.strokeRect(x + s - m, y, m, m);
                    ctx.strokeRect(x + s - m, y + s - m, m, m);
                    ctx.strokeRect(x, y + s - m, m, m);

                    // Labels
                    ctx.fillText('A', x - 20, y + 4);
                    ctx.fillText('B', x + s + 10, y + 4);
                    ctx.fillText('C', x + s + 10, y + s + 16);
                    ctx.fillText('D', x - 20, y + s + 16);

                    ctx.font = 'italic bold 15px sans-serif';
                    ctx.fillText('side (s)', x + s / 2 - 25, y - 12);
                    ctx.fillText('side (s)', x + s + 18, y + s / 2);
                    break;
                }

                case 'rectangle_abcd': {
                    const x = 180, y = 130, w = 380, h = 210;

                    ctx.strokeRect(x, y, w, h);

                    const m = 16;
                    ctx.strokeRect(x, y, m, m);
                    ctx.strokeRect(x + w - m, y, m, m);
                    ctx.strokeRect(x + w - m, y + h - m, m, m);
                    ctx.strokeRect(x, y + h - m, m, m);

                    ctx.fillText('A', x - 20, y + 4);
                    ctx.fillText('B', x + w + 10, y + 4);
                    ctx.fillText('C', x + w + 10, y + h + 16);
                    ctx.fillText('D', x - 20, y + h + 16);

                    ctx.font = 'italic bold 15px sans-serif';
                    ctx.fillText('Length (l)', x + w / 2 - 35, y - 12);
                    ctx.fillText('Width (w)', x + w + 16, y + h / 2);
                    break;
                }

                case 'circle_radius_r': {
                    const cx = 380, cy = 230, r = 140;

                    ctx.beginPath();
                    ctx.arc(cx, cy, r, 0, Math.PI * 2);
                    ctx.stroke();

                    // Center dot
                    ctx.beginPath();
                    ctx.arc(cx, cy, 4, 0, Math.PI * 2);
                    ctx.fill();

                    // Radius line to edge
                    const angle = -Math.PI / 6;
                    const px = cx + r * Math.cos(angle);
                    const py = cy + r * Math.sin(angle);

                    ctx.beginPath();
                    ctx.setLineDash([5, 4]);
                    ctx.moveTo(cx, cy);
                    ctx.lineTo(px, py);
                    ctx.stroke();
                    ctx.setLineDash([]);

                    ctx.fillText('O', cx - 18, cy + 18);
                    ctx.fillText('P', px + 10, py + 4);
                    ctx.fillText('r', (cx + px) / 2 - 4, (cy + py) / 2 - 12);
                    break;
                }

                case 'coordinate_plane': {
                    const cx = 380, cy = 230;

                    // X-axis
                    ctx.beginPath();
                    ctx.moveTo(120, cy);
                    ctx.lineTo(640, cy);
                    ctx.stroke();
                    drawArrowHead(630, cy, 640, cy);
                    drawArrowHead(130, cy, 120, cy);

                    // Y-axis
                    ctx.beginPath();
                    ctx.moveTo(cx, 400);
                    ctx.lineTo(cx, 60);
                    ctx.stroke();
                    drawArrowHead(cx, 70, cx, 60);
                    drawArrowHead(cx, 390, cx, 400);

                    // Ticks
                    const step = 45;
                    ctx.font = '11px monospace';
                    for (let i = -4; i <= 4; i++) {
                        if (i !== 0) {
                            const tx = cx + i * step;
                            ctx.beginPath();
                            ctx.moveTo(tx, cy - 4);
                            ctx.lineTo(tx, cy + 4);
                            ctx.stroke();
                            ctx.fillText(i.toString(), tx - 4, cy + 18);

                            const ty = cy - i * step;
                            ctx.beginPath();
                            ctx.moveTo(cx - 4, ty);
                            ctx.lineTo(cx + 4, ty);
                            ctx.stroke();
                            ctx.fillText(i.toString(), cx - 18, ty + 4);
                        }
                    }

                    ctx.font = 'bold 15px sans-serif';
                    ctx.fillText('X', 645, cy + 5);
                    ctx.fillText("X'", 95, cy + 5);
                    ctx.fillText('Y', cx - 6, 48);
                    ctx.fillText("Y'", cx - 6, 420);
                    ctx.fillText('O', cx + 6, cy + 18);
                    break;
                }

                case 'cylinder_rh': {
                    const cx = 380, topY = 120, botY = 340, rx = 120, ry = 28;

                    ctx.beginPath();
                    ctx.ellipse(cx, topY, rx, ry, 0, 0, Math.PI * 2);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.moveTo(cx - rx, topY);
                    ctx.lineTo(cx - rx, botY);
                    ctx.moveTo(cx + rx, topY);
                    ctx.lineTo(cx + rx, botY);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.ellipse(cx, botY, rx, ry, 0, 0, Math.PI);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.setLineDash([5, 4]);
                    ctx.ellipse(cx, botY, rx, ry, 0, Math.PI, Math.PI * 2);
                    ctx.stroke();

                    // Height dimension
                    ctx.beginPath();
                    ctx.setLineDash([4, 4]);
                    ctx.moveTo(cx + rx + 35, topY);
                    ctx.lineTo(cx + rx + 35, botY);
                    ctx.stroke();
                    drawArrowHead(cx + rx + 35, topY + 10, cx + rx + 35, topY);
                    drawArrowHead(cx + rx + 35, botY - 10, cx + rx + 35, botY);
                    ctx.setLineDash([]);
                    ctx.fillText('height (h)', cx + rx + 48, (topY + botY) / 2 + 5);

                    // Radius line on top
                    ctx.beginPath();
                    ctx.arc(cx, topY, 3, 0, Math.PI * 2);
                    ctx.fill();
                    ctx.setLineDash([4, 4]);
                    ctx.moveTo(cx, topY);
                    ctx.lineTo(cx + rx, topY);
                    ctx.stroke();
                    ctx.setLineDash([]);
                    ctx.fillText('radius (r)', cx + rx / 2 - 25, topY - 10);
                    break;
                }

                case 'cone_rhl': {
                    const cx = 380, apexY = 90, botY = 350, rx = 130, ry = 28;

                    ctx.beginPath();
                    ctx.moveTo(cx, apexY);
                    ctx.lineTo(cx - rx, botY);
                    ctx.moveTo(cx, apexY);
                    ctx.lineTo(cx + rx, botY);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.ellipse(cx, botY, rx, ry, 0, 0, Math.PI);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.setLineDash([5, 4]);
                    ctx.ellipse(cx, botY, rx, ry, 0, Math.PI, Math.PI * 2);
                    ctx.stroke();

                    // Height & Radius
                    ctx.beginPath();
                    ctx.setLineDash([4, 4]);
                    ctx.moveTo(cx, apexY);
                    ctx.lineTo(cx, botY);
                    ctx.lineTo(cx + rx, botY);
                    ctx.stroke();
                    ctx.setLineDash([]);
                    ctx.strokeRect(cx, botY - 14, 14, 14);

                    ctx.fillText('h', cx - 18, (apexY + botY) / 2);
                    ctx.fillText('r', cx + rx / 2 - 4, botY + 22);
                    ctx.fillText('slant height (l)', cx + rx / 2 + 35, (apexY + botY) / 2 - 10);
                    break;
                }

                case 'cube_3d': {
                    const s = 170, off = 65;
                    const fx = 260, fy = 170;
                    const bx = fx + off, by = fy - off;

                    ctx.strokeRect(fx, fy, s, s);

                    ctx.beginPath();
                    ctx.moveTo(bx, by);
                    ctx.lineTo(bx + s, by);
                    ctx.lineTo(bx + s, by + s);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.moveTo(fx, fy);
                    ctx.lineTo(bx, by);
                    ctx.moveTo(fx + s, fy);
                    ctx.lineTo(bx + s, by);
                    ctx.moveTo(fx + s, fy + s);
                    ctx.lineTo(bx + s, by + s);
                    ctx.stroke();

                    ctx.beginPath();
                    ctx.setLineDash([5, 4]);
                    ctx.moveTo(fx, fy + s);
                    ctx.lineTo(bx, by + s);
                    ctx.lineTo(bx, by);
                    ctx.moveTo(bx, by + s);
                    ctx.lineTo(bx + s, by + s);
                    ctx.stroke();
                    ctx.setLineDash([]);

                    ctx.fillText('a', fx + s / 2 - 4, fy + s + 22);
                    ctx.fillText('a', fx + s + 12, fy + s / 2);
                    ctx.fillText('a', fx + s + off / 2 + 10, fy - off / 2 + 10);
                    break;
                }
            }

            ctx.restore();
            pushUndoState();
        };

        // Auto-Trim Margins for High-Quality Export
        function getTrimmedCanvasDataUrl() {
            if (!canvas || !ctx) return '';
            const shouldTrim = document.getElementById('draw_auto_trim')?.checked ?? true;
            if (!shouldTrim) {
                return canvas.toDataURL('image/png');
            }

            const w = canvas.width;
            const h = canvas.height;
            const imgData = ctx.getImageData(0, 0, w, h);
            const data = imgData.data;

            let minX = w, minY = h, maxX = 0, maxY = 0;
            let hasContent = false;

            for (let y = 0; y < h; y++) {
                for (let x = 0; x < w; x++) {
                    const idx = (y * w + x) * 4;
                    const r = data[idx];
                    const g = data[idx + 1];
                    const b = data[idx + 2];
                    const a = data[idx + 3];

                    // Pixel differs significantly from white/grid
                    if (a > 20 && (r < 235 || g < 235 || b < 235)) {
                        if (x < minX) minX = x;
                        if (x > maxX) maxX = x;
                        if (y < minY) minY = y;
                        if (y > maxY) maxY = y;
                        hasContent = true;
                    }
                }
            }

            if (!hasContent) {
                return canvas.toDataURL('image/png');
            }

            const padding = 24;
            minX = Math.max(0, minX - padding);
            minY = Math.max(0, minY - padding);
            maxX = Math.min(w, maxX + padding);
            maxY = Math.min(h, maxY + padding);

            const cropW = Math.max(50, maxX - minX);
            const cropH = Math.max(50, maxY - minY);

            const trimCanvas = document.createElement('canvas');
            trimCanvas.width = cropW;
            trimCanvas.height = cropH;
            const tCtx = trimCanvas.getContext('2d');

            // Pure white background
            tCtx.fillStyle = '#ffffff';
            tCtx.fillRect(0, 0, cropW, cropH);

            // Copy cropped image
            tCtx.drawImage(canvas, minX, minY, cropW, cropH, 0, 0, cropW, cropH);
            return trimCanvas.toDataURL('image/png');
        }

        // Open & Close Modal
        window.openDrawToolModal = function(prefix = 'create') {
            drawTargetPrefix = prefix;
            const modal = document.getElementById('drawToolModal');
            if (!modal) return;
            modal.classList.remove('hidden');

            if (!canvas) {
                initDrawCanvas();
            }
        };

        window.closeDrawToolModal = function() {
            const modal = document.getElementById('drawToolModal');
            if (modal) modal.classList.add('hidden');
            cancelTextPlacement();
        };

        window.downloadDrawCanvas = function() {
            const dataUrl = getTrimmedCanvasDataUrl();
            if (!dataUrl) return;
            const a = document.createElement('a');
            a.href = dataUrl;
            a.download = `geometric-diagram-${Date.now()}.png`;
            document.body.appendChild(a);
            a.click();
            document.body.removeChild(a);
        };

        window.insertDrawingIntoQuestion = function() {
            const dataUrl = getTrimmedCanvasDataUrl();
            if (!dataUrl) return;

            const targetQuill = drawTargetPrefix === 'edit' ? (window.editQuill || null) : (window.createQuill || null);
            if (!targetQuill) {
                alert('Question text editor not initialized.');
                return;
            }

            targetQuill.focus();
            let range = targetQuill.getSelection();
            if (!range) {
                range = { index: targetQuill.getLength() - 1, length: 0 };
            }

            // Insert image embed
            targetQuill.insertEmbed(range.index, 'image', dataUrl, 'user');
            targetQuill.setSelection(range.index + 1, 0);

            // Synchronize with hidden input
            const targetInputId = drawTargetPrefix === 'edit' ? 'edit_q_name' : 'create_q_name';
            const targetInput = document.getElementById(targetInputId);
            if (targetInput) {
                targetInput.value = targetQuill.root.innerHTML;
            }

            // Remove client-side validation error
            const clientErr = document.getElementById(drawTargetPrefix + '_q_name_client_error');
            if (clientErr) clientErr.classList.add('hidden');
            const container = document.getElementById(drawTargetPrefix + '_q_editor_container');
            if (container) container.classList.remove('border-red-500', 'ring-1', 'ring-red-500');

            closeDrawToolModal();

            // Display toast feedback
            showDrawToast('Diagram successfully inserted into question prompt!');
        };

        function showDrawToast(msg) {
            let toast = document.getElementById('draw_tool_toast');
            if (!toast) {
                toast = document.createElement('div');
                toast.id = 'draw_tool_toast';
                toast.style.zIndex = '999999';
                toast.className = 'fixed bottom-5 right-5 px-4 py-2.5 rounded-xl bg-emerald-600 text-white font-semibold text-xs shadow-2xl flex items-center space-x-2 transition-all duration-300 transform translate-y-20 opacity-0';
                toast.innerHTML = `
                    <svg class="w-4 h-4 text-white" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg>
                    <span id="draw_tool_toast_msg"></span>
                `;
                document.body.appendChild(toast);
            }
            document.getElementById('draw_tool_toast_msg').textContent = msg;
            toast.classList.remove('translate-y-20', 'opacity-0');
            setTimeout(() => {
                toast.classList.add('translate-y-20', 'opacity-0');
            }, 3000);
        }

        document.addEventListener('DOMContentLoaded', function() {
            // Lazy init when modal opens
        });
    })();
</script>
