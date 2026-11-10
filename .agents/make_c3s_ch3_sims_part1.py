#!/usr/bin/env python3
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 3: Celebrating Festivals
Simulators Part 1: Simulators 1 to 8
"""

simulators_part1 = {
    1: """
<div class="sim-container" style="background: linear-gradient(180deg, #1e293b 0%, #0f172a 100%); border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🏔️ Himalayan Mountain Journey Simulator</h3>
    <span id="altMeter1" style="background: #0369a1; padding: 4px 10px; border-radius: 20px; font-weight: bold; font-size: 0.85rem;">Altitude: 1,200 m (Pine Belt)</span>
  </div>
  
  <div style="position: relative; width: 100%; height: 260px; background: #0f172a; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg id="mountainSvg1" viewBox="0 0 600 260" style="width: 100%; height: 100%;">
      <!-- Distant Snowy Peaks -->
      <polygon points="50,140 130,40 210,140" fill="#cbd5e1" stroke="#94a3b8" />
      <polygon points="110,65 130,40 150,65" fill="#f8fafc" />
      <polygon points="180,150 290,20 400,150" fill="#94a3b8" stroke="#64748b" />
      <polygon points="265,50 290,20 315,50" fill="#f8fafc" />
      <polygon points="370,160 480,50 580,160" fill="#cbd5e1" stroke="#94a3b8" />
      <polygon points="455,75 480,50 505,75" fill="#f8fafc" />

      <!-- Mountain Slopes -->
      <path d="M0,260 L0,180 Q150,130 300,190 T600,160 L600,260 Z" fill="#1e3a5f" opacity="0.6"/>
      
      <!-- Winding Hairpin Road -->
      <path id="hairpinRoad" d="M 40,240 Q 150,230 240,225 Q 380,220 540,210 Q 580,190 540,170 Q 350,160 180,145 Q 60,135 120,110 Q 220,90 420,80 Q 520,75 560,60" fill="none" stroke="#475569" stroke-width="18" stroke-linecap="round"/>
      <path d="M 40,240 Q 150,230 240,225 Q 380,220 540,210 Q 580,190 540,170 Q 350,160 180,145 Q 60,135 120,110 Q 220,90 420,80 Q 520,75 560,60" fill="none" stroke="#fef08a" stroke-width="2" stroke-dasharray="6,6" stroke-linecap="round"/>

      <!-- Coniferous Needle Trees -->
      <g id="coniferTrees">
        <!-- Tree 1 -->
        <polygon points="80,230 70,250 90,250" fill="#15803d" />
        <polygon points="80,220 72,235 88,235" fill="#16a34a" />
        <rect x="78" y="250" width="4" height="8" fill="#78350f" />
        <!-- Tree 2 -->
        <polygon points="220,180 212,196 228,196" fill="#15803d" />
        <polygon points="220,170 214,183 226,183" fill="#16a34a" />
        <rect x="218" y="196" width="4" height="6" fill="#78350f" />
        <!-- Tree 3 -->
        <polygon points="380,120 373,135 387,135" fill="#15803d" />
        <polygon points="380,110 375,122 385,122" fill="#16a34a" />
        <rect x="378" y="135" width="4" height="6" fill="#78350f" />
        <!-- Tree 4 -->
        <polygon points="510,130 502,148 518,148" fill="#15803d" />
        <rect x="508" y="148" width="4" height="7" fill="#78350f" />
      </g>

      <!-- Passenger Bus -->
      <g id="travelBus" transform="translate(40, 230)">
        <rect x="-16" y="-12" width="32" height="18" rx="4" fill="#f59e0b" stroke="#78350f" stroke-width="1.5" />
        <rect x="-12" y="-10" width="7" height="6" rx="1" fill="#e0f2fe" />
        <rect x="-3" y="-10" width="7" height="6" rx="1" fill="#e0f2fe" />
        <rect x="6" y="-10" width="7" height="6" rx="1" fill="#e0f2fe" />
        <circle cx="-9" cy="8" r="4" fill="#1e293b" />
        <circle cx="9" cy="8" r="4" fill="#1e293b" />
        <!-- Headlight beam -->
        <polygon points="16,-6 40,-12 40,0" fill="#fef08a" opacity="0.4" />
      </g>
    </svg>
  </div>

  <div style="margin-top: 12px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <button onclick="sim1Climb()" style="background: #0284c7; color: white; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-weight: bold;">🧗 Drive Up Hairpin Bends</button>
    <button onclick="sim1ToggleSnow()" style="background: #475569; color: white; border: none; padding: 8px 12px; border-radius: 6px; cursor: pointer; font-weight: bold;">❄️ Toggle Mountain Snow</button>
  </div>
  <div id="sim1Feedback" style="margin-top: 8px; font-size: 0.85rem; color: #bae6fd; text-align: center; min-height: 20px;">
    Click "Drive Up Hairpin Bends" to observe sharp curves and changing vegetation zones!
  </div>
</div>

