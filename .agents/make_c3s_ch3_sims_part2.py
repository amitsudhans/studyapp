#!/usr/bin/env python3
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 3: Celebrating Festivals
Simulators Part 2: Simulators 9 to 16
"""

simulators_part2 = {
    9: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🛶 Vallam Kali & Onam Pookkalam</h3>
    <button onclick="sim9RowStroke()" style="background: #0284c7; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">🥁 Strike Drum & Row!</button>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: linear-gradient(180deg, #0284c7 0%, #0369a1 60%, #075985 100%); border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Gentle Water Ripples -->
      <path d="M 0,50 Q 50,40 100,50 T 200,50 T 300,50 T 400,50 T 500,50" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4"/>
      <path d="M 0,110 Q 50,100 100,110 T 200,110 T 300,110 T 400,110 T 500,110" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4"/>
      <path d="M 0,170 Q 50,160 100,170 T 200,170 T 300,170 T 400,170 T 500,170" fill="none" stroke="#38bdf8" stroke-width="1.5" opacity="0.4"/>

      <!-- Long Wooden Snake Boat (Chundan Vallam) -->
      <g id="snakeBoat" transform="translate(40, 100)" style="transition: transform 0.4s ease-out;">
        <!-- Curving Stern/Bow -->
        <path d="M -20,20 Q 20,40 180,35 Q 340,30 380,5 Q 360,35 180,45 Q 20,50 -20,20 Z" fill="#78350f" stroke="#451a03" stroke-width="2"/>
        <!-- High raised rear curl -->
        <path d="M -20,20 Q -40,-10 -30,-30 Q -25,-10 -20,20 Z" fill="#b45309" stroke="#78350f" stroke-width="1.5"/>
        <circle cx="-30" cy="-30" r="4" fill="#facc15" />

        <!-- Rowers Silhouette -->
        <g fill="#f8fafc">
          <circle cx="60" cy="22" r="4" /><rect x="58" y="26" width="4" height="12" />
          <circle cx="100" cy="22" r="4" /><rect x="98" y="26" width="4" height="12" />
          <circle cx="140" cy="22" r="4" /><rect x="138" y="26" width="4" height="12" />
          <circle cx="180" cy="22" r="4" /><rect x="178" y="26" width="4" height="12" />
          <circle cx="220" cy="22" r="4" /><rect x="218" y="26" width="4" height="12" />
          <circle cx="260" cy="22" r="4" /><rect x="258" y="26" width="4" height="12" />
          <circle cx="300" cy="22" r="4" /><rect x="298" y="26" width="4" height="12" />
        </g>

        <!-- Oars (Paddles in unison) -->
        <g id="boatOars" stroke="#facc15" stroke-width="2" stroke-linecap="round">
          <line x1="60" y1="36" x2="50" y2="52" />
          <line x1="100" y1="36" x2="90" y2="52" />
          <line x1="140" y1="36" x2="130" y2="52" />
          <line x1="180" y1="36" x2="170" y2="52" />
          <line x1="220" y1="36" x2="210" y2="52" />
          <line x1="260" y1="36" x2="250" y2="52" />
          <line x1="300" y1="36" x2="290" y2="52" />
        </g>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <button onclick="sim9ShowPookkalam()" style="background: #e11d48; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🌸 View Onam Pookkalam</button>
    <button onclick="sim9ResetRace()" style="background: #475569; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🔄 Reset Race</button>
  </div>

  <div id="sim9Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 36px; line-height: 1.4;">
    Click "Strike Drum & Row!" to synchronize the oarsmen and propel the majestic snake boat forward!
  </div>
</div>

<script>
let sim9PosX = 40;
let sim9OarToggle = false;

function sim9RowStroke() {
  sim9PosX = (sim9PosX + 30) % 300;
  sim9OarToggle = !sim9OarToggle;
  const boat = document.getElementById('snakeBoat');
  boat.setAttribute('transform', `translate(${sim9PosX}, 100)`);
  
  const oars = document.getElementById('boatOars');
  if(sim9OarToggle) {
    oars.innerHTML = `
      <line x1="60" y1="36" x2="70" y2="52" />
      <line x1="100" y1="36" x2="110" y2="52" />
      <line x1="140" y1="36" x2="150" y2="52" />
      <line x1="180" y1="36" x2="190" y2="52" />
      <line x1="220" y1="36" x2="230" y2="52" />
      <line x1="260" y1="36" x2="270" y2="52" />
      <line x1="300" y1="36" x2="310" y2="52" />
    `;
  } else {
    oars.innerHTML = `
      <line x1="60" y1="36" x2="50" y2="52" />
      <line x1="100" y1="36" x2="90" y2="52" />
      <line x1="140" y1="36" x2="130" y2="52" />
      <line x1="180" y1="36" x2="170" y2="52" />
      <line x1="220" y1="36" x2="210" y2="52" />
      <line x1="260" y1="36" x2="250" y2="52" />
      <line x1="300" y1="36" x2="290" y2="52" />
    `;
  }
  document.getElementById('sim9Info').innerHTML = '🚣‍♂️ <strong>Row in Unison!</strong> Up to 100 oarsmen row to the thunderous rhythm of Vanchipattu (boat songs) along Kerala backwaters during Onam!';
}

function sim9ResetRace() {
  sim9PosX = 40;
  document.getElementById('snakeBoat').setAttribute('transform', 'translate(40, 100)');
  document.getElementById('sim9Info').innerText = 'Race reset to starting position. Strike the drum to row!';
}

function sim9ShowPookkalam() {
  document.getElementById('sim9Info').innerHTML = '🌸 <strong>Onam Pookkalam:</strong> Families design concentric geometric flower carpets on courtyard floors using yellow marigolds, orange palash, and white jasmine to welcome prosperity and goodwill.';
}
</script>
""",

    10: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🔥 Winter Harvest Bonfire & Pongal Pot</h3>
    <span id="calMeter10" style="background: #b45309; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Thermal Energy: Normal</span>
  </div>

  <div style="display: grid; grid-template-columns: 1fr 1fr; gap: 10px;">
    <!-- Lohri Bonfire -->
    <div style="background: #1e293b; border-radius: 8px; padding: 10px; text-align: center; border: 1px solid #334155;">
      <div style="font-weight: bold; color: #f97316; font-size: 0.9rem; margin-bottom: 6px;">Lohri Bonfire Offering</div>
      <svg viewBox="0 0 160 120" style="width: 100%; height: 100px;">
        <!-- Wooden logs -->
        <rect x="40" y="90" width="80" height="12" rx="3" fill="#78350f" transform="rotate(-15 80 96)"/>
        <rect x="40" y="90" width="80" height="12" rx="3" fill="#92400e" transform="rotate(15 80 96)"/>
        <!-- Flame layers -->
        <polygon id="bonfireOuter" points="80,20 60,85 100,85" fill="#f97316" />
        <polygon id="bonfireInner" points="80,45 68,85 92,85" fill="#facc15" />
      </svg>
      <button onclick="sim10TossRewri()" style="background: #ea580c; color: white; border: none; padding: 6px 10px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold; margin-top: 6px;">🌾 Toss Sesame & Rewri</button>
    </div>

    <!-- Pongal Boiling Pot -->
    <div style="background: #1e293b; border-radius: 8px; padding: 10px; text-align: center; border: 1px solid #334155;">
      <div style="font-weight: bold; color: #facc15; font-size: 0.9rem; margin-bottom: 6px;">Pongal Clay Pot</div>
      <svg viewBox="0 0 160 120" style="width: 100%; height: 100px;">
        <!-- Stove base -->
        <rect x="50" y="100" width="60" height="10" fill="#64748b" />
        <polygon points="80,95 72,105 88,105" fill="#ef4444" />
        <!-- Earthen Clay Pot -->
        <ellipse cx="80" cy="75" rx="32" ry="24" fill="#b45309" stroke="#78350f" stroke-width="2"/>
        <ellipse cx="80" cy="55" rx="20" ry="6" fill="#78350f" />
        <!-- Boiling milk foam overflow -->
        <ellipse id="pongalFoam" cx="80" cy="53" rx="22" ry="7" fill="#ffffff" opacity="0.4"/>
      </svg>
      <button onclick="sim10BoilPongal()" style="background: #ca8a04; color: white; border: none; padding: 6px 10px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold; margin-top: 6px;">🥛 Boil Fresh Rice & Milk</button>
    </div>
  </div>

  <div id="sim10Status" style="margin-top: 10px; background: #1e293b; padding: 8px 12px; border-radius: 6px; font-size: 0.85rem; color: #cbd5e1; border-left: 3px solid #f97316;">
    Winter foods like sesame, jaggery, and peanuts supply dense thermal calories, protecting health during chilly weather!
  </div>
