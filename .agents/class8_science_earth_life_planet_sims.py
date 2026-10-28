# -*- coding: utf-8 -*-
"""
Interactive SVG Simulators for NCERT Class 8 Science Chapter 13:
Our Home: Earth, a Unique Life Sustaining Planet (Slides 1 to 16)
"""

SIMULATORS_JS = r"""
    // ==========================================
    // 16 BESPOKE INTERACTIVE SVG SIMULATORS (Ch 13)
    // ==========================================

    // Slide 1: Earth: The Unique Living Oasis (4 Spheres Interaction)
    function simEarthUniqueOasis() {
      simHeaderTitle.textContent = "Earth's Four Interconnected Spheres Explorer";
      let activeSphere = 'all';

      simCanvas.innerHTML = `
        <svg id="oasisSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <defs>
            <radialGradient id="spaceGrad" cx="50%" cy="50%" r="75%">
              <stop offset="0%" stop-color="#0b172a"/>
              <stop offset="100%" stop-color="#020617"/>
            </radialGradient>
            <radialGradient id="earthAtmosphereGlow" cx="50%" cy="50%" r="50%">
              <stop offset="70%" stop-color="#38bdf8" stop-opacity="0.8"/>
              <stop offset="90%" stop-color="#0284c7" stop-opacity="0.4"/>
              <stop offset="100%" stop-color="#0284c7" stop-opacity="0"/>
            </radialGradient>
            <radialGradient id="oceanGrad" cx="45%" cy="40%" r="60%">
              <stop offset="0%" stop-color="#0284c7"/>
              <stop offset="50%" stop-color="#0369a1"/>
              <stop offset="100%" stop-color="#0c4a6e"/>
            </radialGradient>
            <radialGradient id="coreGlow" cx="50%" cy="50%" r="50%">
              <stop offset="0%" stop-color="#fef08a"/>
              <stop offset="60%" stop-color="#f97316"/>
              <stop offset="100%" stop-color="#dc2626"/>
            </radialGradient>
            <filter id="glow">
              <feGaussianBlur stdDeviation="3" result="blur"/>
              <feComposite in="SourceGraphic" in2="blur" operator="over"/>
            </filter>
          </defs>

          <!-- Space Background with Stars -->
          <rect x="0" y="0" width="540" height="330" fill="url(#spaceGrad)"/>
          <g opacity="0.6">
            <circle cx="40" cy="30" r="1" fill="#ffffff"/>
            <circle cx="120" cy="80" r="1.5" fill="#bae6fd"/>
            <circle cx="500" cy="40" r="1" fill="#ffffff"/>
            <circle cx="480" cy="120" r="1.2" fill="#fde68a"/>
            <circle cx="60" cy="270" r="1.2" fill="#ffffff"/>
            <circle cx="470" cy="280" r="1.5" fill="#bae6fd"/>
          </g>

          <!-- Sun Rays from Left -->
          <g id="sunBeam" opacity="0.4">
            <polygon points="0,60 0,260 200,200 200,120" fill="url(#coreGlow)" opacity="0.15"/>
          </g>

          <!-- Atmosphere Halo -->
          <circle id="atmoHalo" cx="240" cy="165" r="128" fill="url(#earthAtmosphereGlow)" filter="url(#glow)"/>

          <!-- Earth Base Globe (Hydrosphere / Ocean) -->
          <circle id="globeOcean" cx="240" cy="165" r="115" fill="url(#oceanGrad)"/>

          <!-- Continents (Lithosphere) -->
          <g id="lithoContinents">
            <!-- Eurasia & Africa -->
            <path d="M 210,95 Q 240,80 270,90 Q 290,110 280,140 Q 260,170 230,165 Q 215,150 205,125 Z" fill="#15803d" opacity="0.95"/>
            <path d="M 230,165 Q 260,170 265,210 Q 240,240 220,220 Q 215,190 230,165 Z" fill="#b45309" opacity="0.85"/>
            <!-- Americas (partially on edge) -->
            <path d="M 145,110 Q 170,120 165,155 Q 150,165 140,140 Z" fill="#15803d" opacity="0.95"/>
            <!-- India / Asia peninsula -->
            <path d="M 255,130 Q 270,140 265,160 Q 255,165 250,145 Z" fill="#22c55e" opacity="0.95"/>
            <!-- Australia -->
            <path d="M 300,210 Q 325,205 325,230 Q 305,245 295,225 Z" fill="#b45309" opacity="0.9"/>
          </g>

          <!-- Biosphere Pulsating Green Halo on Land & Ocean Surface -->
          <g id="bioHalo" opacity="0.85">
            <circle cx="240" cy="165" r="116" stroke="#4ade80" stroke-width="3" fill="none" stroke-dasharray="6,4"/>
            <!-- Living organisms icons -->
            <text x="245" y="118" font-size="12">🌲</text>
            <text x="260" y="150" font-size="11">🐅</text>
            <text x="180" y="190" font-size="13">🐋</text>
            <text x="210" y="200" font-size="11">🌾</text>
          </g>

          <!-- Swirling Weather Clouds (Atmosphere) -->
          <g id="atmoClouds" opacity="0.8">
            <path d="M 160,120 Q 200,105 240,115 Q 270,100 310,120" stroke="#f8fafc" stroke-width="4" stroke-linecap="round" fill="none" opacity="0.75"/>
            <path d="M 190,180 Q 230,195 280,185 Q 310,195 330,175" stroke="#f8fafc" stroke-width="5" stroke-linecap="round" fill="none" opacity="0.8"/>
            <path d="M 150,210 Q 180,225 210,215" stroke="#f8fafc" stroke-width="3" stroke-linecap="round" fill="none" opacity="0.65"/>
          </g>

          <!-- Interactive Sphere Callout Cards -->
          <g id="sphereCallout" transform="translate(385, 45)">
            <rect x="0" y="0" width="145" height="240" rx="10" fill="rgba(15, 23, 42, 0.92)" stroke="#38bdf8" stroke-width="1.5"/>
            <text id="calloutTitle" x="72" y="24" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Earth: All 4 Spheres</text>
            <line x1="12" y1="34" x2="133" y2="34" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>
            
            <text id="cLine1" x="12" y="55" fill="#f8fafc" font-size="10" font-weight="700">🌍 Total Harmony:</text>
            <text id="cLine2" x="12" y="75" fill="#94a3b8" font-size="9">• Lithosphere (Crust)</text>
            <text id="cLine3" x="12" y="93" fill="#94a3b8" font-size="9">• Hydrosphere (71% Water)</text>
            <text id="cLine4" x="12" y="111" fill="#94a3b8" font-size="9">• Atmosphere (N₂ & O₂)</text>
            <text id="cLine5" x="12" y="129" fill="#94a3b8" font-size="9">• Biosphere (Living Realm)</text>
            
            <rect x="10" y="145" width="125" height="80" rx="6" fill="rgba(30, 41, 59, 0.8)"/>
            <text id="cStat1" x="16" y="165" fill="#38bdf8" font-size="9" font-weight="700">Vital Life Metric:</text>
            <text id="cStat2" x="16" y="182" fill="#cbd5e1" font-size="8.5">Water: 1.4B km³</text>
            <text id="cStat3" x="16" y="198" fill="#cbd5e1" font-size="8.5">Mean Temp: +15°C</text>
            <text id="cStat4" x="16" y="214" fill="#4ade80" font-size="8.5">Habitability: 100%</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8; margin-right:0.3rem;">Filter Sphere:</span>
          <button class="sim-btn active" id="btnSphereAll">🌐 All 4 Spheres</button>
          <button class="sim-btn" id="btnSphereLitho">🪨 Lithosphere</button>
          <button class="sim-btn" id="btnSphereHydro">💧 Hydrosphere</button>
          <button class="sim-btn" id="btnSphereAtmo">💨 Atmosphere</button>
          <button class="sim-btn" id="btnSphereBio">🌱 Biosphere</button>
        </div>
      `;

      function highlightSphere(sphere) {
        activeSphere = sphere;
        const atmoHalo = document.getElementById('atmoHalo');
        const globeOcean = document.getElementById('globeOcean');
        const lithoContinents = document.getElementById('lithoContinents');
        const bioHalo = document.getElementById('bioHalo');
        const atmoClouds = document.getElementById('atmoClouds');
        const calloutTitle = document.getElementById('calloutTitle');
        const cLine1 = document.getElementById('cLine1');
        const cLine2 = document.getElementById('cLine2');
        const cLine3 = document.getElementById('cLine3');
        const cLine4 = document.getElementById('cLine4');
        const cLine5 = document.getElementById('cLine5');
        const cStat1 = document.getElementById('cStat1');
        const cStat2 = document.getElementById('cStat2');
        const cStat3 = document.getElementById('cStat3');
        const cStat4 = document.getElementById('cStat4');

        // Reset opacities
        atmoHalo.style.opacity = '0.8';
        globeOcean.style.opacity = '1';
        lithoContinents.style.opacity = '1';
        bioHalo.style.opacity = '0.85';
        atmoClouds.style.opacity = '0.8';

        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));

        if (sphere === 'all') {
          document.getElementById('btnSphereAll').classList.add('active');
          calloutTitle.textContent = "Earth: All 4 Spheres";
          calloutTitle.setAttribute('fill', '#38bdf8');
          cLine1.textContent = "🌍 Total Harmony:";
          cLine2.textContent = "• Lithosphere (Crust & soil)";
          cLine3.textContent = "• Hydrosphere (Oceans & rivers)";
          cLine4.textContent = "• Atmosphere (Shield & gases)";
          cLine5.textContent = "• Biosphere (Living zone)";
          cStat1.textContent = "System Status:";
          cStat2.textContent = "Oceans cover: 71%";
          cStat3.textContent = "Dynamic Homeostasis";
          cStat4.textContent = "Sustains 8.7M+ Species";
          cStat4.setAttribute('fill', '#4ade80');
        } else if (sphere === 'litho') {
          document.getElementById('btnSphereLitho').classList.add('active');
          atmoHalo.style.opacity = '0.2';
          globeOcean.style.opacity = '0.35';
          bioHalo.style.opacity = '0.2';
          atmoClouds.style.opacity = '0.2';
          calloutTitle.textContent = "🪨 Lithosphere";
          calloutTitle.setAttribute('fill', '#f59e0b');
          cLine1.textContent = "Rocky Crust & Mantle:";
          cLine2.textContent = "• Solid continental bedrock";
          cLine3.textContent = "• Weathered topsoil & clay";
          cLine4.textContent = "• Mineral pharmacy (Fe, Ca, P)";
          cLine5.textContent = "• Tectonic plate movement";
          cStat1.textContent = "Lithosphere Data:";
          cStat2.textContent = "Crust Depth: 5–70 km";
          cStat3.textContent = "Mass: 5.97×10²⁴ kg";
          cStat4.textContent = "Anchors Root Systems";
          cStat4.setAttribute('fill', '#fbbf24');
        } else if (sphere === 'hydro') {
          document.getElementById('btnSphereHydro').classList.add('active');
          atmoHalo.style.opacity = '0.2';
          lithoContinents.style.opacity = '0.3';
          bioHalo.style.opacity = '0.2';
          atmoClouds.style.opacity = '0.2';
          calloutTitle.textContent = "💧 Hydrosphere";
          calloutTitle.setAttribute('fill', '#38bdf8');
          cLine1.textContent = "Liquid Water Domain:";
          cLine2.textContent = "• 71% of Earth's surface";
          cLine3.textContent = "• 97% saline ocean water";
          cLine4.textContent = "• 3% fresh water (glaciers/rivers)";
          cLine5.textContent = "• Universal biochemical solvent";
          cStat1.textContent = "Hydrosphere Data:";
          cStat2.textContent = "Volume: 1.386B km³";
          cStat3.textContent = "High Heat Capacity";
          cStat4.textContent = "Regulates Global Climate";
          cStat4.setAttribute('fill', '#38bdf8');
        } else if (sphere === 'atmo') {
          document.getElementById('btnSphereAtmo').classList.add('active');
          atmoHalo.style.opacity = '1';
          globeOcean.style.opacity = '0.35';
          lithoContinents.style.opacity = '0.3';
          bioHalo.style.opacity = '0.2';
          calloutTitle.textContent = "💨 Atmosphere";
          calloutTitle.setAttribute('fill', '#a78bfa');
          cLine1.textContent = "Gaseous Protective Shield:";
          cLine2.textContent = "• 78% Nitrogen (N₂)";
          cLine3.textContent = "• 21% Oxygen (O₂)";
          cLine4.textContent = "• 0.04% Carbon Dioxide (CO₂)";
          cLine5.textContent = "• Stratospheric Ozone (O₃)";
          cStat1.textContent = "Atmospheric Data:";
          cStat2.textContent = "Mass: 5.15×10¹⁸ kg";
          cStat3.textContent = "Blocks UV & Meteors";
          cStat4.textContent = "Retains Heat (+15°C Mean)";
          cStat4.setAttribute('fill', '#c084fc');
        } else if (sphere === 'bio') {
          document.getElementById('btnSphereBio').classList.add('active');
          atmoHalo.style.opacity = '0.3';
          globeOcean.style.opacity = '0.5';
          lithoContinents.style.opacity = '0.5';
          bioHalo.style.opacity = '1';
          calloutTitle.textContent = "🌱 Biosphere";
          calloutTitle.setAttribute('fill', '#4ade80');
          cLine1.textContent = "The Global Realm of Life:";
          cLine2.textContent = "• Extends from ocean trenches";
          cLine3.textContent = "• To high alpine slopes (~10km)";
          cLine4.textContent = "• Plants, animals, microbes";
          cLine5.textContent = "• Marine phytoplankton (>50% O₂)";
          cStat1.textContent = "Biosphere Data:";
          cStat2.textContent = "Species: ~8.7 Million";
          cStat3.textContent = "Driven by Solar Energy";
          cStat4.textContent = "Only Known Living Planet";
          cStat4.setAttribute('fill', '#4ade80');
        }
        sfx.playClick();
      }

      document.getElementById('btnSphereAll').addEventListener('click', () => highlightSphere('all'));
      document.getElementById('btnSphereLitho').addEventListener('click', () => highlightSphere('litho'));
      document.getElementById('btnSphereHydro').addEventListener('click', () => highlightSphere('hydro'));
      document.getElementById('btnSphereAtmo').addEventListener('click', () => highlightSphere('atmo'));
      document.getElementById('btnSphereBio').addEventListener('click', () => highlightSphere('bio'));
    }

    // Slide 2: Comparative Planetary Habitability Scanner
    function simSolarSystemPlanets() {
      simHeaderTitle.textContent = "Solar System Planetary Scanner & Habitability Gauge";

      const planets = {
        mercury: {
          name: "Mercury",
          color: "#94a3b8",
          type: "Rocky Terrestrial",
          dist: "0.39 AU (58M km)",
          temp: "-180°C to +430°C",
          pressure: "0.000000000001 atm",
          atmo: "Trace exosphere (Na, He, O₂)",
          verdict: "☠️ DEAD VACUUM / THERMAL EXTREMES",
          verdictColor: "#ef4444",
          svgDetail: `<circle cx="160" cy="150" r="45" fill="#64748b"/><circle cx="140" cy="130" r="12" fill="#475569"/><circle cx="175" cy="165" r="8" fill="#475569"/><circle cx="150" cy="170" r="14" fill="#334155"/>`
        },
        venus: {
          name: "Venus",
          color: "#f59e0b",
          type: "Rocky Terrestrial",
          dist: "0.72 AU (108M km)",
          temp: "+465°C (Average)",
          pressure: "92 atm (Crushing)",
          atmo: "96.5% CO₂, 3.5% N₂, H₂SO₄ clouds",
          verdict: "☠️ LETHAL RUNAWAY GREENHOUSE FURNACE",
          verdictColor: "#ef4444",
          svgDetail: `<circle cx="160" cy="150" r="62" fill="#d97706"/><circle cx="160" cy="150" r="65" fill="#f59e0b" opacity="0.3"/><path d="M 105,130 Q 160,110 215,135" stroke="#b45309" stroke-width="6" fill="none" opacity="0.5"/><path d="M 100,165 Q 160,185 220,160" stroke="#fde68a" stroke-width="5" fill="none" opacity="0.4"/>`
        },
        earth: {
          name: "Earth",
          color: "#0284c7",
          type: "Rocky Terrestrial (Living Oasis)",
          dist: "1.00 AU (149.6M km)",
          temp: "+15°C (Average)",
          pressure: "1.00 atm",
          atmo: "78% N₂, 21% O₂, 0.9% Ar, 0.04% CO₂",
          verdict: "🌟 PERFECT GOLDILOCKS LIFE OASIS",
          verdictColor: "#10b981",
          svgDetail: `<circle cx="160" cy="150" r="65" fill="#0284c7"/><path d="M 130,120 Q 160,105 185,120 Q 170,160 140,150 Z" fill="#22c55e"/><path d="M 155,155 Q 190,160 185,190 Q 160,200 150,175 Z" fill="#15803d"/><circle cx="160" cy="150" r="67" stroke="#38bdf8" stroke-width="2" fill="none" opacity="0.8"/><path d="M 110,135 Q 160,150 210,130" stroke="#ffffff" stroke-width="4" stroke-linecap="round" fill="none" opacity="0.7"/>`
        },
        mars: {
          name: "Mars",
          color: "#ef4444",
          type: "Rocky Terrestrial (Red Planet)",
          dist: "1.52 AU (228M km)",
          temp: "-60°C (Down to -125°C)",
          pressure: "0.006 atm (0.6% Earth)",
          atmo: "95% CO₂, 2.6% N₂, 1.9% Ar",
          verdict: "⚠️ FRIGID DESERT / THIN TOXIC AIR",
          verdictColor: "#f59e0b",
          svgDetail: `<circle cx="160" cy="150" r="48" fill="#c2410c"/><circle cx="160" cy="104" r="10" fill="#ffffff" opacity="0.8"/><path d="M 125,140 Q 160,135 195,150 Q 180,170 140,165 Z" fill="#9a3412"/><circle cx="145" cy="135" r="7" fill="#7c2d12"/>`
        },
        jupiter: {
          name: "Jupiter",
          color: "#d97706",
          type: "Gas Giant",
          dist: "5.20 AU (778M km)",
          temp: "-110°C (Cloud tops)",
          pressure: "Millions of atm (Deep core)",
          atmo: "90% H₂, 10% He, trace CH₄/NH₃",
          verdict: "☠️ VIOLENT GAS STORM / NO SOLID SURFACE",
          verdictColor: "#ef4444",
          svgDetail: `<circle cx="160" cy="150" r="95" fill="#b45309"/><ellipse cx="160" cy="120" rx="93" ry="12" fill="#fed7aa" opacity="0.5"/><ellipse cx="160" cy="145" rx="95" ry="14" fill="#78350f" opacity="0.6"/><ellipse cx="160" cy="175" rx="92" ry="12" fill="#fed7aa" opacity="0.5"/><ellipse cx="205" cy="165" rx="16" ry="10" fill="#dc2626"/><circle cx="205" cy="165" r="5" fill="#f87171"/>`
        },
        saturn: {
          name: "Saturn",
          color: "#fbbf24",
          type: "Gas Giant (Ringed World)",
          dist: "9.58 AU (1.43B km)",
          temp: "-140°C",
          pressure: "Crushing gaseous interior",
          atmo: "96% H₂, 3% He, trace CH₄",
          verdict: "☠️ FRIGID HYDROGEN GIANT / NO CRUST",
          verdictColor: "#ef4444",
          svgDetail: `<ellipse cx="160" cy="150" rx="135" ry="24" fill="none" stroke="#fde68a" stroke-width="12" opacity="0.75" transform="rotate(-18 160 150)"/><circle cx="160" cy="150" r="75" fill="#d97706"/><ellipse cx="160" cy="150" rx="135" ry="24" fill="none" stroke="#d97706" stroke-width="3" opacity="0.9" transform="rotate(-18 160 150)"/>`
        },
        uranus: {
          name: "Uranus",
          color: "#38bdf8",
          type: "Ice Giant",
          dist: "19.2 AU (2.87B km)",
          temp: "-195°C",
          pressure: "High pressure slush mantle",
          atmo: "83% H₂, 15% He, 2% Methane (CH₄)",
          verdict: "☠️ CRYOGENIC ICE GIANT / -195°C VOID",
          verdictColor: "#ef4444",
          svgDetail: `<circle cx="160" cy="150" r="60" fill="#0284c7"/><circle cx="160" cy="150" r="58" fill="#38bdf8" opacity="0.7"/><ellipse cx="160" cy="150" rx="8" ry="90" fill="none" stroke="#bae6fd" stroke-width="2" opacity="0.6"/>`
        },
        neptune: {
          name: "Neptune",
          color: "#2563eb",
          type: "Ice Giant",
          dist: "30.1 AU (4.50B km)",
          temp: "-200°C",
          pressure: "High pressure icy mantle",
          atmo: "80% H₂, 19% He, 1.5% CH₄",
          verdict: "☠️ SUPERSONIC FROZEN WINDS (>2,000 km/h)",
          verdictColor: "#ef4444",
          svgDetail: `<circle cx="160" cy="150" r="58" fill="#1d4ed8"/><path d="M 115,130 Q 160,145 205,125" stroke="#60a5fa" stroke-width="4" fill="none" opacity="0.6"/><circle cx="185" cy="165" r="8" fill="#1e3a8a"/>`
        }
      };

      simCanvas.innerHTML = `
        <svg id="planetSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#030712"/>
          
          <!-- Distant Sun Indicator on left -->
          <path d="M 0,0 L 0,330 Q 30,165 0,0" fill="#f59e0b" opacity="0.2"/>
          <line x1="5" y1="165" x2="60" y2="165" stroke="#fbbf24" stroke-width="2" stroke-dasharray="4,4"/>
          <text x="15" y="155" fill="#fbbf24" font-size="9" font-weight="700">Solar Rays</text>

          <!-- Planet Visual Box -->
          <g id="planetDisplayGroup">
            <!-- Injected dynamically -->
          </g>

          <!-- Planetary Metrics Panel -->
          <g transform="translate(290, 25)">
            <rect x="0" y="0" width="235" height="280" rx="12" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text id="pName" x="117" y="28" fill="#38bdf8" font-size="16" font-weight="800" text-anchor="middle">Earth</text>
            <text id="pType" x="117" y="46" fill="#94a3b8" font-size="10" text-anchor="middle">Rocky Terrestrial (Living Oasis)</text>
            <line x1="15" y1="56" x2="220" y2="56" stroke="rgba(56, 189, 248, 0.3)" stroke-width="1"/>

            <text x="15" y="78" fill="#f8fafc" font-size="10" font-weight="700">Orbit Distance:</text>
            <text id="pDist" x="15" y="94" fill="#38bdf8" font-size="10">1.00 AU (149.6M km)</text>

            <text x="15" y="118" fill="#f8fafc" font-size="10" font-weight="700">Surface Temperature:</text>
            <text id="pTemp" x="15" y="134" fill="#f59e0b" font-size="10">+15°C (Average)</text>

            <text x="15" y="158" fill="#f8fafc" font-size="10" font-weight="700">Surface Pressure:</text>
            <text id="pPress" x="15" y="174" fill="#cbd5e1" font-size="10">1.00 atm</text>

            <text x="15" y="198" fill="#f8fafc" font-size="10" font-weight="700">Atmosphere Composition:</text>
            <text id="pAtmo" x="15" y="214" fill="#cbd5e1" font-size="9.5">78% N₂, 21% O₂, 0.04% CO₂</text>

            <!-- Habitability Status Banner -->
            <rect x="12" y="232" width="211" height="36" rx="6" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1" id="pVerdictBox"/>
            <text id="pVerdict" x="117" y="254" fill="#10b981" font-size="9" font-weight="800" text-anchor="middle">🌟 PERFECT GOLDILOCKS LIFE OASIS</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.5rem; align-items:center;">
          <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center;">
            <button class="sim-btn" data-planet="mercury">Mercury</button>
            <button class="sim-btn" data-planet="venus">Venus</button>
            <button class="sim-btn active" data-planet="earth">Earth 🌍</button>
            <button class="sim-btn" data-planet="mars">Mars</button>
            <button class="sim-btn" data-planet="jupiter">Jupiter</button>
            <button class="sim-btn" data-planet="saturn">Saturn</button>
            <button class="sim-btn" data-planet="uranus">Uranus</button>
            <button class="sim-btn" data-planet="neptune">Neptune</button>
          </div>
        </div>
      `;

      function selectPlanet(key) {
        const data = planets[key];
        if (!data) return;

        document.getElementById('planetDisplayGroup').innerHTML = data.svgDetail;
        document.getElementById('pName').textContent = data.name;
        document.getElementById('pType').textContent = data.type;
        document.getElementById('pDist').textContent = data.dist;
        document.getElementById('pTemp').textContent = data.temp;
        document.getElementById('pPress').textContent = data.pressure;
        document.getElementById('pAtmo').textContent = data.atmo;
        
        const vText = document.getElementById('pVerdict');
        const vBox = document.getElementById('pVerdictBox');
        vText.textContent = data.verdict;
        vText.setAttribute('fill', data.verdictColor);
        vBox.setAttribute('stroke', data.verdictColor);
        vBox.setAttribute('fill', data.verdictColor === '#10b981' ? 'rgba(16, 185, 129, 0.15)' : 'rgba(239, 68, 68, 0.15)');

        simControls.querySelectorAll('.sim-btn').forEach(b => {
          b.classList.toggle('active', b.dataset.planet === key);
        });
        sfx.playClick();
      }

      simControls.querySelectorAll('.sim-btn').forEach(btn => {
        btn.addEventListener('click', () => selectPlanet(btn.dataset.planet));
      });

      selectPlanet('earth');
    }

    // Slide 3: Earth's Position in the Goldilocks Zone
    function simGoldilocksZone() {
      simHeaderTitle.textContent = "Circumstellar Habitable Zone (Goldilocks Orbit) Simulator";
      let orbitAU = 1.0;

      simCanvas.innerHTML = `
        <svg id="goldilocksSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Orbit Guide Circles from Sun -->
          <!-- Sun in center-left at (100, 165) -->
          <circle cx="100" cy="165" r="45" fill="#f59e0b"/>
          <circle cx="100" cy="165" r="48" fill="#fbbf24" opacity="0.3"/>
          <text x="100" y="170" fill="#78350f" font-size="12" font-weight="900" text-anchor="middle">SUN</text>

          <!-- Zone Shading Bands -->
          <!-- Inner Scorched Zone: 0.3 to 0.95 AU (radius 50 to 140) -->
          <path d="M 100,25 A 140,140 0 0,1 100,305 A 50,50 0 0,0 100,115 Z" fill="#ef4444" opacity="0.12"/>
          <text x="135" y="55" fill="#f87171" font-size="9" font-weight="700">Too Hot (Boiling)</text>

          <!-- Goldilocks Habitable Zone: 0.95 to 1.37 AU (radius 140 to 210) -->
          <path id="goldilocksBand" d="M 100,0 A 210,210 0 0,1 100,330 L 100,305 A 140,140 0 0,0 100,25 Z" fill="#10b981" opacity="0.22"/>
          <text x="210" y="40" fill="#34d399" font-size="10" font-weight="800">✨ Goldilocks Zone (0.95–1.37 AU)</text>

          <!-- Outer Freezing Zone: >1.37 AU (radius > 210) -->
          <path d="M 100,0 A 280,280 0 0,1 100,330 L 100,330 A 210,210 0 0,0 100,0 Z" fill="#38bdf8" opacity="0.12"/>
          <text x="285" y="45" fill="#67e8f9" font-size="9" font-weight="700">Too Cold (Frozen)</text>

          <!-- Planet Orbit Line -->
          <ellipse id="orbitPath" cx="100" cy="165" rx="150" ry="150" fill="none" stroke="#64748b" stroke-width="1.5" stroke-dasharray="4,4"/>

          <!-- Dynamic Planet -->
          <g id="planetMarker" transform="translate(250, 165)">
            <circle id="planetBody" cx="0" cy="0" r="16" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
            <text id="waterEmoji" x="0" y="5" font-size="10" text-anchor="middle">💧</text>
          </g>

          <!-- Live Readout Overlay Card -->
          <g transform="translate(325, 170)">
            <rect x="0" y="0" width="200" height="145" rx="10" fill="rgba(15, 23, 42, 0.92)" stroke="#10b981" stroke-width="1.5" id="readoutCard"/>
            <text x="100" y="24" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Orbit Habitability Monitor</text>
            <line x1="12" y1="32" x2="188" y2="32" stroke="rgba(255,255,255,0.15)"/>
            
            <text x="12" y="52" fill="#94a3b8" font-size="9.5">Distance: <tspan id="lblDist" fill="#f8fafc" font-weight="700">1.00 AU (150M km)</tspan></text>
            <text x="12" y="72" fill="#94a3b8" font-size="9.5">Solar Flux: <tspan id="lblFlux" fill="#fbbf24" font-weight="700">1,361 W/m² (100%)</tspan></text>
            <text x="12" y="92" fill="#94a3b8" font-size="9.5">Estimated Temp: <tspan id="lblTemp" fill="#4ade80" font-weight="700">+15°C</tspan></text>
            <text x="12" y="112" fill="#94a3b8" font-size="9.5">Water State: <tspan id="lblWater" fill="#38bdf8" font-weight="700">Liquid Oceans Stable</tspan></text>

            <rect x="10" y="122" width="180" height="18" rx="4" fill="rgba(16, 185, 129, 0.2)" id="statusBox"/>
            <text id="lblStatus" x="100" y="135" fill="#34d399" font-size="8.5" font-weight="800" text-anchor="middle">OPTIMAL FOR LIFE</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.6rem; align-items:center; width:100%;">
          <div style="display:flex; align-items:center; gap:0.8rem; width:80%; max-width:480px;">
            <span style="font-size:0.85rem; font-weight:700; color:#cbd5e1; white-space:nowrap;">Orbit Radius:</span>
            <input type="range" id="orbitSlider" min="0.4" max="2.2" step="0.05" value="1.0" style="flex:1;">
            <span id="sliderValText" style="font-size:0.9rem; font-weight:800; color:#38bdf8; min-width:55px;">1.00 AU</span>
          </div>
          <div style="display:flex; gap:0.5rem; justify-content:center; flex-wrap:wrap;">
            <button class="sim-btn" id="btnPresetVenus">Venus (0.72 AU)</button>
            <button class="sim-btn active" id="btnPresetEarth">Earth (1.00 AU)</button>
            <button class="sim-btn" id="btnPresetMars">Mars (1.52 AU)</button>
          </div>
        </div>
      `;

      function updateOrbit(val) {
        orbitAU = parseFloat(val);
        document.getElementById('sliderValText').textContent = orbitAU.toFixed(2) + ' AU';
        
        // Scale pixel radius: 1.0 AU = 150px (from Sun cx=100)
        // Range: 0.4 AU = 60px, 2.2 AU = 330px
        const rPx = orbitAU * 150;
        const orbitPath = document.getElementById('orbitPath');
        orbitPath.setAttribute('rx', rPx);
        orbitPath.setAttribute('ry', rPx);

        const planetMarker = document.getElementById('planetMarker');
        const newX = 100 + rPx;
        planetMarker.setAttribute('transform', `translate(${newX}, 165)`);

        // Compute physics-based parameters
        // Solar flux = 1361 / (AU^2)
        const flux = Math.round(1361 / (orbitAU * orbitAU));
        const fluxPct = Math.round((flux / 1361) * 100);

        // Effective temp (with simple Earth-like greenhouse of +33K)
        // T_eq = 255 * (1 / sqrt(AU)) -> T_surf = T_eq + 33 - 273
        const tSurf = Math.round((255 / Math.sqrt(orbitAU)) + 33 - 273);

        const lblDist = document.getElementById('lblDist');
        const lblFlux = document.getElementById('lblFlux');
        const lblTemp = document.getElementById('lblTemp');
        const lblWater = document.getElementById('lblWater');
        const lblStatus = document.getElementById('lblStatus');
        const statusBox = document.getElementById('statusBox');
        const planetBody = document.getElementById('planetBody');
        const waterEmoji = document.getElementById('waterEmoji');
        const readoutCard = document.getElementById('readoutCard');

        lblDist.textContent = `${orbitAU.toFixed(2)} AU (${Math.round(orbitAU * 149.6)}M km)`;
        lblFlux.textContent = `${flux.toLocaleString()} W/m² (${fluxPct}%)`;
        lblTemp.textContent = `${tSurf > 0 ? '+' : ''}${tSurf}°C`;

        if (orbitAU < 0.95) {
          // Too hot
          lblWater.textContent = "Boils to Steam (Vaporizer)";
          lblWater.setAttribute('fill', '#f87171');
          lblStatus.textContent = "TOO HOT: RUNAWAY GREENHOUSE";
          statusBox.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
          lblStatus.setAttribute('fill', '#f87171');
          readoutCard.setAttribute('stroke', '#ef4444');
          planetBody.setAttribute('fill', '#dc2626');
          planetBody.setAttribute('stroke', '#f87171');
          waterEmoji.textContent = "♨️";
        } else if (orbitAU > 1.37) {
          // Too cold
          lblWater.textContent = "Frozen Solid (Global Glaciation)";
          lblWater.setAttribute('fill', '#38bdf8');
          lblStatus.textContent = "TOO COLD: GLOBAL ICE AGE";
          statusBox.setAttribute('fill', 'rgba(56, 189, 248, 0.25)');
          lblStatus.setAttribute('fill', '#38bdf8');
          readoutCard.setAttribute('stroke', '#38bdf8');
          planetBody.setAttribute('fill', '#e0f2fe');
          planetBody.setAttribute('stroke', '#0284c7');
          waterEmoji.textContent = "❄️";
        } else {
          // Goldilocks zone
          lblWater.textContent = "Liquid Water Stable (Oceans Thrive)";
          lblWater.setAttribute('fill', '#4ade80');
          lblStatus.textContent = "GOLDILOCKS ZONE: LIFE FLOURISHES";
          statusBox.setAttribute('fill', 'rgba(16, 185, 129, 0.25)');
          lblStatus.setAttribute('fill', '#34d399');
          readoutCard.setAttribute('stroke', '#10b981');
          planetBody.setAttribute('fill', '#0284c7');
          planetBody.setAttribute('stroke', '#22c55e');
          waterEmoji.textContent = "💧";
        }
      }

      const orbitSlider = document.getElementById('orbitSlider');
      orbitSlider.addEventListener('input', (e) => {
        updateOrbit(e.target.value);
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
      });

      document.getElementById('btnPresetVenus').addEventListener('click', () => {
        orbitSlider.value = 0.72;
        updateOrbit(0.72);
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnPresetVenus').classList.add('active');
        sfx.playClick();
      });

      document.getElementById('btnPresetEarth').addEventListener('click', () => {
        orbitSlider.value = 1.0;
        updateOrbit(1.0);
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnPresetEarth').classList.add('active');
        sfx.playCorrect();
      });

      document.getElementById('btnPresetMars').addEventListener('click', () => {
        orbitSlider.value = 1.52;
        updateOrbit(1.52);
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnPresetMars').classList.add('active');
        sfx.playClick();
      });

      updateOrbit(1.0);
    }

    // Slide 4: Earth's Optimal Size & Gravity
    function simEarthSizeGravity() {
      simHeaderTitle.textContent = "Planetary Size, Surface Gravity & Atmospheric Escape Simulator";

      simCanvas.innerHTML = `
        <svg id="gravSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#030712"/>

          <!-- Planet Surface Arc at Bottom -->
          <path id="planetSurfaceArc" d="M 0,280 Q 270,240 540,280 L 540,330 L 0,330 Z" fill="#0f172a" stroke="#38bdf8" stroke-width="2"/>

          <!-- Gravity Field Arrows -->
          <g id="gravArrows" opacity="0.6">
            <line x1="80" y1="200" x2="80" y2="245" stroke="#38bdf8" stroke-width="2" marker-end="url(#arrow)"/>
            <line x1="180" y1="190" x2="180" y2="240" stroke="#38bdf8" stroke-width="2"/>
            <line x1="270" y1="185" x2="270" y2="238" stroke="#38bdf8" stroke-width="2"/>
            <line x1="360" y1="190" x2="360" y2="240" stroke="#38bdf8" stroke-width="2"/>
            <line x1="460" y1="200" x2="460" y2="245" stroke="#38bdf8" stroke-width="2"/>
          </g>

          <!-- Animated Atmospheric Particles Container -->
          <g id="particleContainer">
            <!-- Populated via script -->
          </g>

          <!-- Top Space Escape Boundary Line -->
          <line x1="20" y1="50" x2="520" y2="50" stroke="#f43f5e" stroke-width="1.5" stroke-dasharray="6,4"/>
          <text x="270" y="42" fill="#f43f5e" font-size="10" font-weight="700" text-anchor="middle">Outer Space Escape Boundary (Thermal Velocity > Escape Velocity)</text>

          <!-- Physics Infobox Panel -->
          <g transform="translate(25, 65)">
            <rect x="0" y="0" width="230" height="150" rx="10" fill="rgba(15, 23, 42, 0.92)" stroke="#38bdf8" stroke-width="1.5"/>
            <text id="gravModelTitle" x="115" y="24" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Earth Model (1.0 M⊕)</text>
            <line x1="12" y1="32" x2="218" y2="32" stroke="rgba(255,255,255,0.1)"/>
            
            <text x="12" y="52" fill="#94a3b8" font-size="9.5">Surface Gravity (g): <tspan id="lblG" fill="#f8fafc" font-weight="700">9.8 m/s²</tspan></text>
            <text x="12" y="72" fill="#94a3b8" font-size="9.5">Escape Velocity (ve): <tspan id="lblVe" fill="#fbbf24" font-weight="700">11.2 km/s</tspan></text>
            <text x="12" y="92" fill="#94a3b8" font-size="9.5">Retained Gases: <tspan id="lblRetained" fill="#4ade80" font-weight="700">N₂, O₂, H₂O, CO₂</tspan></text>
            <text x="12" y="112" fill="#94a3b8" font-size="9.5">Escaped Gases: <tspan id="lblEscaped" fill="#f87171" font-weight="700">Light H₂, He</tspan></text>
            
            <rect x="10" y="122" width="210" height="20" rx="4" fill="rgba(16, 185, 129, 0.2)" id="gravStatusBox"/>
            <text id="lblGravStatus" x="115" y="136" fill="#34d399" font-size="8.5" font-weight="800" text-anchor="middle">BALANCED: IDEAL ATMOSPHERE</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; justify-content:center; align-items:center;">
          <span style="font-size:0.85rem; font-weight:700; color:#94a3b8;">Select Planetary Mass:</span>
          <button class="sim-btn" id="btnMassSmall">🌑 Small World (0.1 M⊕, Mars/Moon)</button>
          <button class="sim-btn active" id="btnMassEarth">🌍 Optimal Earth (1.0 M⊕)</button>
          <button class="sim-btn" id="btnMassGiant">🪐 Super-Giant (5.0 M⊕)</button>
        </div>
      `;

      function renderAtmosphereParticles(mode) {
        const c = document.getElementById('particleContainer');
        c.innerHTML = '';

        const lblG = document.getElementById('lblG');
        const lblVe = document.getElementById('lblVe');
        const lblRetained = document.getElementById('lblRetained');
        const lblEscaped = document.getElementById('lblEscaped');
        const lblGravStatus = document.getElementById('lblGravStatus');
        const gravStatusBox = document.getElementById('gravStatusBox');
        const gravModelTitle = document.getElementById('gravModelTitle');

        if (mode === 'small') {
          gravModelTitle.textContent = "Small World (Mars / Moon 0.1 M⊕)";
          lblG.textContent = "3.7 m/s² (Weak)";
          lblVe.textContent = "4.3 km/s (Low)";
          lblRetained.textContent = "Only trace dense CO₂";
          lblEscaped.textContent = "N₂, O₂, H₂O vapor, H₂, He";
          lblGravStatus.textContent = "TOO WEAK: ATMOSPHERE LOST TO SPACE";
          gravStatusBox.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
          lblGravStatus.setAttribute('fill', '#f87171');

          // Sparse particles drifting up and out
          for (let i = 0; i < 20; i++) {
            const x = 50 + Math.random() * 440;
            const y = 30 + Math.random() * 200;
            c.innerHTML += `
              <circle cx="${x}" cy="${y}" r="3" fill="#f87171" opacity="0.6"/>
              <line x1="${x}" y1="${y}" x2="${x}" y2="${y - 18}" stroke="#f87171" stroke-width="1.5" stroke-dasharray="2,2"/>
            `;
          }
        } else if (mode === 'giant') {
          gravModelTitle.textContent = "Super-Giant World (5.0 M⊕)";
          lblG.textContent = "24.5 m/s² (Crushing)";
          lblVe.textContent = "25.0 km/s (Extreme)";
          lblRetained.textContent = "All gases including H₂, He, NH₃";
          lblEscaped.textContent = "Virtually Nothing";
          lblGravStatus.textContent = "TOO HEAVY: CRUSHING TOXIC GAS ENVELOPE";
          gravStatusBox.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
          lblGravStatus.setAttribute('fill', '#f87171');

          // Extremely dense packed layer near surface
          for (let i = 0; i < 60; i++) {
            const x = 30 + Math.random() * 480;
            const y = 180 + Math.random() * 80;
            c.innerHTML += `<circle cx="${x}" cy="${y}" r="3.5" fill="#a78bfa" opacity="0.85"/>`;
          }
        } else {
          // Earth
          gravModelTitle.textContent = "Optimal Earth (1.0 M⊕)";
          lblG.textContent = "9.8 m/s² (Optimal)";
          lblVe.textContent = "11.2 km/s (Goldilocks)";
          lblRetained.textContent = "Vital N₂, O₂, H₂O, CO₂";
          lblEscaped.textContent = "Toxic primordial H₂, He";
          lblGravStatus.textContent = "PERFECT: RETAINS BREATHABLE AIR";
          gravStatusBox.setAttribute('fill', 'rgba(16, 185, 129, 0.25)');
          lblGravStatus.setAttribute('fill', '#34d399');

          // Balanced distribution: heavy gases bounce near bottom, light H2 escape at top
          for (let i = 0; i < 35; i++) {
            const x = 50 + Math.random() * 440;
            const y = 120 + Math.random() * 120;
            c.innerHTML += `<circle cx="${x}" cy="${y}" r="3" fill="#38bdf8" opacity="0.85"/>`;
          }
          // Escaping light gas
          for (let i = 0; i < 8; i++) {
            const x = 80 + Math.random() * 380;
            const y = 25 + Math.random() * 40;
            c.innerHTML += `
              <circle cx="${x}" cy="${y}" r="2" fill="#fbbf24" opacity="0.7"/>
              <line x1="${x}" y1="${y}" x2="${x}" y2="${y - 12}" stroke="#fbbf24" stroke-width="1.2"/>
            `;
          }
        }
      }

      document.getElementById('btnMassSmall').addEventListener('click', () => {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnMassSmall').classList.add('active');
        renderAtmosphereParticles('small');
        sfx.playClick();
      });

      document.getElementById('btnMassEarth').addEventListener('click', () => {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnMassEarth').classList.add('active');
        renderAtmosphereParticles('earth');
        sfx.playCorrect();
      });

      document.getElementById('btnMassGiant').addEventListener('click', () => {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnMassGiant').classList.add('active');
        renderAtmosphereParticles('giant');
        sfx.playClick();
      });

      renderAtmosphereParticles('earth');
    }

    // Slide 5: Earth's Magnetic Shield (Magnetosphere)
    function simGeomagneticShield() {
      simHeaderTitle.textContent = "Geodynamo & Magnetospheric Solar Wind Shield";
      let dynamoOn = true;

      simCanvas.innerHTML = `
        <svg id="magnetoSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Solar Wind Stream Particles from Left -->
          <g id="solarWindParticles">
            <!-- Generated via script -->
          </g>

          <!-- Magnetic Field Lines Group -->
          <g id="fieldLinesGroup">
            <!-- Dipole loops around Earth -->
            <path d="M 280,165 C 280,60 180,60 180,165 C 180,270 280,270 280,165" stroke="#38bdf8" stroke-width="1.8" fill="none" opacity="0.6"/>
            <path d="M 320,165 C 320,30 140,30 140,165 C 140,300 320,300 320,165" stroke="#38bdf8" stroke-width="1.8" fill="none" opacity="0.5"/>
            <!-- Bow shock on left -->
            <path id="bowShock" d="M 110,20 Q 70,165 110,310" stroke="#fbbf24" stroke-width="3" fill="none" stroke-linecap="round" opacity="0.8"/>
            <text x="75" y="40" fill="#fbbf24" font-size="9" font-weight="700">Bow Shock</text>
          </g>

          <!-- Earth with Cutaway Core -->
          <g id="earthCoreGroup" transform="translate(230, 165)">
            <!-- Outer Globe -->
            <circle cx="0" cy="0" r="42" fill="#0284c7" stroke="#38bdf8" stroke-width="1.5"/>
            <!-- Molten Outer Core -->
            <circle id="outerCoreCircle" cx="0" cy="0" r="24" fill="#ea580c" stroke="#f97316" stroke-width="2"/>
            <!-- Solid Inner Core -->
            <circle cx="0" cy="0" r="10" fill="#fef08a"/>
            <!-- Magnetic Poles -->
            <text x="0" y="-48" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">N</text>
            <text x="0" y="58" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">S</text>
            <!-- Auroral Rings -->
            <ellipse id="auroraN" cx="0" cy="-38" rx="14" ry="4" fill="none" stroke="#4ade80" stroke-width="2" opacity="0.9"/>
            <ellipse id="auroraS" cx="0" cy="38" rx="14" ry="4" fill="none" stroke="#4ade80" stroke-width="2" opacity="0.9"/>
          </g>

          <!-- Status Indicator HUD -->
          <g transform="translate(365, 30)">
            <rect x="0" y="0" width="160" height="150" rx="10" fill="rgba(15, 23, 42, 0.92)" stroke="#38bdf8" stroke-width="1.5" id="magHudBox"/>
            <text x="80" y="22" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Magnetosphere HUD</text>
            <line x1="10" y1="30" x2="150" y2="30" stroke="rgba(255,255,255,0.15)"/>
            
            <text x="10" y="48" fill="#94a3b8" font-size="9">Geodynamo: <tspan id="hudCore" fill="#4ade80" font-weight="700">ACTIVE</tspan></text>
            <text x="10" y="66" fill="#94a3b8" font-size="9">Field Strength: <tspan id="hudField" fill="#38bdf8" font-weight="700">30–60 µT</tspan></text>
            <text x="10" y="84" fill="#94a3b8" font-size="9">Solar Wind: <tspan id="hudWind" fill="#fbbf24" font-weight="700">DEFLECTED</tspan></text>
            <text x="10" y="102" fill="#94a3b8" font-size="9">Atmosphere: <tspan id="hudAtmo" fill="#4ade80" font-weight="700">PROTECTED</tspan></text>
            
            <rect x="8" y="114" width="144" height="26" rx="4" fill="rgba(16, 185, 129, 0.2)" id="hudBanner"/>
            <text id="hudBannerText" x="80" y="131" fill="#34d399" font-size="8.5" font-weight="800" text-anchor="middle">AURORAS VISIBLE AT POLES</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnToggleDynamo">⚡ Geodynamo: ON</button>
          <button class="sim-btn" id="btnSolarFlare">🔥 Trigger Solar Storm / CME</button>
        </div>
      `;

      function renderSolarWind(active, storm = false) {
        const swGroup = document.getElementById('solarWindParticles');
        swGroup.innerHTML = '';

        const count = storm ? 60 : 35;
        const color = storm ? '#ef4444' : '#fbbf24';

        for (let i = 0; i < count; i++) {
          const startY = 30 + Math.random() * 270;
          if (active) {
            // Deflected around Earth
            let d;
            if (startY < 165) {
              d = `M 10,${startY} Q 80,${startY} 110,${startY * 0.6} T 350,20`;
            } else {
              d = `M 10,${startY} Q 80,${startY} 110,${165 + (startY - 165) * 1.3} T 350,310`;
            }
            swGroup.innerHTML += `<path d="${d}" stroke="${color}" stroke-width="${storm ? 2.5 : 1.5}" fill="none" opacity="0.6" stroke-dasharray="8,6"/>`;
          } else {
            // Slam directly into Earth and strip atmosphere
            swGroup.innerHTML += `<line x1="10" y1="${startY}" x2="250" y2="${startY}" stroke="#ef4444" stroke-width="2" opacity="0.7" stroke-dasharray="6,4"/>`;
          }
        }
      }

      function updateDynamoState() {
        const fieldLines = document.getElementById('fieldLinesGroup');
        const auroraN = document.getElementById('auroraN');
        const auroraS = document.getElementById('auroraS');
        const outerCore = document.getElementById('outerCoreCircle');
        const hudCore = document.getElementById('hudCore');
        const hudField = document.getElementById('hudField');
        const hudWind = document.getElementById('hudWind');
        const hudAtmo = document.getElementById('hudAtmo');
        const hudBanner = document.getElementById('hudBanner');
        const hudBannerText = document.getElementById('hudBannerText');
        const magHudBox = document.getElementById('magHudBox');
        const btnToggleDynamo = document.getElementById('btnToggleDynamo');

        if (dynamoOn) {
          fieldLines.style.display = 'block';
          auroraN.style.display = 'block';
          auroraS.style.display = 'block';
          outerCore.setAttribute('fill', '#ea580c');
          btnToggleDynamo.textContent = "⚡ Geodynamo: ON";
          btnToggleDynamo.classList.add('active');
          
          hudCore.textContent = "ACTIVE (MOLTEN Fe-Ni)";
          hudCore.setAttribute('fill', '#4ade80');
          hudField.textContent = "30–60 µT (Dipole)";
          hudWind.textContent = "DEFLECTED SAFELY";
          hudWind.setAttribute('fill', '#38bdf8');
          hudAtmo.textContent = "SHIELDED & STABLE";
          hudAtmo.setAttribute('fill', '#4ade80');
          hudBanner.setAttribute('fill', 'rgba(16, 185, 129, 0.2)');
          hudBannerText.textContent = "AURORAS VISIBLE AT POLES";
          hudBannerText.setAttribute('fill', '#34d399');
          magHudBox.setAttribute('stroke', '#38bdf8');
          renderSolarWind(true, false);
        } else {
          fieldLines.style.display = 'none';
          auroraN.style.display = 'none';
          auroraS.style.display = 'none';
          outerCore.setAttribute('fill', '#475569'); // frozen core
          btnToggleDynamo.textContent = "❄️ Geodynamo: FROZEN CORE";
          btnToggleDynamo.classList.remove('active');

          hudCore.textContent = "SOLID / FROZEN (MARS)";
          hudCore.setAttribute('fill', '#ef4444');
          hudField.textContent = "0 µT (Collapsed)";
          hudWind.textContent = "BOMBARDING SURFACE";
          hudWind.setAttribute('fill', '#ef4444');
          hudAtmo.textContent = "BEING STRIPPED AWAY";
          hudAtmo.setAttribute('fill', '#ef4444');
          hudBanner.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
          hudBannerText.textContent = "ATMOSPHERE & OCEANS LOST!";
          hudBannerText.setAttribute('fill', '#f87171');
          magHudBox.setAttribute('stroke', '#ef4444');
          renderSolarWind(false, false);
        }
      }

      document.getElementById('btnToggleDynamo').addEventListener('click', () => {
        dynamoOn = !dynamoOn;
        updateDynamoState();
        sfx.playClick();
      });

      document.getElementById('btnSolarFlare').addEventListener('click', () => {
        renderSolarWind(dynamoOn, true);
        sfx.playCorrect();
        setTimeout(() => renderSolarWind(dynamoOn, false), 1500);
      });

      updateDynamoState();
    }

    // Slide 6: Air, Water, and Sunlight
    function simAirWaterSunlight() {
      simHeaderTitle.textContent = "Atmospheric Filter, Ozone Shield & Natural Greenhouse Heating";

      simCanvas.innerHTML = `
        <svg id="airWaterSunSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#030712"/>

          <!-- Atmospheric Column Layers -->
          <!-- Space -->
          <rect x="50" y="20" width="440" height="40" fill="#020617"/>
          <text x="60" y="42" fill="#64748b" font-size="9" font-weight="700">Space (Vacuum)</text>

          <!-- Mesosphere & Thermosphere -->
          <rect x="50" y="60" width="440" height="50" fill="#1e1b4b" opacity="0.6"/>
          <text x="60" y="88" fill="#818cf8" font-size="9">Mesosphere (Meteor burnup)</text>

          <!-- Stratosphere with Ozone Layer -->
          <rect x="50" y="110" width="440" height="60" fill="#0c4a6e" opacity="0.65"/>
          <rect id="ozoneBand" x="50" y="125" width="440" height="30" fill="#0284c7" opacity="0.85"/>
          <text id="lblOzoneBand" x="60" y="144" fill="#e0f2fe" font-size="10" font-weight="800">Stratospheric Ozone Layer (O₃) - UV Absorber</text>

          <!-- Troposphere (Weather & Life) -->
          <rect x="50" y="170" width="440" height="90" fill="#0369a1" opacity="0.5"/>
          <text x="60" y="195" fill="#bae6fd" font-size="10" font-weight="700">Troposphere (78% N₂, 21% O₂, H₂O vapor, CO₂)</text>

          <!-- Earth Surface & Oceans -->
          <rect x="50" y="260" width="440" height="50" fill="#15803d"/>
          <path d="M 280,260 Q 360,250 490,260 L 490,310 L 280,310 Z" fill="#0284c7"/>
          <text x="120" y="285" fill="#ffffff" font-size="10" font-weight="700">Fertile Soil & Forests</text>
          <text x="360" y="285" fill="#bae6fd" font-size="10" font-weight="700">Liquid Oceans (71%)</text>

          <!-- Incoming Solar Radiation Rays -->
          <g id="solarRaysGroup">
            <!-- Shortwave visible light penetrating to ground -->
            <line x1="180" y1="20" x2="180" y2="260" stroke="#fde047" stroke-width="3" stroke-dasharray="6,4"/>
            <text x="140" y="48" fill="#fde047" font-size="8.5" font-weight="700">Visible Light</text>

            <!-- Harmful UV rays blocked by Ozone -->
            <line id="uvRay" x1="260" y1="20" x2="260" y2="135" stroke="#f43f5e" stroke-width="3.5"/>
            <circle id="uvAbsorbed" cx="260" cy="135" r="5" fill="#f43f5e"/>
            <text x="270" y="55" fill="#f43f5e" font-size="8.5" font-weight="800">Lethal UV-B / UV-C</text>

            <!-- Thermal Infrared (Outgoing) -->
            <path id="irRay" d="M 330,260 Q 340,220 330,200 Q 315,220 330,240" stroke="#f97316" stroke-width="2.5" fill="none"/>
            <text x="345" y="225" fill="#f97316" font-size="8.5" font-weight="700">Trapped IR Heat</text>
          </g>

          <!-- Metrics Overlay Box -->
          <g transform="translate(370, 70)">
            <rect x="0" y="0" width="155" height="135" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.2"/>
            <text x="77" y="20" fill="#38bdf8" font-size="10" font-weight="800" text-anchor="middle">Atmospheric Balance</text>
            <line x1="8" y1="26" x2="147" y2="26" stroke="rgba(255,255,255,0.1)"/>
            
            <text x="8" y="45" fill="#94a3b8" font-size="8.5">Surface Temp: <tspan id="lblAtmoTemp" fill="#4ade80" font-weight="700">+15°C</tspan></text>
            <text x="8" y="65" fill="#94a3b8" font-size="8.5">Without Greenhouse: <tspan fill="#f87171" font-weight="700">-18°C</tspan></text>
            <text x="8" y="85" fill="#94a3b8" font-size="8.5">Natural Warming: <tspan fill="#fbbf24" font-weight="700">+33°C Lift</tspan></text>
            <text x="8" y="105" fill="#94a3b8" font-size="8.5">UV Shielding: <tspan id="lblUvStatus" fill="#4ade80" font-weight="700">99% Blocked</tspan></text>
            
            <rect x="6" y="113" width="143" height="16" rx="3" fill="rgba(16, 185, 129, 0.2)" id="shieldStatusPill"/>
            <text id="lblShieldPill" x="77" y="125" fill="#34d399" font-size="7.5" font-weight="800" text-anchor="middle">HABITABLE BIOSPHERE</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnOzoneNormal">🛡️ Ozone Shield: Intact (300 DU)</button>
          <button class="sim-btn" id="btnOzoneDepleted">⚠️ Ozone Depleted (Hole)</button>
          <button class="sim-btn" id="btnGreenhouseToggle">🌡️ Greenhouse: Natural (+15°C)</button>
        </div>
      `;

      let ozoneIntact = true;
      let ghEnhanced = false;

      function updateAtmosphere() {
        const ozoneBand = document.getElementById('ozoneBand');
        const uvRay = document.getElementById('uvRay');
        const uvAbsorbed = document.getElementById('uvAbsorbed');
        const lblUvStatus = document.getElementById('lblUvStatus');
        const lblAtmoTemp = document.getElementById('lblAtmoTemp');
        const lblShieldPill = document.getElementById('lblShieldPill');
        const shieldStatusPill = document.getElementById('shieldStatusPill');

        if (ozoneIntact) {
          ozoneBand.setAttribute('fill', '#0284c7');
          ozoneBand.setAttribute('opacity', '0.85');
          uvRay.setAttribute('y2', '135');
          uvAbsorbed.style.display = 'block';
          lblUvStatus.textContent = "99% Blocked (Safe)";
          lblUvStatus.setAttribute('fill', '#4ade80');
        } else {
          ozoneBand.setAttribute('fill', '#334155');
          ozoneBand.setAttribute('opacity', '0.3');
          uvRay.setAttribute('y2', '260'); // passes straight to ground
          uvAbsorbed.style.display = 'none';
          lblUvStatus.textContent = "LETHAL UV REACHES GROUND";
          lblUvStatus.setAttribute('fill', '#ef4444');
        }

        if (ghEnhanced) {
          lblAtmoTemp.textContent = "+18°C (Global Warming)";
          lblAtmoTemp.setAttribute('fill', '#ef4444');
        } else {
          lblAtmoTemp.textContent = "+15°C (Perfect)";
          lblAtmoTemp.setAttribute('fill', '#4ade80');
        }

        if (ozoneIntact && !ghEnhanced) {
          lblShieldPill.textContent = "HABITABLE BIOSPHERE";
          shieldStatusPill.setAttribute('fill', 'rgba(16, 185, 129, 0.2)');
          lblShieldPill.setAttribute('fill', '#34d399');
        } else {
          lblShieldPill.textContent = "CELLULAR DAMAGE & WARMING";
          shieldStatusPill.setAttribute('fill', 'rgba(239, 68, 68, 0.25)');
          lblShieldPill.setAttribute('fill', '#f87171');
        }
      }

      document.getElementById('btnOzoneNormal').addEventListener('click', () => {
        ozoneIntact = true;
        document.getElementById('btnOzoneNormal').classList.add('active');
        document.getElementById('btnOzoneDepleted').classList.remove('active');
        updateAtmosphere();
        sfx.playCorrect();
      });

      document.getElementById('btnOzoneDepleted').addEventListener('click', () => {
        ozoneIntact = false;
        document.getElementById('btnOzoneDepleted').classList.add('active');
        document.getElementById('btnOzoneNormal').classList.remove('active');
        updateAtmosphere();
        sfx.playIncorrect();
      });

      document.getElementById('btnGreenhouseToggle').addEventListener('click', (e) => {
        ghEnhanced = !ghEnhanced;
        e.target.textContent = ghEnhanced ? "🔥 Greenhouse: Enhanced (+18°C)" : "🌡️ Greenhouse: Natural (+15°C)";
        e.target.classList.toggle('active', ghEnhanced);
        updateAtmosphere();
        sfx.playClick();
      });
    }

    // Slide 7: Soil, Rocks, and Essential Minerals
    function simSoilLithosphereMinerals() {
      simHeaderTitle.textContent = "Soil Profile Horizons & Root Mineral Pharmacy Explorer";

      simCanvas.innerHTML = `
        <svg id="soilSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Plant Above Ground -->
          <g transform="translate(140, 20)">
            <!-- Stem and leaves -->
            <path d="M 30,70 Q 30,30 30,0" stroke="#22c55e" stroke-width="4" fill="none"/>
            <path d="M 30,40 Q 5,20 0,35 Q 20,45 30,40" fill="#15803d"/>
            <path d="M 30,20 Q 55,0 60,15 Q 40,25 30,20" fill="#15803d"/>
            <text x="40" y="10" font-size="14">🌱</text>
          </g>

          <!-- Soil Horizon Strata Layers -->
          <!-- O Horizon: Humus & Organic litter (y: 90 to 120) -->
          <rect id="layerO" x="30" y="90" width="260" height="30" fill="#3f2e18" stroke="#78350f" stroke-width="1"/>
          <text x="40" y="110" fill="#fef08a" font-size="10" font-weight="700">O Horizon: Humus & Leaf Litter</text>

          <!-- A Horizon: Topsoil (rich organic + minerals, y: 120 to 180) -->
          <rect id="layerA" x="30" y="120" width="260" height="60" fill="#583a1b" stroke="#78350f" stroke-width="1"/>
          <text x="40" y="145" fill="#fed7aa" font-size="10" font-weight="700">A Horizon: Topsoil (Fertile Zone)</text>
          <text x="40" y="162" fill="#d97706" font-size="8.5">Earthworms, bacteria, root hairs</text>

          <!-- B Horizon: Subsoil (accumulated clay & iron, y: 180 to 240) -->
          <rect id="layerB" x="30" y="180" width="260" height="60" fill="#7c2d12" stroke="#9a3412" stroke-width="1"/>
          <text x="40" y="210" fill="#fca5a5" font-size="10" font-weight="700">B Horizon: Subsoil (Clay & Minerals)</text>

          <!-- C Horizon: Weathered Parent Rock (y: 240 to 285) -->
          <rect id="layerC" x="30" y="240" width="260" height="45" fill="#475569" stroke="#334155" stroke-width="1"/>
          <text x="40" y="265" fill="#cbd5e1" font-size="9.5" font-weight="700">C Horizon: Weathered Bedrock</text>

          <!-- R Horizon: Solid Bedrock (y: 285 to 320) -->
          <rect id="layerR" x="30" y="285" width="260" height="35" fill="#1e293b"/>
          <text x="40" y="307" fill="#94a3b8" font-size="9.5" font-weight="700">R Horizon: Solid Bedrock</text>

          <!-- Root Branching into Topsoil & Subsoil -->
          <g id="rootsGroup">
            <path d="M 170,90 Q 170,140 170,170 Q 150,200 130,220" stroke="#fef08a" stroke-width="3" fill="none"/>
            <path d="M 170,130 Q 200,150 215,180" stroke="#fde047" stroke-width="2" fill="none"/>
            <path d="M 170,150 Q 140,165 120,185" stroke="#fde047" stroke-width="1.8" fill="none"/>
          </g>

          <!-- Animated Nutrient Ion Particles -->
          <g id="ionParticlesGroup">
            <!-- Dynamically injected -->
          </g>

          <!-- Horizon & Weathering Inspector Card -->
          <g transform="translate(310, 30)">
            <rect x="0" y="0" width="215" height="270" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1.5"/>
            <text id="soilCardTitle" x="107" y="26" fill="#fbbf24" font-size="12" font-weight="800" text-anchor="middle">A Horizon: Fertile Topsoil</text>
            <line x1="12" y1="36" x2="203" y2="36" stroke="rgba(255,255,255,0.15)"/>
            
            <text id="sDetail1" x="12" y="58" fill="#f8fafc" font-size="9.5" font-weight="700">Formation Duration:</text>
            <text id="sDetail2" x="12" y="74" fill="#38bdf8" font-size="9">200 to 1,000 years for 1 cm!</text>

            <text id="sDetail3" x="12" y="98" fill="#f8fafc" font-size="9.5" font-weight="700">Biological Role:</text>
            <text id="sDetail4" x="12" y="114" fill="#cbd5e1" font-size="9">Primary zone for plant roots</text>

            <text x="12" y="138" fill="#f8fafc" font-size="9.5" font-weight="700">Essential Mineral Pharmacy:</text>
            <text id="sMineralList" x="12" y="154" fill="#4ade80" font-size="8.5">• Nitrogen (N): Amino acids & proteins</text>
            <text id="sMineralList2" x="12" y="170" fill="#4ade80" font-size="8.5">• Phosphorus (P): ATP & root strength</text>
            <text id="sMineralList3" x="12" y="186" fill="#4ade80" font-size="8.5">• Potassium (K): Water & enzyme balance</text>
            <text id="sMineralList4" x="12" y="202" fill="#4ade80" font-size="8.5">• Iron (Fe) & Magnesium (Mg): Chlorophyll</text>

            <rect x="10" y="218" width="195" height="40" rx="6" fill="rgba(245, 158, 11, 0.15)" stroke="#f59e0b" stroke-width="1"/>
            <text id="sBottomTip" x="107" y="242" fill="#fbbf24" font-size="8.5" font-weight="800" text-anchor="middle">Non-Renewable on Human Lifespans</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.4rem; justify-content:center; align-items:center;">
          <button class="sim-btn" id="btnH_O">O (Humus)</button>
          <button class="sim-btn active" id="btnH_A">A (Topsoil)</button>
          <button class="sim-btn" id="btnH_B">B (Subsoil)</button>
          <button class="sim-btn" id="btnH_C">C (Weathered)</button>
          <button class="sim-btn" id="btnH_R">R (Bedrock)</button>
          <button class="sim-btn" id="btnAbsorbIons">⚡ Simulate Root Ion Absorption</button>
        </div>
      `;

      function selectHorizon(h) {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        const sTitle = document.getElementById('soilCardTitle');
        const sDetail1 = document.getElementById('sDetail1');
        const sDetail2 = document.getElementById('sDetail2');
        const sDetail3 = document.getElementById('sDetail3');
        const sDetail4 = document.getElementById('sDetail4');

        if (h === 'O') {
          document.getElementById('btnH_O').classList.add('active');
          sTitle.textContent = "O Horizon: Organic Humus";
          sDetail1.textContent = "Composition:";
          sDetail2.textContent = "Decomposed leaves, twigs, forest litter";
          sDetail3.textContent = "Ecological Role:";
          sDetail4.textContent = "Recycles nutrients, prevents erosion";
        } else if (h === 'A') {
          document.getElementById('btnH_A').classList.add('active');
          sTitle.textContent = "A Horizon: Fertile Topsoil";
          sDetail1.textContent = "Formation Duration:";
          sDetail2.textContent = "200 to 1,000 years per centimetre";
          sDetail3.textContent = "Biological Role:";
          sDetail4.textContent = "Hosts earthworms, microbes & plant roots";
        } else if (h === 'B') {
          document.getElementById('btnH_B').classList.add('active');
          sTitle.textContent = "B Horizon: Mineral Subsoil";
          sDetail1.textContent = "Composition:";
          sDetail2.textContent = "Dense clay, iron, aluminium oxides";
          sDetail3.textContent = "Role:";
          sDetail4.textContent = "Leached minerals accumulate from above";
        } else if (h === 'C') {
          document.getElementById('btnH_C').classList.add('active');
          sTitle.textContent = "C Horizon: Weathered Rock";
          sDetail1.textContent = "Origin:";
          sDetail2.textContent = "Broken chunks of bedrock (regolith)";
          sDetail3.textContent = "Role:";
          sDetail4.textContent = "Transition zone from rock to mineral soil";
        } else if (h === 'R') {
          document.getElementById('btnH_R').classList.add('active');
          sTitle.textContent = "R Horizon: Solid Bedrock";
          sDetail1.textContent = "Structure:";
          sDetail2.textContent = "Unweathered parent rock (basalt, granite)";
          sDetail3.textContent = "Role:";
          sDetail4.textContent = "Foundation of Earth's continental crust";
        }
        sfx.playClick();
      }

      function animateIons() {
        const c = document.getElementById('ionParticlesGroup');
        c.innerHTML = '';
        const ions = [
          { name: "K⁺", color: "#f59e0b", x: 140, y: 150 },
          { name: "NO₃⁻", color: "#38bdf8", x: 190, y: 140 },
          { name: "PO₄³⁻", color: "#4ade80", x: 160, y: 170 },
          { name: "Ca²⁺", color: "#e879f9", x: 210, y: 165 },
          { name: "Fe²⁺", color: "#f87171", x: 130, y: 190 }
        ];

        ions.forEach(ion => {
          c.innerHTML += `
            <circle cx="${ion.x}" cy="${ion.y}" r="6" fill="${ion.color}" opacity="0.9"/>
            <text x="${ion.x}" y="${ion.y + 3}" fill="#0f172a" font-size="7" font-weight="900" text-anchor="middle">${ion.name}</text>
            <path d="M ${ion.x},${ion.y} Q 170,120 170,90" stroke="${ion.color}" stroke-width="1.5" stroke-dasharray="3,3" fill="none"/>
          `;
        });
        sfx.playCorrect();
      }

      document.getElementById('btnH_O').addEventListener('click', () => selectHorizon('O'));
      document.getElementById('btnH_A').addEventListener('click', () => selectHorizon('A'));
      document.getElementById('btnH_B').addEventListener('click', () => selectHorizon('B'));
      document.getElementById('btnH_C').addEventListener('click', () => selectHorizon('C'));
      document.getElementById('btnH_R').addEventListener('click', () => selectHorizon('R'));
      document.getElementById('btnAbsorbIons').addEventListener('click', animateIons);
    }

    // Slide 8: The Living Web: Microbes, Plants & Animals
    function simBiosphereWeb() {
      simHeaderTitle.textContent = "Biosphere Food Web & Marine Phytoplankton Engine";

      simCanvas.innerHTML = `
        <svg id="webSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Sunlit Epipelagic Zone (Top Ocean Layer) -->
          <rect x="20" y="20" width="500" height="110" fill="#0369a1" opacity="0.7"/>
          <text x="30" y="40" fill="#e0f2fe" font-size="10" font-weight="800">Sunlit Euphotic Zone (0–200m)</text>

          <!-- Animated Sunlight Rays -->
          <line x1="100" y1="20" x2="100" y2="120" stroke="#fde047" stroke-width="2" opacity="0.6"/>
          <line x1="220" y1="20" x2="220" y2="120" stroke="#fde047" stroke-width="2" opacity="0.6"/>
          <line x1="340" y1="20" x2="340" y2="120" stroke="#fde047" stroke-width="2" opacity="0.6"/>

          <!-- Phytoplankton Micro-Cells (Diatoms & Cyanobacteria) -->
          <g id="phytoGroup">
            <!-- Microscopic green dots with oxygen bubbles -->
            <circle cx="80" cy="70" r="5" fill="#22c55e"/>
            <circle cx="120" cy="60" r="4" fill="#4ade80"/>
            <circle cx="160" cy="80" r="6" fill="#16a34a"/>
            <circle cx="200" cy="65" r="5" fill="#22c55e"/>
            <circle cx="260" cy="75" r="4.5" fill="#4ade80"/>
            <circle cx="300" cy="60" r="5.5" fill="#16a34a"/>
            <!-- O2 bubbles rising -->
            <circle cx="82" cy="50" r="3" fill="#bae6fd" opacity="0.8"/>
            <circle cx="162" cy="55" r="3.5" fill="#bae6fd" opacity="0.8"/>
            <circle cx="262" cy="48" r="3" fill="#bae6fd" opacity="0.8"/>
            <text x="180" y="95" fill="#4ade80" font-size="9" font-weight="700">Microscopic Marine Phytoplankton (>50% of Global O₂!)</text>
          </g>

          <!-- Mesopelagic / Twilight Zone (Middle Layer) -->
          <rect x="20" y="130" width="500" height="100" fill="#0f172a" opacity="0.85"/>
          <text x="30" y="150" fill="#94a3b8" font-size="10" font-weight="700">Consumer Zone: Zooplankton, Fish & Marine Mammals</text>

          <!-- Marine Animals -->
          <g transform="translate(100, 160)">
            <text x="0" y="0" font-size="16">🦐</text>
            <text x="80" y="10" font-size="18">🐟</text>
            <text x="180" y="-5" font-size="20">🐬</text>
            <text x="280" y="20" font-size="26">🐋</text>
          </g>

          <!-- Bathypelagic & Seabed Decomposer Zone (Bottom Layer) -->
          <rect x="20" y="230" width="500" height="80" fill="#020617"/>
          <text x="30" y="250" fill="#64748b" font-size="9.5" font-weight="700">Abyssal Seabed & Microbial Decomposers (Recycling Zone)</text>

          <!-- Marine Snow & Decomposers -->
          <g transform="translate(60, 265)">
            <circle cx="30" cy="10" r="2" fill="#cbd5e1" opacity="0.6"/>
            <circle cx="100" cy="25" r="2" fill="#cbd5e1" opacity="0.6"/>
            <circle cx="200" cy="15" r="2" fill="#cbd5e1" opacity="0.6"/>
            <text x="300" y="15" fill="#fbbf24" font-size="9">Marine Snow (Nutrient Recycling by Microbes)</text>
            <text x="50" y="25" font-size="14">🦀</text>
            <text x="150" y="25" font-size="14">🦠</text>
          </g>

          <!-- Real-Time Production Badge -->
          <g transform="translate(350, 30)">
            <rect x="0" y="0" width="160" height="60" rx="8" fill="rgba(15, 23, 42, 0.92)" stroke="#22c55e" stroke-width="1.5"/>
            <text x="80" y="18" fill="#4ade80" font-size="10" font-weight="800" text-anchor="middle">Planetary Oxygen Engine</text>
            <text x="80" y="36" fill="#f8fafc" font-size="11" font-weight="800" text-anchor="middle">Phytoplankton: >50%</text>
            <text x="80" y="50" fill="#94a3b8" font-size="8.5" text-anchor="middle">Forests & Land Plants: ~48%</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnTrophProducers">🌱 Producers (Phytoplankton/Plants)</button>
          <button class="sim-btn" id="btnTrophConsumers">🐟 Consumers (Zooplankton/Fish/Whales)</button>
          <button class="sim-btn" id="btnTrophDecomposers">🦠 Decomposers (Bacteria/Fungi)</button>
        </div>
      `;

      function highlightTrophic(lvl) {
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        const pGroup = document.getElementById('phytoGroup');
        
        if (lvl === 'prod') {
          document.getElementById('btnTrophProducers').classList.add('active');
          pGroup.style.opacity = '1';
        } else if (lvl === 'cons') {
          document.getElementById('btnTrophConsumers').classList.add('active');
        } else {
          document.getElementById('btnTrophDecomposers').classList.add('active');
        }
        sfx.playClick();
      }

      document.getElementById('btnTrophProducers').addEventListener('click', () => highlightTrophic('prod'));
      document.getElementById('btnTrophConsumers').addEventListener('click', () => highlightTrophic('cons'));
      document.getElementById('btnTrophDecomposers').addEventListener('click', () => highlightTrophic('decomp'));
    }

    // Slide 9: The Importance of Natural Balance (Dynamic Homeostasis)
    function simCarbonOxygenBalance() {
      simHeaderTitle.textContent = "Carbon-Oxygen Dynamic Balance Seesaw Simulator";
      let photoRate = 100;
      let respRate = 100;

      simCanvas.innerHTML = `
        <svg id="balanceSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#030712"/>

          <!-- Fulcrum Triangle in Center -->
          <polygon points="270,220 250,265 290,265" fill="#334155" stroke="#64748b" stroke-width="2"/>
          <circle cx="270" cy="220" r="5" fill="#38bdf8"/>
          <text x="270" y="285" fill="#94a3b8" font-size="9" font-weight="700" text-anchor="middle">Dynamic Homeostasis Pivot</text>

          <!-- Tilting Seesaw Plank -->
          <g id="seesawPlankGroup" transform="rotate(0 270 220)">
            <rect x="70" y="216" width="400" height="8" rx="4" fill="#0ea5e9"/>
            
            <!-- Left Side: Photosynthesis (O2 Producer) -->
            <g transform="translate(100, 160)">
              <rect x="-40" y="-45" width="80" height="45" rx="6" fill="rgba(34, 197, 94, 0.2)" stroke="#22c55e" stroke-width="1.5"/>
              <text x="0" y="-28" fill="#4ade80" font-size="10" font-weight="800" text-anchor="middle">🌿 Photosynthesis</text>
              <text x="0" y="-12" fill="#86efac" font-size="9" text-anchor="middle">Generates O₂</text>
              <circle cx="0" cy="10" r="14" fill="#22c55e"/>
              <text x="0" y="14" font-size="12" text-anchor="middle">🌳</text>
            </g>

            <!-- Right Side: Respiration & Combustion (CO2 Producer) -->
            <g transform="translate(440, 160)">
              <rect x="-40" y="-45" width="80" height="45" rx="6" fill="rgba(245, 158, 11, 0.2)" stroke="#f59e0b" stroke-width="1.5"/>
              <text x="0" y="-28" fill="#fbbf24" font-size="10" font-weight="800" text-anchor="middle">💨 Respiration</text>
              <text x="0" y="-12" fill="#fde68a" font-size="9" text-anchor="middle">& Combustion</text>
              <circle cx="0" cy="10" r="14" fill="#d97706"/>
              <text x="0" y="14" font-size="12" text-anchor="middle">🏭</text>
            </g>
          </g>

          <!-- Atmosphere Dial & Metrics at Top -->
          <g transform="translate(150, 25)">
            <rect x="0" y="0" width="240" height="100" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5"/>
            <text x="120" y="22" fill="#38bdf8" font-size="12" font-weight="800" text-anchor="middle">Atmospheric Gas Equilibrium</text>
            <line x1="12" y1="30" x2="228" y2="30" stroke="rgba(255,255,255,0.1)"/>
            
            <text x="20" y="52" fill="#94a3b8" font-size="10">Oxygen (O₂): <tspan id="valO2" fill="#4ade80" font-weight="800">20.95%</tspan></text>
            <text x="20" y="72" fill="#94a3b8" font-size="10">Carbon Dioxide: <tspan id="valCO2" fill="#fbbf24" font-weight="800">420 ppm (0.042%)</tspan></text>
            
            <rect x="12" y="80" width="216" height="15" rx="3" fill="rgba(16, 185, 129, 0.2)" id="balancePill"/>
            <text id="lblBalanceText" x="120" y="91" fill="#34d399" font-size="8" font-weight="800" text-anchor="middle">STABLE EQUILIBRIUM</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.5rem; align-items:center; width:100%;">
          <div style="display:flex; gap:1rem; flex-wrap:wrap; justify-content:center; width:90%;">
            <div style="display:flex; align-items:center; gap:0.5rem;">
              <span style="font-size:0.8rem; font-weight:700; color:#4ade80;">Photosynthesis:</span>
              <input type="range" id="sliderPhoto" min="50" max="150" value="100" style="width:100px;">
              <span id="txtPhoto" style="font-size:0.8rem; font-weight:700; color:#f8fafc; min-width:35px;">100%</span>
            </div>
            <div style="display:flex; align-items:center; gap:0.5rem;">
              <span style="font-size:0.8rem; font-weight:700; color:#fbbf24;">Respiration/Industry:</span>
              <input type="range" id="sliderResp" min="50" max="200" value="100" style="width:100px;">
              <span id="txtResp" style="font-size:0.8rem; font-weight:700; color:#f8fafc; min-width:35px;">100%</span>
            </div>
          </div>
          <button class="sim-btn" id="btnResetSeesaw">⚖️ Restore Perfect Natural Balance</button>
        </div>
      `;

      function updateSeesaw() {
        const diff = respRate - photoRate;
        // Angle clamp between -15 and +15 degrees
        let angle = diff * 0.2;
        if (angle > 15) angle = 15;
        if (angle < -15) angle = -15;

        document.getElementById('seesawPlankGroup').setAttribute('transform', `rotate(${angle} 270 220)`);
        
        // Compute gas variations
        const o2Pct = (20.95 + (photoRate - respRate) * 0.02).toFixed(2);
        const co2Ppm = Math.round(420 + (respRate - photoRate) * 2.5);

        document.getElementById('valO2').textContent = `${o2Pct}%`;
        document.getElementById('valCO2').textContent = `${co2Ppm} ppm`;

        const pill = document.getElementById('balancePill');
        const pillText = document.getElementById('lblBalanceText');

        if (diff > 30) {
          pill.setAttribute('fill', 'rgba(239, 68, 68, 0.3)');
          pillText.textContent = "CRITICAL: RUNAWAY CO₂ ACCUMULATION";
          pillText.setAttribute('fill', '#f87171');
        } else if (diff < -30) {
          pill.setAttribute('fill', 'rgba(56, 189, 248, 0.3)');
          pillText.textContent = "OXYGEN SURPLUS / LOW CO₂";
          pillText.setAttribute('fill', '#38bdf8');
        } else {
          pill.setAttribute('fill', 'rgba(16, 185, 129, 0.2)');
          pillText.textContent = "STABLE EQUILIBRIUM (HOMEOSTASIS)";
          pillText.setAttribute('fill', '#34d399');
        }
      }

      document.getElementById('sliderPhoto').addEventListener('input', (e) => {
        photoRate = parseInt(e.target.value);
        document.getElementById('txtPhoto').textContent = photoRate + '%';
        updateSeesaw();
      });

      document.getElementById('sliderResp').addEventListener('input', (e) => {
        respRate = parseInt(e.target.value);
        document.getElementById('txtResp').textContent = respRate + '%';
        updateSeesaw();
      });

      document.getElementById('btnResetSeesaw').addEventListener('click', () => {
        photoRate = 100;
        respRate = 100;
        document.getElementById('sliderPhoto').value = 100;
        document.getElementById('sliderResp').value = 100;
        document.getElementById('txtPhoto').textContent = '100%';
        document.getElementById('txtResp').textContent = '100%';
        updateSeesaw();
        sfx.playCorrect();
      });
    }

    // Slide 10: Asexual Reproduction: Rapid Propagation (4 Modes)
    function simAsexualReproduction() {
      simHeaderTitle.textContent = "Asexual Reproduction: 4 Propagation Modes Explorer";
      let activeMode = 'amoeba';

      simCanvas.innerHTML = `
        <svg id="asexualSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Mode Display Canvas Group -->
          <g id="asexualDisplayGroup">
            <!-- Dynamic Content -->
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnAsexAmoeba">1. Binary Fission (Amoeba)</button>
          <button class="sim-btn" id="btnAsexHydra">2. Budding (Hydra)</button>
          <button class="sim-btn" id="btnAsexPotato">3. Vegetative (Bryophyllum / Potato)</button>
          <button class="sim-btn" id="btnAsexRhizopus">4. Spores (Rhizopus Mold)</button>
        </div>
      `;

      function renderMode(mode) {
        activeMode = mode;
        const g = document.getElementById('asexualDisplayGroup');
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));

        if (mode === 'amoeba') {
          document.getElementById('btnAsexAmoeba').classList.add('active');
          g.innerHTML = `
            <!-- Title -->
            <text x="270" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Mode 1: Binary Fission in Amoeba (Single Cell Division)</text>
            
            <!-- Stage 1: Parent Cell -->
            <g transform="translate(70, 70)">
              <rect x="-40" y="0" width="80" height="150" rx="8" fill="rgba(30, 41, 59, 0.6)"/>
              <text x="0" y="20" fill="#94a3b8" font-size="9" text-anchor="middle">Stage 1: Parent</text>
              <circle cx="0" cy="75" r="28" fill="#0284c7" opacity="0.7"/>
              <circle cx="0" cy="75" r="8" fill="#f43f5e"/>
              <text x="0" y="130" fill="#cbd5e1" font-size="8" text-anchor="middle">Intact Nucleus</text>
            </g>

            <text x="135" y="150" fill="#38bdf8" font-size="16">→</text>

            <!-- Stage 2: Nuclear Elongation -->
            <g transform="translate(195, 70)">
              <rect x="-40" y="0" width="80" height="150" rx="8" fill="rgba(30, 41, 59, 0.6)"/>
              <text x="0" y="20" fill="#94a3b8" font-size="9" text-anchor="middle">Stage 2: Elongation</text>
              <ellipse cx="0" cy="75" rx="34" ry="22" fill="#0284c7" opacity="0.7"/>
              <ellipse cx="0" cy="75" rx="16" ry="6" fill="#f43f5e"/>
              <text x="0" y="130" fill="#cbd5e1" font-size="8" text-anchor="middle">Nucleus Divides</text>
            </g>

            <text x="260" y="150" fill="#38bdf8" font-size="16">→</text>

            <!-- Stage 3: Cytoplasm Constriction -->
            <g transform="translate(325, 70)">
              <rect x="-40" y="0" width="80" height="150" rx="8" fill="rgba(30, 41, 59, 0.6)"/>
              <text x="0" y="20" fill="#94a3b8" font-size="9" text-anchor="middle">Stage 3: Cleavage</text>
              <circle cx="-16" cy="75" r="20" fill="#0284c7" opacity="0.7"/>
              <circle cx="16" cy="75" r="20" fill="#0284c7" opacity="0.7"/>
              <circle cx="-16" cy="75" r="6" fill="#f43f5e"/>
              <circle cx="16" cy="75" r="6" fill="#f43f5e"/>
              <text x="0" y="130" fill="#cbd5e1" font-size="8" text-anchor="middle">Constriction Furrow</text>
            </g>

            <text x="390" y="150" fill="#38bdf8" font-size="16">→</text>

            <!-- Stage 4: 2 Identical Daughters -->
            <g transform="translate(455, 70)">
              <rect x="-45" y="0" width="90" height="150" rx="8" fill="rgba(16, 185, 129, 0.15)" stroke="#10b981" stroke-width="1"/>
              <text x="0" y="20" fill="#4ade80" font-size="9" font-weight="700" text-anchor="middle">Stage 4: 2 Daughters</text>
              <circle cx="0" cy="55" r="18" fill="#10b981" opacity="0.8"/>
              <circle cx="0" cy="55" r="5" fill="#f43f5e"/>
              <circle cx="0" cy="100" r="18" fill="#10b981" opacity="0.8"/>
              <circle cx="0" cy="100" r="5" fill="#f43f5e"/>
              <text x="0" y="135" fill="#34d399" font-size="8" font-weight="800" text-anchor="middle">100% Clones</text>
            </g>

            <!-- Bottom Summary Bar -->
            <rect x="50" y="250" width="440" height="50" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1"/>
            <text x="270" y="270" fill="#f8fafc" font-size="10" font-weight="700" text-anchor="middle">Key Feature: No gametes needed; 1 parent splits into 2 genetically identical daughter cells.</text>
            <text x="270" y="288" fill="#38bdf8" font-size="9" text-anchor="middle">Examples: Amoeba proteus, Paramecium, Leishmania, Escherichia coli bacteria.</text>
          `;
        } else if (mode === 'hydra') {
          document.getElementById('btnAsexHydra').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Mode 2: Budding in Hydra (Multicellular Outgrowth)</text>
            
            <g transform="translate(100, 60)">
              <!-- Parent Hydra body -->
              <path d="M 120,220 C 110,180 120,130 130,80" stroke="#22c55e" stroke-width="20" stroke-linecap="round" fill="none"/>
              <!-- Tentacles on top -->
              <path d="M 130,80 Q 110,40 100,30" stroke="#4ade80" stroke-width="4" fill="none"/>
              <path d="M 130,80 Q 130,30 135,20" stroke="#4ade80" stroke-width="4" fill="none"/>
              <path d="M 130,80 Q 150,40 160,35" stroke="#4ade80" stroke-width="4" fill="none"/>
              <text x="130" y="110" fill="#f8fafc" font-size="10" font-weight="700">Parent Hydra</text>

              <!-- Outgrowth Bud forming -->
              <g id="budGroup">
                <path d="M 138,150 Q 170,140 185,120" stroke="#86efac" stroke-width="12" stroke-linecap="round" fill="none"/>
                <!-- Miniature tentacles on bud -->
                <path d="M 185,120 Q 195,105 205,100" stroke="#86efac" stroke-width="2.5" fill="none"/>
                <path d="M 185,120 Q 200,120 210,125" stroke="#86efac" stroke-width="2.5" fill="none"/>
                <text x="195" y="145" fill="#fde047" font-size="9" font-weight="800">Developing Bud</text>
              </g>
            </g>

            <rect x="50" y="250" width="440" height="50" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#22c55e" stroke-width="1"/>
            <text x="270" y="270" fill="#f8fafc" font-size="10" font-weight="700" text-anchor="middle">Mechanism: Mitotic cell divisions produce a bulbous bud that develops mouth & tentacles,</text>
            <text x="270" y="288" fill="#4ade80" font-size="9" text-anchor="middle">then detaches to mature as an independent organism. Also seen in single-celled Yeast!</text>
          `;
        } else if (mode === 'potato') {
          document.getElementById('btnAsexPotato').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Mode 3: Vegetative Propagation (Bryophyllum Leaf & Potato Tubers)</text>
            
            <!-- Bryophyllum leaf SVG -->
            <g transform="translate(140, 60)">
              <!-- Leaf outline with serrated notches -->
              <path d="M 50,150 Q 130,50 220,140 Q 150,220 50,150 Z" fill="#15803d" stroke="#22c55e" stroke-width="2"/>
              <path d="M 50,150 Q 140,140 220,140" stroke="#86efac" stroke-width="2" fill="none"/>
              <!-- Sprouting plantlets in notches -->
              <g transform="translate(120, 85)">
                <text x="0" y="0" font-size="14">🌱</text>
                <text x="0" y="15" fill="#fde047" font-size="8" font-weight="700" text-anchor="middle">Adventitious Bud</text>
              </g>
              <g transform="translate(180, 105)">
                <text x="0" y="0" font-size="14">🌱</text>
              </g>
              <g transform="translate(150, 185)">
                <text x="0" y="0" font-size="14">🌱</text>
              </g>
            </g>

            <rect x="50" y="250" width="440" height="50" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1"/>
            <text x="270" y="270" fill="#f8fafc" font-size="10" font-weight="700" text-anchor="middle">Botanical Principle: New offspring sprout directly from vegetative parts (leaves, stems, roots).</text>
            <text x="270" y="288" fill="#fde047" font-size="9" text-anchor="middle">Examples: Bryophyllum leaf notches, Potato 'eyes' (stem buds), Ginger rhizomes, Rose stem cuttings.</text>
          `;
        } else if (mode === 'rhizopus') {
          document.getElementById('btnAsexRhizopus').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Mode 4: Spore Formation in Bread Mold (Rhizopus stolonifer)</text>
            
            <g transform="translate(180, 60)">
              <!-- Bread base -->
              <rect x="-80" y="160" width="320" height="30" rx="4" fill="#78350f" opacity="0.8"/>
              <text x="80" y="180" fill="#fed7aa" font-size="10" font-weight="700" text-anchor="middle">Stale Moist Bread Substrate</text>

              <!-- Hyphae and Sporangiophores -->
              <path d="M 40,160 Q 45,100 40,60" stroke="#94a3b8" stroke-width="3" fill="none"/>
              <path d="M 120,160 Q 115,90 120,50" stroke="#94a3b8" stroke-width="3" fill="none"/>

              <!-- Sporangium bulb -->
              <circle cx="40" cy="55" r="16" fill="#1e293b" stroke="#64748b" stroke-width="1.5"/>
              <text x="40" y="40" fill="#cbd5e1" font-size="8" font-weight="700" text-anchor="middle">Sporangium</text>

              <!-- Ruptured Sporangium releasing millions of spores -->
              <path d="M 108,50 A 16,16 0 1,1 132,45" fill="none" stroke="#64748b" stroke-width="2"/>
              <!-- Escaping microscopic spores -->
              <circle cx="135" cy="35" r="2" fill="#fbbf24"/>
              <circle cx="145" cy="45" r="2.5" fill="#fbbf24"/>
              <circle cx="150" cy="30" r="2" fill="#fbbf24"/>
              <circle cx="160" cy="50" r="2.2" fill="#fbbf24"/>
              <circle cx="140" cy="60" r="2.2" fill="#fbbf24"/>
              <text x="165" y="25" fill="#fde047" font-size="9" font-weight="800">Dormant Spores (Wind Dispersal)</text>
            </g>

            <rect x="50" y="250" width="440" height="50" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1"/>
            <text x="270" y="270" fill="#f8fafc" font-size="10" font-weight="700" text-anchor="middle">Survival Feature: Spores are microscopic single cells enclosed in tough resistant walls</text>
            <text x="270" y="288" fill="#38bdf8" font-size="9" text-anchor="middle">that survive extreme heat, drought, and cold until landing on moist nutrient food!</text>
          `;
        }
        sfx.playClick();
      }

      document.getElementById('btnAsexAmoeba').addEventListener('click', () => renderMode('amoeba'));
      document.getElementById('btnAsexHydra').addEventListener('click', () => renderMode('hydra'));
      document.getElementById('btnAsexPotato').addEventListener('click', () => renderMode('potato'));
      document.getElementById('btnAsexRhizopus').addEventListener('click', () => renderMode('rhizopus'));

      renderMode('amoeba');
    }

    // Slide 11: Sexual Reproduction: Genetic Diversity
    function simSexualReproduction() {
      simHeaderTitle.textContent = "Gametogenesis, Fertilization & Genetic Recombination Laboratory";

      simCanvas.innerHTML = `
        <svg id="sexualSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#030712"/>

          <!-- Male Gamete: Sperm Cell (n = 23) -->
          <g id="spermCell" transform="translate(100, 150)">
            <ellipse cx="0" cy="0" rx="14" ry="9" fill="#38bdf8"/>
            <circle cx="-4" cy="0" r="5" fill="#1e3a8a"/>
            <!-- Wavy Flagellum Tail -->
            <path d="M -14,0 Q -30,-15 -45,0 Q -60,15 -75,0" stroke="#38bdf8" stroke-width="2.5" fill="none"/>
            <text x="-40" y="-20" fill="#38bdf8" font-size="10" font-weight="800">Male Gamete (Sperm)</text>
            <text x="-40" y="-7" fill="#bae6fd" font-size="9">Haploid (n = 23 chromosomes)</text>
          </g>

          <text x="180" y="155" fill="#f8fafc" font-size="22" font-weight="900">+</text>

          <!-- Female Gamete: Ovum / Egg Cell (n = 23) -->
          <g id="ovumCell" transform="translate(260, 150)">
            <!-- Outer Zona Pellucida membrane -->
            <circle cx="0" cy="0" r="48" fill="#f43f5e" opacity="0.25" stroke="#f43f5e" stroke-width="2"/>
            <circle cx="0" cy="0" r="38" fill="#e11d48" opacity="0.75"/>
            <!-- Nucleus -->
            <circle cx="0" cy="0" r="14" fill="#ffe4e6"/>
            <text x="0" y="4" fill="#881337" font-size="9" font-weight="800" text-anchor="middle">n = 23</text>
            <text x="0" y="-56" fill="#f43f5e" font-size="10" font-weight="800" text-anchor="middle">Female Gamete (Ovum)</text>
          </g>

          <text x="330" y="155" fill="#f8fafc" font-size="22" font-weight="900">→</text>

          <!-- Fertilized Diploid Zygote (2n = 46) -->
          <g id="zygoteCell" transform="translate(420, 150)">
            <circle cx="0" cy="0" r="50" fill="rgba(16, 185, 129, 0.25)" stroke="#10b981" stroke-width="2.5"/>
            <circle cx="0" cy="0" r="40" fill="#059669" opacity="0.8"/>
            <!-- Combined Nucleus -->
            <ellipse cx="-6" cy="0" rx="9" ry="12" fill="#38bdf8" opacity="0.85"/>
            <ellipse cx="6" cy="0" rx="9" ry="12" fill="#f43f5e" opacity="0.85"/>
            <text x="0" y="4" fill="#f8fafc" font-size="10" font-weight="900" text-anchor="middle">2n=46</text>
            <text x="0" y="-58" fill="#34d399" font-size="10" font-weight="800" text-anchor="middle">Diploid Zygote</text>
            <text x="0" y="68" fill="#a7f3d0" font-size="9" font-weight="700" text-anchor="middle">Unique Genetic Blend!</text>
          </g>

          <!-- Diversity Recombination Banner -->
          <rect x="40" y="245" width="460" height="60" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.2"/>
          <text x="270" y="268" fill="#f8fafc" font-size="10.5" font-weight="700" text-anchor="middle">Why Sexual Reproduction is Crucial: Shuffles genes from 2 distinct parents,</text>
          <text x="270" y="286" fill="#4ade80" font-size="9.5" text-anchor="middle">creating offspring with novel traits, disease resistance, and evolutionary adaptability!</text>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnFertilize">💥 Trigger Fertilization Animation</button>
          <button class="sim-btn" id="btnShuffleAlleles">🧬 Shuffle Genetic Trait Combinations</button>
        </div>
      `;

      document.getElementById('btnFertilize').addEventListener('click', () => {
        const sperm = document.getElementById('spermCell');
        sperm.setAttribute('transform', 'translate(210, 150)');
        sfx.playCorrect();
        setTimeout(() => {
          sperm.setAttribute('transform', 'translate(100, 150)');
        }, 1200);
      });

      document.getElementById('btnShuffleAlleles').addEventListener('click', () => {
        sfx.playClick();
      });
    }

    // Slide 12: Reproduction: The Generational Bridge (4-Billion-Year Continuum)
    function simReproductionContinuity() {
      simHeaderTitle.textContent = "The 4-Billion-Year Unbroken Chain of Reproduction";

      simCanvas.innerHTML = `
        <svg id="timelineSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Deep Time Spiral / Line -->
          <line x1="40" y1="165" x2="500" y2="165" stroke="#38bdf8" stroke-width="4" stroke-linecap="round"/>

          <!-- Milestone Nodes along the 4 Billion Year Chain -->
          <!-- 3.8 Ga: LUCA / First Microbial Cells -->
          <g id="nodeLuca" transform="translate(60, 165)">
            <circle cx="0" cy="0" r="14" fill="#0284c7" stroke="#38bdf8" stroke-width="2"/>
            <text x="0" y="5" font-size="10" text-anchor="middle">🦠</text>
            <text x="0" y="-24" fill="#38bdf8" font-size="9" font-weight="800" text-anchor="middle">3.8 Ga</text>
            <text x="0" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">First Life (LUCA)</text>
          </g>

          <!-- 2.4 Ga: Great Oxidation Event (Cyanobacteria) -->
          <g id="nodeOxy" transform="translate(150, 165)">
            <circle cx="0" cy="0" r="14" fill="#15803d" stroke="#4ade80" stroke-width="2"/>
            <text x="0" y="5" font-size="10" text-anchor="middle">🌱</text>
            <text x="0" y="-24" fill="#4ade80" font-size="9" font-weight="800" text-anchor="middle">2.4 Ga</text>
            <text x="0" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">Oxygen Rush</text>
          </g>

          <!-- 540 Ma: Cambrian Explosion -->
          <g id="nodeCambrian" transform="translate(250, 165)">
            <circle cx="0" cy="0" r="14" fill="#b45309" stroke="#fbbf24" stroke-width="2"/>
            <text x="0" y="5" font-size="10" text-anchor="middle">🦐</text>
            <text x="0" y="-24" fill="#fbbf24" font-size="9" font-weight="800" text-anchor="middle">540 Ma</text>
            <text x="0" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">Cambrian Surge</text>
          </g>

          <!-- 230 Ma: Age of Reptiles & Dinosaurs -->
          <g id="nodeDino" transform="translate(350, 165)">
            <circle cx="0" cy="0" r="14" fill="#991b1b" stroke="#f87171" stroke-width="2"/>
            <text x="0" y="5" font-size="10" text-anchor="middle">🦕</text>
            <text x="0" y="-24" fill="#f87171" font-size="9" font-weight="800" text-anchor="middle">230 Ma</text>
            <text x="0" y="32" fill="#94a3b8" font-size="8" text-anchor="middle">Dinosaurs</text>
          </g>

          <!-- Present Day: Modern Humans & Living Earth -->
          <g id="nodePresent" transform="translate(460, 165)">
            <circle cx="0" cy="0" r="18" fill="#059669" stroke="#34d399" stroke-width="3"/>
            <text x="0" y="6" font-size="12" text-anchor="middle">🌍</text>
            <text x="0" y="-28" fill="#34d399" font-size="10" font-weight="900" text-anchor="middle">Present</text>
            <text x="0" y="36" fill="#a7f3d0" font-size="8.5" font-weight="700" text-anchor="middle">8.7M Species</text>
          </g>

          <!-- Continuity Message Banner -->
          <g transform="translate(50, 240)">
            <rect x="0" y="0" width="440" height="65" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1.5" id="continuityBox"/>
            <text id="lblContTitle" x="220" y="24" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Unbroken Continuum of Hereditary Information</text>
            <text id="lblContDesc" x="220" y="44" fill="#cbd5e1" font-size="9.5" text-anchor="middle">Every living organism alive today is linked to 3.8-billion-year-old ancestors through reproduction!</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.6rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnShowContinuity">🔗 Unbroken Chain: Continuous Life</button>
          <button class="sim-btn" id="btnSimExtinction">⚠️ Simulate Reproductive Failure (Extinction)</button>
        </div>
      `;

      document.getElementById('btnShowContinuity').addEventListener('click', () => {
        document.getElementById('btnShowContinuity').classList.add('active');
        document.getElementById('btnSimExtinction').classList.remove('active');
        document.getElementById('continuityBox').setAttribute('stroke', '#38bdf8');
        document.getElementById('lblContTitle').textContent = "Unbroken Continuum of Hereditary Information";
        document.getElementById('lblContTitle').setAttribute('fill', '#38bdf8');
        document.getElementById('lblContDesc').textContent = "Every living organism alive today is linked to 3.8-billion-year-old ancestors through reproduction!";
        sfx.playCorrect();
      });

      document.getElementById('btnSimExtinction').addEventListener('click', () => {
        document.getElementById('btnSimExtinction').classList.add('active');
        document.getElementById('btnShowContinuity').classList.remove('active');
        document.getElementById('continuityBox').setAttribute('stroke', '#ef4444');
        document.getElementById('lblContTitle').textContent = "EXTINCTION: When Reproduction Ceases";
        document.getElementById('lblContTitle').setAttribute('fill', '#ef4444');
        document.getElementById('lblContDesc').textContent = "If death rate permanently exceeds reproduction rate, a species vanishes forever. No second chance!";
        sfx.playIncorrect();
      });
    }

    // Slide 13: Enhanced Greenhouse Effect & Cryosphere Retreat
    function simGreenhouseGlobalWarming() {
      simHeaderTitle.textContent = "Enhanced Greenhouse Warming & Himalayan Cryosphere Melting Simulator";
      let co2Val = 420;

      simCanvas.innerHTML = `
        <svg id="warmingSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#020617"/>

          <!-- Sky with Enhanced Infrared Trapping Arrows -->
          <rect x="20" y="20" width="500" height="150" fill="#0f172a"/>
          <g id="warmingIrRays">
            <!-- Dynamically populated heat vectors -->
          </g>

          <!-- Himalayan Mountain Peak with Glacial Ice Cap -->
          <polygon points="120,70 20,270 220,270" fill="#334155"/>
          <!-- Snow & Glacier Cap -->
          <polygon id="glacierCap" points="120,70 70,170 170,170" fill="#f8fafc" stroke="#bae6fd" stroke-width="1.5"/>
          <text x="120" y="105" fill="#0369a1" font-size="9" font-weight="800" text-anchor="middle">Glacial Ice</text>

          <!-- Lowland Coastal Plain & Rising Ocean -->
          <polygon points="220,270 340,240 520,270 520,310 20,310 20,270" fill="#15803d"/>
          <!-- Coastal Water -->
          <rect id="seaLevelRect" x="340" y="255" width="180" height="55" fill="#0284c7" opacity="0.8"/>
          <text id="lblSeaLevel" x="430" y="280" fill="#e0f2fe" font-size="9" font-weight="700">Sea Level: Baseline</text>

          <!-- Climate Dashboard HUD -->
          <g transform="translate(320, 30)">
            <rect x="0" y="0" width="190" height="135" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#f59e0b" stroke-width="1.5" id="climateHudBox"/>
            <text x="95" y="22" fill="#fbbf24" font-size="11" font-weight="800" text-anchor="middle">Climate Crisis Gauges</text>
            <line x1="10" y1="30" x2="180" y2="30" stroke="rgba(255,255,255,0.15)"/>
            
            <text x="10" y="50" fill="#94a3b8" font-size="9">CO₂ Concentration: <tspan id="hudCo2" fill="#f59e0b" font-weight="800">420 ppm</tspan></text>
            <text x="10" y="70" fill="#94a3b8" font-size="9">Global Temp Rise: <tspan id="hudTemp" fill="#ef4444" font-weight="800">+1.2°C</tspan></text>
            <text x="10" y="90" fill="#94a3b8" font-size="9">Glacier Mass Balance: <tspan id="hudGlacier" fill="#38bdf8" font-weight="700">-28% Shrinkage</tspan></text>
            
            <rect x="8" y="102" width="174" height="22" rx="4" fill="rgba(239, 68, 68, 0.2)" id="hudAlertPill"/>
            <text id="lblClimateAlert" x="95" y="117" fill="#f87171" font-size="8" font-weight="800" text-anchor="middle">ELEVATED WARMING DETECTED</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.5rem; align-items:center; width:100%;">
          <div style="display:flex; align-items:center; gap:0.8rem; width:80%; max-width:480px;">
            <span style="font-size:0.85rem; font-weight:700; color:#fbbf24; white-space:nowrap;">CO₂ Level:</span>
            <input type="range" id="sliderCo2" min="280" max="600" step="10" value="420" style="flex:1;">
            <span id="txtCo2" style="font-size:0.9rem; font-weight:800; color:#f8fafc; min-width:60px;">420 ppm</span>
          </div>
          <div style="display:flex; gap:0.5rem; justify-content:center; flex-wrap:wrap;">
            <button class="sim-btn" id="btnCo2_1850">Pre-Industrial (280 ppm)</button>
            <button class="sim-btn active" id="btnCo2_2026">Current Era (420 ppm)</button>
            <button class="sim-btn" id="btnCo2_2080">Runaway Projection (560 ppm)</button>
          </div>
        </div>
      `;

      function updateClimate(val) {
        co2Val = parseInt(val);
        document.getElementById('txtCo2').textContent = co2Val + ' ppm';

        const hudCo2 = document.getElementById('hudCo2');
        const hudTemp = document.getElementById('hudTemp');
        const hudGlacier = document.getElementById('hudGlacier');
        const hudAlertPill = document.getElementById('hudAlertPill');
        const lblClimateAlert = document.getElementById('lblClimateAlert');
        const glacierCap = document.getElementById('glacierCap');
        const seaLevelRect = document.getElementById('seaLevelRect');
        const lblSeaLevel = document.getElementById('lblSeaLevel');
        const climateHudBox = document.getElementById('climateHudBox');

        hudCo2.textContent = `${co2Val} ppm`;

        // Calculate metrics
        // Temp rise = (co2 - 280) * (3.0 / 280) roughly
        const tRise = Math.max(0, ((co2Val - 280) * 0.009)).toFixed(1);
        hudTemp.textContent = `+${tRise}°C`;

        if (co2Val <= 290) {
          hudTemp.textContent = "+0.0°C (Baseline)";
          hudGlacier.textContent = "Stable Equilibrium";
          hudGlacier.setAttribute('fill', '#4ade80');
          hudAlertPill.setAttribute('fill', 'rgba(16, 185, 129, 0.2)');
          lblClimateAlert.textContent = "PRE-INDUSTRIAL CLIMATE STABILITY";
          lblClimateAlert.setAttribute('fill', '#34d399');
          climateHudBox.setAttribute('stroke', '#10b981');
          glacierCap.setAttribute('points', '120,70 60,190 180,190'); // full thick glacier
          seaLevelRect.setAttribute('y', '265');
          seaLevelRect.setAttribute('height', '45');
          lblSeaLevel.textContent = "Sea Level: Historic Normal";
        } else if (co2Val < 480) {
          hudGlacier.textContent = "-28% Glacial Loss";
          hudGlacier.setAttribute('fill', '#f59e0b');
          hudAlertPill.setAttribute('fill', 'rgba(245, 158, 11, 0.2)');
          lblClimateAlert.textContent = "MODERATE CRYOSPHERE RETREAT";
          lblClimateAlert.setAttribute('fill', '#fbbf24');
          climateHudBox.setAttribute('stroke', '#f59e0b');
          glacierCap.setAttribute('points', '120,70 75,160 165,160'); // partially melted
          seaLevelRect.setAttribute('y', '255');
          seaLevelRect.setAttribute('height', '55');
          lblSeaLevel.textContent = "Sea Level: +22 cm Rise";
        } else {
          hudGlacier.textContent = "-75% SEVERE COLLAPSE";
          hudGlacier.setAttribute('fill', '#ef4444');
          hudAlertPill.setAttribute('fill', 'rgba(239, 68, 68, 0.3)');
          lblClimateAlert.textContent = "CRITICAL: FLOODS & SEA LEVEL SURGE";
          lblClimateAlert.setAttribute('fill', '#f87171');
          climateHudBox.setAttribute('stroke', '#ef4444');
          glacierCap.setAttribute('points', '120,70 100,120 140,120'); // tiny sliver left
          seaLevelRect.setAttribute('y', '240'); // flooding plains
          seaLevelRect.setAttribute('height', '70');
          lblSeaLevel.textContent = "Sea Level: +1.2 m COASTAL INUNDATION";
        }
      }

      const sliderCo2 = document.getElementById('sliderCo2');
      sliderCo2.addEventListener('input', (e) => {
        updateClimate(e.target.value);
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
      });

      document.getElementById('btnCo2_1850').addEventListener('click', () => {
        sliderCo2.value = 280;
        updateClimate(280);
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnCo2_1850').classList.add('active');
        sfx.playClick();
      });

      document.getElementById('btnCo2_2026').addEventListener('click', () => {
        sliderCo2.value = 420;
        updateClimate(420);
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnCo2_2026').classList.add('active');
        sfx.playCorrect();
      });

      document.getElementById('btnCo2_2080').addEventListener('click', () => {
        sliderCo2.value = 560;
        updateClimate(560);
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));
        document.getElementById('btnCo2_2080').classList.add('active');
        sfx.playIncorrect();
      });

      updateClimate(420);
    }

    // Slide 14: Deforestation & Habitat Fragmentation Laboratory
    function simDeforestationBiodiversityLoss() {
      simHeaderTitle.textContent = "Deforestation, Habitat Fragmentation & Biodiversity Threat Laboratory";
      let canopyPct = 80;

      simCanvas.innerHTML = `
        <svg id="deforestSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- River dividing habitat -->
          <path d="M 270,30 Q 250,150 280,310" stroke="#0284c7" stroke-width="24" fill="none"/>
          <text x="275" y="50" fill="#bae6fd" font-size="8" font-weight="700">Riparian River</text>

          <!-- Forest Ground Landscape -->
          <rect x="20" y="30" width="230" height="270" rx="8" fill="#14532d" id="leftForestBase"/>
          <rect x="290" y="30" width="230" height="270" rx="8" fill="#14532d" id="rightForestBase"/>

          <!-- Dynamic Trees Group -->
          <g id="treesDisplayGroup">
            <!-- Injected via script -->
          </g>

          <!-- Wildlife Icons -->
          <g id="wildlifeGroup">
            <text x="60" y="100" font-size="18" id="wl1">🐅</text>
            <text x="140" y="180" font-size="18" id="wl2">🐘</text>
            <text x="80" y="240" font-size="16" id="wl3">🦌</text>
            <text x="350" y="120" font-size="16" id="wl4">🦜</text>
            <text x="420" y="220" font-size="16" id="wl5">🐒</text>
          </g>

          <!-- Threat Meter Overlay Card -->
          <g transform="translate(180, 240)">
            <rect x="0" y="0" width="180" height="65" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5" id="iucnCard"/>
            <text x="90" y="20" fill="#f8fafc" font-size="10" font-weight="800" text-anchor="middle">IUCN Extinction Vulnerability</text>
            <rect x="12" y="30" width="156" height="22" rx="4" fill="rgba(16, 185, 129, 0.2)" id="iucnPill"/>
            <text id="lblIucnStatus" x="90" y="45" fill="#34d399" font-size="9" font-weight="900" text-anchor="middle">LEAST CONCERN (STABLE)</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-direction:column; gap:0.5rem; align-items:center; width:100%;">
          <div style="display:flex; align-items:center; gap:0.8rem; width:80%; max-width:480px;">
            <span style="font-size:0.85rem; font-weight:700; color:#4ade80; white-space:nowrap;">Forest Canopy Cover:</span>
            <input type="range" id="sliderCanopy" min="20" max="100" step="10" value="80" style="flex:1;">
            <span id="txtCanopy" style="font-size:0.9rem; font-weight:800; color:#f8fafc; min-width:50px;">80%</span>
          </div>
          <button class="sim-btn" id="btnReforestDrive">🌲 Undertake Mass Afforestation & Corridors</button>
        </div>
      `;

      function renderCanopy(pct) {
        canopyPct = parseInt(pct);
        document.getElementById('txtCanopy').textContent = canopyPct + '%';

        const tg = document.getElementById('treesDisplayGroup');
        tg.innerHTML = '';

        const treeCount = Math.round(canopyPct / 4); // 5 to 25 trees
        for (let i = 0; i < treeCount; i++) {
          const side = Math.random() > 0.5 ? 'left' : 'right';
          const x = side === 'left' ? 40 + Math.random() * 180 : 310 + Math.random() * 180;
          const y = 50 + Math.random() * 220;
          tg.innerHTML += `<text x="${x}" y="${y}" font-size="18">🌳</text>`;
        }

        const iucnCard = document.getElementById('iucnCard');
        const iucnPill = document.getElementById('iucnPill');
        const lblIucnStatus = document.getElementById('lblIucnStatus');
        const wlGroup = document.getElementById('wildlifeGroup');

        if (canopyPct >= 70) {
          iucnCard.setAttribute('stroke', '#10b981');
          iucnPill.setAttribute('fill', 'rgba(16, 185, 129, 0.25)');
          lblIucnStatus.textContent = "LEAST CONCERN (HABITAT INTACT)";
          lblIucnStatus.setAttribute('fill', '#34d399');
          wlGroup.style.opacity = '1';
        } else if (canopyPct >= 45) {
          iucnCard.setAttribute('stroke', '#f59e0b');
          iucnPill.setAttribute('fill', 'rgba(245, 158, 11, 0.25)');
          lblIucnStatus.textContent = "VULNERABLE (FRAGMENTED)";
          lblIucnStatus.setAttribute('fill', '#fbbf24');
          wlGroup.style.opacity = '0.6';
        } else {
          iucnCard.setAttribute('stroke', '#ef4444');
          iucnPill.setAttribute('fill', 'rgba(239, 68, 68, 0.3)');
          lblIucnStatus.textContent = "CRITICALLY ENDANGERED";
          lblIucnStatus.setAttribute('fill', '#f87171');
          wlGroup.style.opacity = '0.2';
        }
      }

      document.getElementById('sliderCanopy').addEventListener('input', (e) => {
        renderCanopy(e.target.value);
      });

      document.getElementById('btnReforestDrive').addEventListener('click', () => {
        document.getElementById('sliderCanopy').value = 90;
        renderCanopy(90);
        sfx.playCorrect();
      });

      renderCanopy(80);
    }

    // Slide 15: Triple Environmental Threat: Air, Water & Soil Pollution
    function simPollutionThreats() {
      simHeaderTitle.textContent = "Anthropogenic Pollution: Air, Water & Soil Impact Inspector";
      let activePollution = 'air';

      simCanvas.innerHTML = `
        <svg id="pollutionSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#0f172a"/>

          <!-- Dynamic Pollution Mode Graphics -->
          <g id="pollutionGraphicsGroup">
            <!-- Injected via script -->
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnPollAir">💨 1. Air Smog & PM2.5</button>
          <button class="sim-btn" id="btnPollWater">🌊 2. Water Eutrophication & Plastic</button>
          <button class="sim-btn" id="btnPollSoil">🪨 3. Soil Toxins & Pesticides</button>
          <button class="sim-btn" id="btnDeployCleanup">🌱 Deploy Advanced Eco-Treatment</button>
        </div>
      `;

      function renderPollution(type) {
        activePollution = type;
        const g = document.getElementById('pollutionGraphicsGroup');
        simControls.querySelectorAll('.sim-btn').forEach(b => b.classList.remove('active'));

        if (type === 'air') {
          document.getElementById('btnPollAir').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#f87171" font-size="13" font-weight="800" text-anchor="middle">Air Pollution: Industrial Chimneys, PM2.5 & Acid Rain</text>
            
            <!-- Factory Chimney -->
            <rect x="80" y="140" width="50" height="130" fill="#334155"/>
            <polygon points="70,140 140,140 130,120 80,120" fill="#1e293b"/>
            <!-- Dark smog plume -->
            <path d="M 105,120 Q 90,60 160,50 Q 260,30 380,60 Q 480,80 500,120" stroke="#71717a" stroke-width="25" fill="none" opacity="0.75" stroke-linecap="round"/>
            <text x="180" y="75" fill="#fecaca" font-size="9" font-weight="700">SO₂, NOₓ, PM₂.₅ & Carbon Monoxide (CO)</text>

            <!-- Acid Rain Droplets falling on Forest -->
            <g opacity="0.8">
              <line x1="320" y1="100" x2="310" y2="150" stroke="#f87171" stroke-width="2" stroke-dasharray="4,4"/>
              <line x1="380" y1="90" x2="370" y2="140" stroke="#f87171" stroke-width="2" stroke-dasharray="4,4"/>
              <line x1="440" y1="110" x2="430" y2="160" stroke="#f87171" stroke-width="2" stroke-dasharray="4,4"/>
              <text x="360" y="170" fill="#f87171" font-size="9" font-weight="800">Acid Rain (H₂SO₄ / HNO₃)</text>
            </g>

            <!-- City ground -->
            <rect x="20" y="270" width="500" height="40" fill="#1e293b"/>
            <text x="40" y="295" fill="#94a3b8" font-size="9">Respiratory diseases: Asthma, Bronchitis, Cardiovascular stress in children & seniors</text>
          `;
        } else if (type === 'water') {
          document.getElementById('btnPollWater').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#38bdf8" font-size="13" font-weight="800" text-anchor="middle">Water Pollution: Chemical Effluents, Plastic Gyres & Eutrophication</text>
            
            <!-- Water Body with Toxic Algal Bloom Blanket -->
            <rect x="30" y="60" width="480" height="190" rx="8" fill="#047857" opacity="0.85"/>
            <text x="270" y="90" fill="#bbf7d0" font-size="11" font-weight="800" text-anchor="middle">Dense Algal Bloom (Eutrophication from Fertilizer Runoff)</text>

            <!-- Asphyxiating fish -->
            <text x="120" y="150" font-size="20">🐟</text>
            <text x="120" y="180" fill="#fca5a5" font-size="8.5" font-weight="700">Hypoxia (Zero Dissolved O₂)</text>

            <!-- Plastic debris -->
            <g transform="translate(300, 130)">
              <text x="0" y="0" font-size="18">🧴</text>
              <text x="40" y="15" font-size="16">🛍️</text>
              <text x="80" y="-5" font-size="18">🥤</text>
              <text x="20" y="40" fill="#fde047" font-size="8.5">Breaks into Microplastics (<5mm)</text>
            </g>

            <rect x="30" y="260" width="480" height="45" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1"/>
            <text x="270" y="285" fill="#f8fafc" font-size="9.5" text-anchor="middle">Bioaccumulation: Microplastics and heavy metals concentrate up the food web to human diners!</text>
          `;
        } else if (type === 'soil') {
          document.getElementById('btnPollSoil').classList.add('active');
          g.innerHTML = `
            <text x="270" y="30" fill="#fbbf24" font-size="13" font-weight="800" text-anchor="middle">Soil Contamination: Non-Biodegradable Waste & Toxic Agrochemicals</text>
            
            <!-- Soil cross section with garbage & chemicals -->
            <rect x="40" y="60" width="460" height="190" rx="8" fill="#451a03" stroke="#78350f" stroke-width="1.5"/>
            
            <!-- Chemical Barrels Leaking -->
            <g transform="translate(100, 100)">
              <rect x="0" y="0" width="40" height="50" rx="4" fill="#f59e0b" stroke="#b45309" stroke-width="2"/>
              <text x="20" y="28" font-size="14" text-anchor="middle">☣️</text>
              <path d="M 20,50 Q 25,80 30,110" stroke="#84cc16" stroke-width="6" fill="none"/>
              <text x="50" y="90" fill="#bef264" font-size="8.5" font-weight="700">Persistent Pesticide Leaching</text>
            </g>

            <!-- Perishing beneficial soil fauna -->
            <g transform="translate(320, 120)">
              <text x="0" y="0" font-size="16">🪱</text>
              <text x="0" y="25" fill="#fca5a5" font-size="8.5" font-weight="700">Earthworm Mortality</text>
              <text x="0" y="55" font-size="16">🗑️ 📦</text>
              <text x="0" y="80" fill="#cbd5e1" font-size="8.5">Landfill Plastic Leachate</text>
            </g>

            <rect x="40" y="260" width="460" height="45" rx="6" fill="rgba(15, 23, 42, 0.95)" stroke="#fbbf24" stroke-width="1"/>
            <text x="270" y="285" fill="#f8fafc" font-size="9.5" text-anchor="middle">Loss of Soil Fertility: Destroys nitrogen-fixing rhizobia bacteria, salinizes fertile cropland.</text>
          `;
        }
        sfx.playClick();
      }

      document.getElementById('btnPollAir').addEventListener('click', () => renderPollution('air'));
      document.getElementById('btnPollWater').addEventListener('click', () => renderPollution('water'));
      document.getElementById('btnPollSoil').addEventListener('click', () => renderPollution('soil'));

      document.getElementById('btnDeployCleanup').addEventListener('click', () => {
        const g = document.getElementById('pollutionGraphicsGroup');
        g.innerHTML = `
          <text x="270" y="40" fill="#4ade80" font-size="14" font-weight="800" text-anchor="middle">✨ Eco-Restoration & Clean Technologies Active!</text>
          
          <rect x="60" y="70" width="420" height="160" rx="10" fill="rgba(6, 78, 59, 0.85)" stroke="#10b981" stroke-width="2"/>
          <text x="270" y="105" fill="#a7f3d0" font-size="12" font-weight="800" text-anchor="middle">Triple Remediation In Progress:</text>
          <text x="270" y="130" fill="#f8fafc" font-size="10" text-anchor="middle">💨 Air: Wet scrubbers & electrostatic precipitators capture 99% PM2.5</text>
          <text x="270" y="155" fill="#f8fafc" font-size="10" text-anchor="middle">🌊 Water: Effluent Treatment Plants (ETP) & constructed wetlands purify water</text>
          <text x="270" y="180" fill="#f8fafc" font-size="10" text-anchor="middle">🪨 Soil: Bioremediation with hyperaccumulating plants & vermicomposting</text>

          <rect x="60" y="245" width="420" height="50" rx="8" fill="rgba(15, 23, 42, 0.95)" stroke="#38bdf8" stroke-width="1"/>
          <text x="270" y="275" fill="#38bdf8" font-size="10" font-weight="700" text-anchor="middle">Ecosystem Recovery: Clean air returns, aquatic dissolved O₂ normalizes!</text>
        `;
        sfx.playCorrect();
      });

      renderPollution('air');
    }

    // Slide 16: Ecological Healing & Sustainable Living Dashboard
    function simEcologicalHealingConservation() {
      simHeaderTitle.textContent = "Planetary Restoration & Circular Sustainability Dashboard";
      
      let state = {
        renewables: true,
        reforest: true,
        rainwater: true,
        circular: true
      };

      simCanvas.innerHTML = `
        <svg id="sustainSvg" viewBox="0 0 540 330" width="100%" height="100%">
          <rect x="0" y="0" width="540" height="330" fill="#030712"/>

          <!-- Eco Landscape Background -->
          <rect x="20" y="20" width="500" height="150" fill="#0c4a6e" opacity="0.6"/>
          <!-- Clean Sun with Solar Rays -->
          <circle cx="80" cy="50" r="22" fill="#fbbf24"/>

          <!-- Wind Turbines -->
          <g transform="translate(180, 70)">
            <line x1="0" y1="0" x2="0" y2="70" stroke="#cbd5e1" stroke-width="3"/>
            <!-- Rotor Blades -->
            <line x1="0" y1="0" x2="-25" y2="-20" stroke="#f8fafc" stroke-width="2"/>
            <line x1="0" y1="0" x2="25" y2="-20" stroke="#f8fafc" stroke-width="2"/>
            <line x1="0" y1="0" x2="0" y2="30" stroke="#f8fafc" stroke-width="2"/>
          </g>
          <g transform="translate(240, 85)">
            <line x1="0" y1="0" x2="0" y2="55" stroke="#cbd5e1" stroke-width="2.5"/>
            <line x1="0" y1="0" x2="-20" y2="-15" stroke="#f8fafc" stroke-width="1.8"/>
            <line x1="0" y1="0" x2="20" y2="-15" stroke="#f8fafc" stroke-width="1.8"/>
          </g>

          <!-- Solar Photovoltaic Rooftop Grid -->
          <g transform="translate(60, 110)">
            <polygon points="0,30 40,0 100,0 60,30" fill="#1e3a8a" stroke="#38bdf8" stroke-width="1.5"/>
            <line x1="20" y1="20" x2="80" y2="20" stroke="#60a5fa" stroke-width="1"/>
            <text x="50" y="45" fill="#93c5fd" font-size="8" font-weight="700">Solar Grid</text>
          </g>

          <!-- Rolling Green Canopy & Clean River -->
          <path d="M 20,170 Q 150,140 280,165 Q 400,150 520,170 L 520,310 L 20,310 Z" fill="#15803d"/>
          <!-- Pristine River Stream with Rainwater Recharge Well -->
          <path d="M 320,165 Q 350,220 380,310 L 440,310 Q 400,220 370,165 Z" fill="#0284c7"/>
          <text x="390" y="240" fill="#bae6fd" font-size="8.5" font-weight="700">Living River</text>

          <!-- Trees & Animals -->
          <text x="140" y="200" font-size="18">🌳</text>
          <text x="170" y="220" font-size="18">🌲</text>
          <text x="210" y="240" font-size="18">🌳</text>
          <text x="260" y="210" font-size="16">🦌</text>
          <text x="290" y="250" font-size="16">🐅</text>

          <!-- Dynamic Planetary Health Meter Gauge -->
          <g transform="translate(340, 30)">
            <rect x="0" y="0" width="170" height="110" rx="10" fill="rgba(15, 23, 42, 0.95)" stroke="#10b981" stroke-width="1.5" id="healthHudBox"/>
            <text x="85" y="22" fill="#38bdf8" font-size="11" font-weight="800" text-anchor="middle">Earth Health Index</text>
            <line x1="10" y1="28" x2="160" y2="28" stroke="rgba(255,255,255,0.1)"/>

            <text x="12" y="48" fill="#94a3b8" font-size="9">Regeneration Score:</text>
            <text id="txtHealthScore" x="12" y="68" fill="#4ade80" font-size="18" font-weight="900">95%</text>

            <rect x="10" y="80" width="150" height="18" rx="4" fill="rgba(16, 185, 129, 0.25)" id="healthStatusBox"/>
            <text id="lblHealthStatus" x="85" y="93" fill="#34d399" font-size="8" font-weight="800" text-anchor="middle">THRIVING REGENERATIVE BIOSPHERE</text>
          </g>
        </svg>
      `;

      simControls.innerHTML = `
        <div style="display:flex; flex-wrap:wrap; gap:0.5rem; justify-content:center; align-items:center;">
          <button class="sim-btn active" id="btnTogRenewable">☀️ Wind & Solar Grid</button>
          <button class="sim-btn active" id="btnTogForest">🌲 Mass Afforestation</button>
          <button class="sim-btn active" id="btnTogRainwater">💧 Rainwater Watersheds</button>
          <button class="sim-btn active" id="btnTogCircular">♻️ Zero-Waste Circular Economy</button>
        </div>
      `;

      function updateHealth() {
        let score = 20;
        if (state.renewables) score += 20;
        if (state.reforest) score += 20;
        if (state.rainwater) score += 20;
        if (state.circular) score += 20;

        const txtHealthScore = document.getElementById('txtHealthScore');
        const healthStatusBox = document.getElementById('healthStatusBox');
        const lblHealthStatus = document.getElementById('lblHealthStatus');
        const healthHudBox = document.getElementById('healthHudBox');

        txtHealthScore.textContent = score + '%';

        if (score >= 80) {
          txtHealthScore.setAttribute('fill', '#4ade80');
          healthHudBox.setAttribute('stroke', '#10b981');
          healthStatusBox.setAttribute('fill', 'rgba(16, 185, 129, 0.25)');
          lblHealthStatus.textContent = "THRIVING REGENERATIVE BIOSPHERE";
          lblHealthStatus.setAttribute('fill', '#34d399');
        } else if (score >= 50) {
          txtHealthScore.setAttribute('fill', '#fbbf24');
          healthHudBox.setAttribute('stroke', '#f59e0b');
          healthStatusBox.setAttribute('fill', 'rgba(245, 158, 11, 0.25)');
          lblHealthStatus.textContent = "MODERATE PARTIAL RECOVERY";
          lblHealthStatus.setAttribute('fill', '#fbbf24');
        } else {
          txtHealthScore.setAttribute('fill', '#ef4444');
          healthHudBox.setAttribute('stroke', '#ef4444');
          healthStatusBox.setAttribute('fill', 'rgba(239, 68, 68, 0.3)');
          lblHealthStatus.textContent = "CRITICAL ECOLOGICAL DEFICIT";
          lblHealthStatus.setAttribute('fill', '#f87171');
        }
      }

      document.getElementById('btnTogRenewable').addEventListener('click', (e) => {
        state.renewables = !state.renewables;
        e.target.classList.toggle('active', state.renewables);
        updateHealth();
        sfx.playClick();
      });

      document.getElementById('btnTogForest').addEventListener('click', (e) => {
        state.reforest = !state.reforest;
        e.target.classList.toggle('active', state.reforest);
        updateHealth();
        sfx.playClick();
      });

      document.getElementById('btnTogRainwater').addEventListener('click', (e) => {
        state.rainwater = !state.rainwater;
        e.target.classList.toggle('active', state.rainwater);
        updateHealth();
        sfx.playClick();
      });

      document.getElementById('btnTogCircular').addEventListener('click', (e) => {
        state.circular = !state.circular;
        e.target.classList.toggle('active', state.circular);
        updateHealth();
        sfx.playClick();
      });

      updateHealth();
    }
"""