<script>
let sim1Step = 0;
const sim1Waypoints = [
  {x: 40, y: 230, alt: "1,200 m (Foothills & Broadleaf)", text: "Starting ascent: Broad valley floor with mild climate."},
  {x: 240, y: 220, alt: "1,600 m (Entering Pine Belt)", text: "First hairpin curve: Coniferous pines with needle leaves appear."},
  {x: 480, y: 190, alt: "2,100 m (Dense Deodar Forest)", text: "Steep slope: Sloping branches help snow slide off naturally."},
  {x: 320, y: 155, alt: "2,500 m (Sharp Hairpin Turn)", text: "Hairpin bend: Bus slows down sharply to safely round the cliff edge."},
  {x: 140, y: 125, alt: "2,900 m (Alpine Rhododendrons)", text: "High terrace: Wild red buransh flowers blossom along rocky ledges."},
  {x: 460, y: 70, alt: "3,300 m (Snowline & Crest)", text: "Alpine peak reached! Cold winds and panoramic snow-capped Himalayan peaks."}
];
let sim1SnowOn = false;

function sim1Climb() {
  sim1Step = (sim1Step + 1) % sim1Waypoints.length;
  const wp = sim1Waypoints[sim1Step];
  const bus = document.getElementById('travelBus');
  bus.setAttribute('transform', `translate(${wp.x}, ${wp.y})`);
  document.getElementById('altMeter1').innerText = `Altitude: ${wp.alt}`;
  document.getElementById('sim1Feedback').innerText = wp.text;
}

