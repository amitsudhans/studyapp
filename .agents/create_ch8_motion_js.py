# -*- coding: utf-8 -*-
"""
Generates .agents/class7_science_time_motion_js.py containing all JavaScript logic
for the 16 simulators in Class 7 Science Chapter 8.
"""

js_code = r'''
/* =========================================================================
   CLASS 7 SCIENCE CHAPTER 8: TIME & MOTION SIMULATORS JAVASCRIPT
   ========================================================================= */

(function() {
  // Global simulator states
  let celestialCycleTab = 'day';
  let celestialAutoTimer = null;
  let celestialVal = 180;

  let ancientTab = 'sundial';
  let ancientVal = 12;
  let ancientAutoTimer = null;

  let evoTab = 'mechanical';
  let evoRunning = true;
  let evoTimer = null;
  let evoTick = 0;

  let anatomyAngle = 0;
  let anatomyTimer = null;

  let isoRunning = false;
  let isoTimer = null;
  let isoAngle = 15;
  let isoLength = 100;
  let isoMass = 100;

  let slowFastRunning = false;
  let slowFastMode = 'equal_time';
  let slowFastTimer = null;

  let journeyRunning = false;
  let journeyTimer = null;

  let dashSpeed = 40;
  let dashOdo = 2458.2;
  let dashTimer = null;

  let uniRunning = false;
  let uniTimer = null;

  let nonUniRunning = false;
  let nonUniTimer = null;

  let heritageTab = 'jaipur';
  let heritageVal = 12;
  let heritageTimer = null;

  let activeTriangleVar = 'D';

  /* -------------------------------------------------------------
     1. NATURAL TIME CYCLES SIM
     ------------------------------------------------------------- */
  window.switchCycleTab = function(tab) {
    celestialCycleTab = tab;
    clearInterval(celestialAutoTimer);
    celestialAutoTimer = null;
    document.getElementById('btnCycleAuto').textContent = '▶ Animate Cycle';

    ['btnCycleDay', 'btnCycleMonth', 'btnCycleYear'].forEach(id => {
      const btn = document.getElementById(id);
      if (btn) {
        btn.className = 'px-3 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
      }
    });

    const activeBtn = document.getElementById(tab === 'day' ? 'btnCycleDay' : tab === 'month' ? 'btnCycleMonth' : 'btnCycleYear');
    if (activeBtn) {
      activeBtn.className = 'px-3 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md';
    }

    const slider = document.getElementById('cycleSlider');
    const label = document.getElementById('cycleSliderLabel');
    const expl = document.getElementById('cycleExplanation');

    if (tab === 'day') {
      label.textContent = 'Earth Rotation:';
      slider.min = 0; slider.max = 360; slider.value = 180;
      expl.innerHTML = '<strong>Solar Day:</strong> Caused by Earth\'s axial rotation (360° every 24 hours). Sunrise to sunrise = 1 day.';
    } else if (tab === 'month') {
      label.textContent = 'Moon Orbital Phase:';
      slider.min = 0; slider.max = 360; slider.value = 180;
      expl.innerHTML = '<strong>Lunar Month:</strong> The Moon completes an orbit around Earth every ~29.5 days, cycling from New Moon to Full Moon.';
    } else {
      label.textContent = 'Earth Orbit Around Sun:';
      slider.min = 0; slider.max = 360; slider.value = 90;
      expl.innerHTML = '<strong>Solar Year:</strong> The Earth revolves around the Sun in ~365.25 days, causing the seasonal cycle of Summer, Monsoon, and Winter.';
    }
    window.updateCelestialCycle(slider.value);
  };

  window.updateCelestialCycle = function(val) {
    celestialVal = parseFloat(val);
    const grp = document.getElementById('celestialVisualGroup');
    const valText = document.getElementById('cycleSliderValue');
    const badge = document.getElementById('cycleOverlayBadge');
    if (!grp) return;

    if (celestialCycleTab === 'day') {
      const hours = ((celestialVal / 360) * 24).toFixed(1);
      if (valText) valText.textContent = celestialVal + '°';
      if (badge) badge.textContent = `Earth Rotation: ${hours} h (Angle: ${Math.round(celestialVal)}°)`;

      grp.innerHTML = `
        <!-- Fixed Distant Sun on left -->
        <circle cx="90" cy="120" r="38" fill="#f59e0b" filter="drop-shadow(0 0 16px rgba(245,158,11,0.8))"/>
        <text x="90" y="125" text-anchor="middle" fill="#78350f" font-size="12" font-weight="bold">SUN</text>
        <!-- Sunlight rays -->
        <line x1="140" y1="100" x2="330" y2="100" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="6 4" opacity="0.6"/>
        <line x1="140" y1="120" x2="330" y2="120" stroke="#fef08a" stroke-width="2" opacity="0.8"/>
        <line x1="140" y1="140" x2="330" y2="140" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="6 4" opacity="0.6"/>
        <!-- Earth Axis & Globe -->
        <g transform="translate(420, 120)">
          <!-- Axial tilt line -->
          <line x1="-30" y1="-75" x2="30" y2="75" stroke="#94a3b8" stroke-width="2" stroke-dasharray="4 2"/>
          <!-- Earth sphere -->
          <circle cx="0" cy="0" r="50" fill="#0284c7"/>
          <!-- Day lit hemisphere (left facing Sun) -->
          <path d="M 0,-50 A 50,50 0 0,0 0,50 Z" fill="#38bdf8" opacity="0.4"/>
          <!-- Night shadowed hemisphere -->
          <path d="M 0,-50 A 50,50 0 0,1 0,50 Z" fill="#0f172a" opacity="0.75"/>
          <!-- Continents rotated -->
          <g transform="rotate(${celestialVal})">
            <circle cx="28" cy="15" r="14" fill="#22c55e" opacity="0.85"/>
            <circle cx="-20" cy="-20" r="18" fill="#16a34a" opacity="0.85"/>
            <!-- Observer pin -->
            <line x1="0" y1="0" x2="0" y2="-52" stroke="#ef4444" stroke-width="3"/>
            <circle cx="0" cy="-52" r="5" fill="#ef4444"/>
            <text x="0" y="-60" text-anchor="middle" fill="#f87171" font-size="10" font-weight="bold">Observer</text>
          </g>
          <text x="0" y="70" text-anchor="middle" fill="#93c5fd" font-size="11" font-weight="bold">EARTH (Rotates 360° in 24 h)</text>
        </g>
      `;
    } else if (celestialCycleTab === 'month') {
      const days = ((celestialVal / 360) * 29.5).toFixed(1);
      const moonRad = (celestialVal * Math.PI) / 180;
      const mx = 360 + 90 * Math.cos(moonRad);
      const my = 120 + 70 * Math.sin(moonRad);

      let phaseName = 'New Moon (Amavasya)';
      if (celestialVal > 45 && celestialVal < 135) phaseName = 'First Quarter (Half Moon)';
      else if (celestialVal >= 135 && celestialVal <= 225) phaseName = 'Full Moon (Purnima)';
      else if (celestialVal > 225 && celestialVal < 315) phaseName = 'Third Quarter';

      if (valText) valText.textContent = celestialVal + '°';
      if (badge) badge.textContent = `Lunar Cycle: Day ${days} (${phaseName})`;

      grp.innerHTML = `
        <!-- Distant Sun on left -->
        <circle cx="60" cy="120" r="32" fill="#f59e0b" filter="drop-shadow(0 0 14px rgba(245,158,11,0.8))"/>
        <!-- Earth in center -->
        <circle cx="360" cy="120" r="34" fill="#0284c7"/>
        <text x="360" y="125" text-anchor="middle" fill="#fff" font-size="11" font-weight="bold">Earth</text>
        <!-- Moon Orbit path -->
        <ellipse cx="360" cy="120" rx="90" ry="70" fill="none" stroke="#475569" stroke-dasharray="4 3" stroke-width="1.5"/>
        <!-- Moon -->
        <g transform="translate(${mx}, ${my})">
          <circle cx="0" cy="0" r="14" fill="#64748b"/>
          <path d="M 0,-14 A 14,14 0 0,0 0,14 Z" fill="#f8fafc"/>
          <circle cx="0" cy="0" r="14" fill="none" stroke="#cbd5e1" stroke-width="1"/>
        </g>
        <text x="360" y="215" text-anchor="middle" fill="#cbd5e1" font-size="11">Moon Orbit: ~29.5 Days (1 Lunar Month)</text>
      `;
    } else {
      // Solar Year View
      const days = Math.round((celestialVal / 360) * 365.25);
      const earthRad = (celestialVal * Math.PI) / 180;
      const ex = 300 + 180 * Math.cos(earthRad);
      const ey = 120 + 80 * Math.sin(earthRad);

      let season = 'Spring';
      if (celestialVal >= 45 && celestialVal < 135) season = 'Summer (Northern Hemisphere)';
      else if (celestialVal >= 135 && celestialVal < 225) season = 'Autumn / Monsoon';
      else if (celestialVal >= 225 && celestialVal < 315) season = 'Winter';

      if (valText) valText.textContent = celestialVal + '°';
      if (badge) badge.textContent = `Year: Day ${days} / 365 (${season})`;

      grp.innerHTML = `
        <!-- Sun in Center -->
        <circle cx="300" cy="120" r="36" fill="#f59e0b" filter="drop-shadow(0 0 16px rgba(245,158,11,0.8))"/>
        <text x="300" y="125" text-anchor="middle" fill="#78350f" font-size="12" font-weight="bold">SUN</text>
        <!-- Orbit Ellipse -->
        <ellipse cx="300" cy="120" rx="180" ry="80" fill="none" stroke="#475569" stroke-dasharray="4 3" stroke-width="1.5"/>
        <!-- Earth on Orbit -->
        <g transform="translate(${ex}, ${ey})">
          <circle cx="0" cy="0" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
          <circle cx="4" cy="-4" r="5" fill="#22c55e"/>
          <text x="0" y="28" text-anchor="middle" fill="#93c5fd" font-size="10" font-weight="bold">Earth</text>
        </g>
        <text x="300" y="225" text-anchor="middle" fill="#cbd5e1" font-size="11">Earth Revolution: 365.25 Days = 1 Solar Year</text>
      `;
    }
  };

  window.toggleCelestialAuto = function() {
    const btn = document.getElementById('btnCycleAuto');
    if (celestialAutoTimer) {
      clearInterval(celestialAutoTimer);
      celestialAutoTimer = null;
      if (btn) btn.textContent = '▶ Animate Cycle';
    } else {
      if (btn) btn.textContent = '⏸ Pause';
      celestialAutoTimer = setInterval(() => {
        celestialVal = (celestialVal + 2) % 360;
        const slider = document.getElementById('cycleSlider');
        if (slider) slider.value = celestialVal;
        window.updateCelestialCycle(celestialVal);
      }, 50);
    }
  };

  window.resetCelestialCycle = function() {
    clearInterval(celestialAutoTimer);
    celestialAutoTimer = null;
    document.getElementById('btnCycleAuto').textContent = '▶ Animate Cycle';
    const slider = document.getElementById('cycleSlider');
    if (slider) slider.value = 180;
    window.updateCelestialCycle(180);
  };

  /* -------------------------------------------------------------
     2. ANCIENT CLOCKS SIM
     ------------------------------------------------------------- */
  window.switchAncientTab = function(tab) {
    ancientTab = tab;
    clearInterval(ancientAutoTimer);
    ancientAutoTimer = null;
    document.getElementById('btnAncientAction').textContent = '▶ Advance Sun';

    ['btnTabSundial', 'btnTabWater', 'btnTabSand'].forEach(id => {
      const b = document.getElementById(id);
      if (b) b.className = 'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    });

    const activeBtn = document.getElementById(tab === 'sundial' ? 'btnTabSundial' : tab === 'water' ? 'btnTabWater' : 'btnTabSand');
    if (activeBtn) activeBtn.className = 'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md';

    const slider = document.getElementById('ancientSlider');
    const label = document.getElementById('ancientControlLabel');
    const desc = document.getElementById('ancientDescription');

    if (tab === 'sundial') {
      label.textContent = 'Sun Position:';
      slider.min = 6; slider.max = 18; slider.step = 0.25; slider.value = 12;
      desc.innerHTML = '<strong>Sundial:</strong> A triangular gnomon casts a moving shadow as the Sun travels across the sky.';
    } else if (tab === 'water') {
      label.textContent = 'Water Drained (min):';
      slider.min = 0; slider.max = 60; slider.step = 1; slider.value = 20;
      desc.innerHTML = '<strong>Clepsydra (Water Clock):</strong> Water trickles at a steady rate through a hole in the container; water marks indicate elapsed hours.';
    } else {
      label.textContent = 'Sand Drained (%):';
      slider.min = 0; slider.max = 100; slider.step = 2; slider.value = 40;
      desc.innerHTML = '<strong>Hourglass:</strong> Fine sand drains steadily through a narrow neck from the upper glass bulb to the lower bulb.';
    }
    window.updateAncientClock(slider.value);
  };

  window.updateAncientClock = function(val) {
    ancientVal = parseFloat(val);
    const grp = document.getElementById('ancientClockGroup');
    const badge = document.getElementById('ancientStatusBadge');
    const valText = document.getElementById('ancientControlValue');
    if (!grp) return;

    if (ancientTab === 'sundial') {
      const hr = Math.floor(ancientVal);
      const min = Math.round((ancientVal - hr) * 60);
      const ampm = ancientVal < 12 ? 'AM' : 'PM';
      const dispHr = hr > 12 ? hr - 12 : (hr === 0 ? 12 : hr);
      const timeStr = `${dispHr}:${min < 10 ? '0' : ''}${min} ${ampm}`;
      if (valText) valText.textContent = timeStr;
      if (badge) badge.textContent = `Time: ${timeStr} (Solar Dial)`;

      // Sun angle from -75 to +75 deg
      const sunAngle = ((ancientVal - 12) / 6) * 70; // deg
      const sunRad = (sunAngle * Math.PI) / 180;
      const sunX = 300 + 200 * Math.sin(sunRad);
      const sunY = 160 - 130 * Math.cos(sunRad);

      // Shadow angle opposite
      const shadowLength = 80 * Math.tan(Math.abs(sunRad));
      const shadowDirection = sunAngle > 0 ? -1 : 1;
      const shadowEndX = 300 + (shadowDirection * Math.min(140, shadowLength));

      grp.innerHTML = `
        <!-- Sky Horizon -->
        <line x1="50" y1="180" x2="550" y2="180" stroke="#475569" stroke-width="2"/>
        <rect x="50" y="180" width="500" height="40" fill="#1e293b"/>
        <!-- Sundial Dial Plate -->
        <ellipse cx="300" cy="180" rx="140" ry="24" fill="#334155" stroke="#64748b" stroke-width="2"/>
        <!-- Hour tick marks on plate -->
        <line x1="180" y1="180" x2="190" y2="180" stroke="#f59e0b" stroke-width="2"/>
        <line x1="220" y1="185" x2="225" y2="180" stroke="#cbd5e1" stroke-width="1.5"/>
        <line x1="260" y1="188" x2="262" y2="180" stroke="#cbd5e1" stroke-width="1.5"/>
        <line x1="300" y1="190" x2="300" y2="180" stroke="#f59e0b" stroke-width="2"/>
        <line x1="340" y1="188" x2="338" y2="180" stroke="#cbd5e1" stroke-width="1.5"/>
        <line x1="380" y1="185" x2="375" y2="180" stroke="#cbd5e1" stroke-width="1.5"/>
        <line x1="420" y1="180" x2="410" y2="180" stroke="#f59e0b" stroke-width="2"/>
        <text x="300" y="202" fill="#fef08a" font-size="9" text-anchor="middle" font-family="monospace">12 NOON</text>

        <!-- Dynamic Shadow -->
        <polygon points="300,180 300,182 ${shadowEndX},183" fill="#020617" opacity="0.8"/>
        <!-- Gnomon Triangle -->
        <polygon points="300,180 300,90 260,180" fill="#f59e0b" stroke="#d97706" stroke-width="1.5"/>
        <text x="275" y="140" fill="#78350f" font-size="9" font-weight="bold">GNOMON</text>

        <!-- Sun -->
        <circle cx="${sunX}" cy="${sunY}" r="18" fill="#fbbf24" filter="drop-shadow(0 0 12px rgba(251,191,36,0.9))"/>
        <!-- Sun ray to gnomon -->
        <line x1="${sunX}" y1="${sunY}" x2="300" y2="90" stroke="#fef08a" stroke-width="1.5" stroke-dasharray="3 3" opacity="0.6"/>
      `;
    } else if (ancientTab === 'water') {
      if (valText) valText.textContent = `${ancientVal} min`;
      if (badge) badge.textContent = `Water Level: ${ancientVal} min elapsed`;
      const waterHeight = (ancientVal / 60) * 110;

      grp.innerHTML = `
        <!-- Upper reservoir -->
        <rect x="180" y="20" width="80" height="60" rx="4" fill="#1e293b" stroke="#475569" stroke-width="2"/>
        <rect x="182" y="${22 + (ancientVal/60)*45}" width="76" height="${56 - (ancientVal/60)*45}" fill="#38bdf8" opacity="0.7"/>
        <!-- Dripping spout -->
        <line x1="220" y1="80" x2="220" y2="110" stroke="#38bdf8" stroke-width="3" stroke-dasharray="4 4"/>
        <circle cx="220" cy="115" r="3" fill="#38bdf8"/>

        <!-- Lower collection cylinder -->
        <rect x="340" y="70" width="90" height="130" rx="4" fill="#0f172a" stroke="#64748b" stroke-width="2"/>
        <!-- Calibrated markings -->
        <line x1="340" y1="160" x2="355" y2="160" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="360" y="163" fill="#cbd5e1" font-size="9">15 min</text>
        <line x1="340" y1="130" x2="355" y2="130" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="360" y="133" fill="#cbd5e1" font-size="9">30 min</text>
        <line x1="340" y1="100" x2="355" y2="100" stroke="#fbbf24" stroke-width="1.5"/>
        <text x="360" y="103" fill="#cbd5e1" font-size="9">45 min</text>
        <!-- Rising water -->
        <rect x="342" y="${198 - waterHeight}" width="86" height="${waterHeight}" fill="#0284c7" opacity="0.85"/>
        <text x="385" y="218" fill="#93c5fd" font-size="10" text-anchor="middle">Clepsydra Outflow</text>
      `;
    } else {
      // Hourglass
      if (valText) valText.textContent = `${ancientVal}%`;
      if (badge) badge.textContent = `Hourglass: ${ancientVal}% sand drained`;
      const topSand = 50 * (1 - ancientVal / 100);
      const botSand = 50 * (ancientVal / 100);

      grp.innerHTML = `
        <!-- Glass Bulb Outline -->
        <path d="M 260,30 L 340,30 L 305,120 L 340,210 L 260,210 L 295,120 Z" fill="#0f172a" stroke="#94a3b8" stroke-width="2"/>
        <!-- Wooden Stands -->
        <rect x="245" y="22" width="110" height="8" rx="2" fill="#78350f"/>
        <rect x="245" y="210" width="110" height="8" rx="2" fill="#78350f"/>
        <line x1="250" y1="30" x2="250" y2="210" stroke="#78350f" stroke-width="3"/>
        <line x1="350" y1="30" x2="350" y2="210" stroke="#78350f" stroke-width="3"/>
        <!-- Top Sand Triangle -->
        <polygon points="268,${120 - topSand} 332,${120 - topSand} 300,120" fill="#f59e0b"/>
        <!-- Falling sand stream -->
        <line x1="300" y1="120" x2="300" y2="180" stroke="#fbbf24" stroke-width="1.5" stroke-dasharray="3 2"/>
        <!-- Bottom Sand Mound -->
        <polygon points="${300 - botSand*0.7},208 ${300 + botSand*0.7},208 300,${208 - botSand*0.6}" fill="#f59e0b"/>
        <text x="300" y="230" fill="#cbd5e1" font-size="10" text-anchor="middle">Sand Hourglass</text>
      `;
    }
  };

  window.toggleAncientAction = function() {
    const btn = document.getElementById('btnAncientAction');
    if (ancientAutoTimer) {
      clearInterval(ancientAutoTimer);
      ancientAutoTimer = null;
      if (btn) btn.textContent = '▶ Advance';
    } else {
      if (btn) btn.textContent = '⏸ Pause';
      ancientAutoTimer = setInterval(() => {
        const slider = document.getElementById('ancientSlider');
        let nextVal = parseFloat(slider.value) + (ancientTab === 'sundial' ? 0.2 : 2);
        if (nextVal > parseFloat(slider.max)) nextVal = parseFloat(slider.min);
        slider.value = nextVal;
        window.updateAncientClock(nextVal);
      }, 100);
    }
  };

  window.resetAncientClock = function() {
    clearInterval(ancientAutoTimer);
    ancientAutoTimer = null;
    document.getElementById('btnAncientAction').textContent = '▶ Advance';
    const slider = document.getElementById('ancientSlider');
    slider.value = ancientTab === 'sundial' ? 12 : ancientTab === 'water' ? 0 : 0;
    window.updateAncientClock(slider.value);
  };

  /* -------------------------------------------------------------
     3. CLOCK EVOLUTION SIM
     ------------------------------------------------------------- */
  window.switchEvoTab = function(tab) {
    evoTab = tab;
    ['btnEvoMech', 'btnEvoQuartz', 'btnEvoAtomic'].forEach(id => {
      const b = document.getElementById(id);
      if (b) b.className = 'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    });
    const active = document.getElementById(tab === 'mechanical' ? 'btnEvoMech' : tab === 'quartz' ? 'btnEvoQuartz' : 'btnEvoAtomic');
    if (active) active.className = 'px-2.5 py-1 text-xs font-semibold rounded-lg bg-cyan-500 text-slate-950 shadow-md';

    const expl = document.getElementById('evoExplanation');
    const badge = document.getElementById('evoMetricsBadge');
    if (tab === 'mechanical') {
      expl.innerHTML = '<strong>Mechanical Escapement:</strong> Escapement wheel regulated by swinging balance wheel or pendulum releases gears one tooth per second.';
      badge.textContent = 'Frequency: 1.0 Hz • Accuracy: ±15 s/day';
    } else if (tab === 'quartz') {
      expl.innerHTML = '<strong>Quartz Crystal Watch:</strong> A battery electrifies a tiny quartz crystal tuning-fork, vibrating at exactly 32,768 Hz. Digital microchips divide by 2^15 to emit 1 second pulses.';
      badge.textContent = 'Frequency: 32,768 Hz • Accuracy: ±1 s/month';
    } else {
      expl.innerHTML = '<strong>Cesium-133 Atomic Clock:</strong> Counts electromagnetic transitions of cesium atoms at 9,192,631,770 Hz. The official international definition of the SI second!';
      badge.textContent = 'Frequency: 9.19 GHz • Accuracy: 1 s in 30 Million Years';
    }
    window.renderEvo();
  };

  window.renderEvo = function() {
    const grp = document.getElementById('evoVisualGroup');
    if (!grp) return;

    if (evoTab === 'mechanical') {
      const angle = (evoTick % 2 === 0 ? 12 : -12);
      grp.innerHTML = `
        <!-- Gear / Escapement Wheel -->
        <g transform="translate(250, 120)">
          <circle cx="0" cy="0" r="45" fill="none" stroke="#f59e0b" stroke-width="4"/>
          <circle cx="0" cy="0" r="8" fill="#d97706"/>
          <!-- Teeth -->
          ${[0,30,60,90,120,150,180,210,240,270,300,330].map(a => `
            <line x1="0" y1="0" x2="${50*Math.cos(a*Math.PI/180)}" y2="${50*Math.sin(a*Math.PI/180)}" stroke="#fbbf24" stroke-width="3"/>
          `).join('')}
        </g>
        <!-- Pallet Fork / Anchor -->
        <g transform="translate(250, 50) rotate(${angle})">
          <polygon points="0,0 -25,25 25,25" fill="#38bdf8" stroke="#0284c7" stroke-width="1.5"/>
          <circle cx="0" cy="0" r="4" fill="#fff"/>
        </g>
        <!-- Balance pendulum -->
        <line x1="250" y1="50" x2="${250 + angle*2}" y2="210" stroke="#94a3b8" stroke-width="2"/>
        <circle cx="${250 + angle*2}" cy="210" r="14" fill="#f59e0b"/>
        <text x="430" y="110" fill="#38bdf8" font-size="12" font-weight="bold">Escapement Fork</text>
        <text x="430" y="130" fill="#94a3b8" font-size="10">Releases gear 1 tooth/sec</text>
      `;
    } else if (evoTab === 'quartz') {
      const vib = (evoTick % 2 === 0 ? 3 : -3);
      grp.innerHTML = `
        <!-- Quartz Tuning Fork -->
        <g transform="translate(180, 120)">
          <path d="M 0,20 L 20,20 L 20,-30 L 30,-30 L 30,20 L 50,20 L 50,40 L 0,40 Z" fill="#38bdf8" stroke="#0284c7" stroke-width="2"/>
          <!-- Prongs vibrating -->
          <line x1="25" y1="-30" x2="${25 + vib}" y2="-70" stroke="#38bdf8" stroke-width="6" stroke-linecap="round"/>
          <line x1="45" y1="-30" x2="${45 - vib}" y2="-70" stroke="#38bdf8" stroke-width="6" stroke-linecap="round"/>
          <text x="35" y="60" text-anchor="middle" fill="#93c5fd" font-size="10">Quartz Fork (32,768 Hz)</text>
        </g>
        <!-- Logic Divider Circuit -->
        <rect x="300" y="90" width="100" height="60" rx="6" fill="#1e293b" stroke="#38bdf8" stroke-width="1.5"/>
        <text x="350" y="115" text-anchor="middle" fill="#fef08a" font-size="11" font-family="monospace">÷ 2¹⁵</text>
        <text x="350" y="135" text-anchor="middle" fill="#4ade80" font-size="9">Binary Divider</text>
        <!-- Arrow -->
        <line x1="240" y1="120" x2="295" y2="120" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
        <!-- 1 Hz pulse LED -->
        <circle cx="470" cy="120" r="16" fill="${evoTick % 2 === 0 ? '#10b981' : '#064e3b'}" stroke="#34d399" stroke-width="2"/>
        <text x="470" y="155" text-anchor="middle" fill="#34d399" font-size="10" font-family="monospace">1 Hz Tick</text>
      `;
    } else {
      // Atomic
      grp.innerHTML = `
        <circle cx="200" cy="120" r="45" fill="#1e1b4b" stroke="#6366f1" stroke-width="2"/>
        <circle cx="200" cy="120" r="10" fill="#a855f7"/>
        <text x="200" y="124" text-anchor="middle" fill="#fff" font-size="8">¹³³Cs</text>
        <!-- Microwave beam -->
        <path d="M 260,120 Q 300,90 340,120 T 420,120" fill="none" stroke="#22d3ee" stroke-width="2.5"/>
        <text x="340" y="85" text-anchor="middle" fill="#67e8f9" font-size="11" font-family="monospace">9,192,631,770 Hz</text>
        <text x="340" y="160" text-anchor="middle" fill="#cbd5e1" font-size="10">Cesium-133 Resonant Hyperfine Frequency</text>
      `;
    }
  };

  window.toggleEvoRun = function() {
    const btn = document.getElementById('btnEvoRun');
    evoRunning = !evoRunning;
    if (btn) btn.textContent = evoRunning ? '⏸ Pause' : '▶ Play';
  };

  window.pulseEvo = function() {
    evoTick++;
    window.renderEvo();
  };

  // Run evolution ticker
  setInterval(() => {
    if (evoRunning) {
      evoTick++;
      window.renderEvo();
    }
  }, 500);

  /* -------------------------------------------------------------
     4. PENDULUM ANATOMY SIM
     ------------------------------------------------------------- */
  window.setAnatomyAngle = function(deg) {
    anatomyAngle = parseFloat(deg);
    const arm = document.getElementById('anatomyPendulumArm');
    const badge = document.getElementById('anatomyAngleBadge');
    const text = document.getElementById('anatomyAngleText');
    if (badge) badge.textContent = `${anatomyAngle.toFixed(1)}°`;
    if (text) text.textContent = `${Math.round(anatomyAngle)}°`;
    if (arm) arm.setAttribute('transform', `rotate(${anatomyAngle}, 300, 24)`);
  };

  window.startAnatomyOscillation = function() {
    clearInterval(anatomyTimer);
    let t = 0;
    let amp = 25;
    document.getElementById('btnAnatomyOscillate').textContent = 'Swinging...';
    anatomyTimer = setInterval(() => {
      t += 0.05;
      const angle = amp * Math.cos(t * 3) * Math.exp(-t * 0.1);
      window.setAnatomyAngle(angle);
      if (Math.abs(angle) < 0.2) {
        clearInterval(anatomyTimer);
        document.getElementById('btnAnatomyOscillate').textContent = '▶ Release to Swing';
      }
    }, 30);
  };

  window.resetAnatomy = function() {
    clearInterval(anatomyTimer);
    document.getElementById('btnAnatomyOscillate').textContent = '▶ Release to Swing';
    document.getElementById('anatomyAngleSlider').value = 0;
    window.setAnatomyAngle(0);
  };

  /* -------------------------------------------------------------
     5. PENDULUM ISOCHRONISM SIM
     ------------------------------------------------------------- */
  window.updateIsoParams = function() {
    isoLength = parseFloat(document.getElementById('isoLenSlider').value);
    isoMass = parseFloat(document.getElementById('isoMassSelect').value);
    isoAngle = parseFloat(document.getElementById('isoAmpSlider').value);

    document.getElementById('isoLenText').textContent = `${isoLength} cm`;
    const massLabel = isoMass === 20 ? '20 g (Wood)' : isoMass === 100 ? '100 g (Brass)' : '300 g (Lead)';
    document.getElementById('isoMassText').textContent = massLabel;
    document.getElementById('isoAmpText').textContent = `${isoAngle}°`;

    // Visual bob radius based on mass
    const r = isoMass === 20 ? 10 : isoMass === 100 ? 15 : 20;
    const bob = document.getElementById('isoBob');
    if (bob) bob.setAttribute('r', r);

    // Theoretical period T = 2 * pi * sqrt(L / g)
    const T = 2 * Math.PI * Math.sqrt((isoLength / 100) / 9.8);
    document.getElementById('isoPeriodResult').textContent = `Theoretical T: ${T.toFixed(2)} s`;
  };

  window.runIsoExperiment = function() {
    if (isoRunning) return;
    isoRunning = true;
    const btn = document.getElementById('btnIsoRun');
    if (btn) btn.textContent = 'Timing 20 Swings...';

    const T = 2 * Math.PI * Math.sqrt((isoLength / 100) / 9.8);
    let oscCount = 0;
    let elapsed = 0;
    let phase = 0;

    clearInterval(isoTimer);
    isoTimer = setInterval(() => {
      elapsed += 0.04;
      phase += (0.04 / T) * 2 * Math.PI;

      const currentAngle = isoAngle * Math.cos(phase);
      const arm = document.getElementById('isoArm');
      if (arm) arm.setAttribute('transform', `rotate(${currentAngle}, 200, 18)`);

      oscCount = Math.floor(elapsed / T);
      document.getElementById('isoCount').textContent = `${Math.min(20, oscCount)} / 20`;
      document.getElementById('isoStopwatch').textContent = `${elapsed.toFixed(2)} s`;

      if (oscCount >= 20) {
        clearInterval(isoTimer);
        isoRunning = false;
        if (btn) btn.textContent = '▶ Time 20 Swings';
        const measuredT = (elapsed / 20).toFixed(2);
        document.getElementById('isoPeriodResult').textContent = `T = Total / 20 = ${elapsed.toFixed(1)} s / 20 = ${measuredT} s`;
      }
    }, 40);
  };

  window.resetIso = function() {
    clearInterval(isoTimer);
    isoRunning = false;
    document.getElementById('btnIsoRun').textContent = '▶ Time 20 Swings';
    document.getElementById('isoCount').textContent = '0 / 20';
    document.getElementById('isoStopwatch').textContent = '0.00 s';
    const arm = document.getElementById('isoArm');
    if (arm) arm.setAttribute('transform', 'rotate(0, 200, 18)');
  };

  /* -------------------------------------------------------------
     6. SI TIME UNITS FORMATTER SIM
     ------------------------------------------------------------- */
  window.calcTimeUnits = function() {
    const val = parseFloat(document.getElementById('timeConvertInput').value) || 0;
    const unit = document.getElementById('timeConvertUnit').value;

    let sec = 0;
    if (unit === 'd') sec = val * 86400;
    else if (unit === 'h') sec = val * 3600;
    else if (unit === 'min') sec = val * 60;
    else sec = val;

    document.getElementById('resSec').textContent = `${sec.toLocaleString()} s`;
    document.getElementById('resMin').textContent = `${(sec / 60).toLocaleString()} min`;
    document.getElementById('resHour').textContent = `${(sec / 3600).toFixed(2)} h`;
    document.getElementById('resDay').textContent = `${(sec / 86400).toFixed(4)} d`;
  };

  window.validateSIGrammar = function(input) {
    const box = document.getElementById('siGrammarFeedback');
    const trimmed = input.trim();
    // Rule: number followed by space and lowercase 's'
    const validPattern = /^\d+(\.\d+)?\s+s$/;

    if (validPattern.test(trimmed)) {
      box.className = 'p-2.5 rounded-lg border bg-emerald-950/50 border-emerald-700/70 text-emerald-300';
      box.innerHTML = `
        <div class="flex items-center gap-1.5 font-bold"><span class="text-base">✓</span> Correct SI Notation!</div>
        <p class="text-[11px] mt-1 text-emerald-200/90 leading-tight">Symbol is strictly lowercase 's', separated by a space, never pluralized ('secs'), and has no trailing period.</p>
      `;
    } else {
      let reason = 'Must have a space before unit symbol \'s\'.';
      if (/secs|sec|SECS/i.test(trimmed)) reason = 'Never add \'s\' to make units plural (use \'s\', not \'secs\').';
      else if (/\.$/.test(trimmed)) reason = 'Do not put a trailing period after an SI unit symbol unless at end of sentence.';
      else if (/[A-Z]/.test(trimmed)) reason = 'SI symbol for second is strictly lowercase \'s\', not capital.';

      box.className = 'p-2.5 rounded-lg border bg-rose-950/50 border-rose-700/70 text-rose-300';
      box.innerHTML = `
        <div class="flex items-center gap-1.5 font-bold"><span class="text-base">✗</span> Syntax Error!</div>
        <p class="text-[11px] mt-1 text-rose-200/90 leading-tight">${reason}</p>
      `;
    }
  };

  window.setSIExample = function(val) {
    document.getElementById('siGrammarInput').value = val;
    window.validateSIGrammar(val);
  };

  /* -------------------------------------------------------------
     7. SLOW OR FAST SIM
     ------------------------------------------------------------- */
  window.setSlowFastMode = function(mode) {
    slowFastMode = mode;
    window.resetSlowFast();
    document.getElementById('btnModeEqTime').className = mode === 'equal_time' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    document.getElementById('btnModeEqDist').className = mode === 'equal_dist' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';

    const inst = document.getElementById('slowFastInstruction');
    inst.textContent = mode === 'equal_time' ?
      'In equal time (10 s), the object covering greater distance is faster.' :
      'Over equal distance (200 m), the object taking less time is faster.';
  };

  window.startSlowFastRace = function() {
    if (slowFastRunning) return;
    slowFastRunning = true;
    document.getElementById('btnSlowFastStart').textContent = 'Racing...';
    let t = 0;
    const vA = 25; // m/s
    const vB = 10; // m/s

    clearInterval(slowFastTimer);
    slowFastTimer = setInterval(() => {
      t += 0.1;
      document.getElementById('slowFastTimer').textContent = `${t.toFixed(1)} s`;

      const dA = vA * t;
      const dB = vB * t;

      if (slowFastMode === 'equal_time') {
        const pctA = Math.min(90, (dA / 250) * 85);
        const pctB = Math.min(90, (dB / 250) * 85);
        document.getElementById('laneAIcon').style.left = `${pctA}%`;
        document.getElementById('laneBIcon').style.left = `${pctB}%`;
        document.getElementById('laneADist').textContent = `d = ${Math.round(dA)} m`;
        document.getElementById('laneBDist').textContent = `d = ${Math.round(dB)} m`;

        if (t >= 10.0) {
          clearInterval(slowFastTimer);
          slowFastRunning = false;
          document.getElementById('btnSlowFastStart').textContent = '▶ Start Race';
          document.getElementById('slowFastVerdict').textContent = `Cheetah wins! (250 m vs 100 m in 10 s)`;
        }
      } else {
        // Equal distance (200m)
        const pctA = Math.min(88, (dA / 200) * 85);
        const pctB = Math.min(88, (dB / 200) * 85);
        document.getElementById('laneAIcon').style.left = `${pctA}%`;
        document.getElementById('laneBIcon').style.left = `${pctB}%`;
        document.getElementById('laneADist').textContent = `d = ${Math.min(200, Math.round(dA))} m`;
        document.getElementById('laneBDist').textContent = `d = ${Math.min(200, Math.round(dB))} m`;

        if (dA >= 200 && dB < 200) {
          document.getElementById('slowFastVerdict').textContent = `Cheetah crossed 200m in 8.0 s! Elephant still running...`;
        }
        if (dB >= 200) {
          clearInterval(slowFastTimer);
          slowFastRunning = false;
          document.getElementById('btnSlowFastStart').textContent = '▶ Start Race';
          document.getElementById('slowFastVerdict').textContent = `Cheetah took 8.0 s vs Elephant 20.0 s. Faster = Less Time!`;
        }
      }
    }, 100);
  };

  window.resetSlowFast = function() {
    clearInterval(slowFastTimer);
    slowFastRunning = false;
    document.getElementById('btnSlowFastStart').textContent = '▶ Start Race';
    document.getElementById('slowFastTimer').textContent = '0.0 s';
    document.getElementById('laneAIcon').style.left = '2%';
    document.getElementById('laneBIcon').style.left = '2%';
    document.getElementById('laneADist').textContent = 'd = 0 m';
    document.getElementById('laneBDist').textContent = 'd = 0 m';
    document.getElementById('slowFastVerdict').textContent = 'Ready to Start Race';
  };

  /* -------------------------------------------------------------
     8. SPEED DEFINITION SIM
     ------------------------------------------------------------- */
  window.calcSpeedDef = function() {
    const d = parseFloat(document.getElementById('speedDistSlider').value);
    const t = parseFloat(document.getElementById('speedTimeSlider').value);

    document.getElementById('speedDistText').textContent = `${d} m`;
    document.getElementById('speedTimeText').textContent = `${t} s`;

    const speedMs = d / t;
    const speedKmh = speedMs * 3.6;

    document.getElementById('gaugeSpeedText').textContent = `${speedMs.toFixed(1)} m/s`;
    document.getElementById('gaugeKmhText').textContent = `${speedKmh.toFixed(1)} km/h`;

    // Needle rotation (0 to 180 deg for 0 to 50 m/s)
    const angle = Math.min(180, (speedMs / 40) * 180);
    const needle = document.getElementById('gaugeNeedleGroup');
    if (needle) needle.setAttribute('transform', `rotate(${angle - 90}, 100, 110)`);
  };

  window.setSpeedPreset = function(speed, label) {
    const t = 10;
    const d = speed * t;
    document.getElementById('speedDistSlider').value = Math.min(1000, Math.max(50, d));
    document.getElementById('speedTimeSlider').value = t;
    window.calcSpeedDef();
  };

  /* -------------------------------------------------------------
     9. SPEED UNIT CONVERTER SIM
     ------------------------------------------------------------- */
  let convDir = 'kmh_to_ms';
  window.setConvDirection = function(dir) {
    convDir = dir;
    document.getElementById('btnDirKmhToMs').className = dir === 'kmh_to_ms' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    document.getElementById('btnDirMsToKmh').className = dir === 'ms_to_kmh' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';

    const label = document.getElementById('convInputLabel');
    const slider = document.getElementById('convSlider');
    if (dir === 'kmh_to_ms') {
      label.textContent = 'Input Speed in km/h:';
      slider.max = 180; slider.step = 18; slider.value = 72;
    } else {
      label.textContent = 'Input Speed in m/s:';
      slider.max = 50; slider.step = 5; slider.value = 20;
    }
    window.updateSpeedConv(slider.value);
  };

  window.updateSpeedConv = function(val) {
    const num = parseFloat(val);
    const inVal = document.getElementById('convInputValue');
    const outVal = document.getElementById('convResultValue');
    const stepText = document.getElementById('convFormulaStep');

    if (convDir === 'kmh_to_ms') {
      inVal.textContent = `${num} km/h`;
      const res = (num * 5) / 18;
      outVal.textContent = `${res.toFixed(1)} m/s`;
      stepText.textContent = `${num} × (5/18) = ${res.toFixed(1)} m/s`;
    } else {
      inVal.textContent = `${num} m/s`;
      const res = (num * 18) / 5;
      outVal.textContent = `${res.toFixed(1)} km/h`;
      stepText.textContent = `${num} × (18/5) = ${res.toFixed(1)} km/h`;
    }
  };

  window.setPresetConv = function(val) {
    document.getElementById('convSlider').value = val;
    window.updateSpeedConv(val);
  };

  /* -------------------------------------------------------------
     10. SPEED TRIANGLE SIM
     ------------------------------------------------------------- */
  window.selectTriangleVar = function(v) {
    activeTriangleVar = v;
    const badge = document.getElementById('triTargetBadge');
    const formulaBox = document.getElementById('triFormulaBox');
    const container = document.getElementById('triInputsContainer');

    if (v === 'D') {
      badge.textContent = 'Distance (D)';
      formulaBox.textContent = 'Distance = Speed × Time';
      container.innerHTML = `
        <div class="flex justify-between items-center"><label class="text-slate-400">Speed (v):</label><input type="number" id="triInput1" value="25" class="w-20 bg-slate-900 border border-slate-700 px-2 py-0.5 rounded font-mono text-cyan-300" oninput="window.calcTriangleResult()"><span class="text-slate-400">m/s</span></div>
        <div class="flex justify-between items-center"><label class="text-slate-400">Time (t):</label><input type="number" id="triInput2" value="12" class="w-20 bg-slate-900 border border-slate-700 px-2 py-0.5 rounded font-mono text-emerald-300" oninput="window.calcTriangleResult()"><span class="text-slate-400">s</span></div>
      `;
    } else if (v === 'S') {
      badge.textContent = 'Speed (S)';
      formulaBox.textContent = 'Speed = Distance / Time';
      container.innerHTML = `
        <div class="flex justify-between items-center"><label class="text-slate-400">Distance (d):</label><input type="number" id="triInput1" value="300" class="w-20 bg-slate-900 border border-slate-700 px-2 py-0.5 rounded font-mono text-amber-300" oninput="window.calcTriangleResult()"><span class="text-slate-400">m</span></div>
        <div class="flex justify-between items-center"><label class="text-slate-400">Time (t):</label><input type="number" id="triInput2" value="15" class="w-20 bg-slate-900 border border-slate-700 px-2 py-0.5 rounded font-mono text-emerald-300" oninput="window.calcTriangleResult()"><span class="text-slate-400">s</span></div>
      `;
    } else {
      badge.textContent = 'Time (T)';
      formulaBox.textContent = 'Time = Distance / Speed';
      container.innerHTML = `
        <div class="flex justify-between items-center"><label class="text-slate-400">Distance (d):</label><input type="number" id="triInput1" value="500" class="w-20 bg-slate-900 border border-slate-700 px-2 py-0.5 rounded font-mono text-amber-300" oninput="window.calcTriangleResult()"><span class="text-slate-400">m</span></div>
        <div class="flex justify-between items-center"><label class="text-slate-400">Speed (v):</label><input type="number" id="triInput2" value="20" class="w-20 bg-slate-900 border border-slate-700 px-2 py-0.5 rounded font-mono text-cyan-300" oninput="window.calcTriangleResult()"><span class="text-slate-400">m/s</span></div>
      `;
    }
    window.calcTriangleResult();
  };

  window.calcTriangleResult = function() {
    const val1 = parseFloat(document.getElementById('triInput1')?.value) || 0;
    const val2 = parseFloat(document.getElementById('triInput2')?.value) || 1;
    const res = document.getElementById('triResultText');
    if (!res) return;

    if (activeTriangleVar === 'D') {
      res.textContent = `${(val1 * val2).toFixed(1)} m`;
    } else if (activeTriangleVar === 'S') {
      res.textContent = `${(val1 / val2).toFixed(1)} m/s`;
    } else {
      res.textContent = `${(val1 / val2).toFixed(1)} s`;
    }
  };

  /* -------------------------------------------------------------
     11. AVERAGE VS INSTANTANEOUS SIM
     ------------------------------------------------------------- */
  window.startJourneySim = function() {
    if (journeyRunning) return;
    journeyRunning = true;
    document.getElementById('btnJourneyStart').textContent = 'Driving...';
    let t = 0;

    clearInterval(journeyTimer);
    journeyTimer = setInterval(() => {
      t += 0.05;
      const pct = (t / 10) * 85;
      document.getElementById('journeyCar').style.left = `${Math.min(85, pct)}%`;

      let speed = 20;
      let cumDist = 0;
      if (pct < 25) {
        speed = 20;
        cumDist = (pct / 25) * 20;
      } else if (pct < 75) {
        speed = 100;
        cumDist = 20 + ((pct - 25) / 50) * 120;
      } else {
        speed = 0;
        cumDist = 140;
      }

      document.getElementById('instSpeedDisplay').textContent = `${speed} km/h`;
      document.getElementById('cumDistDisplay').textContent = `${Math.round(cumDist)} km`;

      const avg = t > 0 ? (cumDist / (t * 0.4)).toFixed(1) : 0;
      document.getElementById('avgSpeedDisplay').textContent = `${avg} km/h`;

      if (t >= 10) {
        clearInterval(journeyTimer);
        journeyRunning = false;
        document.getElementById('btnJourneyStart').textContent = '▶ Drive Highway';
        document.getElementById('avgSpeedDisplay').textContent = '46.7 km/h';
      }
    }, 50);
  };

  window.resetJourneySim = function() {
    clearInterval(journeyTimer);
    journeyRunning = false;
    document.getElementById('btnJourneyStart').textContent = '▶ Drive Highway';
    document.getElementById('journeyCar').style.left = '2%';
    document.getElementById('instSpeedDisplay').textContent = '20 km/h';
    document.getElementById('cumDistDisplay').textContent = '0 km';
    document.getElementById('avgSpeedDisplay').textContent = '-- km/h';
  };

  /* -------------------------------------------------------------
     12. SPEEDO & ODOMETER SIM
     ------------------------------------------------------------- */
  window.setDashSpeed = function(val) {
    dashSpeed = parseFloat(val);
    document.getElementById('dashThrottleVal').textContent = `${dashSpeed} km/h`;
    document.getElementById('dashSpeedNum').textContent = `${dashSpeed} km/h`;

    // Angle: 0 to 140 km/h maps to -60 to +60 deg
    const angle = ((dashSpeed / 140) * 120) - 60;
    const needle = document.getElementById('dashNeedle');
    if (needle) needle.setAttribute('transform', `rotate(${angle + 30}, 80, 95)`);
  };

  window.pulseBrake = function() {
    dashSpeed = Math.max(0, dashSpeed - 20);
    document.getElementById('dashThrottle').value = dashSpeed;
    window.setDashSpeed(dashSpeed);
  };

  window.resetTripOdo = function() {
    dashOdo = 0.0;
    document.getElementById('odoTenth').textContent = '0';
  };

  // Run continuous odometer accumulation
  setInterval(() => {
    if (dashSpeed > 0) {
      dashOdo += (dashSpeed / 3600) * 0.5;
      const tenth = Math.floor((dashOdo * 10) % 10);
      const el = document.getElementById('odoTenth');
      if (el) el.textContent = tenth;
    }
  }, 500);

  /* -------------------------------------------------------------
     13. UNIFORM LINEAR MOTION SIM
     ------------------------------------------------------------- */
  window.runUniformSim = function() {
    if (uniRunning) return;
    uniRunning = true;
    document.getElementById('btnUniSim').textContent = 'Cruising...';
    let t = 0;

    clearInterval(uniTimer);
    uniTimer = setInterval(() => {
      t += 0.05;
      const pct = (t / 5) * 85;
      document.getElementById('uniCar').style.left = `${Math.min(85, pct)}%`;

      // Update dot on straight graph
      const dotX = 25 + (t / 5) * 150;
      const dotY = 120 - (t / 5) * 95;
      const dot = document.getElementById('uniGraphDot');
      if (dot) {
        dot.setAttribute('cx', Math.min(175, dotX));
        dot.setAttribute('cy', Math.max(25, dotY));
      }

      if (t >= 5) {
        clearInterval(uniTimer);
        uniRunning = false;
        document.getElementById('btnUniSim').textContent = '▶ Start Cruise';
      }
    }, 50);
  };

  window.resetUniformSim = function() {
    clearInterval(uniTimer);
    uniRunning = false;
    document.getElementById('btnUniSim').textContent = '▶ Start Cruise';
    document.getElementById('uniCar').style.left = '2%';
    const dot = document.getElementById('uniGraphDot');
    if (dot) { dot.setAttribute('cx', 25); dot.setAttribute('cy', 120); }
  };

  /* -------------------------------------------------------------
     14. NON-UNIFORM MOTION SIM
     ------------------------------------------------------------- */
  window.runNonUniformSim = function() {
    if (nonUniRunning) return;
    nonUniRunning = true;
    document.getElementById('btnNonUniSim').textContent = 'Driving...';
    let t = 0;

    clearInterval(nonUniTimer);
    nonUniTimer = setInterval(() => {
      t += 0.05;
      // Acceleration then braking curve
      const progress = Math.pow(t / 5, 1.8);
      const pct = Math.min(85, progress * 85);
      document.getElementById('nonUniCar').style.left = `${pct}%`;

      const dotX = 25 + (t / 5) * 150;
      const dotY = 120 - (progress) * 95;
      const dot = document.getElementById('nonUniGraphDot');
      if (dot) {
        dot.setAttribute('cx', Math.min(175, dotX));
        dot.setAttribute('cy', Math.max(25, dotY));
      }

      if (t >= 5) {
        clearInterval(nonUniTimer);
        nonUniRunning = false;
        document.getElementById('btnNonUniSim').textContent = '▶ Drive City Track';
      }
    }, 50);
  };

  window.resetNonUniformSim = function() {
    clearInterval(nonUniTimer);
    nonUniRunning = false;
    document.getElementById('btnNonUniSim').textContent = '▶ Drive City Track';
    document.getElementById('nonUniCar').style.left = '2%';
    const dot = document.getElementById('nonUniGraphDot');
    if (dot) { dot.setAttribute('cx', 25); dot.setAttribute('cy', 120); }
  };

  /* -------------------------------------------------------------
     15. DISTANCE-TIME GRAPH SIM
     ------------------------------------------------------------- */
  window.selectGraphLine = function(type) {
    ['btnGraphFast', 'btnGraphSlow', 'btnGraphRest'].forEach(id => {
      const b = document.getElementById(id);
      if (b) b.className = 'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    });

    const active = document.getElementById(type === 'fast' ? 'btnGraphFast' : type === 'slow' ? 'btnGraphSlow' : 'btnGraphRest');
    if (active) active.className = 'px-2.5 py-1 text-xs font-semibold rounded-lg bg-emerald-500 text-slate-950 shadow-md';

    const lFast = document.getElementById('dtLineFast');
    const lSlow = document.getElementById('dtLineSlow');
    const lRest = document.getElementById('dtLineRest');
    const title = document.getElementById('graphAnalyTitle');
    const desc = document.getElementById('graphAnalyDesc');
    const rise = document.getElementById('slopeRise');
    const run = document.getElementById('slopeRun');
    const spd = document.getElementById('slopeSpeed');

    if (type === 'fast') {
      lFast.style.opacity = '1'; lSlow.style.opacity = '0.2'; lRest.style.opacity = '0.2';
      title.className = 'text-emerald-400 font-bold mb-1';
      title.textContent = 'Steep Line (High Speed)';
      desc.textContent = 'Steeper upward slope means more distance covered per second. Speed is high (20 m/s).';
      rise.textContent = '80 m'; run.textContent = '4 s'; spd.textContent = '20 m/s';
    } else if (type === 'slow') {
      lFast.style.opacity = '0.2'; lSlow.style.opacity = '1'; lRest.style.opacity = '0.2';
      title.className = 'text-sky-400 font-bold mb-1';
      title.textContent = 'Gentle Line (Low Speed)';
      desc.textContent = 'Gentle slope means less distance covered per second. Speed is moderate/low (5 m/s).';
      rise.textContent = '40 m'; run.textContent = '8 s'; spd.textContent = '5 m/s';
    } else {
      lFast.style.opacity = '0.2'; lSlow.style.opacity = '0.2'; lRest.style.opacity = '1';
      title.className = 'text-rose-400 font-bold mb-1';
      title.textContent = 'Horizontal Line (At Rest)';
      desc.textContent = 'Flat horizontal line means distance does not change over time. Speed is exactly zero (Object Stationary).';
      rise.textContent = '0 m'; run.textContent = '10 s'; spd.textContent = '0 m/s (Stationary)';
    }
  };

  /* -------------------------------------------------------------
     16. INDIAN TIME HERITAGE SIM
     ------------------------------------------------------------- */
  window.switchHeritageTab = function(tab) {
    heritageTab = tab;
    clearInterval(heritageTimer);
    heritageTimer = null;
    document.getElementById('btnHeritageAction').textContent = '▶ Advance';

    document.getElementById('btnHeritJaipur').className = tab === 'jaipur' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';
    document.getElementById('btnHeritGhatika').className = tab === 'ghatika' ?
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-amber-500 text-slate-950 shadow-md' :
      'px-2.5 py-1 text-xs font-semibold rounded-lg bg-slate-800 text-slate-300 hover:bg-slate-700';

    const label = document.getElementById('heritageControlLabel');
    const slider = document.getElementById('heritageSlider');
    const note = document.getElementById('heritageNote');

    if (tab === 'jaipur') {
      label.textContent = 'Solar Time of Day:';
      slider.min = 6; slider.max = 18; slider.step = 0.1; slider.value = 12;
      note.innerHTML = '<strong>Brihat Samrat Yantra (Jaipur, 1734):</strong> Built by Maharaja Sawai Jai Singh II. The massive 27-meter tall gnomon casts a shadow moving at 1 mm per second across calibrated marble quadrants, measuring local time to 2 seconds precision!';
    } else {
      label.textContent = 'Ghatika Elapsed (min):';
      slider.min = 0; slider.max = 24; slider.step = 0.5; slider.value = 8;
      note.innerHTML = '<strong>Ghatika Yantra (Sinking Copper Bowl):</strong> A calibrated hemispherical copper bowl floats in water. Water trickles through a precision pinhole at the bottom until the bowl sinks after exactly 24 minutes (1 Ghatika = 60 Palas = 360 Pranas).';
    }
    window.updateHeritage(slider.value);
  };

  window.updateHeritage = function(val) {
    heritageVal = parseFloat(val);
    const grp = document.getElementById('heritageVisualGroup');
    const badge = document.getElementById('heritageBadge');
    const valText = document.getElementById('heritageControlValue');
    if (!grp) return;

    if (heritageTab === 'jaipur') {
      const hr = Math.floor(heritageVal);
      const min = Math.round((heritageVal - hr) * 60);
      const ampm = heritageVal < 12 ? 'AM' : 'PM';
      const dispHr = hr > 12 ? hr - 12 : (hr === 0 ? 12 : hr);
      const timeStr = `${dispHr}:${min < 10 ? '0' : ''}${min} ${ampm}`;
      if (valText) valText.textContent = timeStr;
      if (badge) badge.textContent = `Jaipur Samrat Yantra: ${timeStr} (±2 s precision)`;

      // Shadow on massive quadrant
      const shadowPos = ((heritageVal - 12) / 6) * 120; // -120 to +120
      grp.innerHTML = `
        <!-- Ground line -->
        <line x1="50" y1="210" x2="550" y2="210" stroke="#475569" stroke-width="2"/>
        <rect x="50" y="210" width="500" height="20" fill="#1e293b"/>
        <!-- Colossal Gnomon Triangular Ramp (27m) -->
        <polygon points="120,210 400,210 400,30" fill="#78350f" stroke="#b45309" stroke-width="2"/>
        <polygon points="125,208 395,208 395,35" fill="#92400e"/>
        <!-- Curved Marble Quadrants -->
        <path d="M 220,210 A 130,130 0 0,1 480,210" fill="none" stroke="#e2e8f0" stroke-width="12" opacity="0.9"/>
        <!-- Marble Quadrant Graduations (2 sec ticks) -->
        <line x1="300" y1="204" x2="300" y2="216" stroke="#0f172a" stroke-width="2"/>
        <line x1="350" y1="195" x2="350" y2="207" stroke="#0f172a" stroke-width="1.5"/>
        <line x1="400" y1="180" x2="400" y2="192" stroke="#0f172a" stroke-width="1.5"/>
        <line x1="450" y1="150" x2="450" y2="162" stroke="#0f172a" stroke-width="2"/>
        <!-- Shadow Cast on Marble -->
        <line x1="350" y1="75" x2="${350 + shadowPos}" y2="204" stroke="#020617" stroke-width="6" opacity="0.85"/>
        <text x="350" y="45" fill="#fef08a" font-size="11" font-weight="bold" text-anchor="middle">27m Gnomon (Jaipur)</text>
        <text x="${350 + shadowPos}" y="226" fill="#fbbf24" font-size="10" font-family="monospace" text-anchor="middle">Shadow (1 mm/s)</text>
      `;
    } else {
      // Ghatika Yantra
      if (valText) valText.textContent = `${heritageVal.toFixed(1)} min`;
      const pct = heritageVal / 24;
      if (badge) badge.textContent = `Ghatika Yantra: ${Math.round(pct * 100)}% filled (${(24 - heritageVal).toFixed(1)} min left)`;

      const sinkY = 120 + pct * 50;
      const waterInside = pct * 24;

      grp.innerHTML = `
        <!-- Large outer water trough -->
        <rect x="180" y="80" width="240" height="120" rx="8" fill="#0f172a" stroke="#475569" stroke-width="3"/>
        <rect x="185" y="110" width="230" height="85" fill="#0284c7" opacity="0.6"/>
        <text x="300" y="105" text-anchor="middle" fill="#93c5fd" font-size="10">Kunda (Water Reservoir)</text>
        <!-- Floating / Sinking Copper Bowl -->
        <g transform="translate(300, ${sinkY})">
          <path d="M -45,-10 A 45,35 0 0,0 45,-10 Z" fill="#b45309" stroke="#f59e0b" stroke-width="2"/>
          <ellipse cx="0" cy="-10" rx="45" ry="10" fill="#92400e" stroke="#f59e0b" stroke-width="1.5"/>
          <!-- Water trickling inside -->
          <ellipse cx="0" cy="${-10 + waterInside}" rx="${45 - waterInside*0.6}" ry="${8 - waterInside*0.1}" fill="#38bdf8" opacity="0.8"/>
          <!-- Bottom pinhole bubble -->
          <circle cx="0" cy="25" r="2.5" fill="#fff" opacity="0.8"/>
        </g>
        <text x="300" y="222" text-anchor="middle" fill="#fde047" font-size="11" font-weight="bold">1 Ghatika = 24 Minutes = 60 Palas</text>
      `;
    }
  };

  window.actionHeritage = function() {
    const btn = document.getElementById('btnHeritageAction');
    if (heritageTimer) {
      clearInterval(heritageTimer);
      heritageTimer = null;
      if (btn) btn.textContent = '▶ Advance';
    } else {
      if (btn) btn.textContent = '⏸ Pause';
      heritageTimer = setInterval(() => {
        const slider = document.getElementById('heritageSlider');
        let nextVal = parseFloat(slider.value) + (heritageTab === 'jaipur' ? 0.15 : 0.5);
        if (nextVal > parseFloat(slider.max)) nextVal = parseFloat(slider.min);
        slider.value = nextVal;
        window.updateHeritage(nextVal);
      }, 100);
    }
  };

  window.resetHeritage = function() {
    clearInterval(heritageTimer);
    heritageTimer = null;
    document.getElementById('btnHeritageAction').textContent = '▶ Advance';
    const slider = document.getElementById('heritageSlider');
    slider.value = heritageTab === 'jaipur' ? 12 : 0;
    window.updateHeritage(slider.value);
  };

  /* -------------------------------------------------------------
     GLOBAL SIMULATOR INITIALIZER
     ------------------------------------------------------------- */
  window.initSimulators = function() {
    try { if (typeof window.updateCelestialCycle === 'function') window.updateCelestialCycle(180); } catch(e){}
    try { if (typeof window.updateAncientClock === 'function') window.updateAncientClock(12); } catch(e){}
    try { if (typeof window.renderEvo === 'function') window.renderEvo(); } catch(e){}
    try { if (typeof window.setAnatomyAngle === 'function') window.setAnatomyAngle(0); } catch(e){}
    try { if (typeof window.updateIsoParams === 'function') window.updateIsoParams(); } catch(e){}
    try { if (typeof window.calcTimeUnits === 'function') window.calcTimeUnits(); } catch(e){}
    try { if (typeof window.calcSpeedDef === 'function') window.calcSpeedDef(); } catch(e){}
    try { if (typeof window.updateSpeedConv === 'function') window.updateSpeedConv(72); } catch(e){}
    try { if (typeof window.selectTriangleVar === 'function') window.selectTriangleVar('D'); } catch(e){}
    try { if (typeof window.setDashSpeed === 'function') window.setDashSpeed(40); } catch(e){}
    try { if (typeof window.updateHeritage === 'function') window.updateHeritage(12); } catch(e){}
  };

  // Run on DOM ready
  if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', window.initSimulators);
  } else {
    setTimeout(window.initSimulators, 50);
  }
})();
'''

with open(".agents/class7_science_time_motion_js.py", "w", encoding="utf-8") as f:
    f.write('# -*- coding: utf-8 -*-\n"""Simulators JS for Class 7 Science Chapter 8"""\n\nSIMULATOR_JS = r\'\'\'' + js_code + '\'\'\'\n')

print("Generated .agents/class7_science_time_motion_js.py cleanly.")
