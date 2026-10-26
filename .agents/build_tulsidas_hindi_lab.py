# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 10 Hindi (Kshitij Part 2), Chapter 2: तुलसीदास - राम-लक्ष्मण-परशुराम संवाद.
Generates public/animations/ram-lakshman-parashuram-samvad.html with:
- 16 Rich Content Slides in pure eloquent Hindi covering every line of the textbook (Pages 10-16).
- 32 In-Slide Checkpoint Questions with instant teacher feedback.
- 4 Dedicated Mastery Quiz Challenge Slides (40 questions total) with popup solution modals in Hindi.
- 16 Bespoke Interactive SVG Laboratory Simulators.
- Animated Teacher Avatar (प्राध्यापिका डॉ. अनन्या - हिंदी साहित्य विशेषज्ञ) with talking mouth synced to Hindi audio narration.
- Web Audio API sound synthesizer and Web Speech API Hindi narration (hi-IN).
- Last Slide Notice with strict unit test compatibility.
"""

import json
import os
import sys

# Ensure data script can be imported
sys.path.append(os.path.dirname(__file__))
from tulsidas_hindi_data import CONTENT_SLIDES, QUIZ_SLIDES


def generate_interactive_simulator(s_idx):
    """Returns bespoke interactive SVG simulator HTML for each content slide (1-16)."""
    if s_idx == 1:
        # Simulator 1: Tulsidas Life Map & Biography Explorer
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.1: गोस्वामी तुलसीदास जीवन-यात्रा एवं पावन तीर्थ अन्वेषक</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5">
                    <button onclick="setSim1Location('rajapur')" id="sim1-btn-rajapur" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">राजापुर (बांदा)</button>
                    <button onclick="setSim1Location('soron')" id="sim1-btn-soron" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">सोरों (सूकरक्षेत्र)</button>
                    <button onclick="setSim1Location('ayodhya')" id="sim1-btn-ayodhya" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">अयोध्या धाम</button>
                    <button onclick="setSim1Location('kashi')" id="sim1-btn-kashi" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">काशी (अस्सी घाट)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim1-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Flowing Sacred Rivers: Ganga & Yamuna -->
                    <path d="M 20 60 Q 180 80 260 140 T 480 210" fill="none" stroke="#0284c7" stroke-width="8" opacity="0.6"/>
                    <path d="M 20 120 Q 150 140 260 140 T 480 170" fill="none" stroke="#0369a1" stroke-width="6" opacity="0.5"/>
                    <text x="70" y="55" fill="#38bdf8" font-size="10" font-weight="bold">माँ गंगा</text>
                    <text x="80" y="140" fill="#0ea5e9" font-size="10" font-weight="bold">माँ यमुना</text>

                    <!-- Interactive Location Markers -->
                    <!-- Rajapur Marker -->
                    <g id="sim1-pin-rajapur" class="cursor-pointer transition transform hover:scale-110" onclick="setSim1Location('rajapur')">
                        <circle cx="160" cy="150" r="14" fill="#d97706" stroke="#fbbf24" stroke-width="2.5"/>
                        <circle cx="160" cy="150" r="6" fill="#ffffff"/>
                        <text x="160" y="178" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">राजापुर (1532)</text>
                    </g>

                    <!-- Soron Marker -->
                    <g id="sim1-pin-soron" class="cursor-pointer transition transform hover:scale-110" onclick="setSim1Location('soron')">
                        <circle cx="110" cy="80" r="12" fill="#78350f" stroke="#f59e0b" stroke-width="2"/>
                        <circle cx="110" cy="80" r="5" fill="#ffffff"/>
                        <text x="110" y="105" fill="#cbd5e1" font-size="10" font-weight="bold" text-anchor="middle">सोरों (सूकरक्षेत्र)</text>
                    </g>

                    <!-- Ayodhya Marker -->
                    <g id="sim1-pin-ayodhya" class="cursor-pointer transition transform hover:scale-110" onclick="setSim1Location('ayodhya')">
                        <circle cx="280" cy="90" r="14" fill="#b45309" stroke="#fbbf24" stroke-width="2.5"/>
                        <circle cx="280" cy="90" r="6" fill="#ffffff"/>
                        <text x="280" y="118" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">अयोध्या (मानस रचना)</text>
                    </g>

                    <!-- Kashi Marker -->
                    <g id="sim1-pin-kashi" class="cursor-pointer transition transform hover:scale-110" onclick="setSim1Location('kashi')">
                        <circle cx="390" cy="160" r="15" fill="#dc2626" stroke="#fca5a5" stroke-width="2.5"/>
                        <circle cx="390" cy="160" r="6" fill="#ffffff"/>
                        <text x="390" y="190" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">काशी अस्सी (1623)</text>
                    </g>

                    <!-- Active Glow Ring -->
                    <circle id="sim1-active-ring" cx="160" cy="150" r="20" fill="none" stroke="#f59e0b" stroke-width="3" stroke-dasharray="4,4" class="animate-spin"/>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim1-info-title">राजापुर (बांदा, उत्तर प्रदेश):</span>
                    <span id="sim1-info-desc">अधिकांश विद्वानों के अनुसार संवत् 1589 (1532 ई.) में जन्म। पिता आत्माराम दुबे और माता हुलसी। अभुक्त मूल नक्षत्र में जन्म के कारण बाल्यकाल में त्याग दिया गया।</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 2:
        # Simulator 2: Awadhi vs Brajbhasha Dual-Pan Scale
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.2: अवधी एवं ब्रजभाषा काव्य-संतुलन तराजू (12 प्रामाणिक ग्रंथ)</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="balanceSim2Language('awadhi')" id="sim2-btn-awadhi" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">अवधी रचनाएँ देखें</button>
                    <button onclick="balanceSim2Language('braj')" id="sim2-btn-braj" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">ब्रजभाषा रचनाएँ देखें</button>
                    <button onclick="balanceSim2Language('equal')" id="sim2-btn-equal" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">समन्वय (दोनों समान)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim2-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Fulcrum Base -->
                    <polygon points="250,70 230,210 270,210" fill="#475569" stroke="#94a3b8" stroke-width="2"/>
                    <circle cx="250" cy="70" r="9" fill="#f59e0b"/>

                    <!-- Balance Beam -->
                    <g id="sim2-beam" transform="rotate(0 250 70)" class="transition-transform duration-700">
                        <line x1="80" y1="70" x2="420" y2="70" stroke="#f59e0b" stroke-width="6" stroke-linecap="round"/>

                        <!-- Left Pan: Awadhi -->
                        <line x1="120" y1="70" x2="90" y2="140" stroke="#cbd5e1" stroke-width="2"/>
                        <line x1="120" y1="70" x2="150" y2="140" stroke="#cbd5e1" stroke-width="2"/>
                        <path d="M 70 140 Q 120 170 170 140 Z" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
                        <text x="120" y="160" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">अवधी भाषा</text>

                        <!-- Right Pan: Braj Bhasha -->
                        <line x1="380" y1="70" x2="350" y2="140" stroke="#cbd5e1" stroke-width="2"/>
                        <line x1="380" y1="70" x2="410" y2="140" stroke="#cbd5e1" stroke-width="2"/>
                        <path d="M 330 140 Q 380 170 430 140 Z" fill="#1e3a8a" stroke="#60a5fa" stroke-width="2"/>
                        <text x="380" y="160" fill="#bfdbfe" font-size="11" font-weight="bold" text-anchor="middle">ब्रज भाषा</text>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim2-desc-title">अवधी एवं ब्रजभाषा का समन्वय:</span>
                    <span id="sim2-desc-body">तुलसीदास जी का दोनों भाषाओं पर असाधारण समान अधिकार था। रामचरितमानस, जानकी मंगल, पार्वती मंगल अवधी में हैं; जबकि विनयपत्रिका, कवितावली, गीतावली, दोहावली ब्रजभाषा के अमर गीतिकाव्य हैं!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 3:
        # Simulator 3: Sita Swayamvar & Shiva's Pinaka Bow Rupture
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.3: सीता स्वयंवर एवं भगवान शिव का 'पिनाक' धनुर्भंग सिम्युलेटर</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="triggerBowSnap()" id="sim3-snap-btn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-gradient-to-r from-amber-600 to-rose-600 hover:from-amber-500 hover:to-rose-500 text-white shadow-lg shadow-amber-500/20 transition cursor-pointer">
                        ⚡ श्रीराम का स्पर्श एवं धनुर्भंग
                    </button>
                    <button onclick="resetBowSim()" class="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                        पुनः स्थापित करें
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-purple-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim3-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Royal Court Background Silhouette -->
                    <rect x="0" y="210" width="500" height="30" fill="#0f172a"/>
                    <circle cx="250" cy="120" r="110" fill="#fbbf24" opacity="0.05"/>

                    <!-- Intact Bow Group -->
                    <g id="sim3-intact-bow">
                        <!-- Bow Arc -->
                        <path d="M 120 180 Q 250 20 380 180" fill="none" stroke="#d97706" stroke-width="12" stroke-linecap="round"/>
                        <path d="M 120 180 Q 250 20 380 180" fill="none" stroke="#fef08a" stroke-width="4" stroke-linecap="round"/>
                        <!-- Bowstring (प्रत्यंचा) -->
                        <line x1="120" y1="180" x2="380" y2="180" stroke="#f8fafc" stroke-width="2.5" stroke-dasharray="3,1"/>
                        <circle cx="250" cy="180" r="5" fill="#38bdf8"/>
                        <text x="250" y="90" fill="#fef08a" font-size="13" font-weight="bold" text-anchor="middle">महादेव शिव का 'पिनाक' धनुष</text>
                    </g>

                    <!-- Broken Bow Pieces (Hidden initially) -->
                    <g id="sim3-broken-bow" class="hidden">
                        <!-- Left Fragment -->
                        <path d="M 100 190 Q 180 70 230 130" fill="none" stroke="#d97706" stroke-width="12" stroke-linecap="round" class="animate-pulse"/>
                        <!-- Right Fragment -->
                        <path d="M 270 130 Q 320 70 400 190" fill="none" stroke="#d97706" stroke-width="12" stroke-linecap="round" class="animate-pulse"/>
                        <!-- Lightning Bolts -->
                        <path d="M 250 30 L 240 100 L 260 120 L 245 180" fill="none" stroke="#fbbf24" stroke-width="4"/>
                        <text x="250" y="70" fill="#f87171" font-size="14" font-weight="black" text-anchor="middle">⚡ प्रचंड घोर ध्वनि: धनुर्भंग! ⚡</text>
                        <text x="250" y="160" fill="#38bdf8" font-size="11" font-weight="bold" text-anchor="middle">"छुअत टूट रघुपतिहु न दोसू"</text>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim3-caption">राजा जनक की सभा:</span>
                    <span id="sim3-detail">राजा जनक की प्रतिज्ञा थी कि जो शिवजी के इस दिव्य पिनाक धनुष पर प्रत्यंचा चढ़ाएगा, उसी से सीता का विवाह होगा। श्रीराम के छूते ही जीर्ण धनुष टूट गया!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 4:
        # Simulator 4: Shri Ram Humility vs Parashuram Rage Meter
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.4: श्रीराम का शील-संयम बनाम परशुराम का प्रचंड क्रोध-गेज</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim4Character('ram')" id="sim4-btn-ram" class="px-2.5 py-1 rounded text-xs font-bold bg-sky-600 text-white transition">श्रीराम का पक्ष (शांत रस)</button>
                    <button onclick="toggleSim4Character('parashuram')" id="sim4-btn-paras" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">परशुराम का पक्ष (रौद्र रस)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim4-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Left: Shri Ram Column (Calm Sky Blue) -->
                    <rect x="40" y="30" width="190" height="170" rx="12" fill="#0c4a6e" stroke="#38bdf8" stroke-width="2" opacity="0.8"/>
                    <text x="135" y="60" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">मर्यादा पुरुषोत्तम श्रीराम</text>
                    <text x="135" y="80" fill="#bae6fd" font-size="10" text-anchor="middle">शांत रस • विनम्रता एवं शील</text>
                    <rect x="60" y="100" width="150" height="14" rx="7" fill="#082f49"/>
                    <rect id="sim4-ram-bar" x="60" y="100" width="145" height="14" rx="7" fill="#38bdf8"/>
                    <text x="135" y="112" fill="#082f49" font-size="9" font-weight="black" text-anchor="middle">विनम्रता: 100%</text>
                    <text x="135" y="145" fill="#f0f9ff" font-size="10" font-weight="bold" text-anchor="middle">"नाथ संभुधनु भंजनिहारा।"</text>
                    <text x="135" y="165" fill="#bae6fd" font-size="10" font-weight="bold" text-anchor="middle">"होइहि केउ एक दास तुम्हारा॥"</text>

                    <!-- Right: Parashuram Column (Fierce Crimson Red) -->
                    <rect x="270" y="30" width="190" height="170" rx="12" fill="#7f1d1d" stroke="#f87171" stroke-width="2" opacity="0.8"/>
                    <text x="365" y="60" fill="#fca5a5" font-size="12" font-weight="bold" text-anchor="middle">भगवान परशुराम</text>
                    <text x="365" y="80" fill="#fecaca" font-size="10" text-anchor="middle">रौद्र रस • प्रचंड क्षोभ एवं कोप</text>
                    <rect x="290" y="100" width="150" height="14" rx="7" fill="#450a0a"/>
                    <rect id="sim4-paras-bar" x="290" y="100" width="145" height="14" rx="7" fill="#ef4444"/>
                    <text x="365" y="112" fill="#ffffff" font-size="9" font-weight="black" text-anchor="middle">क्रोध: 100%</text>
                    <text x="365" y="145" fill="#fff1f2" font-size="10" font-weight="bold" text-anchor="middle">"सुनि रिसाइ बोले मुनि कोही।"</text>
                    <text x="365" y="165" fill="#fecaca" font-size="10" font-weight="bold" text-anchor="middle">"सेवकु सो जो करै सेवकाई॥"</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim4-quote-title">तुलसीदास जी का संवाद शिल्प:</span>
                    <span id="sim4-quote-desc">श्रीराम का कथन अत्यंत मधुर, निरहंकारी और दास-भाव से भरा है, जबकि परशुराम का उत्तर क्रोधी स्वभाव और प्रतिशोध की ज्वाला से युक्त है।</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 5:
        # Simulator 5: Definition of Servant vs Enemy & Sahasrabahu Comparison
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.5: परशुराम का तर्क-विश्लेषक: सेवक बनाम शत्रु (सहस्रबाहु)</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="setSim5Mode('sevak')" id="sim5-btn-sevak" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition">सच्चा सेवक कौन?</button>
                    <button onclick="setSim5Mode('shatru')" id="sim5-btn-shatru" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">शत्रु (अरि) कौन?</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim5-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Central Decision Tree -->
                    <circle cx="250" cy="50" r="35" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                    <text x="250" y="48" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">परशुराम का</text>
                    <text x="250" y="62" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">तर्क-विधान</text>

                    <!-- Branch Lines -->
                    <line x1="225" y1="75" x2="130" y2="130" stroke="#10b981" stroke-width="3"/>
                    <line x1="275" y1="75" x2="370" y2="130" stroke="#ef4444" stroke-width="3"/>

                    <!-- Left Card: Sevak -->
                    <g id="sim5-card-sevak" class="transition-opacity duration-300">
                        <rect x="40" y="130" width="180" height="90" rx="10" fill="#064e3b" stroke="#34d399" stroke-width="2"/>
                        <text x="130" y="155" fill="#6ee7b7" font-size="11" font-weight="bold" text-anchor="middle">✓ 'सेवकु सो जो करै सेवकाई'</text>
                        <text x="130" y="175" fill="#d1fae5" font-size="9" text-anchor="middle">• सेवा कर्म करने वाला</text>
                        <text x="130" y="195" fill="#d1fae5" font-size="9" text-anchor="middle">• गुरु व प्रभु को सुख देने वाला</text>
                    </g>

                    <!-- Right Card: Shatru -->
                    <g id="sim5-card-shatru" class="transition-opacity duration-300">
                        <rect x="280" y="130" width="180" height="90" rx="10" fill="#7f1d1d" stroke="#f87171" stroke-width="2"/>
                        <text x="370" y="155" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">✗ 'अरिकरनी करि करिअ लराई'</text>
                        <text x="370" y="175" fill="#fee2e2" font-size="9" text-anchor="middle">• शिव धनुष तोड़कर शत्रु-कर्म किया</text>
                        <text x="370" y="195" fill="#fecaca" font-size="9" font-weight="bold" text-anchor="middle">• 'सहसबाहु सम सो रिपु मोरा'</text>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim5-desc">सहस्रबाहु की उपमा:</span>
                    <span id="sim5-desc-txt">परशुराम कहते हैं कि जिसने भी शिवजी का धनुष तोड़ा है, वह सहस्त्रबाहु के समान मेरा घोर शत्रु है। वह इस राजाओं के समाज से तुरंत अलग हो जाए, नहीं तो सभी राजा मारे जाएँगे!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 6:
        # Simulator 6: Childhood Dhanuhi vs Shiva's Pinaka Bow
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.6: लक्ष्मण का हास-व्यंग्य: लड़कपन की धनुहियाँ बनाम शिव-धनुष</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim6Bow('dhanuhi')" id="sim6-btn-dhanuhi" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">लड़कपन की धनुहियाँ</button>
                    <button onclick="toggleSim6Bow('pinaka')" id="sim6-btn-pinaka" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">महादेव का पिनाक धनुष</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim6-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Left: Childhood Toy Bows -->
                    <g id="sim6-dhanuhi-group">
                        <path d="M 80 180 Q 140 100 200 180" fill="none" stroke="#22c55e" stroke-width="4"/>
                        <line x1="80" y1="180" x2="200" y2="180" stroke="#86efac" stroke-width="1.5"/>
                        <circle cx="140" cy="180" r="3" fill="#22c55e"/>

                        <path d="M 60 130 Q 110 70 160 130" fill="none" stroke="#a3e635" stroke-width="3"/>
                        <line x1="60" y1="130" x2="160" y2="130" stroke="#d9f99d" stroke-width="1.5"/>

                        <text x="140" y="215" fill="#86efac" font-size="11" font-weight="bold" text-anchor="middle">"बहु धनुही तोरी लरिकाईं"</text>
                        <text x="140" y="50" fill="#4ade80" font-size="10" font-weight="bold" text-anchor="middle">बाल्यकाल के साधारण खिलौने-धनुष</text>
                    </g>

                    <!-- Right: Giant Divine Pinaka Bow -->
                    <g id="sim6-pinaka-group">
                        <path d="M 280 190 Q 380 10 480 190" fill="none" stroke="#eab308" stroke-width="12" stroke-linecap="round"/>
                        <path d="M 280 190 Q 380 10 480 190" fill="none" stroke="#fef08a" stroke-width="4" stroke-linecap="round"/>
                        <line x1="280" y1="190" x2="480" y2="190" stroke="#f8fafc" stroke-width="2.5"/>
                        <text x="380" y="215" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">"एहि धनु पर ममता केहि हेतू"</text>
                        <text x="380" y="50" fill="#facc15" font-size="10" font-weight="bold" text-anchor="middle">भगवान शिव का विश्वविदित धनुष</text>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim6-desc">लक्ष्मण की व्यंग्योक्ति:</span>
                    <span id="sim6-text">"हे मुनिवर! हमने बचपन में खेल-खेल में बहुत सी ऐसी छोटी धनुहियाँ तोड़ी हैं, तब तो आपने कभी ऐसा क्रोध नहीं किया। फिर इस पुराने धनुष पर इतनी ममता किस कारण है?"</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 7:
        # Simulator 7: Old Bow 'June Dhanu' Touch-Break Tensile Test
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.7: 'जून धनु' (जीर्ण-शीर्ण धनुष) तनन-परीक्षण: 'छुअत टूट रघुपतिहु न दोसू'</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="applyTensionSim7()" id="sim7-touch-btn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">
                        👆 श्रीराम का केवल स्पर्श (Touch)
                    </button>
                    <button onclick="resetSim7()" class="px-2.5 py-1.5 rounded-lg text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                        पुनः परीक्षण
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim7-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Bow Graphic Under Tensile Stress -->
                    <g id="sim7-bow-group">
                        <path id="sim7-bow-arc" d="M 120 160 Q 250 50 380 160" fill="none" stroke="#d97706" stroke-width="10" stroke-linecap="round"/>
                        <line id="sim7-bow-string" x1="120" y1="160" x2="380" y2="160" stroke="#f8fafc" stroke-width="2"/>
                        <!-- Aged cracks on June Dhanu -->
                        <path d="M 245 95 L 255 105 L 248 115" stroke="#78350f" stroke-width="2"/>
                    </g>

                    <!-- Touch Vector Finger -->
                    <g id="sim7-finger" class="transition transform duration-500" transform="translate(0, -40)">
                        <path d="M 250 30 L 250 85" stroke="#38bdf8" stroke-width="4" stroke-dasharray="4,2"/>
                        <circle cx="250" cy="90" r="7" fill="#38bdf8"/>
                        <text x="250" y="25" fill="#38bdf8" font-size="10" font-weight="bold" text-anchor="middle">श्रीराम का सुकोमल स्पर्श</text>
                    </g>

                    <text id="sim7-status-text" x="250" y="200" fill="#fef08a" font-size="12" font-weight="bold" text-anchor="middle">
                        धनुष अत्यंत पुराना (जून) एवं जीर्ण-शीर्ण अवस्था में है।
                    </text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim7-sub">लक्ष्मण का वैज्ञानिक तर्क:</span>
                    <span id="sim7-sub-desc">"का छति लाभु जून धनु तोरें। देखा राम नयन के भोरें॥" पुराने धनुष के टूटने से क्या हानि और क्या लाभ! श्रीराम ने तो इसे नए के धोखे से देखा था, पर यह तो छूते ही टूट गया, इसमें रघुपति का कोई दोष नहीं!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 8:
        # Simulator 8: Parashuram's Fierce Axe (Parashu) 3D Model & Reprimand
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.8: परशुराम का भयानक कुठार (फरसा) एवं पराक्रम गर्जना</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="swingSim8Axe()" id="sim8-swing-btn" class="px-3 py-1 rounded text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition cursor-pointer">
                        🪓 फरसा घुमाएँ (Axe Swing)
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-rose-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim8-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Parashu Axe SVG -->
                    <g id="sim8-axe" class="transition-transform duration-500 origin-[250px_180px]">
                        <!-- Wooden Handle -->
                        <rect x="245" y="40" width="10" height="160" rx="4" fill="#78350f" stroke="#b45309" stroke-width="2"/>
                        <!-- Steel Axe Blade -->
                        <path d="M 255 50 C 330 40, 360 100, 255 110 Z" fill="#94a3b8" stroke="#f1f5f9" stroke-width="3"/>
                        <path d="M 270 55 C 335 60, 345 95, 270 100 Z" fill="#cbd5e1"/>
                        <circle cx="250" cy="80" r="12" fill="#d97706"/>
                        <!-- Blade Edge Gleam -->
                        <line x1="335" y1="48" x2="335" y2="102" stroke="#ffffff" stroke-width="3" stroke-linecap="round"/>
                    </g>

                    <!-- Text Badges -->
                    <rect x="20" y="25" width="160" height="55" rx="8" fill="#450a0a" stroke="#f87171" stroke-width="1.5"/>
                    <text x="100" y="45" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">बाल ब्रह्मचारी अति कोही</text>
                    <text x="100" y="65" fill="#fecaca" font-size="9" text-anchor="middle">बिस्वबिदित छत्रियकुल द्रोही</text>

                    <rect x="320" y="25" width="160" height="55" rx="8" fill="#450a0a" stroke="#f87171" stroke-width="1.5"/>
                    <text x="400" y="45" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">रे नृपबालक कालबस</text>
                    <text x="400" y="65" fill="#fecaca" font-size="9" text-anchor="middle">बोलत तोहि न संभार</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-rose-400" id="sim8-desc">परशुराम की चेतावनी:</span>
                    <span id="sim8-desc-txt">"अरे दुष्ट! क्या तूने मेरा स्वभाव नहीं सुना? मैं तुझे बालक जानकर नहीं मार रहा हूँ, और तू मुझे केवल एक साधारण निस्तेज मुनि समझ रहा है!"</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 9:
        # Simulator 9: 21 Times Kshatriya-Free Earth & 'Garbhanh ke arbhak dalan'
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.9: इक्कीस बार क्षत्रिय-विहीन धरा एवं फरसे की विभीषिका</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="incrementSim9Victory()" id="sim9-step-btn" class="px-3 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">
                        ⚔️ विजय गणना (1 से 21 बार)
                    </button>
                    <button onclick="resetSim9()" class="px-2 py-1 rounded text-xs font-medium bg-slate-800 text-slate-300 hover:bg-slate-700 transition">
                        पुनः
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim9-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Globe of Earth -->
                    <circle cx="250" cy="110" r="65" fill="#0369a1" stroke="#38bdf8" stroke-width="3"/>
                    <path d="M 210 90 Q 240 60 270 80 Q 290 120 240 140 Z" fill="#15803d"/>
                    <path d="M 220 135 Q 260 160 270 140 Z" fill="#16a34a"/>

                    <!-- Counter Badge in Center -->
                    <rect x="180" y="185" width="140" height="30" rx="8" fill="#1e293b" stroke="#f59e0b" stroke-width="2"/>
                    <text id="sim9-count-text" x="250" y="205" fill="#fef08a" font-size="12" font-weight="black" text-anchor="middle">
                        21 बार भूप-विहीन पृथ्वी
                    </text>

                    <!-- Quote Pill Left -->
                    <rect x="20" y="40" width="140" height="60" rx="8" fill="#450a0a" stroke="#f87171" stroke-width="1"/>
                    <text x="90" y="60" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">"भुजबल भूमि</text>
                    <text x="90" y="75" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">भूप बिनु कीन्ही"</text>
                    <text x="90" y="90" fill="#fecaca" font-size="8" text-anchor="middle">बिपुल बार महिदेवन्ह दीन्ही</text>

                    <!-- Quote Pill Right -->
                    <rect x="340" y="40" width="140" height="60" rx="8" fill="#450a0a" stroke="#f87171" stroke-width="1"/>
                    <text x="410" y="60" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">"गर्भन्ह के अर्भक दलन</text>
                    <text x="410" y="75" fill="#fca5a5" font-size="9" font-weight="bold" text-anchor="middle">परसु मोर अति घोर"</text>
                    <text x="410" y="90" fill="#fecaca" font-size="8" text-anchor="middle">मातु पितहि जनि सोचबस करसि</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">परशुराम का पराक्रम:</span>
                    <span id="sim9-explanation">परशुराम ने अपनी भुजाओं के बल से 21 बार पृथ्वी को क्षत्रिय राजाओं से रहित कर ब्राह्मणों को दान में दे दिया था। उनका फरसा इतना भयानक है कि गर्भ में पल रहे नवजात शिशु भी इसके भय से नष्ट हो जाते हैं।</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 10:
        # Simulator 10: 'Phunki Paharu' Mountain vs 'Kumhadbattiya' Touch-Me-Not
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.10: 'फूँकि पहारू' बनाम 'कुम्हड़बतिया' शक्ति-परीक्षण</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="blowSim10Wind()" id="sim10-blow-btn" class="px-2.5 py-1 rounded text-xs font-bold bg-sky-600 text-white transition cursor-pointer">💨 फूँक मारें (Blow Mountain)</button>
                    <button onclick="pointSim10Finger()" id="sim10-finger-btn" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition cursor-pointer">👉 तर्जनी दिखाएँ (Kumhadbattiya)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim10-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Left: Immovable Mountain (पहाड़) -->
                    <polygon points="40,200 130,50 220,200" fill="#334155" stroke="#94a3b8" stroke-width="2"/>
                    <polygon points="100,200 160,80 240,200" fill="#475569" stroke="#cbd5e1" stroke-width="2"/>
                    <text x="130" y="218" fill="#cbd5e1" font-size="11" font-weight="bold" text-anchor="middle">अटल पर्वत ("पहारू")</text>

                    <!-- Wind Stream (Hidden initially) -->
                    <g id="sim10-wind" class="hidden">
                        <path d="M 20 80 Q 70 60 120 70 T 170 60" fill="none" stroke="#38bdf8" stroke-width="3" stroke-dasharray="6,3" class="animate-pulse"/>
                        <path d="M 20 100 Q 70 80 120 90 T 170 80" fill="none" stroke="#38bdf8" stroke-width="2" stroke-dasharray="6,3"/>
                        <text x="70" y="50" fill="#38bdf8" font-size="10" font-weight="bold">"चहत उड़ावन फूँकि पहारू"</text>
                    </g>

                    <!-- Right: Delicate Wax Gourd Fruit / Touch-me-not flower (कुम्हड़बतिया) -->
                    <g id="sim10-plant">
                        <circle id="sim10-fruit" cx="370" cy="130" r="30" fill="#15803d" stroke="#4ade80" stroke-width="3"/>
                        <path d="M 370 100 Q 380 80 395 75" fill="none" stroke="#22c55e" stroke-width="3"/>
                        <text x="370" y="190" fill="#fca5a5" font-size="11" font-weight="bold" text-anchor="middle">"इहाँ कुम्हड़बतिया कोउ नाहीं"</text>
                        <text x="370" y="210" fill="#fecaca" font-size="9" text-anchor="middle">"जे तरजनी देखि मरि जाहीं"</text>
                    </g>

                    <!-- Index Finger (तर्जनी) -->
                    <g id="sim10-pointing-hand" class="hidden">
                        <line x1="450" y1="130" x2="410" y2="130" stroke="#f87171" stroke-width="5" stroke-linecap="round"/>
                        <circle cx="410" cy="130" r="5" fill="#f87171"/>
                    </g>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim10-sub-title">लक्ष्मण का निर्भीक कटाक्ष:</span>
                    <span id="sim10-sub-desc">"हे मुनिवर! आप बार-बार फरसा दिखाकर फूँक से पहाड़ उड़ाना चाहते हैं! यहाँ कोई कुम्हड़े का छोटा कच्चा फल नहीं है जो आपकी तर्जनी अँगुली देखते ही मुरझा जाएगा!"</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 11:
        # Simulator 11: Raghu Clan Code of Honor Shield
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.11: रघुकुल मर्यादा ढाल: 'इन्ह पर न सुराई' (चार पूज्य वर्ग)</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5">
                    <button onclick="setSim11Category('sur')" id="sim11-btn-sur" class="px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">1. सुर (देवता)</button>
                    <button onclick="setSim11Category('mahisur')" id="sim11-btn-mahisur" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">2. महिसुर (ब्राह्मण)</button>
                    <button onclick="setSim11Category('harijan')" id="sim11-btn-harijan" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">3. हरिजन (भक्त)</button>
                    <button onclick="setSim11Category('gai')" id="sim11-btn-gai" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">4. गाई (गौ माता)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim11-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Central Shield of Honor -->
                    <path d="M 250 25 L 350 55 L 340 160 C 330 200, 250 225, 250 225 C 250 225, 170 200, 160 160 L 150 55 Z" fill="#b45309" stroke="#fbbf24" stroke-width="3"/>
                    <circle cx="250" cy="115" r="45" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
                    <text id="sim11-shield-icon" x="250" y="125" font-size="30" text-anchor="middle">👑</text>

                    <!-- Text details inside/outside shield -->
                    <text x="250" y="195" fill="#fef08a" font-size="11" font-weight="black" text-anchor="middle">रघुकुल की मर्यादा</text>

                    <!-- Left Rule Card -->
                    <rect x="20" y="70" width="120" height="70" rx="8" fill="#1e293b" stroke="#f87171" stroke-width="1.5"/>
                    <text x="80" y="95" fill="#fca5a5" font-size="10" font-weight="bold" text-anchor="middle">बधें पापु</text>
                    <text x="80" y="115" fill="#fecaca" font-size="8.5" text-anchor="middle">(इनका वध करने पर</text>
                    <text x="80" y="130" fill="#fecaca" font-size="8.5" text-anchor="middle">घोर पाप लगता है)</text>

                    <!-- Right Rule Card -->
                    <rect x="360" y="70" width="120" height="70" rx="8" fill="#1e293b" stroke="#fbbf24" stroke-width="1.5"/>
                    <text x="420" y="95" fill="#fef08a" font-size="10" font-weight="bold" text-anchor="middle">अपकीरति हारें</text>
                    <text x="420" y="115" fill="#fef3c7" font-size="8.5" text-anchor="middle">(इनसे पराजित होने पर</text>
                    <text x="420" y="130" fill="#fef3c7" font-size="8.5" text-anchor="middle">अपयश मिलता है)</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim11-info-title">सुर, महिसुर, हरिजन अरु गाई:</span>
                    <span id="sim11-info-body">लक्ष्मण कहते हैं कि रघुकुल में देवता, ब्राह्मण, भगवान के भक्त और गौ माता पर वीरता नहीं दिखाई जाती। इसलिए यदि आप हमें मारेंगे भी, तो भी हम आपके चरण ही पकड़ेंगे!</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 12:
        # Simulator 12: 'Koti Kulis' Thunderbolt Words vs Physical Weapons
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.12: 'कोटि कुलिस सम बचनु तुम्हारा' वज्र वाणी शक्ति-मापी</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="strikeSim12Thunder()" id="sim12-thunder-btn" class="px-3 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">
                        ⚡ वज्र वाणी का प्रहार (Strike Vajra)
                    </button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim12-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Thunderbolt Visual -->
                    <g id="sim12-vajra-group">
                        <polygon points="250,20 220,110 260,110 230,200 290,95 250,95" fill="#fbbf24" stroke="#f59e0b" stroke-width="2"/>
                    </g>

                    <!-- Left: Physical Weapons Box -->
                    <rect x="30" y="60" width="160" height="90" rx="10" fill="#1e293b" stroke="#64748b" stroke-width="2"/>
                    <text x="110" y="85" fill="#94a3b8" font-size="11" font-weight="bold" text-anchor="middle">भौतिक अस्त्र-शस्त्र</text>
                    <text x="110" y="110" fill="#cbd5e1" font-size="9" text-anchor="middle">धनुष, बाण एवं कुठार (फरसा)</text>
                    <text x="110" y="135" fill="#f87171" font-size="10" font-weight="bold" text-anchor="middle">"ब्यर्थ धरहु धनु बान कुठारा"</text>

                    <!-- Right: Vajra Words Box -->
                    <rect x="310" y="60" width="160" height="90" rx="10" fill="#450a0a" stroke="#f59e0b" stroke-width="2"/>
                    <text x="390" y="85" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">कोटि कुलिस (वाणी)</text>
                    <text x="390" y="110" fill="#fecaca" font-size="9" text-anchor="middle">करोड़ों वज्रों के समान कठोर शब्द</text>
                    <text x="390" y="135" fill="#fbbf24" font-size="10" font-weight="bold" text-anchor="middle">उपमा अलंकार का चरमोत्कर्ष</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim12-desc">लक्ष्मण का अद्वितीय कटाक्ष:</span>
                    <span id="sim12-text">"हे मुनिवर! आपका एक-एक वचन ही करोड़ों वज्रों के समान कठोर और घातक है, आपने धनुष, बाण और फरसा तो व्यर्थ ही धारण कर रखा है!"</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 13:
        # Simulator 13: Parashuram & Sahasrabahu Kamadhenu Legend Storyboard
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.13: पौराणिक कथा-प्रवाह: परशुराम, जमदग्नि एवं सहस्रबाहु का वैर</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="stepSim13Legend(1)" id="sim13-btn-1" class="px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">चरण 1: कामधेनु</button>
                    <button onclick="stepSim13Legend(2)" id="sim13-btn-2" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">चरण 2: अपहरण</button>
                    <button onclick="stepSim13Legend(3)" id="sim13-btn-3" class="px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">चरण 3: भुजा-छेदन</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim13-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Step 1 Scene: Kamadhenu in Jamadagni Ashram -->
                    <g id="sim13-scene-1">
                        <!-- Ashram Hut -->
                        <polygon points="120,80 70,130 170,130" fill="#78350f" stroke="#d97706" stroke-width="2"/>
                        <rect x="80" y="130" width="80" height="50" fill="#451a03"/>
                        <rect x="105" y="145" width="30" height="35" fill="#0f172a"/>
                        <!-- Cow Graphic -->
                        <ellipse cx="260" cy="140" rx="40" ry="25" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
                        <circle cx="225" cy="125" r="15" fill="#f8fafc" stroke="#94a3b8" stroke-width="2"/>
                        <circle cx="220" cy="122" r="3" fill="#0f172a"/>
                        <text x="260" y="190" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">दिव्य कामधेनु (सुरभि)</text>
                    </g>

                    <text id="sim13-step-heading" x="250" y="40" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">
                        चरण 1: जमदग्नि ऋषि के आश्रम में कामधेनु गाय
                    </text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim13-caption">पौराणिक पृष्ठभूमि:</span>
                    <span id="sim13-desc-text">सहस्रबाहु (कार्तवीर्य अर्जुन) ने जमदग्नि ऋषि के आश्रम से कामधेनु गाय का बलपूर्वक हरण कर लिया था। परशुराम ने क्रोधित होकर उसकी हजार भुजाएँ काट डाली थीं।</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 14:
        # Simulator 14: Doha-Chaupai Matra Metric Laboratory
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.14: छंद शास्त्र: दोहा-चौपाई मात्रा गणक एवं यति-गति प्रयोगशाला</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="setSim14Chhand('chaupai')" id="sim14-btn-chaupai" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">चौपाई (16 मात्रा)</button>
                    <button onclick="setSim14Chhand('doha')" id="sim14-btn-doha" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">दोहा (13 + 11)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim14-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Verse Container -->
                    <rect x="20" y="30" width="460" height="150" rx="12" fill="#0f172a" stroke="#d97706" stroke-width="2"/>

                    <!-- Chhand Title & Formula -->
                    <text id="sim14-chhand-title" x="250" y="65" fill="#fef08a" font-size="13" font-weight="bold" text-anchor="middle">
                        चौपाई छंद (सममात्रिक छंद - प्रत्येक चरण 16 मात्राएँ)
                    </text>

                    <!-- Example Verse Line -->
                    <text id="sim14-verse-line1" x="250" y="105" fill="#38bdf8" font-size="12" font-weight="bold" text-anchor="middle">
                        "ना थ सं भु ध नु भं ज नि हा रा"
                    </text>
                    <!-- Matra Signs Underneath -->
                    <text id="sim14-matra-symbols" x="250" y="130" fill="#f43f5e" font-size="12" font-weight="bold" font-family="monospace" text-anchor="middle">
                        ऽ  ।  ऽ  ।  ।  ।  ऽ  ।  ।  ऽ  ऽ = 16
                    </text>

                    <rect x="180" y="145" width="140" height="25" rx="6" fill="#1e293b"/>
                    <text id="sim14-rule" x="250" y="162" fill="#a7f3d0" font-size="10" font-weight="bold" text-anchor="middle">
                        चरण के अंत में गुरु-लघु नियम
                    </text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400" id="sim14-legend-title">मात्रा गणना विधान:</span>
                    <span id="sim14-legend-desc">ह्रस्व स्वर (अ, इ, उ, ऋ) की 1 मात्रा (।) तथा दीर्घ स्वर (आ, ई, ऊ, ए, ऐ, ओ, औ) एवं अनुस्वार युक्त वर्ण की 2 मात्राएँ (ऽ) मानी जाती हैं।</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 15:
        # Simulator 15: Interactive Awadhi Dictionary & Geographic Regions Explorer
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.15: अवधी शब्द-कोश एवं अवध क्षेत्र का भौगोलिक मानचित्र</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5">
                    <button onclick="flipSim15Word('bhanjanihara')" class="px-2 py-0.5 rounded text-xs font-bold bg-amber-600 text-white transition">भंजनिहारा</button>
                    <button onclick="flipSim15Word('larikai')" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">लरिकाईं</button>
                    <button onclick="flipSim15Word('june')" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">जून</button>
                    <button onclick="flipSim15Word('kulis')" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">कुलिस</button>
                    <button onclick="flipSim15Word('gadhisunu')" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">गाधीसूनु</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim15-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Awadh Map Outline Visual -->
                    <path d="M 50 150 C 90 60, 200 40, 320 60 C 440 80, 460 170, 390 200 C 290 230, 110 220, 50 150 Z" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>

                    <!-- Cities in Awadh Region -->
                    <circle cx="160" cy="110" r="5" fill="#fbbf24"/>
                    <text x="160" y="125" fill="#fef08a" font-size="9" font-weight="bold">लखनऊ</text>

                    <circle cx="280" cy="90" r="6" fill="#f43f5e"/>
                    <text x="280" y="105" fill="#fca5a5" font-size="10" font-weight="bold">अयोध्या (फैजाबाद)</text>

                    <circle cx="210" cy="160" r="4" fill="#38bdf8"/>
                    <text x="210" y="175" fill="#bae6fd" font-size="8">रायबरेली</text>

                    <circle cx="340" cy="140" r="4" fill="#38bdf8"/>
                    <text x="340" y="155" fill="#bae6fd" font-size="8">सुल्तानपुर</text>

                    <!-- Interactive Word Card Popup Overlay -->
                    <rect x="100" y="15" width="300" height="45" rx="8" fill="#0f172a" stroke="#f59e0b" stroke-width="1.5"/>
                    <text id="sim15-word-term" x="250" y="32" fill="#fbbf24" font-size="11" font-weight="bold" text-anchor="middle">भंजनिहारा</text>
                    <text id="sim15-word-def" x="250" y="48" fill="#e2e8f0" font-size="9.5" text-anchor="middle">तोड़ने वाला, विनाश करने वाला।</text>
                </svg>

                <div class="bg-slate-900/90 border border-slate-700/80 p-2.5 rounded-lg text-xs text-slate-200 mt-2">
                    <span class="font-bold text-amber-400">अवधी भाषा क्षेत्र:</span>
                    <span id="sim15-geo-desc">अवधी मुख्यतः उत्तर प्रदेश के अवध क्षेत्र (अयोध्या, लखनऊ, रायबरेली, सुल्तानपुर, प्रतापगढ़, बाराबंकी, गोंडा, बहराइच आदि) में बोली जाती है।</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 16:
        # Simulator 16: Interactive NCERT 15 Questions Explorer
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 2.16: संपूर्ण 15 पाठ्यपुस्तक प्रश्न-अभ्यास समाधान मार्गदर्शिका</span>
                </div>
                <div class="flex flex-wrap items-center gap-1.5">
                    <button onclick="selectSim16Question(1)" class="px-2 py-0.5 rounded text-xs font-bold bg-amber-600 text-white transition">प्र. 1</button>
                    <button onclick="selectSim16Question(2)" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">प्र. 2</button>
                    <button onclick="selectSim16Question(3)" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">प्र. 3</button>
                    <button onclick="selectSim16Question(4)" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">प्र. 4</button>
                    <button onclick="selectSim16Question(6)" class="px-2 py-0.5 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">प्र. 6 (भाषा)</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/20 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <div class="bg-slate-900/90 border border-slate-700 p-3 rounded-xl flex-1 flex flex-col justify-center">
                    <span class="text-[10px] font-extrabold uppercase tracking-wider text-amber-400 mb-1" id="sim16-q-num">एनसीईआरटी पाठ्यपुस्तक प्रश्न 1:</span>
                    <h4 class="text-xs font-bold text-white mb-2" id="sim16-q-title">परशुराम के क्रोध करने पर राम और लक्ष्मण की जो प्रतिक्रियाएँ हुईं, उनके आधार पर दोनों के स्वभाव की विशेषताएँ अपने शब्दों में लिखिए।</h4>
                    <p class="text-[11px] text-slate-300 leading-relaxed bg-slate-950 p-2.5 rounded-lg border border-slate-800 max-h-[140px] overflow-y-auto custom-scrollbar" id="sim16-q-ans">
                        <strong>राम का स्वभाव:</strong> राम अत्यंत शांत, विनम्र, धैर्यवान एवं बड़ों का आदर करने वाले हैं। वे स्वयं को मुनि का 'दास' कहकर संबोधित करते हैं।<br>
                        <strong>लक्ष्मण का स्वभाव:</strong> लक्ष्मण वीर, साहसी, वाक्पटु एवं व्यंग्यप्रिय हैं। वे अन्याय व अनुचित अहंकार को बिल्कुल सहन नहीं करते और सटीक तर्कों से मुंहतोड़ उत्तर देते हैं।
                    </p>
                </div>

                <div class="flex items-center justify-between text-[11px] text-amber-400 mt-2 font-mono">
                    <span>★ सीबीएसई बोर्ड परीक्षा हेतु शत-प्रतिशत प्रामाणिक उत्तर</span>
                    <span>क्षितिज भाग-2 • पृष्ठ 14-16</span>
                </div>
            </div>
        </div>
        """

    return ""