function sim1ToggleSnow() {
  sim1SnowOn = !sim1SnowOn;
  const trees = document.getElementById('coniferTrees');
  if(sim1SnowOn) {
    trees.style.filter = "drop-shadow(0px -3px 2px #ffffff)";
    document.getElementById('sim1Feedback').innerText = "Snowfall blankets the slope! Notice how conical tree shapes prevent heavy snow buildup.";
  } else {
    trees.style.filter = "none";
    document.getElementById('sim1Feedback').innerText = "Spring sunshine melts the snow, watering alpine meadows and awakening wild blooms.";
  }
}
</script>
""",

    2: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 12px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🛑 Universal Road Signboard Matcher</h3>
    <span id="scoreBadge2" style="background: #1e293b; border: 1px solid #38bdf8; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem;">Recognized: 0 / 4</span>
  </div>

  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 10px; margin-bottom: 12px;">
    <!-- Sign 1: No Horn -->
    <div onclick="sim2SelectSign(0)" id="signCard0" style="background: #1e293b; border: 2px solid #475569; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer; transition: all 0.2s;">
      <svg viewBox="0 0 60 60" style="width: 50px; height: 50px; display: block; margin: 0 auto;">
        <circle cx="30" cy="30" r="26" fill="white" stroke="#dc2626" stroke-width="5" />
        <path d="M18,30 L28,24 L28,36 Z M28,27 L36,22 L36,38 L28,33" fill="#1e293b"/>
        <line x1="12" y1="12" x2="48" y2="48" stroke="#dc2626" stroke-width="5" />
      </svg>
      <div style="font-size: 0.75rem; margin-top: 4px; font-weight: bold;">No Horn</div>
    </div>

    <!-- Sign 2: Speed Breaker -->
    <div onclick="sim2SelectSign(1)" id="signCard1" style="background: #1e293b; border: 2px solid #475569; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer; transition: all 0.2s;">
      <svg viewBox="0 0 60 60" style="width: 50px; height: 50px; display: block; margin: 0 auto;">
        <polygon points="30,6 56,52 4,52" fill="white" stroke="#dc2626" stroke-width="4" stroke-linejoin="round" />
        <path d="M16,42 Q23,32 30,32 Q37,32 44,42" fill="none" stroke="#1e293b" stroke-width="4" stroke-linecap="round"/>
      </svg>
      <div style="font-size: 0.75rem; margin-top: 4px; font-weight: bold;">Speed Breaker</div>
    </div>

    <!-- Sign 3: School Ahead -->
    <div onclick="sim2SelectSign(2)" id="signCard2" style="background: #1e293b; border: 2px solid #475569; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer; transition: all 0.2s;">
      <svg viewBox="0 0 60 60" style="width: 50px; height: 50px; display: block; margin: 0 auto;">
        <polygon points="30,6 56,52 4,52" fill="white" stroke="#dc2626" stroke-width="4" stroke-linejoin="round" />
        <circle cx="26" cy="24" r="3.5" fill="#1e293b" />
        <rect x="23" y="28" width="6" height="12" fill="#1e293b" />
        <circle cx="36" cy="26" r="3" fill="#1e293b" />
        <rect x="33" y="30" width="5" height="10" fill="#1e293b" />
      </svg>
      <div style="font-size: 0.75rem; margin-top: 4px; font-weight: bold;">School Ahead</div>
    </div>

    <!-- Sign 4: Falling Rocks -->
    <div onclick="sim2SelectSign(3)" id="signCard3" style="background: #1e293b; border: 2px solid #475569; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer; transition: all 0.2s;">
      <svg viewBox="0 0 60 60" style="width: 50px; height: 50px; display: block; margin: 0 auto;">
        <polygon points="30,6 56,52 4,52" fill="white" stroke="#dc2626" stroke-width="4" stroke-linejoin="round" />
        <polygon points="8,50 8,24 24,50" fill="#64748b" />
        <circle cx="34" cy="30" r="3" fill="#475569" />
        <circle cx="42" cy="40" r="4" fill="#334155" />
      </svg>
      <div style="font-size: 0.75rem; margin-top: 4px; font-weight: bold;">Falling Rocks</div>
    </div>
  </div>

  <div id="sim2DisplayBox" style="background: #1e293b; border-left: 4px solid #38bdf8; padding: 12px; border-radius: 6px; min-height: 70px;">
    <div id="sim2Title" style="font-weight: bold; color: #38bdf8; font-size: 0.95rem;">Select any signboard above</div>
    <div id="sim2Desc" style="font-size: 0.85rem; color: #cbd5e1; margin-top: 4px;">Click any signboard to inspect its shape, color code, safety rule, and practical driver action on mountain highways.</div>
  </div>
</div>

<script>
const sim2Data = [
  {title: "🚫 Prohibitory Sign: No Horn Zone", desc: "Circular signs with red borders indicate strict prohibitions. Used near hospitals, schools, and silent mountain nature reserves to eliminate harmful noise pollution.", rule: "Driver Action: Do not sound the vehicle horn under any circumstances."},
  {title: "⚠️ Warning Sign: Speed Breaker Ahead", desc: "Triangular signs with red borders warn of upcoming roadway physical hazards. Warns drivers that a raised asphalt hump is approaching.", rule: "Driver Action: Decelerate smoothly to 15-20 km/h to prevent passenger jolting and axle damage."},
  {title: "⚠️ Warning Sign: School Ahead", desc: "Triangular warning sign featuring crossing schoolchildren. Positioned 50-100 meters before educational campus entry gates.", rule: "Driver Action: Slow down significantly, scan sidewalks actively, and be prepared to stop immediately for crossing students."},
  {title: "⚠️ Mountain Hazard: Falling Rocks", desc: "Triangular warning sign highlighting geological vulnerability on steep mountain cuttings where loose rocks frequently tumble after rain.", rule: "Driver Action: Maintain vigilant speed, scan high cliff faces, do not park alongside rock faces, and pass promptly."}
];
let sim2Found = new Set();

function sim2SelectSign(idx) {
  for(let i=0; i<4; i++) {
    document.getElementById(`signCard${i}`).style.borderColor = (i === idx) ? '#38bdf8' : '#475569';
  }
  const item = sim2Data[idx];
  document.getElementById('sim2Title').innerText = item.title;
  document.getElementById('sim2Desc').innerHTML = `<strong>Meaning:</strong> ${item.desc}<br><strong style="color: #4ade80;">Safety Protocol:</strong> ${item.rule}`;
  sim2Found.add(idx);
  document.getElementById('scoreBadge2').innerText = `Recognized: ${sim2Found.size} / 4`;
}
</script>
""",

    3: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌱 Terraced Mountain Garden Explorer</h3>
    <button onclick="sim3ToggleRain()" id="rainBtn3" style="background: #0284c7; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">🌧️ Simulate Gentle Rain</button>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Stepped Mountain Terraces -->
      <!-- Top Terrace -->
      <polygon points="50,40 220,40 220,70 50,70" fill="#3f2e21" stroke="#292017" stroke-width="2"/>
      <rect x="50" y="38" width="170" height="6" fill="#15803d" />
      
      <!-- Middle Terrace -->
      <polygon points="150,90 350,90 350,120 150,120" fill="#3f2e21" stroke="#292017" stroke-width="2"/>
      <rect x="150" y="88" width="200" height="6" fill="#15803d" />

      <!-- Bottom Terrace -->
      <polygon points="260,140 480,140 480,170 260,170" fill="#3f2e21" stroke="#292017" stroke-width="2"/>
      <rect x="260" y="138" width="220" height="6" fill="#15803d" />

      <!-- Stone retaining walls -->
      <pattern id="stonePat" width="10" height="10" patternUnits="userSpaceOnUse">
        <rect width="10" height="10" fill="#64748b" />
        <line x1="0" y1="5" x2="10" y2="5" stroke="#334155" />
        <line x1="5" y1="0" x2="5" y2="5" stroke="#334155" />
      </pattern>
      <rect x="210" y="40" width="15" height="30" fill="url(#stonePat)" />
      <rect x="340" y="90" width="15" height="30" fill="url(#stonePat)" />
      <rect x="470" y="140" width="15" height="30" fill="url(#stonePat)" />

      <!-- Terrace 1 Flowers: Velvet Roses -->
      <g onclick="sim3Inspect('rose')" style="cursor: pointer;">
        <circle cx="80" cy="30" r="7" fill="#e11d48" />
        <circle cx="120" cy="32" r="6" fill="#e11d48" />
        <circle cx="160" cy="29" r="7" fill="#e11d48" />
        <text x="100" y="20" fill="#fecdd3" font-size="9" font-weight="bold">Rose Bed</text>
      </g>

      <!-- Terrace 2 Flowers: Golden Marigolds -->
      <g onclick="sim3Inspect('marigold')" style="cursor: pointer;">
        <circle cx="190" cy="80" r="7" fill="#f59e0b" />
        <circle cx="230" cy="82" r="8" fill="#d97706" />
        <circle cx="270" cy="79" r="7" fill="#f59e0b" />
        <text x="210" y="70" fill="#fef08a" font-size="9" font-weight="bold">Marigolds</text>
      </g>

      <!-- Terrace 3 Flowers: Alpine Tulips -->
      <g onclick="sim3Inspect('tulip')" style="cursor: pointer;">
        <!-- Tulip cups -->
        <path d="M 310,135 C 305,120 305,115 315,115 C 320,122 320,122 325,115 C 335,115 335,120 330,135 Z" fill="#ec4899" />
        <path d="M 360,135 C 355,120 355,115 365,115 C 370,122 370,122 375,115 C 385,115 385,120 380,135 Z" fill="#8b5cf6" />
        <path d="M 410,135 C 405,120 405,115 415,115 C 420,122 420,122 425,115 C 435,115 435,120 430,135 Z" fill="#facc15" />
        <text x="340" y="105" fill="#fbcfe8" font-size="9" font-weight="bold">Alpine Tulips</text>
      </g>

      <!-- Rain animation drops -->
      <g id="rainGroup3" opacity="0">
        <line x1="100" y1="10" x2="95" y2="25" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <line x1="200" y1="20" x2="195" y2="35" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <line x1="300" y1="15" x2="295" y2="30" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
        <line x1="400" y1="30" x2="395" y2="45" stroke="#38bdf8" stroke-width="1.5" stroke-dasharray="4,4"/>
      </g>
    </svg>
  </div>

  <div id="sim3Info" style="margin-top: 10px; background: #1e293b; padding: 10px 12px; border-radius: 6px; font-size: 0.85rem; color: #cbd5e1; border-left: 3px solid #10b981;">
    💡 <strong>Stepped Terrace Advantage:</strong> Flat steps slow down rushing water, trapping nutrient-rich topsoil and preventing hillside erosion. Click any flower bed to inspect its botanical features!
  </div>