</div>

<script>
function sim10TossRewri() {
  const outer = document.getElementById('bonfireOuter');
  outer.setAttribute('points', '80,10 55,85 105,85');
  document.getElementById('calMeter10').innerText = 'Thermal Energy: High 🔥';
  document.getElementById('calMeter10').style.background = '#dc2626';
  document.getElementById('sim10Status').innerHTML = '🔥 <strong>Lohri Bonfire Gratitude:</strong> Tossing sesame seeds, rewri, and puffed rice into the flame expresses reverence to the Sun and Agni for winter harvest abundance!';
  setTimeout(() => {
    outer.setAttribute('points', '80,20 60,85 100,85');
  }, 1200);
}

function sim10BoilPongal() {
  const foam = document.getElementById('pongalFoam');
  foam.setAttribute('rx', '28');
  foam.setAttribute('ry', '12');
  foam.setAttribute('opacity', '1');
  document.getElementById('sim10Status').innerHTML = '✨ <strong>Pongalo Pongal!</strong> Freshly harvested rice boiled with milk and dark jaggery overflows from the earthen pot, symbolizing limitless abundance and family joy!';
}
</script>
""",

    11: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🍽️ Festive Delicacy Pantry Matcher</h3>
    <span id="dishesMatchedBadge" style="background: #0369a1; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Explored: 0 / 5</span>
  </div>

  <div style="display: grid; grid-template-columns: repeat(5, 1fr); gap: 6px; margin-bottom: 12px;">
    <button onclick="sim11ShowDish(0)" id="dBtn0" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🍪 Thekua
    </button>
    <button onclick="sim11ShowDish(1)" id="dBtn1" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🥟 Gujiya
    </button>
    <button onclick="sim11ShowDish(2)" id="dBtn2" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🎋 Pitha
    </button>
    <button onclick="sim11ShowDish(3)" id="dBtn3" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🍜 Seviyan
    </button>
    <button onclick="sim11ShowDish(4)" id="dBtn4" style="background: #1e293b; border: 1px solid #475569; color: white; padding: 6px; border-radius: 6px; cursor: pointer; text-align: center; font-size: 0.75rem; font-weight: bold;">
      🎂 Plum Cake
    </button>
  </div>

  <div id="sim11Details" style="background: #1e293b; border-radius: 8px; padding: 12px; border-left: 4px solid #38bdf8; min-height: 80px;">
    <div id="sim11Name" style="font-weight: bold; color: #38bdf8; font-size: 0.95rem;">Select any traditional dish above</div>
    <div id="sim11Body" style="font-size: 0.85rem; color: #cbd5e1; margin-top: 4px; line-height: 1.4;">
      Discover how regional agricultural grains (wheat, rice, jaggery, nuts) are transformed into iconic festival foods across India!
    </div>
  </div>
</div>

<script>
const sim11Data = [
  {name: "🍪 Thekua (Chhath Puja - Bihar & Eastern UP)", body: "<strong>Ingredients:</strong> Whole wheat flour, jaggery, pure ghee, crushed cardamom.<br><strong>Tradition:</strong> Dough is pressed onto hand-carved wooden dies and deep-fried into crispy, fragrant cookies offered to the Sun god."},
  {name: "🥟 Gujiya (Holi - Northern & Central India)", body: "<strong>Ingredients:</strong> Crisp flour pastry stuffed with sweetened mawa (milk solids), coconut, and dry fruits.<br><strong>Tradition:</strong> Shaped into elegant half-moons and fried to celebrate spring colors and sweetness with visitors."},
  {name: "🎋 Pitha (Magh Bihu - Assam)", body: "<strong>Ingredients:</strong> Sticky Bora rice flour filled with roasted black sesame seeds, molasses, or coconut.<br><strong>Tradition:</strong> Gently steamed or roasted inside freshly cut hollow green bamboo pipes over fragrant wood embers."},
  {name: "🍜 Seviyan / Sheer Khurma (Eid-ul-Fitr)", body: "<strong>Ingredients:</strong> Roasted fine vermicelli noodles simmered in creamy milk with sweet dates, cardamom, and slivered pistachios.<br><strong>Tradition:</strong> Served hot or chilled to welcome friends and family, symbolizing sweetness and generous hospitality."},
  {name: "🎂 Spiced Plum Cake (Christmas)", body: "<strong>Ingredients:</strong> Flour, brown sugar, soaked raisins, candied orange peel, cinnamon, nutmeg, and cloves.<br><strong>Tradition:</strong> Baked in winter ovens and shared during Christmas gatherings as a token of peace, warmth, and fellowship."}
];
let sim11Visited = new Set();

function sim11ShowDish(idx) {
  for(let i=0; i<5; i++) {
    document.getElementById(`dBtn${i}`).style.borderColor = (i === idx) ? '#38bdf8' : '#475569';
  }
  const item = sim11Data[idx];
  document.getElementById('sim11Name').innerText = item.name;
  document.getElementById('sim11Body').innerHTML = item.body;
  sim11Visited.add(idx);
  document.getElementById('dishesMatchedBadge').innerText = `Explored: ${sim11Visited.size} / 5`;
}
</script>
""",

    12: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🌳 Sarhul Sacred Grove & Rain Prediction</h3>
    <span id="rainForecastBadge12" style="background: #065f46; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Rain Forecast: Pending</span>
  </div>

  <div style="position: relative; width: 100%; height: 200px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 200" style="width: 100%; height: 100%;">
      <!-- Forest Canopy (Sarna / Jaherthan Grove) -->
      <polygon points="80,180 120,40 160,180" fill="#15803d" />
      <polygon points="140,180 190,30 240,180" fill="#166534" />
      <polygon points="220,180 270,50 320,180" fill="#15803d" />
      <polygon points="300,180 360,35 420,180" fill="#166534" />

      <!-- Center Sacred Sal Tree Trunk -->
      <rect x="235" y="70" width="30" height="110" fill="#78350f" stroke="#451a03" stroke-width="2"/>
      <circle cx="250" cy="70" r="50" fill="#15803d" />
      <circle cx="250" cy="65" r="45" fill="#fef08a" opacity="0.3"/> <!-- Blooming blossoms -->

      <!-- Sacred Clay Water Pot (Ghara) at tree base -->
      <g id="sacredPot">
        <ellipse cx="250" cy="170" rx="16" ry="12" fill="#b45309" stroke="#78350f" stroke-width="1.5"/>
        <ellipse cx="250" cy="162" rx="10" ry="3" fill="#78350f" />
        <rect id="waterLevelBar" x="244" y="166" width="12" height="6" fill="#38bdf8" />
      </g>

      <!-- Traditional Drum (Dholak) -->
      <g transform="translate(140, 160)">
        <ellipse cx="0" cy="0" rx="16" ry="9" fill="#92400e" stroke="#451a03" />
        <line x1="-16" y1="0" x2="16" y2="0" stroke="#fef08a" stroke-dasharray="2,2"/>
      </g>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <button onclick="sim12CheckWater()" style="background: #059669; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🏺 Inspect Sacred Water Pot</button>
    <button onclick="sim12WearSalFlower()" style="background: #d97706; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🌼 Receive Sal Blossom</button>
  </div>

  <div id="sim12Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 36px; line-height: 1.4;">
    Click "Inspect Sacred Water Pot" to test the traditional ecological knowledge used by the Pahan to forecast monsoon rains!
  </div>