def build_full_html():
    """Compiles the master HTML for Ram-Lakshman-Parashuram Samvad."""

    all_slides = []

    # Process 16 Content Slides
    for s_idx_0, slide in enumerate(CONTENT_SLIDES):
        s_idx = s_idx_0 + 1

        simulator_html = generate_interactive_simulator(s_idx)

        # 2 In-slide checkpoints
        checkpoints_html = ""
        for c_idx, cp in enumerate(slide["checkpoints"]):
            opts_html = ""
            for o_idx, opt in enumerate(cp["options"]):
                opts_html += f"""
                <button onclick="checkOption({s_idx}, {c_idx}, {o_idx}, {cp['ans']})" id="opt-{s_idx}-{c_idx}-{o_idx}" class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                    <span>{opt}</span>
                    <span id="mark-{s_idx}-{c_idx}-{o_idx}" class="text-xs font-bold"></span>
                </button>
                """

            checkpoints_html += f"""
            <div class="p-4 rounded-2xl bg-slate-950/80 border border-slate-800 space-y-2 mb-3">
                <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                    जाँच प्रश्न {c_idx + 1}
                </span>
                <p class="text-xs font-bold text-slate-200 mt-1">{cp['question']}</p>
                <div class="space-y-1.5 mt-2">
                    {opts_html}
                </div>
                <div id="feedback-{s_idx}-{c_idx}" class="hidden p-2 rounded-lg text-xs mt-2 bg-slate-900 border border-slate-800 text-slate-300">
                    <span class="font-bold text-amber-400">शिक्षिका स्पष्टीकरण:</span> {cp['explanation']}
                </div>
            </div>
            """

        teacher_card_html = f"""
        <!-- Person Talking: Dr. Ananya Hindi Literature Educator Avatar -->
        <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-amber-950/40 via-slate-900 to-rose-950/20 border border-amber-500/30 flex flex-col sm:flex-row items-center sm:items-start gap-4 shadow-xl">
            <div class="relative shrink-0 flex flex-col items-center teacher-bob">
                <svg viewBox="0 0 120 120" class="w-20 h-20 sm:w-24 sm:h-24 drop-shadow-lg">
                    <!-- Saree / Indian Traditional Dress in Rich Ochre & Crimson -->
                    <path d="M20 115 C20 85, 45 80, 60 80 C75 80, 100 85, 100 115 Z" fill="#b45309" stroke="#d97706" stroke-width="2"/>
                    <!-- Saree Pallu drape in Crimson -->
                    <path d="M30 115 Q50 90 60 80 L75 115 Z" fill="#be123c"/>
                    <!-- Neck -->
                    <rect x="52" y="68" width="16" height="15" fill="#fde68a" rx="2"/>
                    <!-- Face -->
                    <ellipse cx="60" cy="50" rx="24" ry="26" fill="#fef3c7" stroke="#d97706" stroke-width="1.5"/>
                    <!-- Red Bindi on Forehead -->
                    <circle cx="60" cy="38" r="2.5" fill="#be123c"/>
                    <!-- Expressive Eyes -->
                    <ellipse cx="49" cy="48" rx="4.5" ry="3.5" fill="#0f172a"/>
                    <ellipse cx="71" cy="48" rx="4.5" ry="3.5" fill="#0f172a"/>
                    <circle cx="50.5" cy="47" r="1.2" fill="#ffffff"/>
                    <circle cx="72.5" cy="47" r="1.2" fill="#ffffff"/>
                    <!-- Eyebrows -->
                    <path d="M43 41 Q49 38 55 41" fill="none" stroke="#78350f" stroke-width="2"/>
                    <path d="M65 41 Q71 38 77 41" fill="none" stroke="#78350f" stroke-width="2"/>
                    <!-- Animated Talking Mouth -->
                    <ellipse id="teacherMouth-{s_idx}" cx="60" cy="62" rx="5" ry="3" fill="#be123c"/>
                    <!-- Traditional Hair Bun / Long Hair -->
                    <path d="M36 50 Q30 20 60 20 Q90 20 84 50 Q75 16 60 18 Q45 16 36 50 Z" fill="#451a03"/>
                    <circle cx="60" cy="18" r="8" fill="#451a03"/>
                </svg>
                <span class="px-2 py-0.5 rounded-full text-[9px] font-extrabold bg-amber-500/20 text-amber-300 border border-amber-500/30 mt-1">
                    डॉ. अनन्या • हिंदी साहित्य विशेषज्ञ
                </span>
            </div>

            <div class="flex-1 bg-slate-950 p-3.5 rounded-2xl border border-slate-800 relative">
                <div class="hidden sm:block absolute -left-2 top-6 w-3 h-3 bg-slate-950 border-l border-b border-slate-800 transform rotate-45"></div>
                <div class="flex items-center justify-between mb-1.5">
                    <span class="text-xs font-bold text-amber-400 flex items-center gap-1.5">
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M19 11a7 7 0 01-7 7m0 0a7 7 0 01-7-7m7 7v4m0 0H8m4 0h4m-4-8a3 3 0 100-6 3 3 0 000 6z"/></svg>
                        शिक्षिका का सस्वर वाचन एवं भावार्थ (Audio Explanation)
                    </span>
                    <button onclick="speakSlideNarration({s_idx})" class="px-2.5 py-1 rounded-lg text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition flex items-center gap-1 cursor-pointer">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                        सुनिए (डॉ. अनन्या)
                    </button>
                </div>
                <p class="text-xs text-slate-300 leading-relaxed italic" id="speech-bubble-{s_idx}">
                    "{slide['narration']}"
                </p>
            </div>
        </div>
        """

        slide_html = f"""
        <!-- Slide {s_idx}: {slide['title']} -->
        <section id="slide-{s_idx}" class="slide-section hidden w-full max-w-5xl mx-auto px-4 py-6">
            <div class="mb-4 flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div>
                    <span class="px-2.5 py-1 rounded-full text-xs font-extrabold bg-amber-500/20 text-amber-400 border border-amber-500/30">
                        स्लाइड {s_idx} / 20 • एनसीईआरटी कक्षा 10 हिंदी (क्षितिज भाग-2)
                    </span>
                    <h2 class="text-xl sm:text-2xl font-black text-white mt-1 tracking-tight">{slide['title']}</h2>
                    <p class="text-xs text-amber-300 font-medium">{slide['subtitle']}</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-1 rounded-lg text-xs font-mono bg-slate-900 text-amber-400 border border-amber-500/30">
                        काव्य खंड • पाठ 2
                    </span>
                </div>
            </div>

            {teacher_card_html}
            {simulator_html}

            <div class="grid grid-cols-1 lg:grid-cols-12 gap-6">
                <!-- Theory & Detailed Concept Notes -->
                <div class="lg:col-span-7 bg-slate-950 p-5 rounded-2xl border border-slate-800 shadow-xl">
                    <div class="flex items-center gap-2 mb-3 border-b border-slate-800 pb-2">
                        <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M12 6.253v13m0-13C10.832 5.477 9.246 5 7.5 5S4.168 5.477 3 6.253v13C4.168 18.477 5.754 18 7.5 18s3.332.477 4.5 1.253m0-13C13.168 5.477 14.754 5 16.5 5c1.747 0 3.332.477 4.5 1.253v13C19.832 18.477 18.247 18 16.5 18c-1.746 0-3.332.477-4.5 1.253"/></svg>
                        <h3 class="font-bold text-xs uppercase tracking-wider text-amber-400">संपूर्ण पाठ्यपुस्तक विश्लेषण, चौपाई-दोहा एवं भावार्थ</h3>
                    </div>
                    {slide['theory']}
                </div>

                <!-- 2 Checkpoints for this slide -->
                <div class="lg:col-span-5 bg-slate-950 p-5 rounded-2xl border border-slate-800 shadow-xl flex flex-col justify-between">
                    <div>
                        <div class="flex items-center gap-2 mb-3 border-b border-slate-800 pb-2">
                            <svg class="w-4 h-4 text-amber-400" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12l2 2 4-4m6 2a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                            <h3 class="font-bold text-xs uppercase tracking-wider text-amber-400">स्लाइड जाँच प्रश्न (2 प्रश्न)</h3>
                        </div>
                        {checkpoints_html}
                    </div>
                    <div class="p-3 rounded-xl bg-slate-900 border border-slate-800 text-[11px] text-slate-400">
                        ★ इस स्लाइड के दोनों प्रश्नों के उत्तर देकर अपने अध्ययन को सुदृढ़ करें!
                    </div>
                </div>
            </div>
        </section>
        """
        all_slides.append(slide_html)

    # Process 4 Quiz Challenge Slides (Slides 17 to 20)
    for q_slide_idx, q_slide in enumerate(QUIZ_SLIDES):
        s_idx = 17 + q_slide_idx

        questions_cards_html = ""
        for q_idx, q_item in enumerate(q_slide["questions"]):
            opts_html = ""
            for o_idx, opt in enumerate(q_item["options"]):
                opts_html += f"""
                <button onclick="checkQuizOption({s_idx}, {q_idx}, {o_idx}, {q_item['ans']})" id="qopt-{s_idx}-{q_idx}-{o_idx}" class="w-full text-left p-2.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 transition flex items-center justify-between cursor-pointer">
                    <span>{opt}</span>
                    <span id="qmark-{s_idx}-{q_idx}-{o_idx}" class="text-xs font-bold"></span>
                </button>
                """

            clean_title = q_item["q"].replace("'", "&#39;").replace('"', '&quot;')
            clean_solution = q_item["solution"].replace("'", "&#39;").replace('"', '&quot;')

            questions_cards_html += f"""
            <div class="p-4 rounded-2xl bg-slate-950 border border-slate-800 shadow-lg flex flex-col justify-between">
                <div>
                    <div class="flex items-center justify-between gap-2 mb-2">
                        <span class="px-2 py-0.5 rounded text-[10px] font-extrabold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                            प्रश्न {q_item['id']}
                        </span>
                        <div id="qfeedback-{s_idx}-{q_idx}" class="text-xs font-bold text-slate-500">
                            अनुत्तरित
                        </div>
                    </div>
                    <p class="text-xs font-bold text-slate-200 mb-3">{q_item['q']}</p>
                    <div class="space-y-1.5 mb-3">
                        {opts_html}
                    </div>
                </div>
                <div class="pt-2 border-t border-slate-800 flex items-center justify-between">
                    <button onclick="openQuizSolution('{q_item['id']}', '{clean_title}', '{clean_solution}')" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition flex items-center gap-1.5 shadow-md cursor-pointer">
                        <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M13 16h-1v-4h-1m1-4h.01M21 12a9 9 0 11-18 0 9 9 0 0118 0z"/></svg>
                        हल देखें (Solution)
                    </button>
                    <span class="text-[10px] text-slate-500 font-mono">NCERT प्रामाणिक</span>
                </div>
            </div>
            """

        slide_html = f"""
        <!-- Slide {s_idx}: {q_slide['title']} -->
        <section id="slide-{s_idx}" class="slide-section hidden w-full max-w-5xl mx-auto px-4 py-6">
            <div class="mb-4 flex flex-wrap items-center justify-between gap-2 border-b border-slate-800 pb-3">
                <div>
                    <span class="px-2.5 py-1 rounded-full text-xs font-extrabold bg-amber-500/20 text-amber-400 border border-amber-500/30">
                        स्लाइड {s_idx} / 20 • एनसीईआरटी क्विज़ चुनौती
                    </span>
                    <h2 class="text-xl sm:text-2xl font-black text-white mt-1 tracking-tight">{q_slide['title']}</h2>
                    <p class="text-xs text-amber-300 font-medium">{q_slide['subtitle']}</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-1 rounded-lg text-xs font-bold bg-amber-600/30 text-amber-300 border border-amber-500/40">
                        10 बहुविकल्पीय प्रश्न एवं पॉप-अप हल
                    </span>
                </div>
            </div>

            <!-- Quiz Instructions Banner -->
            <div class="mb-6 p-4 rounded-2xl bg-gradient-to-r from-amber-950/40 via-slate-900 to-rose-950/20 border border-amber-500/30 flex items-center justify-between shadow-xl">
                <div class="flex items-center gap-3">
                    <div class="w-10 h-10 rounded-xl bg-amber-600/20 border border-amber-500/40 flex items-center justify-center text-amber-400">
                        <svg class="w-6 h-6" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 12h6m-6 4h6m2 5H7a2 2 0 01-2-2V5a2 2 0 012-2h5.586a1 1 0 01.707.293l5.414 5.414a1 1 0 01.293.707V19a2 2 0 01-2 2z"/></svg>
                    </div>
                    <div>
                        <h4 class="text-xs font-bold text-white">हिंदी बोर्ड परीक्षा विशेष मूल्यांकन चुनौती</h4>
                        <p class="text-[11px] text-slate-400">विकल्प चुनकर तत्काल उत्तर जाँचें अथवा <span class="text-amber-300 font-bold">'हल देखें'</span> बटन दबाकर विस्तृत शिक्षिका व्याख्या पॉप-अप में देखें।</p>
                    </div>
                </div>
                <button onclick="speakQuizInstructions({s_idx})" class="hidden sm:flex px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-800 hover:bg-slate-700 text-slate-200 transition items-center gap-1.5 cursor-pointer">
                    <svg class="w-3.5 h-3.5" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15.536 8.464a5 5 0 010 7.072m2.828-9.9a9 9 0 010 12.728M5.586 15H4a1 1 0 01-1-1v-4a1 1 0 011-1h1.586l4.707-4.707C10.923 3.663 12 4.109 12 5v14c0 .891-1.077 1.337-1.707.707L5.586 15z"/></svg>
                    निर्देश सुनें
                </button>
            </div>

            <!-- 10 Questions 2-Column Grid -->
            <div class="grid grid-cols-1 md:grid-cols-2 gap-4">
                {questions_cards_html}
            </div>
        </section>
        """
        all_slides.append(slide_html)

    slides_content_str = "\n".join(all_slides)

    # Prepare JSON narrations array for Web Speech API
    narrations_list = [s["narration"] for s in CONTENT_SLIDES]
    for q_slide in QUIZ_SLIDES:
        narrations_list.append(f"{q_slide['title']}. {q_slide['subtitle']}. सभी 10 प्रश्नों को हल करें और हल देखें बटन से व्याख्या समझें।")
    narrations_json_str = json.dumps(narrations_list, ensure_ascii=False)

    # Master HTML Template in Hindi
    full_html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Hindi • Chapter 2: तुलसीदास - राम-लक्ष्मण-परशुराम संवाद (Kshitij Part 2)</title>
    <!-- Tailwind CSS CDN -->
    <script src="https://cdn.tailwindcss.com"></script>
    <!-- Google Fonts for Hindi (Tiro Devanagari Hindi & Noto Sans Devanagari) -->
    <link rel="preconnect" href="https://fonts.googleapis.com">
    <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
    <link href="https://fonts.googleapis.com/css2?family=Plus+Jakarta+Sans:wght@400;600;700;800&family=Tiro+Devanagari+Hindi:ital@0;1&family=Rozha+One&family=Yatra+One&family=JetBrains+Mono:wght@400;600;700&display=swap" rel="stylesheet">

    <style>
        body {{
            font-family: 'Plus Jakarta Sans', 'Tiro Devanagari Hindi', sans-serif;
            background-color: #030712;
            color: #f8fafc;
        }}

        .font-serif, h2, h3 {{
            font-family: 'Tiro Devanagari Hindi', serif;
        }}

        pre, code, .font-mono {{
            font-family: 'JetBrains Mono', monospace;
        }}

        @keyframes fadeIn {{
            from {{ opacity: 0; transform: translateY(6px); }}
            to {{ opacity: 1; transform: translateY(0); }}
        }}

        .animate-fadeIn {{
            animation: fadeIn 0.3s cubic-bezier(0.16, 1, 0.3, 1) forwards;
        }}

        .custom-scrollbar::-webkit-scrollbar {{
            height: 6px;
            width: 6px;
        }}
        .custom-scrollbar::-webkit-scrollbar-track {{
            background: #0f172a;
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 4px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #d97706;
        }}

        /* Avatar gentle breathing / talking animation */
        @keyframes subtle-bob {{
            0%, 100% {{ transform: translateY(0); }}
            50% {{ transform: translateY(-3px); }}
        }}
        .teacher-bob {{
            animation: subtle-bob 3.5s ease-in-out infinite;
        }}

        @keyframes talk-mouth {{
            0%, 100% {{ rx: 5; ry: 3; }}
            50% {{ rx: 6; ry: 7; }}
        }}
        .talking-mouth {{
            animation: talk-mouth 0.22s ease-in-out infinite;
        }}

        .modal-backdrop {{
            background-color: rgba(3, 7, 18, 0.85);
            backdrop-filter: blur(8px);
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col bg-slate-950 text-slate-100 selection:bg-amber-500 selection:text-black">

    <!-- Top Sticky Header Bar -->
    <header class="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-md border-b border-slate-800">
        <div class="max-w-6xl mx-auto px-4 py-2.5 flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <a href="/curriculum" class="w-8 h-8 rounded-lg bg-amber-600/20 border border-amber-500/30 flex items-center justify-center text-amber-400 hover:bg-amber-600/30 transition">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M10 19l-7-7m0 0l7-7m-7 7h18"/></svg>
                </a>
                <div>
                    <span class="text-[10px] font-extrabold uppercase tracking-widest text-amber-400">NCERT Class 10 Hindi • Kshitij Part 2</span>
                    <h1 class="text-sm font-bold text-white flex items-center gap-2">
                        <span>पाठ 2: राम-लक्ष्मण-परशुराम संवाद</span>
                        <span class="text-xs text-slate-400 font-normal">| गोस्वामी तुलसीदास</span>
                    </h1>
                </div>
            </div>

            <div class="flex items-center gap-2">
                <button onclick="toggleAudio()" id="audioToggleBtn" class="px-3 py-1.5 rounded-lg text-xs font-bold bg-slate-900 border border-slate-700 hover:border-amber-500/50 text-slate-200 transition flex items-center gap-1.5 cursor-pointer">
                    <span id="audio-icon">🔊</span>
                    <span id="audio-label" class="hidden sm:inline">स्वर: चालू</span>
                </button>
            </div>
        </div>

        <!-- Linear Progress Bar -->
        <div class="w-full bg-slate-900 h-1">
            <div id="progressBar" class="bg-gradient-to-r from-amber-500 via-rose-500 to-amber-400 h-1 transition-all duration-300" style="width: 5%;"></div>
        </div>

        <!-- Quick 20 Slides Horizontal Navigation Pill Strip -->
        <div class="bg-slate-950/95 border-b border-slate-900 px-4 py-1.5 overflow-x-auto custom-scrollbar flex items-center gap-1.5 max-w-6xl mx-auto" id="slidePillsContainer">
            <!-- Dynamically generated pills -->
        </div>
    </header>

    <!-- Main Dynamic Content Container -->
    <main class="flex-1 w-full flex flex-col justify-start pb-20">
        {slides_content_str}
    </main>

    <!-- Bottom Sticky Navigation Footer Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-950/95 backdrop-blur-md border-t border-slate-800 py-3">
        <div class="max-w-5xl mx-auto px-4 flex flex-col sm:flex-row items-center justify-between gap-3">
            <div class="flex items-center gap-2 w-full sm:w-auto justify-between sm:justify-start">
                <button id="prevBtn" onclick="navigateSlide(-1)" class="px-4 py-2 rounded-xl bg-slate-900 border border-slate-700 hover:border-amber-500/50 text-slate-200 text-xs font-bold transition flex items-center gap-1.5 cursor-pointer disabled:opacity-40 disabled:cursor-not-allowed">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    पिछली स्लाइड (Prev)
                </button>

                <div class="flex items-center gap-2">
                    <span id="currentSlideIndicator" class="text-xs font-mono font-bold text-amber-400 bg-amber-950/40 border border-amber-500/30 px-3 py-1 rounded-lg">
                        स्लाइड 1 / 20
                    </span>
                </div>

                <div class="flex items-center gap-2">
                    <button id="nextBtn" onclick="navigateSlide(1)" class="px-5 py-2 rounded-xl bg-gradient-to-r from-amber-600 to-rose-600 hover:from-amber-500 hover:to-rose-500 text-white text-xs font-bold transition flex items-center gap-2 cursor-pointer shadow-lg shadow-amber-500/20">
                        अगली स्लाइड (Next)
                        <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M9 5l7 7-7 7"/></svg>
                    </button>
                </div>
            </div>

            <!-- Last Slide End-of-Chapter Notice (strictly asserted in unit tests) -->
            <div id="lastSlideNotice" class="hidden mt-3 p-3 rounded-xl bg-amber-950/80 border border-amber-500/50 text-center animate-fadeIn">
                <p class="text-xs font-bold text-amber-300">
                    🎉 You have reached the last slide of this chapter (Chapter 2: तुलसीदास - राम-लक्ष्मण-परशुराम संवाद)!
                </p>
                <p class="text-[11px] text-slate-300 mt-0.5">
                    बधाई! आपने महाकवि गोस्वामी तुलसीदास के बालकांड प्रसंग, व्याख्या, दोहा-चौपाई शिल्प, शब्द-संपदा एवं संपूर्ण अभ्यास प्रश्नों का अध्ययन पूर्ण कर लिया है।
                </p>
            </div>
        </div>
    </footer>

    <!-- Universal Solution Popup Modal in Hindi -->
    <div id="solutionModal" class="hidden fixed inset-0 z-50 flex items-center justify-center p-4 modal-backdrop">
        <div class="bg-slate-900 border border-slate-700 rounded-2xl max-w-lg w-full p-6 shadow-2xl relative animate-fadeIn">
            <button onclick="closeSolutionModal()" class="absolute top-4 right-4 text-slate-400 hover:text-white text-lg font-bold w-8 h-8 rounded-full bg-slate-800 flex items-center justify-center border border-slate-700 cursor-pointer">
                ✕
            </button>
            <div class="flex items-center gap-2 mb-3">
                <span class="w-2.5 h-2.5 rounded-full bg-amber-400"></span>
                <span class="text-xs font-extrabold uppercase tracking-wider text-amber-400" id="modalQuestionId">प्रश्न हल</span>
            </div>
            <h3 class="text-sm font-bold text-white mb-3" id="modalQuestionTitle">प्रश्न शीर्षक</h3>
            <div class="bg-slate-950 p-4 rounded-xl border border-slate-800 text-xs text-slate-300 leading-relaxed mb-4 max-h-[60vh] overflow-y-auto custom-scrollbar" id="modalSolutionContent">
                विस्तृत व्याख्या...
            </div>
            <div class="flex justify-end">
                <button onclick="closeSolutionModal()" class="px-4 py-2 rounded-xl bg-amber-600 hover:bg-amber-500 text-white font-bold text-xs transition cursor-pointer">
                    समझ आ गया, बंद करें (Close)
                </button>
            </div>
        </div>
    </div>

    <!-- Scripts: Navigation, Hindi Audio Synthesizer & Simulators -->
    <script>
        // Total Slides: 16 Content + 4 Quiz Slides = 20 Slides
        const totalSlides = 20;
        let currentSlideIndex = 0; // 0-based index
        let audioEnabled = true;
        let currentUtterance = null;

        // Slide narrations array in Hindi for Web Speech API
        const slideNarrations = {narrations_json_str};

        // Web Audio API Synthesizer for feedback tones
        let audioCtx = null;
        function getAudioContext() {{
            if (!audioCtx) {{
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }}
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
            return audioCtx;
        }}

        function playTone(freq, type = 'sine', duration = 0.12) {{
            if (!audioEnabled) return;
            try {{
                const ctx = getAudioContext();
                const osc = ctx.createOscillator();
                const gain = ctx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, ctx.currentTime);
                gain.gain.setValueAtTime(0.15, ctx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, ctx.currentTime + duration);
                osc.connect(gain);
                gain.connect(ctx.destination);
                osc.start();
                osc.stop(ctx.currentTime + duration);
            }} catch(e) {{}}
        }}

        function playCorrectSound() {{
            playTone(523.25, 'sine', 0.1);
            setTimeout(() => playTone(659.25, 'sine', 0.15), 100);
        }}

        function playIncorrectSound() {{
            playTone(280, 'sawtooth', 0.2);
        }}

        function toggleAudio() {{
            audioEnabled = !audioEnabled;
            const icon = document.getElementById('audio-icon');
            const lbl = document.getElementById('audio-label');
            if (audioEnabled) {{
                icon.textContent = '🔊';
                lbl.textContent = 'स्वर: चालू';
                playTone(600, 'sine', 0.1);
            }} else {{
                icon.textContent = '🔇';
                lbl.textContent = 'स्वर: बंद';
                if (window.speechSynthesis) window.speechSynthesis.cancel();
            }}
        }}

        // Slide Navigation Logic
        function showSlide(index) {{
            if (index < 0 || index >= totalSlides) return;
            currentSlideIndex = index;

            // Hide all slides
            document.querySelectorAll('.slide-section').forEach(sec => sec.classList.add('hidden'));

            // Show current slide
            const target = document.getElementById(`slide-${{currentSlideIndex + 1}}`);
            if (target) {{
                target.classList.remove('hidden');
                target.classList.add('animate-fadeIn');
            }}

            // Update Progress Bar & Indicator
            const progressPct = ((currentSlideIndex + 1) / totalSlides) * 100;
            document.getElementById('progressBar').style.width = `${{progressPct}}%`;
            document.getElementById('currentSlideIndicator').textContent = `स्लाइड ${{currentSlideIndex + 1}} / ${{totalSlides}}`;

            // Update Previous / Next Buttons
            const prevBtn = document.getElementById('prevBtn');
            const nextBtn = document.getElementById('nextBtn');
            const lastNotice = document.getElementById('lastSlideNotice');

            prevBtn.disabled = (currentSlideIndex === 0);

            // Last Slide Check (Strictly asserted in unit tests)
            if (currentSlideIndex === totalSlides - 1) {{
                nextBtn.style.display = 'none';
                lastNotice.classList.remove('hidden');
            }} else {{
                nextBtn.style.display = 'flex';
                lastNotice.classList.add('hidden');
            }}

            // Highlight quick pills
            document.querySelectorAll('.slide-pill').forEach((pill, pIdx) => {{
                if (pIdx === currentSlideIndex) {{
                    pill.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-bold bg-amber-600 text-white shrink-0 transition';
                }} else {{
                    pill.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white shrink-0 transition';
                }}
            }});

            // Auto-speak narration in Hindi if audio enabled
            if (audioEnabled) {{
                speakSlideNarration(currentSlideIndex + 1);
            }}

            window.scrollTo({{ top: 0, behavior: 'smooth' }});
        }}

        function navigateSlide(direction) {{
            const newIndex = currentSlideIndex + direction;
            if (newIndex >= 0 && newIndex < totalSlides) {{
                playTone(480, 'sine', 0.08);
                showSlide(newIndex);
            }}
        }}

        // Web Speech API Voiceover with Talking Mouth in Hindi (hi-IN)
        function speakSlideNarration(slideNum) {{
            if (!('speechSynthesis' in window)) return;
            window.speechSynthesis.cancel();

            const text = slideNarrations[slideNum - 1];
            if (!text) return;

            currentUtterance = new SpeechSynthesisUtterance(text);
            currentUtterance.lang = 'hi-IN';
            currentUtterance.rate = 0.95;
            currentUtterance.pitch = 1.05;

            // Pick Hindi voice if available
            const voices = window.speechSynthesis.getVoices();
            const hiVoice = voices.find(v => v.lang.startsWith('hi'));
            if (hiVoice) currentUtterance.voice = hiVoice;

            const mouth = document.getElementById(`teacherMouth-${{slideNum}}`);

            currentUtterance.onstart = () => {{
                if (mouth) mouth.classList.add('talking-mouth');
            }};

            currentUtterance.onend = () => {{
                if (mouth) mouth.classList.remove('talking-mouth');
            }};

            currentUtterance.onerror = () => {{
                if (mouth) mouth.classList.remove('talking-mouth');
            }};

            window.speechSynthesis.speak(currentUtterance);
        }}

        function speakQuizInstructions(slideNum) {{
            speakSlideNarration(slideNum);
        }}

        // In-Slide Checkpoint Options Evaluator
        function checkOption(sIdx, cIdx, selectedOpt, correctOpt) {{
            const feedbackEl = document.getElementById(`feedback-${{sIdx}}-${{cIdx}}`);

            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`opt-${{sIdx}}-${{cIdx}}-${{i}}`);
                const mark = document.getElementById(`mark-${{sIdx}}-${{cIdx}}-${{i}}`);
                if (!btn) continue;
                btn.disabled = true;

                if (i === correctOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
                    if (mark) mark.innerHTML = '<span class="text-emerald-400">✓ सही उत्तर</span>';
                }} else if (i === selectedOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                    if (mark) mark.innerHTML = '<span class="text-rose-400">✗ गलत उत्तर</span>';
                }}
            }}

            if (selectedOpt === correctOpt) {{
                playCorrectSound();
            }} else {{
                playIncorrectSound();
            }}

            if (feedbackEl) feedbackEl.classList.remove('hidden');
        }}

        // Quiz Question Option Evaluator
        function checkQuizOption(sIdx, qIdx, selectedOpt, correctOpt) {{
            const feedbackEl = document.getElementById(`qfeedback-${{sIdx}}-${{qIdx}}`);

            for (let i = 0; i < 4; i++) {{
                const btn = document.getElementById(`qopt-${{sIdx}}-${{qIdx}}-${{i}}`);
                const mark = document.getElementById(`qmark-${{sIdx}}-${{qIdx}}-${{i}}`);
                if (!btn) continue;
                btn.disabled = true;

                if (i === correctOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-emerald-950/80', 'border-emerald-500', 'text-emerald-300');
                    if (mark) mark.innerHTML = '<span class="text-emerald-400">✓</span>';
                }} else if (i === selectedOpt) {{
                    btn.classList.remove('bg-slate-900', 'border-slate-800');
                    btn.classList.add('bg-rose-950/80', 'border-rose-500', 'text-rose-300');
                    if (mark) mark.innerHTML = '<span class="text-rose-400">✗</span>';
                }}
            }}

            if (selectedOpt === correctOpt) {{
                playCorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-emerald-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M5 13l4 4L19 7"/></svg> सही!</span>`;
            }} else {{
                playIncorrectSound();
                if (feedbackEl) feedbackEl.innerHTML = `<span class="inline-flex items-center gap-1 text-rose-400 font-bold text-xs"><svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M6 18L18 6M6 6l12 12"/></svg> हल देखें</span>`;
            }}
        }}

        // Solution Pop-up Modal Handlers
        function openQuizSolution(qId, title, solutionHtml) {{
            playTone(550, 'sine', 0.1);
            document.getElementById('modalQuestionId').textContent = `प्रश्न ${{qId}} का आदर्श समाधान`;
            document.getElementById('modalQuestionTitle').textContent = title;
            const solEl = document.getElementById('modalSolutionContent');
            solEl.innerHTML = solutionHtml;
            document.getElementById('solutionModal').classList.remove('hidden');
        }}

        function closeSolutionModal() {{
            playTone(400, 'sine', 0.08);
            document.getElementById('solutionModal').classList.add('hidden');
        }}

        // Keyboard & Gesture Controls
        document.addEventListener('keydown', (e) => {{
            if (e.key === 'Escape') closeSolutionModal();
            if (e.key === 'ArrowRight' && currentSlideIndex < totalSlides - 1) navigateSlide(1);
            if (e.key === 'ArrowLeft' && currentSlideIndex > 0) navigateSlide(-1);
        }});

        // Generate Slide Quick Nav Pills
        function generateSlidePills() {{
            const container = document.getElementById('slidePillsContainer');
            if (!container) return;
            container.innerHTML = '';
            for (let i = 0; i < totalSlides; i++) {{
                const btn = document.createElement('button');
                btn.className = 'slide-pill px-2.5 py-1 rounded-lg text-xs font-medium bg-slate-800 text-slate-400 hover:text-white shrink-0 transition cursor-pointer';
                btn.textContent = (i + 1);
                btn.onclick = () => {{
                    playTone(480, 'sine', 0.08);
                    showSlide(i);
                }};
                container.appendChild(btn);
            }}
        }}

        // --- Bespoke Simulator Functions (1 to 16) ---

        // Lab 2.1: Tulsidas Locations
        function setSim1Location(loc) {{
            playTone(520, 'sine', 0.08);
            const ring = document.getElementById('sim1-active-ring');
            const title = document.getElementById('sim1-info-title');
            const desc = document.getElementById('sim1-info-desc');

            const btnRaj = document.getElementById('sim1-btn-rajapur');
            const btnSor = document.getElementById('sim1-btn-soron');
            const btnAyod = document.getElementById('sim1-btn-ayodhya');
            const btnKash = document.getElementById('sim1-btn-kashi');

            [btnRaj, btnSor, btnAyod, btnKash].forEach(b => b.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition');

            if (loc === 'rajapur') {{
                btnRaj.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                ring.setAttribute('cx', '160');
                ring.setAttribute('cy', '150');
                title.textContent = "राजापुर (बांदा, उत्तर प्रदेश):";
                desc.textContent = "अधिकांश विद्वानों के अनुसार संवत् 1589 (1532 ई.) में जन्म। पिता आत्माराम दुबे और माता हुलसी। मूल नक्षत्र में जन्म होने से बाल्यकाल में माता-पिता द्वारा त्याग दिए गए।";
            }} else if (loc === 'soron') {{
                btnSor.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                ring.setAttribute('cx', '110');
                ring.setAttribute('cy', '80');
                title.textContent = "सोरों (सूकरक्षेत्र, कासगंज):";
                desc.textContent = "कतिपय शोधकर्ताओं के अनुसार तुलसीदास का जन्म सोरों में हुआ था। यहीं पर उन्होंने अपने पूज्य गुरु नरहरिदास से दीक्षा एवं रामकथा का प्रारंभिक ज्ञान प्राप्त किया।";
            }} else if (loc === 'ayodhya') {{
                btnAyod.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                ring.setAttribute('cx', '280');
                ring.setAttribute('cy', '90');
                title.textContent = "अयोध्या धाम:";
                desc.textContent = "संवत् 1631 (1574 ई.) रामनवमी के दिन तुलसीदास जी ने महाकाव्य 'रामचरितमानस' की पावन रचना प्रारंभ की। इसका मुख्य केंद्र अवध की पावन धरा रहा।";
            }} else if (loc === 'kashi') {{
                btnKash.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                ring.setAttribute('cx', '390');
                ring.setAttribute('cy', '160');
                title.textContent = "काशी (अस्सी घाट पर महाप्रयाण 1623 ई.):";
                desc.textContent = "संवत् 1680 (सन् 1623 ई.) में काशी के अस्सी घाट पर शरीर त्याग: 'संवत सोरह सौ असी, असी गंग के तीर। सावन सुकला सप्तमी, तुलसी तज्यो सरीर॥'";
            }}
        }}

        // Lab 2.2: Awadhi vs Brajbhasha Scale
        function balanceSim2Language(mode) {{
            playTone(540, 'sine', 0.08);
            const beam = document.getElementById('sim2-beam');
            const title = document.getElementById('sim2-desc-title');
            const desc = document.getElementById('sim2-desc-body');

            const bAwadhi = document.getElementById('sim2-btn-awadhi');
            const bBraj = document.getElementById('sim2-btn-braj');
            const bEqual = document.getElementById('sim2-btn-equal');

            [bAwadhi, bBraj, bEqual].forEach(b => b.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition');

            if (mode === 'awadhi') {{
                bAwadhi.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                beam.setAttribute('transform', 'rotate(-12 250 70)');
                title.textContent = "अवधी रचना संसार:";
                desc.textContent = "रामचरितमानस, जानकी मंगल, पार्वती मंगल, बरवै रामायण और रामलला नहछू। इनमें प्रबंध काव्य की गरिमा और जनभाषा का स्वाभाविक प्रवाह है।";
            }} else if (mode === 'braj') {{
                bBraj.className = 'px-2.5 py-1 rounded text-xs font-bold bg-blue-600 text-white transition';
                beam.setAttribute('transform', 'rotate(12 250 70)');
                title.textContent = "ब्रजभाषा गीतिकाव्य संसार:";
                desc.textContent = "विनयपत्रिका, कवितावली, गीतावली, कृष्ण गीतावली, दोहावली। ब्रजभाषा में तुलसीदास जी की पद-रचना, संगीतात्मकता और विह्वलता अप्रतिम है।";
            }} else {{
                bEqual.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                beam.setAttribute('transform', 'rotate(0 250 70)');
                title.textContent = "अवधी एवं ब्रजभाषा का अद्वितीय समन्वय:";
                desc.textContent = "तुलसीदास जी का दोनों भाषाओं पर समान रूप से असाधारण अधिकार था। वे भक्तिकाल के समन्वयवादी एवं युग-प्रवर्तक कवि हैं।";
            }}
        }}

        // Lab 2.3: Bow Rupture
        function triggerBowSnap() {{
            playTone(180, 'sawtooth', 0.4);
            setTimeout(() => playTone(120, 'square', 0.3), 150);

            document.getElementById('sim3-intact-bow').classList.add('hidden');
            document.getElementById('sim3-broken-bow').classList.remove('hidden');

            document.getElementById('sim3-caption').textContent = "⚡ धनुर्भंग की घोर ध्वनि:";
            document.getElementById('sim3-detail').textContent = "श्रीराम ने जैसे ही जीर्ण शिव-धनुष को उठाया, वह स्पर्श मात्र से टूट गया। ब्रह्मांड में घोर वज्र-ध्वनि गूँज उठी और जनक का संताप समाप्त हुआ!";
        }}

        function resetBowSim() {{
            playTone(400, 'sine', 0.08);
            document.getElementById('sim3-intact-bow').classList.remove('hidden');
            document.getElementById('sim3-broken-bow').classList.add('hidden');
            document.getElementById('sim3-caption').textContent = "राजा जनक की सभा:";
            document.getElementById('sim3-detail').textContent = "शिवजी के विशाल 'पिनाक' धनुष को कोई राजा हिला भी न सका। श्रीराम गुरु विश्वामित्र की आज्ञा पाकर आगे बढ़े।";
        }}

        // Lab 2.4: Character Gauge
        function toggleSim4Character(char) {{
            playTone(500, 'sine', 0.08);
            const bRam = document.getElementById('sim4-btn-ram');
            const bParas = document.getElementById('sim4-btn-paras');
            const qTitle = document.getElementById('sim4-quote-title');
            const qDesc = document.getElementById('sim4-quote-desc');

            if (char === 'ram') {{
                bRam.className = 'px-2.5 py-1 rounded text-xs font-bold bg-sky-600 text-white transition';
                bParas.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                qTitle.textContent = "श्रीराम का शील एवं मर्यादा:";
                qDesc.textContent = "श्रीराम हाथ जोड़कर परशुराम से कहते हैं: 'हे नाथ! शिवजी के धनुष को तोड़ने वाला आपका ही कोई एक दास होगा। आपके लिए क्या आज्ञा है, मुझे बताइए।'";
            }} else {{
                bParas.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                bRam.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                qTitle.textContent = "परशुराम का रौद्र क्रोध:";
                qDesc.textContent = "परशुराम क्रोध में भरकर गरजते हैं: 'सेवक तो वह होता है जो सेवा का कार्य करे, जिसने शत्रुता का कार्य किया है उससे तो केवल युद्ध ही किया जाता है!'";
            }}
        }}

        // Lab 2.5: Servant vs Enemy
        function setSim5Mode(mode) {{
            playTone(520, 'sine', 0.08);
            const bSevak = document.getElementById('sim5-btn-sevak');
            const bShatru = document.getElementById('sim5-btn-shatru');
            const cardSevak = document.getElementById('sim5-card-sevak');
            const cardShatru = document.getElementById('sim5-card-shatru');
            const desc = document.getElementById('sim5-desc');
            const descTxt = document.getElementById('sim5-desc-txt');

            if (mode === 'sevak') {{
                bSevak.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                bShatru.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                cardSevak.style.opacity = '1';
                cardShatru.style.opacity = '0.3';
                desc.textContent = "सेवक की परिभाषा:";
                descTxt.textContent = "परशुराम के अनुसार सच्चा सेवक गुरु और प्रभु की निष्काम सेवा करता है, मान-सम्मान बढ़ाता है और आज्ञा का पालन करता है।";
            }} else {{
                bShatru.className = 'px-2.5 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                bSevak.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                cardSevak.style.opacity = '0.3';
                cardShatru.style.opacity = '1';
                desc.textContent = "सहस्रबाहु सम सो रिपु मोरा:";
                descTxt.textContent = "जिसने शिव-धनुष तोड़ा है उसने अक्षम्य अपराध किया है। वह सहस्रबाहु के समान मेरा शत्रु है और मृत्यु का भागी है!";
            }}
        }}

        // Lab 2.6: Bow Comparison
        function toggleSim6Bow(type) {{
            playTone(550, 'sine', 0.08);
            const bDhan = document.getElementById('sim6-btn-dhanuhi');
            const bPin = document.getElementById('sim6-btn-pinaka');
            const desc = document.getElementById('sim6-desc');
            const text = document.getElementById('sim6-text');

            if (type === 'dhanuhi') {{
                bDhan.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                bPin.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                desc.textContent = "लड़कपन की धनुहियाँ (लक्ष्मण का तर्क):";
                text.textContent = "लक्ष्मण मुस्कुराते हुए कहते हैं कि हमने बचपन में अनगिनत छोटी धनुहियाँ तोड़ी हैं, तब तो किसी मुनि ने ऐसा क्रोध नहीं किया।";
            }} else {{
                bPin.className = 'px-2.5 py-1 rounded text-xs font-bold bg-yellow-600 text-white transition';
                bDhan.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                desc.textContent = "भगवान शिव का पिनाक धनुष (परशुराम की दृष्टि):";
                text.textContent = "परशुराम कहते हैं कि जिसे तुम साधारण धनुही बता रहे हो, वह तीनों लोकों में विख्यात भगवान शिव का महाधनुष 'त्रिपुरारि धनु' है!";
            }}
        }}

        // Lab 2.7: Tensile Touch Test
        function applyTensionSim7() {{
            playTone(200, 'sawtooth', 0.2);
            const finger = document.getElementById('sim7-finger');
            const bowArc = document.getElementById('sim7-bow-arc');
            const status = document.getElementById('sim7-status-text');

            finger.setAttribute('transform', 'translate(0, 0)');
            bowArc.setAttribute('stroke', '#ef4444');
            bowArc.setAttribute('stroke-dasharray', '8,4');
            status.textContent = "⚡ स्पर्श मात्र से भग्न! 'छुअत टूट रघुपतिहु न दोसू' (राम का कोई दोष नहीं)";
            status.setAttribute('fill', '#f87171');
        }}

        function resetSim7() {{
            playTone(400, 'sine', 0.08);
            const finger = document.getElementById('sim7-finger');
            const bowArc = document.getElementById('sim7-bow-arc');
            const status = document.getElementById('sim7-status-text');

            finger.setAttribute('transform', 'translate(0, -40)');
            bowArc.setAttribute('stroke', '#d97706');
            bowArc.removeAttribute('stroke-dasharray');
            status.textContent = "धनुष अत्यंत पुराना (जून) एवं जीर्ण-शीर्ण अवस्था में है।";
            status.setAttribute('fill', '#fef08a');
        }}

        // Lab 2.8: Axe Swing
        function swingSim8Axe() {{
            playTone(220, 'triangle', 0.25);
            const axe = document.getElementById('sim8-axe');
            axe.style.transform = 'rotate(-35deg)';
            setTimeout(() => {{
                playTone(180, 'sawtooth', 0.2);
                axe.style.transform = 'rotate(20deg)';
                setTimeout(() => axe.style.transform = 'rotate(0deg)', 250);
            }}, 200);
        }}

        // Lab 2.9: 21 Victories Counter
        let sim9Count = 1;
        function incrementSim9Victory() {{
            sim9Count = (sim9Count % 21) + 1;
            playTone(300 + sim9Count * 15, 'sine', 0.08);
            document.getElementById('sim9-count-text').textContent = `${{sim9Count}} बार भूप-विहीन पृथ्वी`;
        }}

        function resetSim9() {{
            sim9Count = 1;
            document.getElementById('sim9-count-text').textContent = "1 बार भूप-विहीन पृथ्वी";
        }}

        // Lab 2.10: Mountain vs Kumhadbattiya
        function blowSim10Wind() {{
            playTone(350, 'sine', 0.3);
            const wind = document.getElementById('sim10-wind');
            wind.classList.remove('hidden');
            setTimeout(() => wind.classList.add('hidden'), 1500);

            document.getElementById('sim10-sub-title').textContent = "पहाड़ पर फूँक का कोई प्रभाव नहीं!";
            document.getElementById('sim10-sub-desc').textContent = "लक्ष्मण चट्टान के समान अडिग हैं; परशुराम के खोखले भय या क्रोध से वे तनिक भी विचलित नहीं होते।";
        }}

        function pointSim10Finger() {{
            playTone(420, 'sine', 0.2);
            const hand = document.getElementById('sim10-pointing-hand');
            hand.classList.remove('hidden');
            setTimeout(() => hand.classList.add('hidden'), 1500);

            document.getElementById('sim10-sub-title').textContent = "इहाँ कुम्हड़बतिया कोउ नाहीं:";
            document.getElementById('sim10-sub-desc').textContent = "लक्ष्मण स्पष्ट कहते हैं कि हम कुम्हड़े के कच्चे फल या छुईमुई के पौधे नहीं हैं जो आपकी तर्जनी अंगुली देखते ही मुरझा जाएँगे!";
        }}

        // Lab 2.11: Raghu Clan Shield
        function setSim11Category(cat) {{
            playTone(500, 'sine', 0.08);
            const icon = document.getElementById('sim11-shield-icon');
            const title = document.getElementById('sim11-info-title');
            const body = document.getElementById('sim11-info-body');

            const bSur = document.getElementById('sim11-btn-sur');
            const bMah = document.getElementById('sim11-btn-mahisur');
            const bHar = document.getElementById('sim11-btn-harijan');
            const bGai = document.getElementById('sim11-btn-gai');

            [bSur, bMah, bHar, bGai].forEach(b => b.className = 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition');

            if (cat === 'sur') {{
                bSur.className = 'px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                icon.textContent = "☀️";
                title.textContent = "1. सुर (देवता):";
                body.textContent = "रघुकुल के क्षत्रिय देवताओं पर कभी शस्त्र नहीं उठाते, उनकी सदैव स्तुति और पूजा करते हैं।";
            }} else if (cat === 'mahisur') {{
                bMah.className = 'px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                icon.textContent = "🪷";
                title.textContent = "2. महिसुर (ब्राह्मण - जैसे परशुराम):";
                body.textContent = "ब्राह्मण पूजनीय हैं। लक्ष्मण कहते हैं कि आप ब्राह्मण हैं, इसलिए यदि आप प्रहार भी करेंगे, तो भी हम आपके चरणों में ही गिरेंगे।";
            }} else if (cat === 'harijan') {{
                bHar.className = 'px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                icon.textContent = "🙏";
                title.textContent = "3. हरिजन (ईश्वर के भक्त):";
                body.textContent = "भगवान के भक्तों और संतों की रघुकुल सदैव रक्षा करता है, उन पर कभी शौर्य नहीं दिखाया जाता।";
            }} else {{
                bGai.className = 'px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                icon.textContent = "🐄";
                title.textContent = "4. गाई (गौ माता):";
                body.textContent = "गौ माता पवित्र एवं रक्षणीय हैं। रघुकुल की प्रतिज्ञा है कि इन चारों पर कभी वीरता का प्रदर्शन नहीं किया जाता।";
            }}
        }}

        // Lab 2.12: Vajra Strike
        function strikeSim12Thunder() {{
            playTone(160, 'sawtooth', 0.35);
            setTimeout(() => playTone(120, 'square', 0.2), 100);

            const vGroup = document.getElementById('sim12-vajra-group');
            vGroup.classList.add('animate-ping');
            setTimeout(() => vGroup.classList.remove('animate-ping'), 600);

            document.getElementById('sim12-desc').textContent = "⚡ करोड़ों वज्रों के समान वाणी:";
            document.getElementById('sim12-text').textContent = "उपमा अलंकार: 'कोटि कुलिस सम बचनु तुम्हारा।' लक्ष्मण का यह कथन सिद्ध करता है कि परशुराम की वाणी ही इतनी तीक्ष्ण है कि किसी अस्त्र-शस्त्र की आवश्यकता ही नहीं है!";
        }}

        // Lab 2.13: Storyboard Legend
        function stepSim13Legend(step) {{
            playTone(480, 'sine', 0.08);
            const b1 = document.getElementById('sim13-btn-1');
            const b2 = document.getElementById('sim13-btn-2');
            const b3 = document.getElementById('sim13-btn-3');
            const head = document.getElementById('sim13-step-heading');
            const desc = document.getElementById('sim13-desc-text');

            [b1, b2, b3].forEach(b => b.className = 'px-2 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition');

            if (step === 1) {{
                b1.className = 'px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                head.textContent = "चरण 1: जमदग्नि ऋषि के आश्रम में कामधेनु गाय";
                desc.textContent = "महर्षि जमदग्नि के आश्रम में सभी मनोरथ पूर्ण करने वाली दिव्य कामधेनु गाय थी। राजा सहस्रबाहु शिकार खेलते हुए आश्रम आया और आतिथ्य सत्कार से चमत्कृत हुआ।";
            }} else if (step === 2) {{
                b2.className = 'px-2 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                head.textContent = "चरण 2: सहस्रबाहु द्वारा कामधेनु का बलपूर्वक अपहरण";
                desc.textContent = "लोभी सहस्रबाहु ने ऋषि जमदग्नि के मना करने पर भी कामधेनु को बलपूर्वक छीन लिया और आश्रम में विध्वंस मचाया।";
            }} else {{
                b3.className = 'px-2 py-1 rounded text-xs font-bold bg-rose-600 text-white transition';
                head.textContent = "चरण 3: परशुराम द्वारा सहस्रबाहु की 1000 भुजाओं का छेदन";
                desc.textContent = "परशुराम ने क्रोधित होकर अपने तीक्ष्ण फरसे से सहस्रबाहु की सभी एक हजार भुजाओं को काट डाला और उसका वध कर कामधेनु को वापस आश्रम लाए।";
            }}
        }}

        // Lab 2.14: Doha & Chaupai Metric
        function setSim14Chhand(type) {{
            playTone(520, 'sine', 0.08);
            const bChau = document.getElementById('sim14-btn-chaupai');
            const bDoh = document.getElementById('sim14-btn-doha');
            const title = document.getElementById('sim14-chhand-title');
            const line = document.getElementById('sim14-verse-line1');
            const matra = document.getElementById('sim14-matra-symbols');
            const rule = document.getElementById('sim14-rule');

            if (type === 'chaupai') {{
                bChau.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                bDoh.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                title.textContent = "चौपाई छंद (सममात्रिक छंद - प्रत्येक चरण 16 मात्राएँ)";
                line.textContent = '"ना थ सं भु ध नु भं ज नि हा रा"';
                matra.textContent = "ऽ  ।  ऽ  ।  ।  ।  ऽ  ।  ।  ऽ  ऽ = 16 मात्राएँ";
                rule.textContent = "नियम: अंत में जगण (।ऽ।) अथवा तगण (ऽऽ।) वर्जित, प्रायः दो गुरु (ऽऽ) होते हैं।";
            }} else {{
                bDoh.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                bChau.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                title.textContent = "दोहा छंद (अर्द्धसम मात्रिक - 13 + 11 = 24 मात्राएँ)";
                line.textContent = '"सु न हु रा म जे हिं सं भु ध नु तो रा" (13) + "स ह स बा हु स म सो रि पु मो रा" (11)';
                matra.textContent = "विषम चरण (1, 3): 13 मात्राएँ | सम चरण (2, 4): 11 मात्राएँ";
                rule.textContent = "यति 13 और 11 मात्राओं के बाद होती है, सम चरणों के अंत में तुक मिलती है।";
            }}
        }}

        // Lab 2.15: Awadhi Vocabulary
        function flipSim15Word(w) {{
            playTone(510, 'sine', 0.08);
            const term = document.getElementById('sim15-word-term');
            const def = document.getElementById('sim15-word-def');

            if (w === 'bhanjanihara') {{
                term.textContent = "भंजनिहारा";
                def.textContent = "तोड़ने वाला, विनाश करने वाला (संस्कृत 'भंजन' से व्युत्पन्न)।";
            }} else if (w === 'larikai') {{
                term.textContent = "लरिकाईं";
                def.textContent = "बचपन, लड़कपन की अवस्था।";
            }} else if (w === 'june') {{
                term.textContent = "जून";
                def.textContent = "पुराना, जीर्ण-शीर्ण, प्राचीन।";
            }} else if (w === 'kulis') {{
                term.textContent = "कुलिस";
                def.textContent = "वज्र, अत्यंत कठोर एवं अभेद्य अस्त्र।";
            }} else if (w === 'gadhisunu') {{
                term.textContent = "गाधीसूनु";
                def.textContent = "गाधि के पुत्र अर्थात् महर्षि विश्वामित्र।";
            }}
        }}

        // Lab 2.16: Question Navigator
        const qData16 = {{
            1: {{
                title: "परशुराम के क्रोध करने पर राम और लक्ष्मण की प्रतिक्रियाओं के आधार पर दोनों के स्वभाव की विशेषताएँ लिखिए।",
                ans: "<strong>राम का स्वभाव:</strong> राम अत्यंत शांत, विनम्र, मर्यादाप्रिय और धैर्यवान हैं। वे परशुराम को गुरु एवं पूज्य मानकर स्वयं को उनका 'दास' कहते हैं।<br><strong>लक्ष्मण का स्वभाव:</strong> लक्ष्मण वीर, साहसी, वाक्पटु एवं व्यंग्यप्रिय हैं। वे अन्याय व अनुचित अहंकार को बिल्कुल सहन नहीं करते और सटीक तर्कों से मुंहतोड़ उत्तर देते हैं।"
            }},
            2: {{
                title: "लक्ष्मण ने वीर योद्धा की क्या-क्या विशेषताएँ बताई हैं?",
                ans: "<strong>वीर योद्धा के लक्षण:</strong> 1. वीर पुरुष स्वयं अपनी प्रशंसा नहीं करते, युद्धभूमि में कर्म करके दिखाते हैं। 2. वे कभी अधैर्य, क्रोध या अहंकार का प्रदर्शन नहीं करते। 3. वे देवता, ब्राह्मण, ईश्वर-भक्त और गौ पर शस्त्र नहीं उठाते।"
            }},
            3: {{
                title: "परशुराम ने अपने विषय में सभा में क्या-क्या कहा?",
                ans: "<strong>परशुराम का आत्म-परिचय:</strong> वे बाल ब्रह्मचारी एवं अत्यंत क्रोधी स्वभाव के हैं। उन्होंने 21 बार पृथ्वी को क्षत्रिय राजाओं से विहीन कर ब्राह्मणों को दान किया है। उनका फरसा गर्भस्थ शिशुओं का भी नाश करने वाला है।"
            }},
            4: {{
                title: "साहस और शक्ति के साथ विनम्रता हो तो बेहतर है। इस कथन पर अपने विचार लिखिए।",
                ans: "साहस और शक्ति जब विनम्रता से विहीन हो जाती है, तो वह परशुराम के क्रोध की भाँति विनाशकारी और उग्र बन जाती है। जब साहस के साथ श्रीराम जैसी विनम्रता जुड़ती है, तो व्यक्ति समाज में वंदनीय और आदर्श बन जाता है।"
            }},
            6: {{
                title: "पाठ के आधार पर तुलसीदास के भाषा-सौंदर्य की चार विशेषताएँ लिखिए।",
                ans: "1. <strong>अवधी भाषा:</strong> साहित्यिक एवं माधुर्यपूर्ण अवधी भाषा का उत्कृष्ट प्रयोग।<br>2. <strong>दोहा-चौपाई शैली:</strong> गेय, छंदोबद्ध एवं संगीतमय विधान।<br>3. <strong>अलंकार सौंदर्य:</strong> उपमा, रूपक, उत्प्रेक्षा, अनुप्रास एवं पुनरुक्ति प्रकाश अलंकारों का सहज प्रयोग।<br>4. <strong>व्यंग्यात्मकता एवं संवाद-कौशल:</strong> पात्रानुकूल अत्यंत सजीव संवाद।"
            }}
        }};

        function selectSim16Question(qNo) {{
            playTone(530, 'sine', 0.08);
            const data = qData16[qNo];
            if (!data) return;
            document.getElementById('sim16-q-num').textContent = `एनसीईआरटी पाठ्यपुस्तक प्रश्न ${{qNo}}:`;
            document.getElementById('sim16-q-title').textContent = data.title;
            document.getElementById('sim16-q-ans').innerHTML = data.ans;
        }}

        // Initialize App on DOM Ready
        window.addEventListener('DOMContentLoaded', () => {{
            generateSlidePills();
            showSlide(0);
        }});
    </script>
</body>
</html>
"""
    return full_html


if __name__ == "__main__":
    html_output = build_full_html()
    target_path = "public/animations/ram-lakshman-parashuram-samvad.html"
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Successfully generated {target_path} ({len(html_output)} bytes)")