</div>

<script>
let sim3Raining = false;
function sim3ToggleRain() {
  sim3Raining = !sim3Raining;
  const rg = document.getElementById('rainGroup3');
  const btn = document.getElementById('rainBtn3');
  if(sim3Raining) {
    rg.setAttribute('opacity', '1');
    btn.innerText = '☀️ Stop Rain';
    document.getElementById('sim3Info').innerHTML = '🌧️ <strong>Rainfall in action:</strong> Notice how water gently trickles from step to step instead of violently washing away fertile soil. Stepped terraces preserve crops and native flora!';
  } else {
    rg.setAttribute('opacity', '0');
    btn.innerText = '🌧️ Simulate Gentle Rain';
    document.getElementById('sim3Info').innerHTML = '☀️ <strong>Terrace farming:</strong> When rain stops, moisture stays soaked inside the flat terraced beds, nurturing roots on steep mountain gradients.';
  }
}

function sim3Inspect(flower) {
  if(flower === 'rose') {
    document.getElementById('sim3Info').innerHTML = '🌹 <strong>Mountain Roses:</strong> Fragrant multi-layered petals attract pollinating insects while deep taproots anchor firmly in rocky terrace soil.';
  } else if(flower === 'marigold') {
    document.getElementById('sim3Info').innerHTML = '🌼 <strong>Golden Marigolds:</strong> Vibrant composite flowers used extensively in festive garlands. Natural insect-repelling oils protect neighboring crops!';
  } else if(flower === 'tulip') {
    document.getElementById('sim3Info').innerHTML = '🌷 <strong>Alpine Tulips:</strong> Perennials growing from underground bulbs that survive cold winter freezes, bursting into vibrant cup-shaped blossoms in springtime.';
  }
}
</script>
""",

    4: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌷 Kashmir Tulip Bloom & Haakh Meal</h3>
    <span id="stageBadge4" style="background: #0369a1; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Stage: Spring Blossom</span>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: linear-gradient(180deg, #38bdf8 0%, #bae6fd 60%, #15803d 60%, #166534 100%); border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Zabarwan mountain backdrop -->
      <polygon points="40,126 120,40 200,126" fill="#64748b" opacity="0.6"/>
      <polygon points="100,60 120,40 140,60" fill="#ffffff" />
      <polygon points="170,126 270,30 370,126" fill="#475569" opacity="0.7"/>
      <polygon points="245,55 270,30 295,55" fill="#ffffff" />
      <polygon points="330,126 440,45 520,126" fill="#64748b" opacity="0.6"/>

      <!-- Terraced Rows of Tulips -->
      <g id="tulipField">
        <!-- Row 1: Crimson -->
        <path d="M 60,160 Q 60,140 65,130 Q 70,140 70,160 Z" fill="#dc2626" />
        <line x1="65" y1="160" x2="65" y2="180" stroke="#166534" stroke-width="3" />
        
        <path d="M 110,160 Q 110,140 115,130 Q 120,140 120,160 Z" fill="#dc2626" />
        <line x1="115" y1="160" x2="115" y2="180" stroke="#166534" stroke-width="3" />

        <path d="M 160,160 Q 160,140 165,130 Q 170,140 170,160 Z" fill="#dc2626" />
        <line x1="165" y1="160" x2="165" y2="180" stroke="#166534" stroke-width="3" />

        <!-- Row 2: Golden Yellow -->
        <path d="M 210,160 Q 210,140 215,130 Q 220,140 220,160 Z" fill="#eab308" />
        <line x1="215" y1="160" x2="215" y2="180" stroke="#166534" stroke-width="3" />

        <path d="M 260,160 Q 260,140 265,130 Q 270,140 270,160 Z" fill="#eab308" />
        <line x1="265" y1="160" x2="265" y2="180" stroke="#166534" stroke-width="3" />

        <path d="M 310,160 Q 310,140 315,130 Q 320,140 320,160 Z" fill="#eab308" />
        <line x1="315" y1="160" x2="315" y2="180" stroke="#166534" stroke-width="3" />

        <!-- Row 3: Purple / White -->
        <path d="M 360,160 Q 360,140 365,130 Q 370,140 370,160 Z" fill="#9333ea" />
        <line x1="365" y1="160" x2="365" y2="180" stroke="#166534" stroke-width="3" />

        <path d="M 410,160 Q 410,140 415,130 Q 420,140 420,160 Z" fill="#f8fafc" stroke="#cbd5e1" />
        <line x1="415" y1="160" x2="415" y2="180" stroke="#166534" stroke-width="3" />
      </g>

      <!-- Winter Snow Blanket Overlay (hidden in spring) -->
      <rect id="snowBlanket" x="0" y="126" width="500" height="84" fill="#f8fafc" opacity="0"/>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr 1fr; gap: 8px;">
    <button onclick="sim4SetSeason('winter')" style="background: #475569; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.8rem;">❄️ Winter Dormancy</button>
    <button onclick="sim4SetSeason('spring')" style="background: #16a34a; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.8rem;">🌷 Spring Blooming</button>
    <button onclick="sim4ShowHaakh()" style="background: #d97706; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.8rem;">🍲 Kashmiri Haakh Meal</button>
  </div>

  <div id="sim4Info" style="margin-top: 8px; font-size: 0.85rem; color: #bae6fd; min-height: 38px; line-height: 1.4;">
    Click "Spring Blooming" to admire millions of colorful tulips at Asia's largest garden in Srinagar!
  </div>
</div>

<script>
function sim4SetSeason(season) {
  const sb = document.getElementById('snowBlanket');
  const tf = document.getElementById('tulipField');
  const badge = document.getElementById('stageBadge4');
  if(season === 'winter') {
    sb.setAttribute('opacity', '0.9');
    tf.style.display = 'none';
    badge.innerText = 'Stage: Winter Dormancy';
    badge.style.background = '#475569';
    document.getElementById('sim4Info').innerHTML = '❄️ <strong>Underground Survival:</strong> Beneath the snow blanket, tulip bulbs conserve stored starches safely in cold soil, awaiting springtime warmth.';
  } else {
    sb.setAttribute('opacity', '0');
    tf.style.display = 'block';
    badge.innerText = 'Stage: Spring Bloom';
    badge.style.background = '#0369a1';
    document.getElementById('sim4Info').innerHTML = '🌷 <strong>Spring Extravaganza:</strong> Warm April sunshine triggers vigorous stem growth and brilliant multi-colored blossoms, welcoming visitors worldwide to Kashmir!';
  }
}

function sim4ShowHaakh() {
  document.getElementById('sim4Info').innerHTML = '🍲 <strong>Traditional Kashmiri Haakh:</strong> Wholesome collard greens cooked in mustard oil with mild mountain spices, served with fragrant hot rice during family festival lunches.';
}
</script>
""",

    5: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌺 Doorstep Spring Floral Welcome</h3>
    <span id="blessingBadge5" style="background: #1e293b; border: 1px solid #facc15; color: #facc15; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem;">Doorstep Offerings: 0</span>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Traditional Mountain House Frontage -->
      <rect x="80" y="20" width="340" height="170" fill="#78350f" stroke="#451a03" stroke-width="3"/>
      <!-- Wooden Door -->
      <rect x="200" y="60" width="100" height="130" fill="#92400e" stroke="#451a03" stroke-width="2"/>
      <circle cx="215" cy="125" r="4" fill="#fbbf24" />
      <line x1="250" y1="60" x2="250" y2="190" stroke="#451a03" stroke-width="1.5"/>

      <!-- Doorstep Threshold (Stone) -->
      <polygon points="170,190 330,190 350,210 150,210" fill="#94a3b8" stroke="#475569" />

      <!-- Flower arrangement on threshold (interactive) -->
      <g id="doorstepFlowers" opacity="0">
        <!-- Mustard blossoms (yellow) -->
        <circle cx="230" cy="198" r="5" fill="#facc15" />
        <circle cx="240" cy="195" r="6" fill="#facc15" />
        <circle cx="248" cy="200" r="5" fill="#fde047" />
        <!-- Scarlet Buransh blossoms (red) -->
        <circle cx="260" cy="197" r="7" fill="#dc2626" />
        <circle cx="270" cy="195" r="8" fill="#ef4444" />
        <circle cx="278" cy="200" r="6" fill="#b91c1c" />
      </g>

      <!-- Elder Blessing Sunburst Effect -->
      <g id="blessingSunburst" opacity="0">
        <circle cx="250" cy="50" r="22" fill="#fbbf24" opacity="0.3"/>
        <text x="250" y="55" text-anchor="middle" fill="#fef08a" font-size="12" font-weight="bold">✨ Elder Blessings ✨</text>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <button onclick="sim5PlaceFlowers()" style="background: #e11d48; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🌸 Place Buransh & Mustard</button>
    <button onclick="sim5ReceiveBlessing()" style="background: #d97706; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🍯 Receive Sweets & Blessings</button>
  </div>

  <div id="sim5Feedback" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 36px; line-height: 1.4;">
    Click "Place Buransh & Mustard" to leave morning spring greetings on the household doorstep!
  </div>