</div>

<script>
function sim12CheckWater() {
  document.getElementById('waterLevelBar').setAttribute('height', '8');
  document.getElementById('waterLevelBar').setAttribute('y', '164');
  document.getElementById('rainForecastBadge12').innerText = 'Rain Forecast: Abundant Monsoon 🌧️';
  document.getElementById('rainForecastBadge12').style.background = '#0284c7';
  document.getElementById('sim12Info').innerHTML = '🌧️ <strong>Monsoon Forecast:</strong> Water in the sacred earthen pot remained full overnight! Tribal elders predict bountiful monsoon rains, signaling ideal timing for paddy sowing.';
}

function sim12WearSalFlower() {
  document.getElementById('sim12Info').innerHTML = '🌼 <strong>Sacred Sal Blossom:</strong> Villagers tuck fragrant white sal flowers behind their ears and over doorways to symbolize renewal, friendship, and eternal gratitude to Mother Earth.';
}
</script>
""",

    13: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🚁 Sal Tree: Winged Seed Flight</h3>
    <button onclick="sim13SpinSeeds()" style="background: #16a34a; color: white; border: none; padding: 4px 12px; border-radius: 6px; cursor: pointer; font-size: 0.85rem; font-weight: bold;">🍃 Release Seeds in Wind</button>
  </div>

  <div style="position: relative; width: 100%; height: 200px; background: #1e293b; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 200" style="width: 100%; height: 100%;">
      <!-- Sal Canopy -->
      <path d="M 0,0 L 0,80 Q 80,120 160,70 Q 240,110 320,60 Q 400,100 500,70 L 500,0 Z" fill="#15803d" />
      <line x1="250" y1="0" x2="250" y2="120" stroke="#78350f" stroke-width="14" />

      <!-- Winged Samara Seed 1 -->
      <g id="samara1" transform="translate(180, 70)" style="transition: transform 1.5s cubic-bezier(0.25, 1, 0.5, 1);">
        <ellipse cx="0" cy="18" rx="5" ry="6" fill="#78350f" />
        <!-- 3 elongated papery wings -->
        <path d="M 0,14 C -12,4 -16,-12 -8,-24 C -2,-16 0,0 0,14 Z" fill="#d97706" opacity="0.85"/>
        <path d="M 0,14 C 12,4 16,-12 8,-24 C 2,-16 0,0 0,14 Z" fill="#d97706" opacity="0.85"/>
        <path d="M 0,14 C 0,-6 0,-18 0,-26 C 2,-18 2,-6 0,14 Z" fill="#b45309" opacity="0.9"/>
      </g>

      <!-- Winged Samara Seed 2 -->
      <g id="samara2" transform="translate(300, 60)" style="transition: transform 1.8s cubic-bezier(0.25, 1, 0.5, 1);">
        <ellipse cx="0" cy="16" rx="4" ry="5" fill="#78350f" />
        <path d="M 0,12 C -10,2 -14,-10 -6,-20 C -1,-14 0,0 0,12 Z" fill="#d97706" opacity="0.85"/>
        <path d="M 0,12 C 10,2 14,-10 6,-20 C 1,-14 0,0 0,12 Z" fill="#d97706" opacity="0.85"/>
      </g>

      <!-- Ground Level -->
      <rect x="0" y="180" width="500" height="20" fill="#3f2e21" />
      <rect x="0" y="178" width="500" height="4" fill="#15803d" />
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: 1fr 1fr; gap: 8px;">
    <button onclick="sim13MakePattal()" style="background: #0284c7; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🍃 Stitched Sal Leaf Pattal</button>
    <button onclick="sim13ShowEcological()" style="background: #475569; color: white; border: none; padding: 8px; border-radius: 6px; cursor: pointer; font-weight: bold; font-size: 0.85rem;">🛡️ Groundwater & Soil Armor</button>
  </div>

  <div id="sim13Info" style="margin-top: 8px; font-size: 0.85rem; color: #cbd5e1; min-height: 36px; line-height: 1.4;">
    Click "Release Seeds in Wind" to observe the aerodynamic helicopter spin of winged sal samara seeds!
  </div>
</div>

<script>
let sim13Fallen = false;

function sim13SpinSeeds() {
  sim13Fallen = !sim13Fallen;
  const s1 = document.getElementById('samara1');
  const s2 = document.getElementById('samara2');
  if(sim13Fallen) {
    s1.setAttribute('transform', 'translate(100, 160) rotate(180)');
    s2.setAttribute('transform', 'translate(420, 165) rotate(220)');
    document.getElementById('sim13Info').innerHTML = '🚁 <strong>Helicopter Seed Flight:</strong> The aerodynamic papery wings cause the seed to spin rapidly, slowing its fall so breezes carry it far from the parent canopy to colonize new clearings!';
  } else {
    s1.setAttribute('transform', 'translate(180, 70) rotate(0)');
    s2.setAttribute('transform', 'translate(300, 60) rotate(0)');
    document.getElementById('sim13Info').innerText = 'Seeds returned to upper canopy branches.';
  }
}

function sim13MakePattal() {
  document.getElementById('sim13Info').innerHTML = '🍃 <strong>Eco-Friendly Sal Pattals:</strong> Broad, leathery sal leaves are stitched with tiny bamboo twigs to create 100% biodegradable plates and bowls, replacing polluting single-use plastics!';
}

function sim13ShowEcological() {
  document.getElementById('sim13Info').innerHTML = '🛡️ <strong>Forest Ecology:</strong> Extensive deep taproots of sal trees absorb heavy monsoon rains, recharge subterranean groundwater aquifers, and securely bind soil against runoff erosion.';
}
</script>
""",

    14: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🏔️ Himalayan Altitude & River Water Towers</h3>
    <span id="altTag14" style="background: #0284c7; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Zone: Glacial Crest (8,848 m)</span>
  </div>

  <div style="position: relative; width: 100%; height: 210px; background: #0f172a; border-radius: 8px; overflow: hidden; border: 1px solid #334155;">
    <svg viewBox="0 0 500 210" style="width: 100%; height: 100%;">
      <!-- Mountain Profile Gradient -->
      <!-- Plains to Everest -->
      <polygon points="20,200 480,20 480,200 20,200" fill="#1e293b" stroke="#334155" stroke-width="2"/>
      
      <!-- Zone 1: Subtropical Plains (0 - 1,000m) -->
      <polygon points="20,200 130,160 130,200" fill="#15803d" opacity="0.6"/>
      <text x="40" y="190" fill="#86efac" font-size="8" font-weight="bold">Plains (200m)</text>

      <!-- Zone 2: Conifer Pine Belt (1,000 - 3,000m) -->
      <polygon points="130,160 270,105 270,200 130,200" fill="#047857" opacity="0.6"/>
      <text x="150" y="160" fill="#6ee7b7" font-size="8" font-weight="bold">Pine & Deodar (2,000m)</text>

      <!-- Zone 3: Alpine Meadows & Scrub (3,000 - 4,500m) -->
      <polygon points="270,105 380,60 380,200 270,200" fill="#0284c7" opacity="0.5"/>
      <text x="280" y="110" fill="#7dd3fc" font-size="8" font-weight="bold">Alpine Meadow (4,000m)</text>

      <!-- Zone 4: Permanent Snow & Glaciers (4,500 - 8,848m) -->
      <polygon points="380,60 480,20 480,200 380,200" fill="#f8fafc" opacity="0.9"/>
      <text x="390" y="45" fill="#0f172a" font-size="9" font-weight="bold">Everest (8,848.86 m)</text>

      <!-- Perennial Meltwater River Stream -->
      <path id="riverStream" d="M 430,70 Q 350,110 250,140 Q 150,170 20,195" fill="none" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>
    </svg>
  </div>

  <div style="margin-top: 10px; display: grid; grid-template-columns: repeat(3, 1fr); gap: 6px;">
    <button onclick="sim14SelectRiver('ganga')" style="background: #0284c7; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold;">🌊 Ganga River Source</button>
    <button onclick="sim14SelectRiver('indus')" style="background: #0369a1; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold;">🏔️ Indus River Basin</button>
    <button onclick="sim14SelectRiver('brahma')" style="background: #075985; color: white; border: none; padding: 6px; border-radius: 6px; cursor: pointer; font-size: 0.8rem; font-weight: bold;">🌏 Brahmaputra Flow</button>
  </div>

  <div id="sim14Info" style="margin-top: 8px; font-size: 0.85rem; color: #bae6fd; min-height: 36px; line-height: 1.4;">
    Click the buttons above to trace how glacial freshwater sustains hundreds of millions across India's river plains!
  </div>
