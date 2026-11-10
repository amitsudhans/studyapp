#!/usr/bin/env python3
"""
Interactive HTML5/SVG Simulators for NCERT Class 3 Science (Our Wondrous World)
Chapter 2: Going to the Mela
Part 1: Simulators for Slides 1 to 8
"""

sims_part1 = {
    1: """
<div class="sim-container" id="sim1">
  <div class="sim-header">
    <div class="sim-title">🗺️ Mela Journey Transport Planner</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim1Select('bus')">Public City Bus</button>
      <button class="sim-btn" onclick="sim1Select('walk')">Walking 6 Kilometers</button>
      <button class="sim-btn" onclick="sim1Select('auto')">Three-Wheeler Auto</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim1Display" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim1Icon" style="font-size:38px;">🚌 🚏</div>
      <div id="sim1Mode" style="font-size:14px; font-weight:bold; color:#38bdf8; margin-top:4px;">City Bus Route 401</div>
      <div id="sim1Stats" style="font-size:11px; color:#cbd5e1; margin-top:2px;">Time: 20 Mins | Comfort: High</div>
    </div>
    <div id="sim1Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🚌 <b>Optimal Choice:</b> Public bus covers 6 km safely and affordably, keeping elderly grandparents and toddlers comfortable!
    </div>
  </div>
</div>
<script>
function sim1Select(mode) {
  document.querySelectorAll('#sim1 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(mode)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim1Icon');
  const label = document.getElementById('sim1Mode');
  const stats = document.getElementById('sim1Stats');
  const fb = document.getElementById('sim1Feedback');

  if (mode === 'bus') {
    icon.innerHTML = '🚌 🚏';
    label.innerHTML = 'City Bus Route 401';
    stats.innerHTML = 'Time: 20 Mins | Comfort: High | Cost: Affordable';
    fb.style.color = '#34d399';
    fb.innerHTML = '🚌 <b>Safe & Group Friendly:</b> The entire extended family travels together in designated seating without physical exhaustion.';
  } else if (mode === 'walk') {
    icon.innerHTML = '🚶 😫 ☀️';
    label.innerHTML = 'Walking 6 Kilometers';
    stats.innerHTML = 'Time: 90 Mins | Fatigue: Extreme | Danger: Highway Traffic';
    fb.style.color = '#f87171';
    fb.innerHTML = '❌ <b>Impractical:</b> Walking 6 km along hot highway roads exhausts growing children and is impossible for elderly grandparents.';
  } else if (mode === 'auto') {
    icon.innerHTML = '🛺 💨';
    label.innerHTML = 'Three-Wheeled Autorickshaw';
    stats.innerHTML = 'Time: 25 Mins | Comfort: Medium | Capacity: Limited (3-4)';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🛺 <b>Convenient for Small Groups:</b> Extended relatives arriving at the railway station use autorickshaws to reach the parade ground.';
  }
}
</script>
""",

    2: """
<div class="sim-container" id="sim2">
  <div class="sim-header">
    <div class="sim-title">👵 Intergenerational Care & Inclusivity Planner</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim2Plan('reassure')">Loving Reassurance</button>
      <button class="sim-btn" onclick="sim2Plan('relatives')">Family Group Support</button>
      <button class="sim-btn" onclick="sim2Plan('wheelchair')">Entrance Wheelchair</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim2Card" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim2Icon" style="font-size:38px;">👵 🤝 ❤️</div>
      <div id="sim2Text" style="font-size:13px; font-weight:bold; color:#fbbf24; margin-top:4px;">Gentle Reassurance</div>
    </div>
    <div id="sim2Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      ❤️ <b>Empathetic Listening:</b> Acknowledging knee pain and assuring continuous assistance encourages hesitant grandparents to join!
    </div>
  </div>
</div>
<script>
function sim2Plan(act) {
  document.querySelectorAll('#sim2 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(act)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim2Icon');
  const text = document.getElementById('sim2Text');
  const fb = document.getElementById('sim2Feedback');

  if (act === 'reassure') {
    icon.innerHTML = '👵 🤝 ❤️';
    text.innerHTML = 'Comforting Reassurance';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '❤️ <b>Empathy:</b> Reassuring elderly grandparents that the family will walk slowly and take frequent pauses relieves anxiety.';
  } else if (act === 'relatives') {
    icon.innerHTML = '👨‍👩‍👧‍👦 🤝 👵';
    text.innerHTML = 'United Family Circle';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🤝 <b>Shared Assistance:</b> Extended kin arriving by train and friendly neighbors team up to assist the grandmother throughout the day.';
  } else if (act === 'wheelchair') {
    icon.innerHTML = '🧑‍🦽 ✨ 🎡';
    text.innerHTML = 'Entrance Wheelchair Reserved';
    fb.style.color = '#34d399';
    fb.innerHTML = '🧑‍🦽 <b>Dignified Access:</b> Knowing a free wheelchair is available at the entrance allows the grandmother to tour the fair in complete comfort!';
  }
}
</script>
""",

    3: """
<div class="sim-container" id="sim3">
  <div class="sim-header">
    <div class="sim-title">🚦 Interactive Pedestrian Road Crossing</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim3Signal('red')">Signal: Red (Stop)</button>
      <button class="sim-btn" onclick="sim3Signal('green')">Signal: Green (Walk)</button>
      <button class="sim-btn" onclick="sim3Look()">Look Right-Left-Right</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim3Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Road Surface -->
      <rect x="0" y="30" width="240" height="80" fill="#334155"/>
      <!-- Zebra Crossing Stripes -->
      <rect x="90" y="30" width="12" height="80" fill="#f8fafc"/>
      <rect x="110" y="30" width="12" height="80" fill="#f8fafc"/>
      <rect x="130" y="30" width="12" height="80" fill="#f8fafc"/>
      <rect x="150" y="30" width="12" height="80" fill="#f8fafc"/>

      <!-- Traffic Signal Pole -->
      <rect x="25" y="10" width="6" height="50" fill="#64748b"/>
      <rect x="18" y="10" width="20" height="35" rx="3" fill="#0f172a"/>
      <circle id="sim3LightRed" cx="28" cy="18" r="4" fill="#ef4444"/>
      <circle id="sim3LightYellow" cx="28" cy="27" r="4" fill="#475569"/>
      <circle id="sim3LightGreen" cx="28" cy="36" r="4" fill="#475569"/>

      <!-- Walking Pedestrians Group -->
      <g id="sim3Walker" transform="translate(120, 115)">
        <circle cx="0" cy="-8" r="6" fill="#38bdf8"/>
        <line x1="0" y1="-2" x2="0" y2="10" stroke="#38bdf8" stroke-width="2.5"/>
        <line x1="0" y1="10" x2="-4" y2="18" stroke="#38bdf8" stroke-width="2"/>
        <line x1="0" y1="10" x2="4" y2="18" stroke="#38bdf8" stroke-width="2"/>
      </g>
    </svg>
    <div id="sim3Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#f87171; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🔴 <b>Red Signal:</b> Traffic is moving! Pedestrians must wait patiently on the sidewalk.
    </div>
  </div>
</div>
<script>
let sim3CanWalk = false;

function sim3Signal(sig) {
  const lr = document.getElementById('sim3LightRed');
  const lg = document.getElementById('sim3LightGreen');
  const w = document.getElementById('sim3Walker');
  const fb = document.getElementById('sim3Feedback');

  if (sig === 'red') {
    sim3CanWalk = false;
    lr.setAttribute('fill', '#ef4444');
    lg.setAttribute('fill', '#475569');
    w.setAttribute('transform', 'translate(120, 115)');
    fb.style.color = '#f87171';
    fb.innerHTML = '🔴 <b>Vehicles Moving:</b> Stand safely behind the curb. Never attempt to cross on red!';
  } else if (sig === 'green') {
    sim3CanWalk = true;
    lr.setAttribute('fill', '#475569');
    lg.setAttribute('fill', '#22c55e');
    w.setAttribute('transform', 'translate(120, 70)');
    fb.style.color = '#34d399';
    fb.innerHTML = '🟢 <b>Pedestrian Green Signal:</b> Vehicles have stopped. Cross calmly across the zebra stripes!';
  }
}

function sim3Look() {
  const fb = document.getElementById('sim3Feedback');
  fb.style.color = '#fbbf24';
  fb.innerHTML = '👀 <b>Safety Check:</b> Look Right, then Left, and Right again to verify all vehicles are fully stationary!';
}
</script>
""",

    4: """
<div class="sim-container" id="sim4">
  <div class="sim-header">
    <div class="sim-title">🚌 Public Bus No. 401 Safety Simulator</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim4Action('seated')">Stay Safely Seated</button>
      <button class="sim-btn" onclick="sim4Action('window')">Window Danger Alert!</button>
      <button class="sim-btn" onclick="sim4Action('reserved')">Reserved Seat Etiquette</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim4Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Bus Body -->
      <rect x="20" y="30" width="200" height="75" rx="8" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
      <!-- Windows -->
      <rect x="35" y="42" width="30" height="25" rx="3" fill="#bae6fd"/>
      <rect x="75" y="42" width="30" height="25" rx="3" fill="#bae6fd"/>
      <rect x="115" y="42" width="30" height="25" rx="3" fill="#bae6fd"/>
      <rect x="155" y="42" width="30" height="25" rx="3" fill="#bae6fd"/>
      <!-- Route Board -->
      <rect x="175" y="33" width="35" height="7" rx="1" fill="#0f172a"/>
      <text x="192" y="39" fill="#facc15" font-size="6" text-anchor="middle" font-weight="bold">ROUTE 401</text>
      <!-- Wheels -->
      <circle cx="65" cy="105" r="14" fill="#1e293b" stroke="#64748b" stroke-width="3"/>
      <circle cx="175" cy="105" r="14" fill="#1e293b" stroke="#64748b" stroke-width="3"/>

      <!-- Passenger Inside Window 2 -->
      <g id="sim4Passenger" transform="translate(90, 55)">
        <circle cx="0" cy="-4" r="5" fill="#f59e0b"/>
      </g>
    </svg>
    <div id="sim4Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      💺 <b>Stay Seated:</b> Passengers remain securely in seats, holding grab rails during vehicle acceleration and braking.
    </div>
  </div>
</div>
<script>
function sim4Action(act) {
  document.querySelectorAll('#sim4 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(act)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const p = document.getElementById('sim4Passenger');
  const fb = document.getElementById('sim4Feedback');

  if (act === 'seated') {
    p.innerHTML = '<circle cx="0" cy="-4" r="5" fill="#f59e0b"/>';
    fb.style.color = '#34d399';
    fb.innerHTML = '💺 <b>Safety In Transit:</b> Sitting upright inside the bus prevents loss of balance during turns and sudden stops.';
  } else if (act === 'window') {
    p.innerHTML = `
      <circle cx="0" cy="-4" r="5" fill="#ef4444"/>
      <line x1="0" y1="0" x2="8" y2="-8" stroke="#ef4444" stroke-width="2"/>
    `;
    fb.style.color = '#f87171';
    fb.innerHTML = '⚠️ <b>DANGER!</b> Sticking hands or head out of moving windows risks fatal collisions with passing poles and trees!';
  } else if (act === 'reserved') {
    p.innerHTML = '<circle cx="0" cy="-4" r="5" fill="#22c55e"/>';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '👵 <b>Civic Courtesy:</b> Giving up front reserved seats to elderly citizens protects them from falls and demonstrates respect.';
  }
}
</script>
""",

    5: """
<div class="sim-container" id="sim5">
  <div class="sim-header">
    <div class="sim-title">🎫 Bus Conductor Ticketing Machine</div>
    <div class="sim-controls">
      <button class="sim-btn" onclick="sim5AddTicket('full')">+ Full Ticket (₹20)</button>
      <button class="sim-btn" onclick="sim5AddTicket('half')">+ Half Ticket (₹10)</button>
      <button class="sim-btn" onclick="sim5Reset()">Reset Tickets</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <!-- Digital Ticket Display -->
    <div id="sim5Receipt" style="width:200px; background:#f8fafc; color:#0f172a; padding:10px; border-radius:8px; font-family:monospace; font-size:11px; border:1px solid #cbd5e1; box-shadow:0 4px 6px rgba(0,0,0,0.3);">
      <div style="text-align:center; font-weight:bold; border-bottom:1px dashed #64748b; padding-bottom:4px;">CITY BUS CORP - ROUTE 401</div>
      <div style="margin-top:4px;">Adult Full (₹20): <span id="sim5FullCount">5</span></div>
      <div>Child Half (₹10): <span id="sim5HalfCount">4</span></div>
      <div style="border-top:1px dashed #64748b; margin-top:4px; padding-top:4px; font-weight:bold;">
        TOTAL FARE: ₹<span id="sim5Total">140</span>
      </div>
    </div>
    <div id="sim5Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#38bdf8; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🧾 <b>5 Full + 4 Half Tickets:</b> (5 × ₹20) + (4 × ₹10) = ₹100 + ₹40 = ₹140 total fare paid!
    </div>
  </div>
</div>
<script>
let sim5Full = 5;
let sim5Half = 4;

function sim5AddTicket(type) {
  if (type === 'full') sim5Full++;
  if (type === 'half') sim5Half++;
  sim5Update();
}

function sim5Reset() {
  sim5Full = 0;
  sim5Half = 0;
  sim5Update();
}

function sim5Update() {
  document.getElementById('sim5FullCount').textContent = sim5Full;
  document.getElementById('sim5HalfCount').textContent = sim5Half;
  const total = (sim5Full * 20) + (sim5Half * 10);
  document.getElementById('sim5Total').textContent = total;
  const fb = document.getElementById('sim5Feedback');
  fb.style.color = '#34d399';
  fb.innerHTML = `🧾 <b>Fare Updated:</b> ${sim5Full} Full (₹${sim5Full*20}) + ${sim5Half} Half (₹${sim5Half*10}) = ₹${total} total transit fare.`;
}
</script>
""",

    6: """
<div class="sim-container" id="sim6">
  <div class="sim-header">
    <div class="sim-title">🎪 Mela Entrance Amenities & Map Explorer</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim6Amenity('lost')">Lost & Found Booth</button>
      <button class="sim-btn" onclick="sim6Amenity('map')">Schematic Wayfinding Map</button>
      <button class="sim-btn" onclick="sim6Amenity('water')">Clean Water Station</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim6Display" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim6Icon" style="font-size:38px;">📢 🎪 ℹ️</div>
      <div id="sim6Label" style="font-size:13px; font-weight:bold; color:#fbbf24; margin-top:4px;">Lost & Found Assistance</div>
    </div>
    <div id="sim6Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#fbbf24; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      📢 <b>Designated Landmark:</b> The Lost & Found booth features loudspeakers and official personnel to help reunite separated family members.
    </div>
  </div>
</div>
<script>
function sim6Amenity(am) {
  document.querySelectorAll('#sim6 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(am)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim6Icon');
  const label = document.getElementById('sim6Label');
  const fb = document.getElementById('sim6Feedback');

  if (am === 'lost') {
    icon.innerHTML = '📢 🎪 ℹ️';
    label.innerHTML = 'Lost & Found Assistance Booth';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '📢 <b>Safety Landmark:</b> Memorize this central location! If separated, children report here for loudspeaker public announcements.';
  } else if (am === 'map') {
    icon.innerHTML = '🗺️ 🧭 📍';
    label.innerHTML = 'Illuminated Wayfinding Map';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🗺️ <b>Wayfinding Orientation:</b> Schematic maps guide visitors to rides, food courts, craft stalls, and emergency exits.';
  } else if (am === 'water') {
    icon.innerHTML = '🚰 💧 🧼';
    label.innerHTML = 'Municipal Drinking Water Station';
    fb.style.color = '#34d399';
    fb.innerHTML = '🚰 <b>Clean Hydration:</b> Filtered drinking water taps keep festive crowds hydrated and provide soap points for handwashing.';
  }
}
</script>
""",

    7: """
<div class="sim-container" id="sim7">
  <div class="sim-header">
    <div class="sim-title">🚒 Emergency Vehicle Fleet Inspector</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim7Vehicle('ambulance')">Medical Ambulance</button>
      <button class="sim-btn" onclick="sim7Vehicle('fire')">Fire Engine</button>
      <button class="sim-btn" onclick="sim7Vehicle('police')">Police Patrol Jeep</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <div id="sim7Display" style="width:210px; height:120px; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:12px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:8px;">
      <div id="sim7Icon" style="font-size:38px;">🚑 🚨 🩺</div>
      <div id="sim7Name" style="font-size:14px; font-weight:bold; color:#f87171; margin-top:4px;">Hospital Ambulance (Call 108/102)</div>
    </div>
    <div id="sim7Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#f87171; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      🚑 <b>Rapid Medical Response:</b> Staffed by paramedics with oxygen and stretchers to treat sudden heat exhaustion or injuries.
    </div>
  </div>
</div>
<script>
function sim7Vehicle(v) {
  document.querySelectorAll('#sim7 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(v)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const icon = document.getElementById('sim7Icon');
  const name = document.getElementById('sim7Name');
  const fb = document.getElementById('sim7Feedback');

  if (v === 'ambulance') {
    icon.innerHTML = '🚑 🚨 🩺';
    name.innerHTML = 'Emergency Ambulance (Call 108/102)';
    fb.style.color = '#f87171';
    fb.innerHTML = '🚑 <b>Emergency Care:</b> Mobile medical units provide immediate first aid, oxygen, and rapid hospital transit.';
  } else if (v === 'fire') {
    icon.innerHTML = '🚒 🧯 💧';
    name.innerHTML = 'Municipal Fire Engine (Call 101)';
    fb.style.color = '#fbbf24';
    fb.innerHTML = '🚒 <b>Fire Safety:</b> Equipped with high-pressure hoses and water tanks to prevent accidental cooking tent fires.';
  } else if (v === 'police') {
    icon.innerHTML = '🚓 👮 🐕';
    name.innerHTML = 'Police Patrol Jeep (Call 112/100)';
    fb.style.color = '#38bdf8';
    fb.innerHTML = '🚓 <b>Public Security:</b> Officers coordinate crowd flows, prevent theft, and maintain peaceful community order.';
  }
}
</script>
""",

    8: """
<div class="sim-container" id="sim8">
  <div class="sim-header">
    <div class="sim-title">🧑‍🦽 Barrier-Free Accessibility & Ramp Tester</div>
    <div class="sim-controls">
      <button class="sim-btn active" onclick="sim8Test('ramp')">Accessible Slope Ramp</button>
      <button class="sim-btn" onclick="sim8Test('stairs')">Steep Staircase (Barrier!)</button>
    </div>
  </div>
  <div class="sim-canvas-wrap" style="min-height:220px; display:flex; flex-direction:column; align-items:center; justify-content:center; padding:12px;">
    <svg id="sim8Svg" viewBox="0 0 240 140" style="width:230px; height:134px; background:rgba(15,23,42,0.6); border-radius:12px; border:1px solid rgba(255,255,255,0.15);">
      <!-- Elevated Pavilion Platform -->
      <rect x="150" y="50" width="90" height="70" fill="#334155"/>
      <text x="195" y="85" fill="#f8fafc" font-size="9" text-anchor="middle">Pavilion</text>

      <!-- Pathway Switch Group -->
      <g id="sim8Pathway">
        <!-- Default Ramp: gentle triangle -->
        <polygon points="30,120 150,120 150,50" fill="#0284c7" opacity="0.7"/>
        <line x1="30" y1="110" x2="150" y2="40" stroke="#facc15" stroke-width="2"/>
        <text x="80" y="85" fill="#facc15" font-size="8" transform="rotate(-28 80 85)">Access Ramp</text>
      </g>

      <!-- Wheelchair Icon Group -->
      <g id="sim8Chair" transform="translate(60, 85)">
        <circle cx="0" cy="0" r="10" fill="none" stroke="#f8fafc" stroke-width="2"/>
        <circle cx="0" cy="-14" r="5" fill="#38bdf8"/>
        <line x1="0" y1="-9" x2="0" y2="2" stroke="#38bdf8" stroke-width="2.5"/>
      </g>
    </svg>
    <div id="sim8Feedback" style="margin-top:10px; font-size:13px; font-weight:bold; color:#34d399; background:rgba(0,0,0,0.4); border:1px solid rgba(255,255,255,0.15); border-radius:10px; padding:6px 20px; text-align:center;">
      ♿ <b>Barrier-Free Ramp:</b> Smooth gentle incline allows wheelchairs to glide safely up to exhibition pavilions without stair barriers!
    </div>
  </div>
</div>
<script>
function sim8Test(type) {
  document.querySelectorAll('#sim8 .sim-controls button').forEach(b => {
    if (b.textContent.toLowerCase().includes(type)) b.classList.add('active');
    else b.classList.remove('active');
  });

  const p = document.getElementById('sim8Pathway');
  const c = document.getElementById('sim8Chair');
  const fb = document.getElementById('sim8Feedback');

  if (type === 'ramp') {
    p.innerHTML = `
      <polygon points="30,120 150,120 150,50" fill="#0284c7" opacity="0.7"/>
      <line x1="30" y1="110" x2="150" y2="40" stroke="#facc15" stroke-width="2"/>
      <text x="80" y="85" fill="#facc15" font-size="8" transform="rotate(-28 80 85)">Access Ramp</text>
    `;
    c.setAttribute('transform', 'translate(100, 60)');
    fb.style.color = '#34d399';
    fb.innerHTML = '♿ <b>Universal Accessibility:</b> Sloping ramps enable smooth rolling for senior wheelchairs and family strollers alike.';
  } else if (type === 'stairs') {
    p.innerHTML = `
      <rect x="60" y="100" width="30" height="20" fill="#475569"/>
      <rect x="90" y="80" width="30" height="40" fill="#475569"/>
      <rect x="120" y="60" width="30" height="60" fill="#475569"/>
    `;
    c.setAttribute('transform', 'translate(45, 105)');
    fb.style.color = '#f87171';
    fb.innerHTML = '⛔ <b>Physical Barrier!</b> Vertical stairs block wheelchair access, excluding elders unless an accessible ramp is built.';
  }
}
</script>
"""
}

if __name__ == "__main__":
    print(f"Loaded {len(sims_part1)} simulators for Part 1 (Slides 1 to 8).")
    for k in sorted(sims_part1.keys()):
        print(f"Sim {k}: length {len(sims_part1[k])} chars")