</div>

<script>
let sim5Placed = false;
let sim5Count = 0;

function sim5PlaceFlowers() {
  sim5Placed = true;
  sim5Count++;
  document.getElementById('doorstepFlowers').setAttribute('opacity', '1');
  document.getElementById('blessingBadge5').innerText = `Doorstep Offerings: ${sim5Count}`;
  document.getElementById('sim5Feedback').innerHTML = '🌸 <strong>Auspicious Spring Offering:</strong> Fresh scarlet buransh (Rhododendron) and golden mustard blossoms placed at the threshold wish health and prosperity to neighbors.';
}

function sim5ReceiveBlessing() {
  if(!sim5Placed) {
    document.getElementById('sim5Feedback').innerText = 'Please place the spring flowers at the doorstep first to greet the household!';
    return;
  }
  document.getElementById('blessingSunburst').setAttribute('opacity', '1');
  document.getElementById('sim5Feedback').innerHTML = '✨ <strong>Generous Elder Blessing:</strong> Elders open the door with radiant smiles, gifting roasted grains, jaggery sweets, and heartfelt blessings for long life and happiness!';
}
</script>
""",

    6: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">✨ Vishu Kani Auspicious Vessel</h3>
    <span id="vishuItemCount" style="background: #854d0e; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Arranged: 0 / 4</span>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Wooden Altar Table -->
      <rect x="60" y="150" width="380" height="50" fill="#5c2c16" stroke="#381a0e" stroke-width="2"/>
      
      <!-- Bronze Mirror (Aranmula Kannadi) behind uruli -->
      <g id="kannadiMirror">
        <ellipse cx="250" cy="80" rx="35" ry="45" fill="#fef08a" stroke="#ca8a04" stroke-width="4"/>
        <ellipse cx="250" cy="80" rx="27" ry="37" fill="#fef9c3" opacity="0.6"/>
        <rect x="246" y="125" width="8" height="30" fill="#ca8a04" />
      </g>

      <!-- Polished Bell-Metal Uruli Vessel -->
      <ellipse cx="250" cy="155" rx="90" ry="24" fill="#ca8a04" stroke="#854d0e" stroke-width="3"/>
      <ellipse cx="250" cy="153" rx="84" ry="20" fill="#eab308" />

      <!-- Items arranged inside Uruli (initially hidden) -->
      <!-- 1: Golden Cucumber (Kani Vellari) & Mango -->
      <g id="vItemHarvest" opacity="0">
        <ellipse cx="220" cy="150" rx="22" ry="12" fill="#facc15" stroke="#ca8a04" />
        <ellipse cx="275" cy="152" rx="14" ry="9" fill="#84cc16" stroke="#4d7c0f" />
        <text x="220" y="153" text-anchor="middle" font-size="8" fill="#713f12">Cucumber</text>
      </g>

      <!-- 2: Kani Konna Flowers (Golden Amaltas) -->
      <g id="vItemKonna" opacity="0">
        <circle cx="250" cy="140" r="5" fill="#fef08a" />
        <circle cx="242" cy="144" r="6" fill="#facc15" />
        <circle cx="258" cy="143" r="6" fill="#facc15" />
        <circle cx="236" cy="148" r="5" fill="#eab308" />
        <circle cx="264" cy="147" r="5" fill="#eab308" />
        <path d="M 250,135 Q 240,150 230,158" stroke="#65a30d" stroke-width="1.5" fill="none"/>
      </g>

      <!-- 3: Rice Grains & Shiny Gold Coins -->
      <g id="vItemCoins" opacity="0">
        <ellipse cx="250" cy="155" rx="50" ry="10" fill="#fef08a" opacity="0.7"/>
        <circle cx="240" cy="156" r="4" fill="#fbbf24" stroke="#b45309" />
        <circle cx="252" cy="157" r="4.5" fill="#fbbf24" stroke="#b45309" />
        <circle cx="262" cy="155" r="4" fill="#fbbf24" stroke="#b45309" />
      </g>

      <!-- 4: Traditional Nilavilakku Oil Lamp -->
      <g id="vItemLamp" opacity="0">
        <rect x="110" y="100" width="6" height="50" fill="#ca8a04" />
        <ellipse cx="113" cy="150" rx="16" ry="6" fill="#ca8a04" />
        <ellipse cx="113" cy="100" rx="12" ry="4" fill="#ca8a04" />
        <path d="M 113,98 Q 113,85 116,80 Q 119,85 113,98 Z" fill="#f97316" />
        <circle cx="114" cy="88" r="5" fill="#fef08a" opacity="0.6"/>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
    <button onclick="sim6Toggle(0)" id="vBtn0" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🥒 Cucumber & Mango</button>
    <button onclick="sim6Toggle(1)" id="vBtn1" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌼 Kani Konna</button>
    <button onclick="sim6Toggle(2)" id="vBtn2" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🪙 Gold Coins & Rice</button>
    <button onclick="sim6Toggle(3)" id="vBtn3" style="background: #334155; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🪔 Nilavilakku Lamp</button>
  </div>

  <div id="sim6Desc" style="margin-top: 8px; font-size: 0.85rem; color: #fde047; min-height: 36px; line-height: 1.4;">
    Click items above to assemble the sacred Vishu Kani in the traditional bell-metal Uruli!
  </div>
</div>

<script>
let sim6Items = [false, false, false, false];
const sim6InfoTexts = [
  "🥒 <strong>Kani Vellari & Mango:</strong> Golden yellow cucumber and fresh raw mango represent the agricultural fruits of the earth and the anticipation of sweet summer harvest.",
  "🌼 <strong>Kani Konna (Cassia fistula):</strong> Radiant hanging golden shower blossoms herald the arrival of spring in Kerala and symbolize prosperity.",
  "🪙 <strong>Rice Grains & Gold Coins:</strong> Staple cereals and shiny coins express gratitude for food security and invite abundance into the household.",
  "🪔 <strong>Illuminated Nilavilakku:</strong> The bronze oil lamp casts a warm glow, reflected in the bronze mirror so the New Year opens with light, peace, and purity."
];

function sim6Toggle(idx) {
  sim6Items[idx] = !sim6Items[idx];
  const ids = ['vItemHarvest', 'vItemKonna', 'vItemCoins', 'vItemLamp'];
  const btn = document.getElementById(`vBtn${idx}`);
  document.getElementById(ids[idx]).setAttribute('opacity', sim6Items[idx] ? '1' : '0');
  btn.style.background = sim6Items[idx] ? '#0284c7' : '#334155';
  
  const count = sim6Items.filter(Boolean).length;
  document.getElementById('vishuItemCount').innerText = `Arranged: ${count} / 4`;
  document.getElementById('sim6Desc').innerHTML = sim6InfoTexts[idx];
}
</script>
""",

    7: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🔄 Four Seasons Festival Wheel</h3>
    <span id="seasonBadge7" style="background: #16a34a; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Spring (Vasant)</span>
  </div>

  <div style="display: grid; grid-template-columns: 140px 1fr; gap: 12px; align-items: center;">
    <!-- Rotating Wheel Graphic -->
    <div style="text-align: center;">
      <svg id="wheelSvg7" viewBox="0 0 120 120" style="width: 110px; height: 110px; transition: transform 0.5s ease-out;">
        <circle cx="60" cy="60" r="55" fill="#1e293b" stroke="#475569" stroke-width="2" />
        <!-- 4 Quadrants -->
        <path d="M60,60 L60,5 A55,55 0 0,1 115,60 Z" fill="#22c55e" opacity="0.8"/> <!-- Spring -->
        <path d="M60,60 L115,60 A55,55 0 0,1 60,115 Z" fill="#f59e0b" opacity="0.8"/> <!-- Summer -->
        <path d="M60,60 L60,115 A55,55 0 0,1 5,60 Z" fill="#0284c7" opacity="0.8"/> <!-- Monsoon -->
        <path d="M60,60 L5,60 A55,55 0 0,1 60,5 Z" fill="#6366f1" opacity="0.8"/> <!-- Winter -->
        <circle cx="60" cy="60" r="16" fill="#0f172a" stroke="#94a3b8" />
        <polygon points="60,48 64,56 56,56" fill="#f8fafc" />
      </svg>
      <div style="font-size: 0.75rem; color: #94a3b8; margin-top: 4px;">Seasonal Dial</div>
    </div>

    <!-- Festival Info Box -->
    <div id="seasonDetailsBox" style="background: #1e293b; border-radius: 8px; padding: 12px; border-left: 4px solid #22c55e; min-height: 100px;">
      <div id="seasonHeading" style="font-weight: bold; color: #4ade80; font-size: 0.95rem;">Spring (Vasant): Vernal Renewal</div>
      <div id="seasonFestivals" style="font-size: 0.85rem; color: #cbd5e1; margin-top: 4px; line-height: 1.4;">
        <strong>Key Celebrations:</strong> Holi (festival of colors), Baisakhi (wheat harvest), Rongali Bihu (Assam).<br>
        <strong>Signature Sweet:</strong> Gujiya stuffed with mawa & dry fruits. Natural herbal gulal made from palash & turmeric!
      </div>
    </div>
  </div>

  <div style="margin-top: 12px; display: grid; grid-template-columns: repeat(4, 1fr); gap: 6px;">
    <button onclick="sim7Select(0)" style="background: #15803d; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌱 Spring</button>
    <button onclick="sim7Select(1)" style="background: #b45309; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">☀️ Summer</button>
    <button onclick="sim7Select(2)" style="background: #0369a1; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">🌧️ Monsoon</button>
    <button onclick="sim7Select(3)" style="background: #4338ca; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.75rem; font-weight: bold;">❄️ Winter</button>
  </div>