</div>

<script>
function sim14SelectRiver(river) {
  const info = document.getElementById('sim14Info');
  if(river === 'ganga') {
    info.innerHTML = '🌊 <strong>Ganga River System:</strong> Born from the Gangotri Glacier at Gaumukh (3,892 m), snow meltwater feeds northern plains, sustaining agriculture and drinking water for over 400 million people.';
    document.getElementById('altTag14').innerText = 'Gangotri Glacier (3,892 m)';
  } else if(river === 'indus') {
    info.innerHTML = '🏔️ <strong>Indus River System:</strong> Originating near Lake Manasarovar in western Tibet/Himalayas, flowing through Ladakh and sustaining fertile valleys.';
    document.getElementById('altTag14').innerText = 'Kailash Glaciers (4,500 m)';
  } else if(river === 'brahma') {
    info.innerHTML = '🌏 <strong>Brahmaputra System:</strong> Originating from the Angsi Glacier, flowing through Tibet and cascading into Assam, depositing rich alluvial silt during monsoons.';
    document.getElementById('altTag14').innerText = 'Angsi Glacier (5,300 m)';
  }
}
</script>
""",

    15: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🏫 School Campus Signboard Navigator</h3>
    <span id="signFoundCount15" style="background: #047857; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Found: 0 / 4</span>
  </div>

  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 12px;">
    <!-- Library -->
    <button onclick="sim15ClickSign(0)" id="scBtn0" style="background: #1e293b; border: 2px solid #334155; color: white; padding: 8px; border-radius: 8px; cursor: pointer; text-align: center;">
      <svg viewBox="0 0 50 50" style="width: 40px; height: 40px; display: block; margin: 0 auto;">
        <rect x="5" y="5" width="40" height="40" rx="6" fill="#0284c7" />
        <path d="M 12,20 Q 25,24 25,35 Q 25,24 38,20 L 38,15 Q 25,19 25,30 Q 25,19 12,15 Z" fill="#ffffff" />
      </svg>
      <div style="font-size: 0.75rem; margin-top: 4px; font-weight: bold;">Library</div>
    </button>

    <!-- Drinking Water -->
    <button onclick="sim15ClickSign(1)" id="scBtn1" style="background: #1e293b; border: 2px solid #334155; color: white; padding: 8px; border-radius: 8px; cursor: pointer; text-align: center;">
      <svg viewBox="0 0 50 50" style="width: 40px; height: 40px; display: block; margin: 0 auto;">
        <rect x="5" y="5" width="40" height="40" rx="6" fill="#0284c7" />
        <rect x="18" y="14" width="14" height="6" rx="2" fill="#ffffff" />
        <rect x="22" y="20" width="6" height="14" fill="#ffffff" />
        <path d="M 25,32 Q 22,38 25,41 Q 28,38 25,32 Z" fill="#38bdf8" />
      </svg>
      <div style="font-size: 0.75rem; margin-top: 4px; font-weight: bold;">Water Tap</div>
    </button>

    <!-- Emergency Fire Exit -->
    <button onclick="sim15ClickSign(2)" id="scBtn2" style="background: #1e293b; border: 2px solid #334155; color: white; padding: 8px; border-radius: 8px; cursor: pointer; text-align: center;">
      <svg viewBox="0 0 50 50" style="width: 40px; height: 40px; display: block; margin: 0 auto;">
        <rect x="5" y="5" width="40" height="40" rx="6" fill="#16a34a" />
        <circle cx="20" cy="18" r="3" fill="#ffffff" />
        <path d="M 18,22 L 23,28 L 20,38 M 23,28 L 30,26" stroke="#ffffff" stroke-width="2.5" fill="none" stroke-linecap="round"/>
        <rect x="32" y="15" width="8" height="22" fill="#ffffff" />
      </svg>
      <div style="font-size: 0.75rem; margin-top: 4px; font-weight: bold;">Fire Exit</div>
    </button>

    <!-- Staircase Handrail -->
    <button onclick="sim15ClickSign(3)" id="scBtn3" style="background: #1e293b; border: 2px solid #334155; color: white; padding: 8px; border-radius: 8px; cursor: pointer; text-align: center;">
      <svg viewBox="0 0 50 50" style="width: 40px; height: 40px; display: block; margin: 0 auto;">
        <rect x="5" y="5" width="40" height="40" rx="6" fill="#eab308" />
        <!-- Stepped lines -->
        <path d="M 12,38 L 20,38 L 20,30 L 28,30 L 28,22 L 36,22 L 36,14" stroke="#1e293b" stroke-width="3" fill="none"/>
        <line x1="12" y1="28" x2="36" y2="10" stroke="#dc2626" stroke-width="2.5"/>
      </svg>
      <div style="font-size: 0.75rem; margin-top: 4px; font-weight: bold;">Use Handrail</div>
    </button>
  </div>

  <div id="sim15Display" style="background: #1e293b; border-radius: 8px; padding: 12px; border-left: 4px solid #38bdf8; min-height: 70px;">
    <div id="sim15Title" style="font-weight: bold; color: #38bdf8; font-size: 0.95rem;">Select any school campus signboard</div>
    <div id="sim15Desc" style="font-size: 0.85rem; color: #cbd5e1; margin-top: 4px;">Learn how visual icons ensure campus safety, order, and easy orientation for students and guests.</div>
  </div>
</div>

<script>
const sim15Signs = [
  {title: "📖 School Library (Blue Informational Sign)", desc: "Directs students to the silent sanctuary of books, encyclopedias, and research tables. Rule: Maintain quiet concentration so peers can read undisturbed."},
  {title: "🚰 Purified Drinking Water Station", desc: "Identifies filtered water dispensers where students fill their clean water bottles. Rule: Keep tap surroundings dry and do not waste drinking water."},
  {title: "🏃 Emergency Fire Exit (Green Safety Sign)", desc: "Universal green safety sign marking fire evacuation routes leading directly to open playground muster points during fire safety drills."},
  {title: "🪜 Staircase Safety & Handrail Caution", desc: "Yellow warning sign placed at stair landings reminding students to walk on the left, hold sturdy handrails, and never run or jump down steps."}
];
let sim15Found = new Set();

function sim15ClickSign(idx) {
  for(let i=0; i<4; i++) {
    document.getElementById(`scBtn${i}`).style.borderColor = (i === idx) ? '#38bdf8' : '#334155';
  }
  const item = sim15Signs[idx];
  document.getElementById('sim15Title').innerText = item.title;
  document.getElementById('sim15Desc').innerText = item.desc;
  sim15Found.add(idx);
  document.getElementById('signFoundCount15').innerText = `Found: ${sim15Found.size} / 4`;
}
</script>
""",

    16: """
<div class="sim-container" style="background: #0f172a; border-radius: 12px; padding: 16px; color: #f8fafc; font-family: system-ui, sans-serif;">
  <div style="display: flex; justify-content: space-between; align-items: center; margin-bottom: 10px;">
    <h3 style="margin: 0; font-size: 1.15rem; color: #38bdf8;">🤝 Community Harmony Feast Matrix</h3>
    <span id="harmonyScore16" style="background: #15803d; padding: 3px 10px; border-radius: 12px; font-size: 0.85rem; font-weight: bold;">Harmony: 100% United</span>
  </div>

  <div style="display: grid; grid-template-columns: repeat(4, 1fr); gap: 8px; margin-bottom: 12px;">
    <!-- Tradition 1: Diwali / Gurpurab Light -->
    <div onclick="sim16Illuminate(0)" id="hCard0" style="background: #1e293b; border: 2px solid #ca8a04; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer;">
      <div style="font-size: 1.4rem;">🪔</div>
      <div style="font-size: 0.75rem; font-weight: bold; color: #facc15; margin-top: 4px;">Light of Wisdom</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Diwali & Gurpurab</div>
    </div>

    <!-- Tradition 2: Eid Sweet Hospitality -->
    <div onclick="sim16Illuminate(1)" id="hCard1" style="background: #1e293b; border: 2px solid #059669; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer;">
      <div style="font-size: 1.4rem;">🌙</div>
      <div style="font-size: 0.75rem; font-weight: bold; color: #4ade80; margin-top: 4px;">Shared Seviyan</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Eid-ul-Fitr</div>
    </div>

    <!-- Tradition 3: Christmas Fellowship -->
    <div onclick="sim16Illuminate(2)" id="hCard2" style="background: #1e293b; border: 2px solid #dc2626; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer;">
      <div style="font-size: 1.4rem;">⭐</div>
      <div style="font-size: 0.75rem; font-weight: bold; color: #f87171; margin-top: 4px;">Peace & Goodwill</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Christmas</div>
    </div>

    <!-- Tradition 4: Sarhul & Harvest Soil -->
    <div onclick="sim16Illuminate(3)" id="hCard3" style="background: #1e293b; border: 2px solid #0284c7; border-radius: 8px; padding: 8px; text-align: center; cursor: pointer;">
      <div style="font-size: 1.4rem;">🌱</div>
      <div style="font-size: 0.75rem; font-weight: bold; color: #38bdf8; margin-top: 4px;">Nature Gratitude</div>
      <div style="font-size: 0.7rem; color: #94a3b8;">Sarhul & Baisakhi</div>
    </div>
  </div>

  <div id="sim16Banner" style="background: #1e293b; border-radius: 8px; padding: 12px; border-left: 4px solid #10b981; min-height: 60px;">
    <div id="sim16Msg" style="font-size: 0.85rem; color: #cbd5e1; line-height: 1.4;">
      Click any celebration card above to explore how diverse cultural traditions unite in mutual respect, hospitality, and shared values!
    </div>
  </div>
</div>

<script>
const sim16Stories = [
  "🪔 <strong>Diwali & Gurpurab:</strong> Lighting earthen lamps symbolizes the triumph of knowledge, truth, and inner light over ignorance, shared warmly with neighbors of all backgrounds.",
  "🌙 <strong>Eid-ul-Fitr:</strong> Celebrating the conclusion of fasting with open hearts, embracing friends, and sharing bowls of rich, sweet sheer khurma and seviyan across communities.",
  "⭐ <strong>Christmas:</strong> Singing carols, sharing spiced fruit cakes, and extending compassionate charity and goodwill to everyone in society.",
  "🌱 <strong>Sarhul, Baisakhi & Pongal:</strong> Celebrating the living Earth, honoring farmers, and rejoicing in bountiful crops that nourish our entire interconnected nation."
];

function sim16Illuminate(idx) {
  document.getElementById('sim16Msg').innerHTML = sim16Stories[idx];
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(simulators_part2)} simulators for Part 2.")
