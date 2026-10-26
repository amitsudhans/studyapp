# -*- coding: utf-8 -*-
"""
HTML Builder for NCERT Class 10 Hindi (Kshitij Part 2), Chapter 1: सूरदास के पद.
Generates public/animations/surdas-ke-pad.html with:
- 16 Rich Content Slides in pure eloquent Hindi covering every line of the textbook (Pages 1-9).
- 32 In-Slide Checkpoint Questions with instant teacher feedback.
- 4 Dedicated Mastery Quiz Challenge Slides (40 questions total) with popup solution modals in Hindi.
- 16 Bespoke Interactive SVG Laboratory Simulators.
- Animated Teacher Avatar (प्राध्यापिका डॉ. अनन्या - हिंदी साहित्य विदुषी) with talking mouth synced to Hindi audio narration.
- Web Audio API sound synthesizer and Web Speech API Hindi narration (hi-IN).
- Last Slide Notice with strict unit test compatibility.
"""

import os
import sys

# Ensure data script can be imported
sys.path.append(os.path.dirname(__file__))
from surdas_hindi_data import CONTENT_SLIDES, QUIZ_SLIDES

def generate_interactive_simulator(s_idx):
    """Returns bespoke interactive SVG simulator HTML for each content slide (1-16)."""
    if s_idx == 1:
        # Simulator 1: Poetic Meter & 1857 Patriotic Rhythm Lab
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 1.1: काव्य सरिता एवं देशभक्ति राग तरंग इंजन</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim1Mode('tulsidas')" id="btn-sim1-tulsi" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition">तुलसीदास मंगलाचरण</button>
                    <button onclick="toggleSim1Mode('1857')" id="btn-sim1-1857" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition">1857 कौमी तराना</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-gradient-to-b from-slate-900 via-amber-950/30 to-slate-950 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim1-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Tulsi Mangalacharan View -->
                    <g id="sim1-tulsi-view">
                        <!-- Ocean Heart -->
                        <path d="M0,180 Q125,160 250,180 T500,180 L500,240 L0,240 Z" fill="#0369a1" opacity="0.7"/>
                        <text x="250" y="215" fill="#bae6fd" font-size="11" font-weight="bold" text-anchor="middle">हृदय सिंधु (क्षीरसागर रूपी विशाल हृदय)</text>

                        <!-- Oyster Shell (Mati Seep) -->
                        <ellipse cx="250" cy="140" rx="45" ry="25" fill="#fef3c7" stroke="#d97706" stroke-width="2"/>
                        <ellipse cx="250" cy="135" rx="35" ry="18" fill="#fffbeb"/>
                        <text x="250" y="140" fill="#78350f" font-size="9" font-weight="bold" text-anchor="middle">मति सीप (बुद्धि)</text>

                        <!-- Swati Raindrop falling from Saraswati Cloud -->
                        <path d="M180,40 Q250,20 320,40 Q350,60 320,80 Q250,90 180,75 Z" fill="#cbd5e1" opacity="0.8"/>
                        <text x="250" y="60" fill="#1e293b" font-size="10" font-weight="bold" text-anchor="middle">स्वाति सारदा (ज्ञान रूपी पावन मेघ)</text>
                        <!-- Animated Drop -->
                        <circle id="sim1-drop" cx="250" cy="95" r="5" fill="#38bdf8" filter="drop-shadow(0 0 6px #38bdf8)"/>

                        <!-- Pearl in Shell (Muktamani Charu) -->
                        <circle cx="250" cy="132" r="8" fill="#ffffff" stroke="#cbd5e1" stroke-width="1.5" filter="drop-shadow(0 0 8px #ffffff)"/>
                        <text x="250" y="115" fill="#fbbf24" font-size="9" font-weight="bold" text-anchor="middle">कबित मुकुतामनि (कविता रूपी मोती)</text>
                    </g>

                    <!-- 1857 View (Hidden initially) -->
                    <g id="sim1-1857-view" opacity="0">
                        <rect x="0" y="0" width="500" height="240" fill="#064e3b" opacity="0.85"/>
                        <!-- Tricolor Rays / National Banner -->
                        <rect x="150" y="30" width="200" height="25" fill="#ea580c" rx="4"/>
                        <rect x="150" y="55" width="200" height="25" fill="#ffffff" rx="4"/>
                        <rect x="150" y="80" width="200" height="25" fill="#16a34a" rx="4"/>
                        <text x="250" y="72" fill="#0f172a" font-size="10" font-weight="bold" text-anchor="middle">आज़ादी का तिरंगा झंडा</text>
                        <text x="250" y="140" fill="#fde047" font-size="13" font-weight="bold" text-anchor="middle">"हम हैं इसके मालिक हिंदुस्तान हमारा"</text>
                        <text x="250" y="170" fill="#ffffff" font-size="11" text-anchor="middle">हिंदू मुसलमाँ सिख हमारा भाई भाई प्यारा</text>
                        <text x="250" y="200" fill="#86efac" font-size="10" text-anchor="middle">गंगो-जमुन की उर्वर धारा एवं बर्फीला हिमालय प्रहरी</text>
                    </g>
                </svg>
            </div>
            <p id="sim1-desc" class="text-xs text-slate-400 mt-2 text-center">
                तुलसीदास जी के अनुसार श्रेष्ठ विचारों की स्वाति बूँद से बुद्धि-सीप में कविता रूपी मुक्तामणि (सच्चा मोती) उत्पन्न होता है!
            </p>
        </div>
        """

    elif s_idx == 2:
        # Simulator 2: Surdas Chronology & Brajbhumi Gaughat Map
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-cyan-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-cyan-400">इंटरैक्टिव लैब 1.2: सूरदास जीवन-यात्रा एवं ब्रजभूमि गऊघाट मानचित्र</span>
                </div>
                <span class="text-xs font-mono text-cyan-300">सन् 1478 — 1583 ई.</span>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-cyan-500/30 p-3">
                <svg id="sim2-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Yamuna River Riverbed curving -->
                    <path d="M50,0 Q180,80 250,120 T450,240" fill="none" stroke="#0284c7" stroke-width="26" opacity="0.6"/>
                    <text x="320" y="175" fill="#38bdf8" font-size="10" font-weight="bold" transform="rotate(30 320 175)">यमुना नदी</text>

                    <!-- Station Nodes -->
                    <!-- Node 1: Runakata / Sihi (Birth) -->
                    <g transform="translate(90, 60)" class="cursor-pointer" onclick="showSim2Info('birth')">
                        <circle cx="0" cy="0" r="14" fill="#059669" stroke="#34d399" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">1478</text>
                        <text x="0" y="24" fill="#6ee7b7" font-size="8.5" font-weight="bold" text-anchor="middle">रुनकता / सीही (जन्म)</text>
                    </g>

                    <!-- Node 2: Gaughat (Residence & Diksha) -->
                    <g transform="translate(230, 95)" class="cursor-pointer" onclick="showSim2Info('gaughat')">
                        <circle cx="0" cy="0" r="18" fill="#d97706" stroke="#fbbf24" stroke-width="2.5"/>
                        <text x="0" y="4" fill="#ffffff" font-size="10" font-weight="bold" text-anchor="middle">गऊघाट</text>
                        <text x="0" y="27" fill="#fde68a" font-size="9" font-weight="bold" text-anchor="middle">वल्लभाचार्य भेंट व निवास</text>
                    </g>

                    <!-- Node 3: Shrinathji Temple (Bhajan Kirtan) -->
                    <g transform="translate(350, 110)" class="cursor-pointer" onclick="showSim2Info('temple')">
                        <rect x="-14" y="-14" width="28" height="28" fill="#7c3aed" stroke="#c084fc" stroke-width="2" rx="4"/>
                        <text x="0" y="4" fill="#ffffff" font-size="8" font-weight="bold" text-anchor="middle">मंदिर</text>
                        <text x="0" y="26" fill="#e9d5ff" font-size="8.5" font-weight="bold" text-anchor="middle">श्रीनाथ जी मंदिर</text>
                    </g>

                    <!-- Node 4: Parasoli (Mahaprayan) -->
                    <g transform="translate(420, 190)" class="cursor-pointer" onclick="showSim2Info('parasoli')">
                        <circle cx="0" cy="0" r="14" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                        <text x="0" y="4" fill="#ffffff" font-size="9" font-weight="bold" text-anchor="middle">1583</text>
                        <text x="0" y="24" fill="#fda4af" font-size="8.5" font-weight="bold" text-anchor="middle">पारसौली (निधन)</text>
                    </g>

                    <!-- Info Box Overlay -->
                    <rect x="20" y="160" width="240" height="65" rx="8" fill="rgba(15,23,42,0.92)" stroke="#0284c7"/>
                    <text x="30" y="180" fill="#38bdf8" font-size="10" font-weight="bold" id="sim2-title">गऊघाट: आध्यात्मिक साधना स्थली</text>
                    <text x="30" y="196" fill="#cbd5e1" font-size="8.5" id="sim2-desc1">मथुरा और वृंदावन के बीच यमुना तट पर निवास</text>
                    <text x="30" y="212" fill="#4ade80" font-size="8.5" id="sim2-desc2">महाप्रभु वल्लभाचार्य ने पद-रचना का मार्ग दिखाया</text>
                </svg>
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                मानचित्र पर किसी भी तीर्थ-स्थल (रुनकता, गऊघाट, श्रीनाथ मंदिर, पारसौली) पर क्लिक करके ऐतिहासिक विवरण देखें!
            </p>
        </div>
        """

    elif s_idx == 3:
        # Simulator 3: Ashta-Chhap Gallery & Three Masterworks
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-violet-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-violet-400">इंटरैक्टिव लैब 1.3: अष्टछाप काव्य वीथिका एवं सूरदास के तीन ग्रंथ</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-violet-500/30 p-3 flex flex-col justify-between">
                <!-- 3 Master Books -->
                <div class="grid grid-cols-3 gap-3">
                    <div onclick="selectSim3Book('sursagar')" id="book-sursagar" class="p-2.5 rounded-xl bg-violet-950/80 border-2 border-violet-500 text-center cursor-pointer transition shadow-lg">
                        <span class="text-xs font-bold text-violet-300 block">सूरसागर</span>
                        <span class="text-[10px] text-emerald-400 font-medium">सर्वाधिक लोकप्रिय</span>
                    </div>
                    <div onclick="selectSim3Book('sahitya')" id="book-sahitya" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-center cursor-pointer hover:border-slate-700 transition">
                        <span class="text-xs font-bold text-slate-300 block">साहित्य लहरी</span>
                        <span class="text-[10px] text-slate-500">118 दृष्टकूट पद</span>
                    </div>
                    <div onclick="selectSim3Book('saravali')" id="book-saravali" class="p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-center cursor-pointer hover:border-slate-700 transition">
                        <span class="text-xs font-bold text-slate-300 block">सूर सारावली</span>
                        <span class="text-[10px] text-slate-500">अवतार लीलाएँ</span>
                    </div>
                </div>

                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs" id="sim3-info-panel">
                    <h5 class="font-bold text-violet-400 text-xs mb-1" id="sim3-book-title">ग्रंथ: 'सूरसागर' (महाकवि का अमर कीर्ति-स्तंभ)</h5>
                    <p class="text-slate-300 text-[11px] leading-relaxed" id="sim3-book-desc">
                        सवा लाख पदों में से वर्तमान में लगभग पाँच हजार पद उपलब्ध हैं। इसी के विश्व-प्रसिद्ध 'भ्रमरगीत' प्रसंग से कक्षा 10 में चार अमर पद संकलित हैं, जो प्रेम-मार्ग की ज्ञान-मार्ग पर विजय का उद्घोष करते हैं।
                    </p>
                </div>

                <div class="flex items-center justify-between text-[10px] text-slate-400 px-1">
                    <span>अष्टछाप के प्रमुख: सूरदास, कुंभनदास, परमानंददास, कृष्णदास</span>
                    <span class="text-emerald-400 font-bold">रस सम्राट: वात्सल्य एवं शृंगार</span>
                </div>
            </div>
        </div>
        """

    elif s_idx == 4:
        # Simulator 4: Bhramargeet Theater with Flying Bee
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 1.4: भ्रमरगीत रंगमंच (उद्धव-गोपी संवाद एवं भौंरा)</span>
                </div>
                <button onclick="animateSim4Bee()" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">भौंरे की उड़ान कराएं 🐝</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-amber-500/30 p-3">
                <svg id="sim4-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Braj Kadamba Tree & Yamuna Shore -->
                    <rect x="0" y="190" width="500" height="50" fill="#14532d"/>
                    <path d="M0 80 Q60 20 120 70 Q160 10 200 60 Q240 100 180 160 L140 190 L90 190 Z" fill="#15803d" opacity="0.6"/>

                    <!-- Gopis Group on Left -->
                    <g transform="translate(90, 140)">
                        <ellipse cx="0" cy="0" rx="14" ry="24" fill="#f43f5e"/>
                        <circle cx="0" cy="-30" r="10" fill="#fde68a"/>
                        <text x="0" y="45" fill="#fecdd3" font-size="9" font-weight="bold" text-anchor="middle">गोपिकाएँ (प्रेम मार्ग)</text>
                    </g>
                    <g transform="translate(130, 150)">
                        <ellipse cx="0" cy="0" rx="12" ry="22" fill="#ec4899"/>
                        <circle cx="0" cy="-28" r="9" fill="#fde68a"/>
                    </g>

                    <!-- Uddhav on Right with Yoga Scroll -->
                    <g transform="translate(400, 140)">
                        <ellipse cx="0" cy="0" rx="16" ry="25" fill="#f59e0b"/>
                        <circle cx="0" cy="-32" r="11" fill="#fde68a"/>
                        <!-- Yoga Scroll in hand -->
                        <rect x="-24" y="-10" width="14" height="20" fill="#f8fafc" stroke="#94a3b8" rx="2"/>
                        <text x="0" y="45" fill="#fde68a" font-size="9" font-weight="bold" text-anchor="middle">उद्धव (ज्ञान मार्ग)</text>
                    </g>

                    <!-- Animated Flying Bumblebee (Madhukar) -->
                    <g id="sim4-bee" transform="translate(250, 90)">
                        <!-- Bee Body -->
                        <ellipse cx="0" cy="0" rx="12" ry="8" fill="#1e293b" stroke="#eab308" stroke-width="2"/>
                        <line x1="-4" y1="-8" x2="-4" y2="8" stroke="#eab308" stroke-width="2"/>
                        <line x1="4" y1="-8" x2="4" y2="8" stroke="#eab308" stroke-width="2"/>
                        <!-- Wings -->
                        <ellipse cx="-4" cy="-10" rx="6" ry="4" fill="#bae6fd" opacity="0.75"/>
                        <ellipse cx="4" cy="-10" rx="6" ry="4" fill="#bae6fd" opacity="0.75"/>
                        <text x="0" y="20" fill="#fbbf24" font-size="8.5" font-weight="bold" text-anchor="middle">भ्रमर (मधुकर)</text>
                    </g>
                </svg>
            </div>
            <p id="sim4-desc" class="text-xs text-slate-400 mt-2 text-center">
                उद्धव के ज्ञानोपदेश के बीच भौंरे का आगमन हुआ, जिसे माध्यम बनाकर गोपियों ने वक्रोक्ति और व्यंग्य के अमर बाण चलाए!
            </p>
        </div>
        """

    elif s_idx == 5:
        # Simulator 5: Love Thread vs Detachment Meter
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-rose-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-rose-400">इंटरैक्टिव लैब 1.5: प्रेम-तंतु बनाम विरक्ति मीटर ('सनेह तगा')</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-rose-500/30 p-4 flex flex-col justify-between">
                <div class="flex justify-between items-center text-xs text-slate-300">
                    <span class="font-bold text-amber-400">उद्धव का शुष्क ज्ञान: 0% राग</span>
                    <span class="font-bold text-rose-400">गोपियों का अनन्य अनुराग: 100% प्रेम</span>
                </div>

                <div class="relative w-full bg-slate-950 h-8 rounded-full border border-slate-800 overflow-hidden my-auto p-1">
                    <div id="sim5-meter-bar" class="h-full bg-gradient-to-r from-amber-500 via-rose-500 to-pink-500 rounded-full w-[10%] transition-all duration-300"></div>
                </div>

                <div class="space-y-2">
                    <div class="flex justify-between text-xs text-slate-300">
                        <span>मीटर खिसकाएँ:</span>
                        <span id="sim5-meter-val" class="font-bold text-amber-400 font-mono">अपरस (अनासक्त - उद्धव)</span>
                    </div>
                    <input type="range" id="sim5-slider" min="0" max="100" value="10" oninput="updateSim5Meter()" class="w-full accent-rose-500 cursor-pointer">
                </div>
            </div>
            <p id="sim5-desc" class="text-xs text-slate-400 mt-2 text-center">
                उद्धव प्रेम के सागर कृष्ण के समीप रहकर भी 'सनेह तगा' (प्रेम के धागे) से अछूते रहे, इसी पर गोपियों ने तीखा व्यंग्य किया!
            </p>
        </div>
        """

    elif s_idx == 6:
        # Simulator 6: Lotus Leaf & Oiled Pot Water Repulsion Lab
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex flex-col sm:flex-row items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-emerald-400">इंटरैक्टिव लैब 1.6: 'पुरइनि पात' एवं 'तेल की गागरि' जल प्रतिरोधक परीक्षण</span>
                </div>
                <button onclick="triggerSim6WaterDrop()" class="px-3 py-1 rounded text-xs font-bold bg-cyan-600 hover:bg-cyan-500 text-white transition cursor-pointer">जल की बूँदें गिराएं 💧</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-emerald-500/30 p-3 grid grid-cols-2 gap-4">
                <!-- Panel 1: Lotus Leaf -->
                <div class="bg-slate-950 rounded-xl border border-slate-800 p-3 flex flex-col items-center justify-between">
                    <span class="text-xs font-bold text-emerald-400">1. पुरइनि पात (कमल का पत्ता)</span>
                    <svg viewBox="0 0 140 100" class="w-28 h-20">
                        <ellipse cx="70" cy="50" rx="50" ry="30" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
                        <line x1="70" y1="50" x2="35" y2="35" stroke="#166534"/>
                        <line x1="70" y1="50" x2="105" y2="35" stroke="#166534"/>
                        <line x1="70" y1="50" x2="70" y2="78" stroke="#166534"/>
                        <!-- Repelled Water Drop -->
                        <circle id="sim6-drop-leaf" cx="70" cy="45" r="7" fill="#38bdf8" opacity="0.9" stroke="#ffffff" stroke-width="1.5"/>
                    </svg>
                    <span class="text-[10px] text-slate-400 text-center" id="sim6-lbl-leaf">जल में डूबा रहकर भी सर्वथा सूखा और बेदाग!</span>
                </div>

                <!-- Panel 2: Oiled Pot -->
                <div class="bg-slate-950 rounded-xl border border-slate-800 p-3 flex flex-col items-center justify-between">
                    <span class="text-xs font-bold text-amber-400">2. तेल की गागरि (चिकना घड़ा)</span>
                    <svg viewBox="0 0 140 100" class="w-28 h-20">
                        <ellipse cx="70" cy="20" rx="20" ry="6" fill="#78350f" stroke="#d97706"/>
                        <path d="M50 20 Q30 50 45 80 Q70 90 95 80 Q110 50 90 20 Z" fill="#92400e" stroke="#d97706" stroke-width="2"/>
                        <!-- Slipping Droplet -->
                        <circle id="sim6-drop-pot" cx="95" cy="40" r="6" fill="#38bdf8" opacity="0.9" stroke="#ffffff" stroke-width="1.5"/>
                    </svg>
                    <span class="text-[10px] text-slate-400 text-center" id="sim6-lbl-pot">पानी में डुबोने पर भी एक बूँद नहीं टिकती!</span>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                उद्धव का मन कमल-पत्ते और तेल-गागर जैसा है—वे कृष्ण-प्रेम के महासागर में रहकर भी प्रेम-रस से पूर्णतः अछूते रहे!
            </p>
        </div>
        """

    elif s_idx == 7:
        # Simulator 7: Jaggery & Ant Irreversible Devotion Lab ('गुर चाँटी ज्यौं पागी')
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 1.7: 'गुर चाँटी ज्यौं पागी' अनन्य प्रेम आकर्षण</span>
                </div>
                <button onclick="attemptDetachAnts()" class="px-2.5 py-1 rounded text-xs font-bold bg-rose-600 hover:bg-rose-500 text-white transition cursor-pointer">चींटियों को अलग करने का प्रयास करें</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim7-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Giant Lump of Jaggery (Gur) representing Krishna -->
                    <ellipse cx="250" cy="120" rx="90" ry="50" fill="#b45309" stroke="#f59e0b" stroke-width="3"/>
                    <ellipse cx="240" cy="110" rx="75" ry="35" fill="#d97706" opacity="0.8"/>
                    <text x="250" y="125" fill="#fef3c7" font-size="14" font-weight="bold" text-anchor="middle">गुड़ (श्रीकृष्ण का मधुर प्रेम)</text>

                    <!-- Clinging Ants (Gopis) -->
                    <g id="sim7-ants">
                        <ellipse cx="190" cy="90" rx="6" ry="4" fill="#0f172a"/><circle cx="184" cy="90" r="3" fill="#0f172a"/>
                        <ellipse cx="280" cy="85" rx="6" ry="4" fill="#0f172a"/><circle cx="286" cy="85" r="3" fill="#0f172a"/>
                        <ellipse cx="220" cy="145" rx="6" ry="4" fill="#0f172a"/><circle cx="215" cy="145" r="3" fill="#0f172a"/>
                        <ellipse cx="300" cy="135" rx="6" ry="4" fill="#0f172a"/><circle cx="306" cy="135" r="3" fill="#0f172a"/>
                    </g>
                </svg>

                <div id="sim7-alert" class="hidden p-2 rounded-lg bg-rose-950/90 border border-rose-500 text-center text-xs text-rose-300 font-bold animate-fadeIn">
                    असंभव! चींटी गुड़ में चिपकने के बाद अलग नहीं हो सकती, वहीं प्राण त्याग देती है। गोपियों का प्रेम भी ऐसा ही अनन्य और अविभाज्य है!
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                गोपियाँ कहती हैं: हम अबला और भोली हैं, जो कृष्ण-प्रेम रूपी गुड़ में चींटियों की भाँति सदैव के लिए लिपट चुकी हैं!
            </p>
        </div>
        """

    elif s_idx == 8:
        # Simulator 8: Heart Pang & Separation Thermometer ('मन की मन ही माँझ रही')
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-rose-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-rose-400">इंटरैक्टिव लैब 1.8: विरह वेदना थर्मामीटर ('अवधि अधार आस आवन की')</span>
                </div>
                <div class="text-xs text-rose-400 font-bold font-mono" id="sim8-temp-val">विरह ताप: 85° व्यथा</div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-rose-500/30 p-4 flex flex-col justify-between">
                <svg id="sim8-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Gopi Heart Shape -->
                    <path d="M250,180 C180,110 170,50 215,35 C240,25 250,55 250,55 C250,55 260,25 285,35 C330,50 320,110 250,180 Z" fill="#881337" stroke="#f43f5e" stroke-width="2" id="sim8-heart"/>
                    <text x="250" y="105" fill="#ffe4e6" font-size="11" font-weight="bold" text-anchor="middle">गोपी-हृदय</text>
                    <text x="250" y="125" fill="#fecdd3" font-size="9" text-anchor="middle">"मन की मन ही माँझ रही"</text>
                </svg>

                <div class="space-y-1">
                    <div class="flex justify-between text-xs text-slate-300">
                        <span>मथुरा में कृष्ण का प्रवास काल (प्रतीक्षा की अवधि):</span>
                        <span id="sim8-day-count" class="font-bold text-rose-400 font-mono">100 दिन व्यतीत</span>
                    </div>
                    <input type="range" id="sim8-slider" min="10" max="100" value="70" oninput="updateSim8Heart()" class="w-full accent-rose-500 cursor-pointer">
                </div>
            </div>
            <p id="sim8-desc" class="text-xs text-slate-400 mt-2 text-center">
                श्रीकृष्ण के लौटने की निश्चित अवधि और उनके आने की आशा ही गोपियों के जीने का आधार थी, जिसने तन-मन की व्यथा सहने की शक्ति दी थी।
            </p>
        </div>
        """

    elif s_idx == 9:
        # Simulator 9: Yoga Message Pouring Ghee into Viraha Fire
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 1.9: विरहाग्नि में योग-संदेश रूपी घी की आहुति</span>
                </div>
                <button onclick="pourYogaGhee()" class="px-2.5 py-1 rounded text-xs font-bold bg-amber-600 hover:bg-amber-500 text-white transition cursor-pointer">योग-संदेश का घी डालें 🔥</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-amber-500/30 p-3 flex items-center justify-center">
                <svg id="sim9-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Viraha Hearth -->
                    <polygon points="170,210 330,210 310,180 190,180" fill="#475569" stroke="#94a3b8"/>
                    <text x="250" y="202" fill="#ffffff" font-size="9" text-anchor="middle">विरह वेदी</text>

                    <!-- Burning Flames -->
                    <g id="sim9-flames">
                        <path d="M220,180 Q210,110 240,60 Q260,110 250,180 Z" fill="#ea580c" opacity="0.85"/>
                        <path d="M240,180 Q250,80 270,40 Q290,100 280,180 Z" fill="#f59e0b" opacity="0.85"/>
                        <path d="M230,180 Q250,110 255,90 Q270,120 260,180 Z" fill="#facc15"/>
                    </g>
                    <text x="250" y="145" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle" id="sim9-flame-text">विरह की आग</text>

                    <!-- Ghee Container pouring down -->
                    <g id="sim9-pot" transform="translate(340, 40)" opacity="0.4">
                        <ellipse cx="20" cy="20" rx="15" ry="8" fill="#ca8a04"/>
                        <path d="M5,20 L35,20 L30,45 L10,45 Z" fill="#eab308"/>
                        <text x="20" y="60" fill="#fef08a" font-size="8" text-anchor="middle">योग-संदेश</text>
                    </g>
                </svg>
            </div>
            <p id="sim9-desc" class="text-xs text-slate-400 mt-2 text-center">
                गोपियाँ विरह की आग में जल रही थीं; उद्धव के ज्ञान संदेश ने विरहाग्नि में घी का काम किया और पीड़ा को प्रचंड कर दिया!
            </p>
        </div>
        """

    elif s_idx == 10:
        # Simulator 10: Haril Bird Firm Grip Demonstrator ('हमारैं हरि हारिल की लकरी')
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-emerald-400">इंटरैक्टिव लैब 1.10: हारिल पक्षी काष्ठ-बंधन मॉडल ('हारिल की लकरी')</span>
                </div>
                <button onclick="attemptReleaseHarilTwig()" class="px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 hover:bg-emerald-500 text-white transition cursor-pointer">लकड़ी छुड़ाने का प्रयास करें</button>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-emerald-500/30 p-3 flex items-center justify-center">
                <svg id="sim10-canvas" viewBox="0 0 500 240" class="w-full h-full">
                    <!-- Tree Branch -->
                    <path d="M0,150 Q200,140 500,160" fill="none" stroke="#78350f" stroke-width="12"/>

                    <!-- Haril Bird (Green Pigeon with Yellow Legs) -->
                    <g transform="translate(230, 90)">
                        <!-- Body -->
                        <ellipse cx="0" cy="0" rx="35" ry="25" fill="#4d7c0f" stroke="#65a30d" stroke-width="2"/>
                        <!-- Head -->
                        <circle cx="-32" cy="-15" r="16" fill="#65a30d"/>
                        <circle cx="-38" cy="-18" r="3" fill="#0f172a"/>
                        <!-- Beak -->
                        <polygon points="-48,-15 -58,-12 -48,-9" fill="#ca8a04"/>
                        <!-- Tail -->
                        <polygon points="30,-5 80,10 32,15" fill="#365314"/>
                        <!-- Yellow Legs Clamping Twig -->
                        <rect x="-10" y="20" width="6" height="30" fill="#facc15" stroke="#ca8a04"/>
                        <rect x="5" y="20" width="6" height="30" fill="#facc15" stroke="#ca8a04"/>

                        <!-- Wooden Twig in Claws ('हारिल की लकरी') -->
                        <rect id="sim10-twig" x="-35" y="45" width="80" height="8" rx="3" fill="#b45309" stroke="#f59e0b" stroke-width="1.5" filter="drop-shadow(0 0 5px #f59e0b)"/>
                        <text x="5" y="65" fill="#fef08a" font-size="9" font-weight="bold" text-anchor="middle">हारिल की लकरी (श्रीकृष्ण)</text>
                    </g>
                </svg>
            </div>
            <p id="sim10-desc" class="text-xs text-slate-400 mt-2 text-center">
                'मन क्रम बचन नंद-नंदन उर, यह दृढ़ करि पकरी' - जैसे हारिल लकड़ी को कभी नहीं छोड़ता, वैसे ही गोपियों ने कृष्ण को दृढ़ता से थाम रखा है!
            </p>
        </div>
        """

    elif s_idx == 11:
        # Simulator 11: Bitter Gourd Rejection & Spinning Mind Wheel ('करुई ककरी' एवं 'मन चक्री')
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-emerald-400">इंटरैक्टिव लैब 1.11: कड़वी ककड़ी स्वाद-प्रतिक्रिया एवं चंचल मन चक्री</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-emerald-500/30 p-3 grid grid-cols-2 gap-4">
                <!-- Panel 1: Bitter Gourd (Karui Kakari) -->
                <div class="bg-slate-950 rounded-xl border border-slate-800 p-3 flex flex-col items-center justify-between">
                    <span class="text-xs font-bold text-rose-400">1. योग = 'करुई ककरी' (कड़वी ककड़ी)</span>
                    <div class="my-auto text-center cursor-pointer" onclick="tasteKaruiKakari()">
                        <svg viewBox="0 0 120 70" class="w-24 h-16">
                            <path d="M10,35 Q60,10 110,35 Q60,60 10,35 Z" fill="#15803d" stroke="#84cc16" stroke-width="2"/>
                            <circle cx="35" cy="35" r="3" fill="#84cc16"/>
                            <circle cx="60" cy="30" r="3" fill="#84cc16"/>
                            <circle cx="85" cy="35" r="3" fill="#84cc16"/>
                        </svg>
                        <button class="mt-1 px-2 py-0.5 rounded text-[10px] font-bold bg-rose-600 text-white">स्वाद चखें 🤢</button>
                    </div>
                    <span class="text-[10px] text-slate-400 text-center" id="sim11-taste-lbl">कड़वी ककड़ी मुँह में जाते ही तुरंत थूक दी जाती है!</span>
                </div>

                <!-- Panel 2: Spinning Mind Wheel (Man Chakri) -->
                <div class="bg-slate-950 rounded-xl border border-slate-800 p-3 flex flex-col items-center justify-between">
                    <span class="text-xs font-bold text-cyan-400">2. योग किसे सौंपें? = 'मन चक्री'</span>
                    <div class="my-auto text-center">
                        <svg viewBox="0 0 100 100" class="w-20 h-20" id="sim11-wheel">
                            <circle cx="50" cy="50" r="40" fill="none" stroke="#0284c7" stroke-width="4" stroke-dasharray="8,4"/>
                            <circle cx="50" cy="50" r="6" fill="#38bdf8"/>
                            <line x1="50" y1="10" x2="50" y2="90" stroke="#0284c7" stroke-width="2"/>
                            <line x1="10" y1="50" x2="90" y2="50" stroke="#0284c7" stroke-width="2"/>
                        </svg>
                    </div>
                    <span class="text-[10px] text-slate-400 text-center">चंचल व डांवाडोल मन वालों के लिए योग आवश्यक है!</span>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                गोपियों का मन श्रीकृष्ण में अचल और स्थिर है; अतः उन्हें योग रूपी बीमारी या कड़वी ककड़ी की रत्ती भर भी आवश्यकता नहीं!
            </p>
        </div>
        """

    elif s_idx == 12:
        # Simulator 12: Krishna's Diplomatic Shift Lab ('हरि हैं राजनीति पढ़ि आए')
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-violet-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-violet-400">इंटरैक्टिव लैब 1.12: श्रीकृष्ण का कूटनीतिक परिवर्तन ('राजनीति पढ़ि आए')</span>
                </div>
                <div class="flex items-center gap-2">
                    <button onclick="toggleSim12Role('gokul')" id="btn-sim12-gokul" class="px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 transition">गोकुल के कृष्ण</button>
                    <button onclick="toggleSim12Role('mathura')" id="btn-sim12-mathura" class="px-2.5 py-1 rounded text-xs font-bold bg-violet-600 text-white transition">मथुरा के राजनीतिज्ञ</button>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-violet-500/30 p-4 flex flex-col justify-between">
                <div class="flex items-center justify-around h-full">
                    <div class="text-center">
                        <svg viewBox="0 0 100 120" class="w-24 h-28 mx-auto" id="sim12-avatar">
                            <!-- Crown / Mor Mukut -->
                            <polygon points="50,15 35,40 65,40" fill="#eab308"/>
                            <circle cx="50" cy="55" r="22" fill="#0284c7"/>
                            <circle cx="43" cy="52" r="3" fill="#ffffff"/>
                            <circle cx="57" cy="52" r="3" fill="#ffffff"/>
                            <path d="M43,65 Q50,72 57,65" fill="none" stroke="#ffffff" stroke-width="2"/>
                            <!-- Robes -->
                            <path d="M25,80 Q50,75 75,80 L80,120 L20,120 Z" fill="#7c3aed"/>
                        </svg>
                        <span class="text-xs font-bold text-violet-300 mt-1 block" id="sim12-role-title">राजा श्रीकृष्ण (मथुरा)</span>
                    </div>

                    <div class="space-y-2 text-xs flex-1 max-w-sm pl-4">
                        <div class="p-2 rounded bg-slate-950 border border-slate-800 flex justify-between">
                            <span class="text-slate-400">व्यवहार शैली:</span>
                            <span class="font-bold text-violet-400" id="sim12-behavior">कूटनीति एवं राजनीति</span>
                        </div>
                        <div class="p-2 rounded bg-slate-950 border border-slate-800 flex justify-between">
                            <span class="text-slate-400">गोपियों को संदेश:</span>
                            <span class="font-bold text-rose-400" id="sim12-message">दूत (उद्धव) द्वारा योग-संदेश</span>
                        </div>
                        <div class="p-2 rounded bg-slate-950 border border-slate-800 flex justify-between">
                            <span class="text-slate-400">गोपियों का व्यंग्य:</span>
                            <span class="font-bold text-amber-300" id="sim12-sarcasm">"बढ़ी बुद्धि जानी जो उनकी"</span>
                        </div>
                    </div>
                </div>
            </div>
            <p id="sim12-desc" class="text-xs text-slate-400 mt-2 text-center">
                गोपियाँ व्यंग्य करती हैं: कृष्ण पहले से ही चतुर थे, अब गुरुओं से राजनीति के बड़े ग्रंथ पढ़कर और भी छल-प्रवीण हो गए हैं!
            </p>
        </div>
        """

    elif s_idx == 13:
        # Simulator 13: King's Duty Balance Scale ('राज धरम तौ यहै सूर')
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-amber-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-amber-400">इंटरैक्टिव लैब 1.13: राजधर्म तुला ('प्रजा न जाहिं सताए')</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-amber-500/30 p-4 flex flex-col justify-between">
                <svg id="sim13-canvas" viewBox="0 0 500 220" class="w-full h-full">
                    <!-- Fulcrum Stand -->
                    <polygon points="250,60 230,190 270,190" fill="#334155"/>
                    <circle cx="250" cy="60" r="8" fill="#f59e0b"/>

                    <!-- Balance Beam -->
                    <line x1="100" y1="90" x2="400" y2="90" stroke="#f59e0b" stroke-width="4" id="sim13-beam"/>

                    <!-- Left Pan: True Rajadharma -->
                    <g transform="translate(100, 90)">
                        <line x1="0" y1="0" x2="-35" y2="50" stroke="#94a3b8" stroke-width="1.5"/>
                        <line x1="0" y1="0" x2="35" y2="50" stroke="#94a3b8" stroke-width="1.5"/>
                        <ellipse cx="0" cy="50" rx="40" ry="10" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
                        <text x="0" y="70" fill="#4ade80" font-size="9" font-weight="bold" text-anchor="middle">सच्चा राजधर्म</text>
                        <text x="0" y="85" fill="#dcfce7" font-size="8" text-anchor="middle">प्रजा-हित व रक्षा</text>
                    </g>

                    <!-- Right Pan: Exploitation / Adharma -->
                    <g transform="translate(400, 90)">
                        <line x1="0" y1="0" x2="-35" y2="50" stroke="#94a3b8" stroke-width="1.5"/>
                        <line x1="0" y1="0" x2="35" y2="50" stroke="#94a3b8" stroke-width="1.5"/>
                        <ellipse cx="0" cy="50" rx="40" ry="10" fill="#be123c" stroke="#f43f5e" stroke-width="2"/>
                        <text x="0" y="70" fill="#f43f5e" font-size="9" font-weight="bold" text-anchor="middle">अनीति व छल</text>
                        <text x="0" y="85" fill="#ffe4e6" font-size="8" text-anchor="middle">प्रजा को सताना</text>
                    </g>
                </svg>
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                सूरदास जी की अमर घोषणा: राजा का परम पावन धर्म यही है कि वह प्रजा को किसी प्रकार का कष्ट न पहुँचने दे!
            </p>
        </div>
        """

    elif s_idx == 14:
        # Simulator 14: Poetic Ornamentation Analyzer (Alankaras in Surdas's Pad)
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-cyan-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-cyan-400">इंटरैक्टिव लैब 1.14: ब्रजभाषा रस-अलंकार विच्छेदक</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-cyan-500/30 p-4 flex flex-col justify-between">
                <div class="flex items-center justify-around gap-2 flex-wrap mb-2">
                    <button onclick="highlightSim14Alankar('rupak')" class="px-2.5 py-1 rounded bg-slate-800 text-xs text-cyan-300 hover:bg-slate-700 transition">रूपक अलंकार</button>
                    <button onclick="highlightSim14Alankar('drishtant')" class="px-2.5 py-1 rounded bg-slate-800 text-xs text-amber-300 hover:bg-slate-700 transition">दृष्टांत अलंकार</button>
                    <button onclick="highlightSim14Alankar('upma')" class="px-2.5 py-1 rounded bg-slate-800 text-xs text-emerald-300 hover:bg-slate-700 transition">उपमा अलंकार</button>
                    <button onclick="highlightSim14Alankar('vunrokti')" class="px-2.5 py-1 rounded bg-slate-800 text-xs text-purple-300 hover:bg-slate-700 transition">पुनरुक्ति प्रकाश</button>
                </div>

                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 text-xs font-serif text-slate-300 text-center leading-relaxed" id="sim14-quote-display">
                    "प्रीति-नदी मैं पाउँ न बोरयौ" ➔ <strong>रूपक अलंकार:</strong> प्रेम पर नदी का अभेद आरोप!
                </div>

                <div class="text-[11px] text-slate-400 text-center" id="sim14-quote-exp">
                    ऊपर दिए गए बटनों पर क्लिक करके सूरदास जी के पदों में प्रयुक्त अलंकारों का साक्षात सौंदर्य परखें।
                </div>
            </div>
        </div>
        """

    elif s_idx == 15:
        # Simulator 15: Haril Bird Interactive Explorer & Vocabulary Cards
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-emerald-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-emerald-400">इंटरैक्टिव लैब 1.15: हारिल पक्षी जैव-पहचान एवं शब्दार्थ कार्ड्स</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-emerald-500/30 p-4 grid grid-cols-1 sm:grid-cols-2 gap-4">
                <!-- Haril Bird Card -->
                <div class="bg-slate-950 p-3 rounded-xl border border-emerald-500/40 flex flex-col justify-between">
                    <span class="text-xs font-bold text-emerald-400">हारिल पक्षी (Common Green Pigeon)</span>
                    <p class="text-[11px] text-slate-300 mt-1">
                        • <strong>संस्कृत नाम:</strong> हारीत<br>
                        • <strong>पहचान:</strong> पीली टाँगें, कोमल हरे पंख, कबूतर जाति<br>
                        • <strong>मुहावरा:</strong> 'हारिल की लकड़ी' अर्थात एकमात्र दृढ़ सहारा
                    </p>
                    <span class="text-[10px] text-emerald-400/80 font-mono mt-1">एनसीईआरटी पृष्ठ 9 ('यह भी जानें')</span>
                </div>

                <!-- Tough Words Flip Selector -->
                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 flex flex-col justify-between">
                    <div class="flex justify-between items-center mb-1">
                        <span class="text-xs font-bold text-amber-400" id="sim15-word-term">अपरस</span>
                        <span class="text-[10px] text-slate-500 font-mono">शब्दार्थ</span>
                    </div>
                    <p class="text-xs text-slate-300" id="sim15-word-def">
                        अलिप्त, नीरस, अछूता (जो प्रेम-रस से वंचित रहा हो)।
                    </p>
                    <div class="flex gap-1.5 mt-2">
                        <button onclick="flipSim15Word('apras')" class="px-2 py-0.5 rounded text-[10px] bg-slate-800 hover:bg-slate-700 text-slate-300">अपरस</button>
                        <button onclick="flipSim15Word('bitha')" class="px-2 py-0.5 rounded text-[10px] bg-slate-800 hover:bg-slate-700 text-slate-300">बिथा</button>
                        <button onclick="flipSim15Word('byadhi')" class="px-2 py-0.5 rounded text-[10px] bg-slate-800 hover:bg-slate-700 text-slate-300">ब्याधि</button>
                        <button onclick="flipSim15Word('chakri')" class="px-2 py-0.5 rounded text-[10px] bg-slate-800 hover:bg-slate-700 text-slate-300">मन चक्री</button>
                    </div>
                </div>
            </div>
        </div>
        """

    elif s_idx == 16:
        # Simulator 16: Gopi Wit vs Uddhav Wisdom Arena
        return """
        <div class="sim-container bg-slate-950 p-4 rounded-2xl border border-slate-800 shadow-xl mb-6">
            <div class="flex items-center justify-between gap-3 mb-3 border-b border-slate-800 pb-2">
                <div class="flex items-center gap-2">
                    <span class="w-3 h-3 rounded-full bg-rose-500 animate-ping"></span>
                    <span class="font-bold text-xs uppercase tracking-wider text-rose-400">इंटरैक्टिव लैब 1.16: गोपियों का वाक्चातुर्य बनाम उद्धव का शुष्क ज्ञान अखाड़ा</span>
                </div>
            </div>

            <div class="relative w-full aspect-[16/9] max-h-[300px] bg-slate-900 rounded-xl overflow-hidden border border-rose-500/30 p-4 flex flex-col justify-between">
                <div class="flex justify-between items-center text-xs">
                    <span class="font-bold text-cyan-400">उद्धव का ज्ञान-तर्क: "निर्गुण ब्रह्म की समाधि लगाओ!"</span>
                    <span class="font-bold text-rose-400">गोपियों का प्रत्युत्तर: प्रेम की अटूट शक्ति</span>
                </div>

                <div class="bg-slate-950 p-3 rounded-xl border border-slate-800 my-auto text-xs" id="sim16-dialogue-box">
                    <span class="font-bold text-rose-400">गोपियों का अचूक वार:</span>
                    <p class="text-slate-300 mt-1" id="sim16-dialogue-text">
                        "हे उद्धव! जो मन कृष्ण के प्रेम में अखंड लीन है, उसे तुम्हारे कड़वी ककड़ी जैसे योग की क्या आवश्यकता? अपना यह योग उन लोगों को सौंपो जिनके मन चकरी की तरह भटकते हैं!"
                    </p>
                </div>

                <div class="flex justify-center gap-2">
                    <button onclick="playSim16Debate(1)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-amber-300">तर्क 1: बड़भागी व्यंग्य</button>
                    <button onclick="playSim16Debate(2)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-emerald-300">तर्क 2: हारिल की लकड़ी</button>
                    <button onclick="playSim16Debate(3)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-rose-300">तर्क 3: कड़वी ककड़ी</button>
                    <button onclick="playSim16Debate(4)" class="px-2.5 py-1 rounded bg-slate-800 hover:bg-slate-700 text-xs text-purple-300">तर्क 4: राजधर्म रक्षा</button>
                </div>
            </div>
            <p class="text-xs text-slate-400 mt-2 text-center">
                गोपियों के अगाध प्रेम, सहज तर्कशीलता और वाक्चातुर्य के सम्मुख प्रकांड ज्ञानी उद्धव पूर्णतः निरुत्तर हो गए!
            </p>
        </div>
        """

    return ""

def build_full_html():
    """Compiles the complete master HTML document in Hindi."""
    all_slides = []

    # Process 16 Content Slides
    for idx, slide in enumerate(CONTENT_SLIDES):
        s_idx = idx + 1
        simulator_html = generate_interactive_simulator(s_idx)

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
                        स्लाइड {s_idx} / 20 • एनसीईआरटी कक्षा 10 हिंदी (क्षितिज)
                    </span>
                    <h2 class="text-xl sm:text-2xl font-black text-white mt-1 tracking-tight">{slide['title']}</h2>
                    <p class="text-xs text-amber-300 font-medium">{slide['subtitle']}</p>
                </div>
                <div class="flex items-center gap-2">
                    <span class="px-2.5 py-1 rounded-lg text-xs font-mono bg-slate-900 text-amber-400 border border-amber-500/30">
                        काव्य खंड • पाठ 1
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
                        <h3 class="font-bold text-xs uppercase tracking-wider text-amber-400">संपूर्ण पाठ्यपुस्तक विश्लेषण एवं भावार्थ</h3>
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

    # Master HTML Template in Hindi
    full_html = f"""<!DOCTYPE html>