</div>

<script>
const sim7Data = [
  {name: "Spring (Vasant)", rot: 0, color: "#22c55e", head: "Spring (Vasant): Vernal Renewal & Harvest", body: "<strong>Key Celebrations:</strong> Holi, Baisakhi, Rongali Bihu, Poila Baisakh.<br><strong>Signature Delicacies:</strong> Crisp Gujiyas, herbal gulal powders from turmeric & flame-of-the-forest blossoms."},
  {name: "Summer (Grishma)", rot: 90, color: "#f59e0b", head: "Summer (Grishma): Tropical Fruits & New Year", body: "<strong>Key Celebrations:</strong> Ugadi, Gudi Padwa, Puthandu, Vishu.<br><strong>Signature Delicacies:</strong> Ugadi Pachadi (six tastes), Holige/Puran Poli, chilled Aam Panna and hydrating cucumber."},
  {name: "Monsoon (Varsha)", rot: 180, color: "#0284c7", head: "Monsoon (Varsha): Rains & Life-Giving Water", body: "<strong>Key Celebrations:</strong> Onam, Teej, Raksha Bandhan.<br><strong>Signature Delicacies:</strong> Onam Sadya feast served on banana leaves, sweet Ghewar, thrilling Vallam Kali snake boat races."},
  {name: "Winter (Shishira)", rot: 270, color: "#6366f1", head: "Winter (Shishira): Solar Rebirth & Warm Feasts", body: "<strong>Key Celebrations:</strong> Makar Sankranti, Lohri, Pongal, Christmas.<br><strong>Signature Delicacies:</strong> Sesame-jaggery rewri & tilgul, Pongal sweet rice in earthen pots, rich spiced Christmas plum cake."}
];

function sim7Select(idx) {
  const item = sim7Data[idx];
  document.getElementById('wheelSvg7').style.transform = `rotate(${item.rot}deg)`;
  document.getElementById('seasonBadge7').innerText = item.name;
  document.getElementById('seasonBadge7').style.background = item.color;
  document.getElementById('seasonDetailsBox').style.borderColor = item.color;
  document.getElementById('seasonHeading').innerText = item.head;
  document.getElementById('seasonHeading').style.color = item.color;
  document.getElementById('seasonFestivals').innerHTML = item.body;
}
</script>
""",

    8: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🥣 Ugadi Pachadi: Six-Taste Balance</h3>
    <span id="tasteScore8" style="background: #0369a1; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Balance: 0 / 6 Tastes</span>
  </div>

  <div style="display: grid; grid-template-columns: repeat(3, 1fr); gap: 8px; margin-bottom: 12px;">
    <button onclick="sim8AddTaste(0)" id="tBtn0" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 8px; border-radius: 6px; cursor: pointer; text-align: left;">
      <div style="font-weight: bold; color: #facc15; font-size: 0.8rem;">🍯 Jaggery (Sweet)</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Represents Joy & Happiness</div>
    </button>
    <button onclick="sim8AddTaste(1)" id="tBtn1" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 8px; border-radius: 6px; cursor: pointer; text-align: left;">
      <div style="font-weight: bold; color: #4ade80; font-size: 0.8rem;">🌿 Neem Petals (Bitter)</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Represents Sadness & Difficulties</div>
    </button>
    <button onclick="sim8AddTaste(2)" id="tBtn2" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 8px; border-radius: 6px; cursor: pointer; text-align: left;">
      <div style="font-weight: bold; color: #a3e635; font-size: 0.8rem;">🥭 Raw Mango (Sour)</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Represents Surprises & Challenges</div>
    </button>
    <button onclick="sim8AddTaste(3)" id="tBtn3" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 8px; border-radius: 6px; cursor: pointer; text-align: left;">
      <div style="font-weight: bold; color: #38bdf8; font-size: 0.8rem;">🧂 Salt (Salty)</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Represents Fear & Caution</div>
    </button>
    <button onclick="sim8AddTaste(4)" id="tBtn4" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 8px; border-radius: 6px; cursor: pointer; text-align: left;">
      <div style="font-weight: bold; color: #f87171; font-size: 0.8rem;">🌶️ Green Chili (Spicy)</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Represents Anger & Passion</div>
    </button>
    <button onclick="sim8AddTaste(5)" id="tBtn5" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 8px; border-radius: 6px; cursor: pointer; text-align: left;">
      <div style="font-weight: bold; color: #fb923c; font-size: 0.8rem;">🌰 Tamarind (Tangy)</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Represents Disgust & Novelty</div>
    </button>
  </div>

  <div id="sim8PachadiBowl" style="background: #1e293b; border-radius: 8px; padding: 12px; border-left: 4px solid #facc15; min-height: 60px;">
    <div id="sim8Msg" style="font-size: 0.85rem; color: #cbd5e1; line-height: 1.4;">
      Click the ingredients above to combine all six distinct tastes into the traditional Ugadi Pachadi bowl!
    </div>
  </div>
</div>

<script>
let sim8Added = [false, false, false, false, false, false];
const sim8Tastes = ["Sweet (Jaggery)", "Bitter (Neem)", "Sour (Raw Mango)", "Salty (Salt)", "Spicy (Chili)", "Tangy (Tamarind)"];

function sim8AddTaste(idx) {
  sim8Added[idx] = !sim8Added[idx];
  const btn = document.getElementById(`tBtn${idx}`);
  btn.style.borderColor = sim8Added[idx] ? '#38bdf8' : '#475569';
  btn.style.background = sim8Added[idx] ? '#0f172a' : '#1e293b';

  const count = sim8Added.filter(Boolean).length;
  document.getElementById('tasteScore8').innerText = `Balance: ${count} / 6 Tastes`;

  if(count === 6) {
    document.getElementById('sim8PachadiBowl').style.borderColor = '#4ade80';
    document.getElementById('sim8Msg').innerHTML = '🌟 <strong>Harmonious Life Wisdom:</strong> All six flavors are united! Ugadi Pachadi reminds us that life is a natural blend of joys, sorrows, anger, fear, challenges, and surprises—all to be accepted with peaceful equanimity.';
  } else {
    document.getElementById('sim8PachadiBowl').style.borderColor = '#facc15';
    document.getElementById('sim8Msg').innerHTML = `Added: <strong>${sim8Tastes[idx]}</strong>. Add remaining ingredients to complete the traditional summer balance!`;
  }
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(simulators_part1)} simulators for Part 1.")