<html lang="hi">
<head>
    <meta charset="UTF-8">
    <meta name="viewport" content="width=device-width, initial-scale=1.0">
    <title>NCERT Class 10 Hindi • Chapter 1: सूरदास के पद (Kshitij Part 2)</title>
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
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb {{
            background: #334155;
            border-radius: 9999px;
        }}
        .custom-scrollbar::-webkit-scrollbar-thumb:hover {{
            background: #475569;
        }}

        @keyframes teacherBob {{
            0%, 100% {{ transform: translateY(0px) rotate(0deg); }}
            50% {{ transform: translateY(-3px) rotate(0.8deg); }}
        }}
        .teacher-bob {{
            animation: teacherBob 4s ease-in-out infinite;
        }}

        @keyframes mouthMove {{
            0%, 100% {{ ry: 3; rx: 5; }}
            50% {{ ry: 6.5; rx: 4.5; }}
        }}
        .talking-mouth {{
            animation: mouthMove 0.25s infinite alternate;
        }}

        .modal-backdrop {{
            background: rgba(3, 7, 18, 0.85);
            backdrop-filter: blur(8px);
        }}
    </style>
</head>
<body class="min-h-screen flex flex-col justify-between selection:bg-amber-500 selection:text-slate-950">

    <!-- Top Navigation Header -->
    <header class="sticky top-0 z-40 bg-slate-950/90 backdrop-blur-md border-b border-slate-800 px-4 py-3">
        <div class="max-w-7xl mx-auto flex items-center justify-between gap-4">
            <div class="flex items-center gap-3">
                <div class="w-9 h-9 rounded-xl bg-gradient-to-tr from-amber-600 to-rose-600 flex items-center justify-center shadow-lg shadow-amber-500/20 text-white font-black text-sm">
                    १
                </div>
                <div>
                    <h1 class="text-xs sm:text-sm font-bold text-white tracking-tight flex items-center gap-2">
                        NCERT कक्षा 10 हिंदी (क्षितिज भाग-2)
                        <span class="hidden md:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30">
                            सूरदास के पद
                        </span>
                    </h1>
                    <p class="text-[10px] text-slate-400">डॉ. अनन्या • 20 सचित्र स्लाइडें, सस्वर वाचन एवं इंटरैक्टिव प्रयोगशाला</p>
                </div>
            </div>

            <!-- Slide Quick Pill Selector -->
            <div class="flex items-center gap-2">
                <div class="hidden sm:flex items-center gap-1.5 overflow-x-auto max-w-xs md:max-w-md custom-scrollbar py-1 px-2 rounded-xl bg-slate-900 border border-slate-800" id="slidePillsContainer">
                    <!-- Pills injected dynamically by JS -->
                </div>

                <!-- Global Audio Toggle -->
                <button onclick="toggleAudio()" id="btn-audio-global" class="px-2.5 py-1.5 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs text-slate-300 flex items-center gap-1.5 transition cursor-pointer">
                    <span id="audio-icon">🔊</span>
                    <span class="hidden md:inline" id="audio-label">स्वर: चालू</span>
                </button>
            </div>
        </div>
    </header>

    <!-- Main Slide Stage Area -->
    <main class="flex-1 w-full flex items-center justify-center p-2 sm:p-4">
        {slides_content_str}
    </main>

    <!-- Fixed Bottom Controls & Progress Bar -->
    <footer class="sticky bottom-0 z-40 bg-slate-950/95 backdrop-blur-md border-t border-slate-800 px-4 py-3">
        <div class="max-w-5xl mx-auto">
            <!-- Progress Bar -->
            <div class="w-full bg-slate-900 h-1.5 rounded-full overflow-hidden mb-3">
                <div id="progressBar" class="bg-gradient-to-r from-amber-500 to-rose-500 h-full w-[5%] transition-all duration-300"></div>
            </div>

            <div class="flex items-center justify-between gap-3">
                <button id="prevBtn" onclick="navigateSlide(-1)" class="px-4 py-2 rounded-xl bg-slate-900 hover:bg-slate-800 border border-slate-800 text-xs font-bold text-slate-200 transition flex items-center gap-2 cursor-pointer shadow-md disabled:opacity-40 disabled:cursor-not-allowed">
                    <svg class="w-4 h-4" fill="none" stroke="currentColor" viewBox="0 0 24 24"><path stroke-linecap="round" stroke-linejoin="round" stroke-width="2" d="M15 19l-7-7 7-7"/></svg>
                    पिछली स्लाइड (Previous)
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
                    🎉 You have reached the last slide of this chapter (Chapter 1: सूरदास के पद - भ्रमरगीत)!
                </p>
                <p class="text-[11px] text-slate-300 mt-0.5">
                    बधाई! आपने महाकवि सूरदास के चारों पदों, व्याख्या, शिल्प-सौंदर्य एवं संपूर्ण अभ्यास प्रश्नों का अध्ययन पूर्ण कर लिया है।
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
        const slideNarrations = [
            "कक्षा 10 हिंदी क्षितिज भाग-2 के काव्य खंड में आपका स्वागत है। गोस्वामी तुलसीदास जी का मंगलाचरण कविता को स्वाति नक्षत्र के जल से उपजा सच्चा मोती बताता है। इसके पश्चात 1857 के प्रथम स्वतंत्रता संग्राम के अमर शहीदों का कौमी गीत प्रस्तुत है।",
            "भक्तिकाल की कृष्णभक्ति शाखा के शिरोमणि कवि सूरदास का जन्म सन् 1478 में माना जाता है। वे महाप्रभु वल्लभाचार्य के शिष्य और अष्टछाप के प्रमुख कवि थे। गऊघाट पर रहकर श्रीनाथ जी के मंदिर में कीर्तन करते थे। सन् 1583 में पारसौली में उनका देहावसान हुआ।",
            "सूरदास जी के तीन प्रमुख ग्रंथ हैं: सूरसागर, साहित्य लहरी और सूर सारावली। सूरदास जी को वात्सल्य और शृंगार रस का सम्राट माना जाता है। उनकी ब्रजभाषा अत्यंत निखरी, मधुर और संगीतमय है।",
            "सूरसागर के भ्रमरगीत प्रसंग से यहाँ चार पद संकलित हैं। श्रीकृष्ण ने मथुरा जाने के बाद स्वयं न आकर उद्धव को योग संदेश देकर भेजा। गोपियों ने काले भौंरे के बहाने उद्धव पर तीखे व्यंग्य बाण चलाए।",
            "प्रथम पद में गोपियाँ उद्धव पर व्यंग्य करती हैं: ऊधौ, तुम्ह हौ अति बड़भागी। तुम प्रेम के सागर कृष्ण के समीप रहकर भी प्रेम-बंधन से अछूते रहे, अतः तुम वास्तव में परम अभागे हो!",
            "गोपियाँ उद्धव के अनासक्त व्यवहार की तुलना कमल के पत्ते और तेल लगी मटकी से करती हैं। जैसे कमल का पत्ता और तेल की गागर जल में रहकर भी जल से अछूते रहते हैं, वैसे ही उद्धव कृष्ण-प्रेम से वंचित रहे।",
            "प्रथम पद के समापन में गोपियाँ कहती हैं कि उद्धव ने प्रेम-नदी में कभी पैर तक नहीं डुबोया। हम भोली गोपियाँ तो गुड़ से लिपटी चींटियों की भाँति कृष्ण-प्रेम में अपने प्राण तक समर्पित कर चुकी हैं।",
            "द्वितीय पद में गोपियाँ कहती हैं: मन की मन ही माँझ रही। कृष्ण के लौटने की निश्चित अवधि और उनके आने की आशा ही हमारे जीने का सहारा थी, जिसके बल पर हमने विरह की व्यथा सही।",
            "उद्धव के योग संदेश ने विरहाग्नि में घी डालने जैसा काम किया। जहाँ से रक्षा की पुकार लगानी थी, वहीं से योग की प्रबल धार बह निकली। जब कृष्ण ने ही प्रेम की मर्यादा नहीं रखी, तो हम धैर्य कैसे रखें!",
            "तृतीय पद में गोपियाँ कहती हैं: हमारैं हरि हारिल की लकरी। जैसे हारिल पक्षी अपने पंजे में दबी लकड़ी को कभी नहीं छोड़ता, वैसे ही हमने मन, कर्म और वचन से कृष्ण को हृदय में दृढ़ता से धारण कर रखा है।",
            "गोपियों को उद्धव का योग संदेश कड़वी ककड़ी के समान त्याज्य लगता है। वे कहती हैं कि अपना यह योग रूपी रोग उन लोगों को जाकर सौंपो जिनके मन चकरी की तरह चंचल और अस्थिर हैं।",
            "चतुर्थ पद में गोपियाँ तीखा कटाक्ष करती हैं: हरि हैं राजनीति पढ़ि आए। कृष्ण अब राजा बनकर राजनीति सीख गए हैं और पहले से भी अधिक चतुर होकर हमारे पास योग संदेश भेज रहे हैं।",
            "गोपियाँ कहती हैं कि प्राचीन काल के भले लोग दूसरों के हित के लिए दौड़ते थे। कृष्ण जो दूसरों को अन्याय से छुड़ाते थे, वे स्वयं हमारे साथ छल कर रहे हैं। राजा का धर्म तो प्रजा की रक्षा करना है, उसे सताना नहीं।",
            "सूरदास के पदों में वियोग शृंगार रस की प्रधानता है। मुक्तक गेय पद शैली, ब्रजभाषा का माधुर्य, और रूपक, उपमा, दृष्टांत, वक्रोक्ति अलंकारों का सुंदर प्रयोग हुआ है।",
            "पाठ की संपूर्ण शब्द-संपदा का अध्ययन करें। हारिल पक्षी पीली टाँगों वाला हरे रंग का कबूतर जाति का पक्षी है, जिसे अंग्रेजी में कॉमन ग्रीन पिजन कहते हैं।",
            "यहाँ एनसीईआरटी अभ्यास के सभी पंद्रह प्रश्नों के आदर्श और प्रामाणिक उत्तर प्रस्तुत हैं, जो बोर्ड परीक्षा के लिए अत्यंत उपयोगी हैं।",
            "प्रश्नोत्तरी भाग 1: सूरदास के जीवन परिचय, रचनाओं और भ्रमरगीत की पृष्ठभूमि पर आधारित दस महत्वपूर्ण प्रश्नों का अभ्यास करें।",
            "प्रश्नोत्तरी भाग 2: पद 1 और पद 2 के अर्थ, अलंकारों और गोपियों के विरह पर आधारित दस प्रश्नों का समाधान करें।",
            "प्रश्नोत्तरी भाग 3: पद 3 और पद 4 के गूढ़ भाव, हारिल की लकड़ी, करुई ककरी और राजधर्म पर आधारित दस प्रश्नों का उत्तर दें।",
            "प्रश्नोत्तरी भाग 4: संपूर्ण पाठ्यपुस्तक अभ्यास, शब्द-संपदा और काव्य-शिल्प पर आधारित अंतिम दस प्रश्नों को हल करें।"
        ];

        // Web Audio API Synthesizer
        let audioCtx = null;
        function initAudio() {{
            if (!audioCtx) {{
                audioCtx = new (window.AudioContext || window.webkitAudioContext)();
            }}
            if (audioCtx.state === 'suspended') {{
                audioCtx.resume();
            }}
        }}

        function playTone(freq, type = 'sine', duration = 0.1) {{
            if (!audioEnabled) return;
            try {{
                initAudio();
                const osc = audioCtx.createOscillator();
                const gain = audioCtx.createGain();
                osc.type = type;
                osc.frequency.setValueAtTime(freq, audioCtx.currentTime);
                gain.gain.setValueAtTime(0.15, audioCtx.currentTime);
                gain.gain.exponentialRampToValueAtTime(0.001, audioCtx.currentTime + duration);
                osc.connect(gain);
                gain.connect(audioCtx.destination);
                osc.start();
                osc.stop(audioCtx.currentTime + duration);
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

        // Lab 1.1
        function toggleSim1Mode(mode) {{
            playTone(520, 'sine', 0.08);
            const bTulsi = document.getElementById('btn-sim1-tulsi');
            const b1857 = document.getElementById('btn-sim1-1857');
            const vTulsi = document.getElementById('sim1-tulsi-view');
            const v1857 = document.getElementById('sim1-1857-view');
            const desc = document.getElementById('sim1-desc');

            if (mode === 'tulsidas') {{
                bTulsi.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                b1857.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                vTulsi.setAttribute('opacity', '1');
                v1857.setAttribute('opacity', '0');
                desc.textContent = "तुलसीदास जी के अनुसार श्रेष्ठ विचारों की स्वाति बूँद से बुद्धि-सीप में कविता रूपी मुक्तामणि (सच्चा मोती) उत्पन्न होता है!";
            }} else {{
                b1857.className = 'px-2.5 py-1 rounded text-xs font-bold bg-emerald-600 text-white transition';
                bTulsi.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 hover:bg-slate-700 transition';
                vTulsi.setAttribute('opacity', '0');
                v1857.setAttribute('opacity', '1');
                desc.textContent = "सन् 1857 का कौमी तराना: 'हिंदू मुसलमाँ सिख हमारा भाई भाई प्यारा / यह है आज़ादी का झंडा इसे सलाम हमारा!'";
            }}
        }}

        // Lab 1.2
        function showSim2Info(site) {{
            playTone(560, 'sine', 0.1);
            const t = document.getElementById('sim2-title');
            const d1 = document.getElementById('sim2-desc1');
            const d2 = document.getElementById('sim2-desc2');

            if (site === 'birth') {{
                t.textContent = 'रुनकता / सीही: सूरदास जन्मभूमि';
                d1.textContent = 'जन्म सन् 1478 में रुनकता (मथुरा) अथवा दिल्ली के पास सीही में माना जाता है।';
                d2.textContent = 'बचपन से ही विरक्त होकर प्रभु भक्ति में लीन हुए।';
            }} else if (site === 'gaughat') {{
                t.textContent = 'गऊघाट: आध्यात्मिक दीक्षा व निवास';
                d1.textContent = 'मथुरा और वृंदावन के बीच यमुना तट पर स्थित गऊघाट।';
                d2.textContent = 'यहीं महाप्रभु वल्लभाचार्य से भेंट हुई और पुष्टिमार्ग में दीक्षित हुए।';
            }} else if (site === 'temple') {{
                t.textContent = 'श्रीनाथ जी मंदिर: अष्टछाप कीर्तन';
                d1.textContent = 'गोवर्धन पर स्थित श्रीनाथ जी के मंदिर में नित्य पद-गायन।';
                d2.textContent = 'अष्टछाप के आठ कवियों में सर्वोच्च पद प्राप्त हुआ।';
            }} else {{
                t.textContent = 'पारसौली: महाप्रयाण (निधन)';
                d1.textContent = 'सन् 1583 में गोवर्धन के निकट पारसौली ग्राम में अंतिम सांस ली।';
                d2.textContent = 'विट्ठलनाथ जी ने कहा था: पुष्टिमार्ग को जहाज़ जात है, सो जाको कछु लेना होय सो लेउ!';
            }}
        }}

        // Lab 1.3
        function selectSim3Book(book) {{
            playTone(500, 'sine', 0.08);
            ['sursagar', 'sahitya', 'saravali'].forEach(b => {{
                const el = document.getElementById(`book-${{b}}`);
                if (el) el.className = 'p-2.5 rounded-xl bg-slate-950 border border-slate-800 text-center cursor-pointer hover:border-slate-700 transition';
            }});
            const active = document.getElementById(`book-${{book}}`);
            if (active) active.className = 'p-2.5 rounded-xl bg-violet-950/80 border-2 border-violet-500 text-center cursor-pointer transition shadow-lg';

            const t = document.getElementById('sim3-book-title');
            const d = document.getElementById('sim3-book-desc');

            if (book === 'sursagar') {{
                t.textContent = "ग्रंथ: 'सूरसागर' (महाकवि का अमर कीर्ति-स्तंभ)";
                d.textContent = "सवा लाख पदों में से वर्तमान में लगभग पाँच हजार पद उपलब्ध हैं। इसी के विश्व-प्रसिद्ध 'भ्रमरगीत' प्रसंग से कक्षा 10 में चार अमर पद संकलित हैं, जो प्रेम-मार्ग की ज्ञान-मार्ग पर विजय का उद्घोष करते हैं।";
            }} else if (book === 'sahitya') {{
                t.textContent = "ग्रंथ: 'साहित्य लहरी' (दृष्टकूट पद संग्रह)";
                d.textContent = "118 पदों का लघु संग्रह, जिसमें अर्थ-गोपनीयता, शब्द-क्रीड़ा और अलंकार-निरूपण की प्रधानता है।";
            }} else {{
                t.textContent = "ग्रंथ: 'सूर सारावली' (सृष्टि व अवतार कथा)";
                d.textContent = "1107 छंदों का बृहद ग्रंथ, जिसमें संसार की उत्पत्ति, भगवान के चौबीस अवतारों और भक्ति-दर्शन का निरूपण है।";
            }}
        }}

        // Lab 1.4
        let beeAngle = 0;
        function animateSim4Bee() {{
            playTone(450, 'triangle', 0.15);
            const bee = document.getElementById('sim4-bee');
            beeAngle = (beeAngle + 60) % 360;
            const x = 250 + Math.cos(beeAngle * Math.PI / 180) * 80;
            const y = 90 + Math.sin(beeAngle * Math.PI / 180) * 35;
            bee.setAttribute('transform', `translate(${{x}}, ${{y}})`);
            document.getElementById('sim4-desc').textContent = "भौंरा गोपियों और उद्धव के बीच मँडरा रहा है; गोपियों ने भौंरे को 'मधुकर' कहकर उद्धव पर व्यंग्य के बाण छोड़े!";
        }}

        // Lab 1.5
        function updateSim5Meter() {{
            const val = document.getElementById('sim5-slider').value;
            document.getElementById('sim5-meter-bar').style.width = `${{val}}%`;
            const valEl = document.getElementById('sim5-meter-val');
            const desc = document.getElementById('sim5-desc');

            if (val < 30) {{
                valEl.textContent = "अपरस (अनासक्त - उद्धव का शुष्क ज्ञान)";
                desc.textContent = "उद्धव प्रेम के सागर के पास रहकर भी 'सनेह तगा' से अछूते रहे (0% अनुराग)।";
            }} else if (val < 70) {{
                valEl.textContent = "मध्यम अनुराग";
                desc.textContent = "सांसारिक आकर्षण, किंतु अनन्य भक्ति का अभाव।";
            }} else {{
                valEl.textContent = "अनन्य प्रेम (गोपियों का आत्मसमर्पण)";
                desc.textContent = "'गुर चाँटी ज्यौं पागी' - जैसे चींटी गुड़ में चिपटती है, वैसे ही गोपियों का 100% एकनिष्ठ अनुराग!";
            }}
        }}

        // Lab 1.6
        function triggerSim6WaterDrop() {{
            playTone(680, 'sine', 0.1);
            const dropLeaf = document.getElementById('sim6-drop-leaf');
            const dropPot = document.getElementById('sim6-drop-pot');

            dropLeaf.setAttribute('cy', '65');
            setTimeout(() => dropLeaf.setAttribute('cy', '45'), 600);

            dropPot.setAttribute('cy', '75');
            setTimeout(() => dropPot.setAttribute('cy', '40'), 600);
        }}

        // Lab 1.7
        function attemptDetachAnts() {{
            playIncorrectSound();
            const alertEl = document.getElementById('sim7-alert');
            alertEl.classList.remove('hidden');
            setTimeout(() => alertEl.classList.add('hidden'), 4500);
        }}

        // Lab 1.8
        function updateSim8Heart() {{
            const days = document.getElementById('sim8-slider').value;
            document.getElementById('sim8-day-count').textContent = `${{days}} दिन व्यतीत`;
            document.getElementById('sim8-temp-val').textContent = `विरह ताप: ${{days}}° व्यथा`;
            const heart = document.getElementById('sim8-heart');
            const scale = 1 + (days / 300);
            heart.setAttribute('transform', `scale(${{scale}}) translate(${{(1 - scale) * 200}}, 0)`);
        }}

        // Lab 1.9
        function pourYogaGhee() {{
            playTone(740, 'sawtooth', 0.2);
            const flames = document.getElementById('sim9-flames');
            flames.setAttribute('transform', 'scale(1.3) translate(-75, -50)');
            document.getElementById('sim9-flame-text').textContent = "विरहाग्नि प्रचंड हो गई! 🔥";
            document.getElementById('sim9-desc').textContent = "उद्धव के निर्गुण योग संदेश ने विरहाग्नि में घी का काम किया; गोपियों का विरह-दुख शांत होने के बजाय और भड़क उठा!";
            setTimeout(() => {{
                flames.removeAttribute('transform');
                document.getElementById('sim9-flame-text').textContent = "विरह की आग";
            }}, 2000);
        }}

        // Lab 1.10
        function attemptReleaseHarilTwig() {{
            playTone(600, 'sine', 0.12);
            const twig = document.getElementById('sim10-twig');
            twig.setAttribute('stroke', '#22c55e');
            twig.setAttribute('stroke-width', '3');
            document.getElementById('sim10-desc').textContent = "दृढ़ बंधन! हारिल पक्षी अपने पंजों से लकड़ी को कभी अलग नहीं होने देता; गोपियों ने भी कृष्ण को हृदय में कसकर थाम रखा है!";
            setTimeout(() => {{
                twig.setAttribute('stroke', '#f59e0b');
                twig.setAttribute('stroke-width', '1.5');
            }}, 1500);
        }}

        // Lab 1.11
        function tasteKaruiKakari() {{
            playIncorrectSound();
            const lbl = document.getElementById('sim11-taste-lbl');
            lbl.textContent = "थू! कड़वी ककड़ी मुँह में जाते ही वमन (उल्टी) की स्थिति हो जाती है; योग संदेश गोपियों को इतना ही अरुचिकर लगा!";
            lbl.className = "text-[10px] text-rose-400 font-bold text-center";
        }}

        // Lab 1.12
        function toggleSim12Role(role) {{
            playTone(role === 'gokul' ? 620 : 420, 'sine', 0.1);
            const bGokul = document.getElementById('btn-sim12-gokul');
            const bMathura = document.getElementById('btn-sim12-mathura');
            const rTitle = document.getElementById('sim12-role-title');
            const beh = document.getElementById('sim12-behavior');
            const msg = document.getElementById('sim12-message');
            const sarc = document.getElementById('sim12-sarcasm');
            const desc = document.getElementById('sim12-desc');

            if (role === 'gokul') {{
                bGokul.className = 'px-2.5 py-1 rounded text-xs font-bold bg-amber-600 text-white transition';
                bMathura.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 transition';
                rTitle.textContent = "माखनचोर कान्हा (गोकुल)";
                beh.textContent = "सरल, सहज एवं निश्छल प्रेम";
                msg.textContent = "मधुर बाँसुरी की तान";
                sarc.textContent = "हृदय चुरा लेने वाला";
                desc.textContent = "गोकुल में कृष्ण सरल बाल-गोपाल और प्रेमी थे; गोपियाँ कहती हैं कि मथुरा जाकर वे राजा बनते ही राजनीतिज्ञ बन गए!";
            }} else {{
                bMathura.className = 'px-2.5 py-1 rounded text-xs font-bold bg-violet-600 text-white transition';
                bGokul.className = 'px-2.5 py-1 rounded text-xs font-bold bg-slate-800 text-slate-300 transition';
                rTitle.textContent = "राजा श्रीकृष्ण (मथुरा)";
                beh.textContent = "कूटनीति एवं राजनीति";
                msg.textContent = "दूत (उद्धव) द्वारा योग-संदेश";
                sarc.textContent = "बढ़ी बुद्धि जानी जो उनकी";
                desc.textContent = "गोपियाँ व्यंग्य करती हैं: कृष्ण पहले से ही चतुर थे, अब गुरुओं से राजनीति के बड़े ग्रंथ पढ़कर और भी छल-प्रवीण हो गए हैं!";
            }}
        }}

        // Lab 1.14
        function highlightSim14Alankar(type) {{
            playTone(550, 'sine', 0.08);
            const q = document.getElementById('sim14-quote-display');
            const exp = document.getElementById('sim14-quote-exp');

            if (type === 'rupak') {{
                q.innerHTML = '"प्रीति-नदी मैं पाउँ न बोरयौ" ➔ <strong class="text-cyan-400">रूपक अलंकार:</strong> प्रेम पर नदी का अभेद आरोप!';
                exp.textContent = "यहाँ प्रेम को नदी का रूप दिया गया है, इसलिए रूपक अलंकार है।";
            }} else if (type === 'drishtant') {{
                q.innerHTML = '"पुरइनि पात रहत जल भीतर... ज्यौं जल माहँ तेल की गागरि" ➔ <strong class="text-amber-400">दृष्टांत अलंकार:</strong>';
                exp.textContent = "कमल के पत्ते और तेल की मटकी के उदाहरण से उद्धव की अनासक्ति को प्रत्यक्ष समझाया गया है।";
            }} else if (type === 'upma') {{
                q.innerHTML = '"गुर चाँटी ज्यौं पागी" एवं "ज्यौं करुई ककरी" ➔ <strong class="text-emerald-400">उपमा अलंकार:</strong>';
                exp.textContent = "'ज्यौं' वाचक शब्द के प्रयोग से उपमेय और उपमान की तुलना की गई है।";
            }} else {{
                q.innerHTML = '"कान्ह-कान्ह" एवं "सुनि-सुनि" ➔ <strong class="text-purple-400">पुनरुक्ति प्रकाश अलंकार:</strong>';
                exp.textContent = "एक ही शब्द की बिना अर्थ-परिवर्तन के संगीतमय आवृत्ति हुई है।";
            }}
        }}

        // Lab 1.15
        function flipSim15Word(w) {{
            playTone(500, 'sine', 0.08);
            const term = document.getElementById('sim15-word-term');
            const def = document.getElementById('sim15-word-def');

            if (w === 'apras') {{
                term.textContent = "अपरस";
                def.textContent = "अलिप्त, नीरस, अछूता (जो प्रेम-रस से वंचित रहा हो)।";
            }} else if (w === 'bitha') {{
                term.textContent = "बिथा";
                def.textContent = "व्यथा, विरह की शारीरिक एवं मानसिक पीड़ा।";
            }} else if (w === 'byadhi') {{
                term.textContent = "ब्याधि";
                def.textContent = "रोग, शारीरिक अथवा मानसिक कष्ट पहुँचाने वाली बीमारी (योग-संदेश)।";
            }} else {{
                term.textContent = "मन चक्री";
                def.textContent = "जिनका मन चंचल, डांवाडोल और अस्थिर हो (कुम्हार के चाक की भाँति घूमने वाला)।";
            }}
        }}

        // Lab 1.16
        const debateLines = [
            "",
            "तर्क 1 (बड़भागी व्यंग्य): हे उद्धव! तुम बहुत 'भाग्यवान' हो जो प्रेम के सागर के पास रहकर भी प्रेम-बंधन से अछूते रहे। तुम जैसे भाग्यहीन संसार में और कौन होगा!",
            "तर्क 2 (हारिल की लकड़ी): हमारे लिए कृष्ण हारिल पक्षी की लकड़ी के समान हैं। हमने मन, कर्म और वचन से कृष्ण को हृदय में पकड़ रखा है; तुम्हारा योग हमारे किसी काम का नहीं!",
            "तर्क 3 (कड़वी ककड़ी): तुम्हारा यह योग संदेश सुनते ही कड़वी ककड़ी जैसा लगता है। यह बीमारी उन लोगों को सौंपो जिनके मन चकरी की तरह भटकते रहते हैं!",
            "तर्क 4 (सच्चा राजधर्म): जो कृष्ण दूसरों को अन्याय से छुड़ाते थे, वे आज स्वयं हमारे साथ छल कर रहे हैं। राजा का धर्म प्रजा को सताना नहीं, बल्कि उसकी रक्षा करना है!"
        ];

        function playSim16Debate(num) {{
            playTone(520 + num * 40, 'sine', 0.1);
            document.getElementById('sim16-dialogue-text').textContent = debateLines[num];
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
    target_path = "public/animations/surdas-ke-pad.html"
    os.makedirs(os.path.dirname(target_path), exist_ok=True)
    with open(target_path, "w", encoding="utf-8") as f:
        f.write(html_output)
    print(f"Successfully generated {target_path} ({len(html_output)} bytes)")

