#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 13 Part 3 Data Generator (Slides 17-20)
Chapter Title: Earth as a System: Energy, Matter, and Life
Strict constraints:
- All slide titles 1-3 words
- Speech word count = 0 (Silent Exercises)
- 10 Challenge Questions per slide (40 questions total)
- 4 options each, answer index, hint, explanation, and 3-step solution walkthrough
- Zero forbidden character names or persona titles
"""

slides_part3 = [
    {
        "id": 17,
        "title": "Spheres & Radiation",
        "subtitle": "Challenge Quiz: Earth Spheres, Solar Radiation & Insolation",
        "speech": "",
        "questions": [
            {
                "question": "Which of the following correctly pairs an Earth sphere with its primary reservoir in the Indian subcontinent?",
                "options": [
                    "Geosphere — Ganga-Brahmaputra river basin",
                    "Cryosphere — Siachen and Gangotri glaciers",
                    "Hydrosphere — Deccan plateau basalt traps",
                    "Atmosphere — Sundarban mangrove ecosystems"
                ],
                "answer": 1,
                "hint": "Identify the sphere composed of frozen ice and snow.",
                "explanation": "Siachen and Gangotri glaciers represent prime reservoirs of the cryosphere, storing frozen freshwater that feeds northern river basins.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Review the 5 spheres: Geosphere (solid rocks/soil), Hydrosphere (liquid water), Cryosphere (frozen ice/snow), Atmosphere (air), and Biosphere (living organisms).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Glaciers like Siachen and Gangotri in the Himalayas belong strictly to the cryosphere as solid-phase water storage.",
                    "Step 3: Verification & Environmental Equilibrium — Options A, C, and D mismatch rivers to geosphere, basalt to hydrosphere, and mangroves to atmosphere. Hence, option B is correct."
                ]
            },
            {
                "question": "What is the speed of solar electromagnetic waves traveling through the vacuum of space toward Earth?",
                "options": [
                    "3 × 10⁶ m s⁻¹",
                    "3 × 10⁸ m s⁻¹",
                    "1.4 × 10³ m s⁻¹",
                    "3 × 10¹⁰ m s⁻¹"
                ],
                "answer": 1,
                "hint": "Recall the fundamental universal constant for the speed of light in a vacuum.",
                "explanation": "All electromagnetic radiation, including sunlight, travels through a vacuum at the speed of light: approximately 3 × 10⁸ m s⁻¹ (or 300,000 km s⁻¹).",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Solar radiation propagates as electromagnetic waves through interplanetary vacuum space.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — In vacuum, Maxwell's electromagnetic equations dictate that phase velocity c = 1/√(ε₀μ₀) ≈ 3.0 × 10⁸ m s⁻¹.",
                    "Step 3: Verification & Environmental Equilibrium — Crossing the ~1.5 × 10¹¹ m Earth-Sun astronomical distance takes roughly 500 seconds (8 minutes 20 seconds) at 3 × 10⁸ m s⁻¹."
                ]
            },
            {
                "question": "Approximately what percentage of solar energy incident on Earth falls within the UV, visible, and infrared bands combined?",
                "options": ["50%", "75%", "90%", "99%"],
                "answer": 3,
                "hint": "The Sun's emission peaks strongly between 100 nm and 3000 nm, encompassing these three bands.",
                "explanation": "Nearly 99% of total solar irradiance incident on top of the atmosphere is concentrated in the ultraviolet, visible, and near-infrared spectra.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Examine Planck's blackbody distribution for a solar photosphere at approximately 5778 K.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — The spectral emission curve peaks in the visible (~500 nm) and tapers into UV and infrared, with 99% falling between 100 nm and 4000 nm.",
                    "Step 3: Verification & Environmental Equilibrium — Negligible energy (<1%) resides in extreme radio, microwave, X-ray, or gamma-ray bands."
                ]
            },
            {
                "question": "What is the wavelength range characteristic of ultraviolet (UV) radiation?",
                "options": [
                    "100 nm to 400 nm",
                    "400 nm to 700 nm",
                    "700 nm to 1 mm",
                    "1 mm to 1 m"
                ],
                "answer": 0,
                "hint": "UV rays have wavelengths just shorter than visible violet light (400 nm).",
                "explanation": "Ultraviolet radiation spans wavelengths from 100 nm to 400 nm, subdivided into UV-A, UV-B, and UV-C.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Identify boundaries of the electromagnetic spectrum relative to visible violet light (λ ≈ 400 nm).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Ultraviolet radiation extends from 100 nm up to the visible boundary at 400 nm (UV-C: 100–280 nm, UV-B: 280–315 nm, UV-A: 315–400 nm).",
                    "Step 3: Verification & Environmental Equilibrium — 400–700 nm is visible light; 700 nm to 1 mm is infrared. Hence, 100 nm to 400 nm is the exact range."
                ]
            },
            {
                "question": "If the clear-sky insolation reaching Earth's surface is 1.0 kW m⁻², how much solar energy is received by 1 m² in one hour (Example 13.1)?",
                "options": [
                    "1.0 × 10³ J",
                    "6.0 × 10⁴ J",
                    "3.6 × 10⁶ J",
                    "1.4 × 10⁷ J"
                ],
                "answer": 2,
                "hint": "Multiply power (1000 W = 1000 J/s) by the number of seconds in one hour (3600 s).",
                "explanation": "Energy = Power × Time = 1000 J s⁻¹ × 3600 s = 3.6 × 10⁶ J (or 3.6 MJ).",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Given surface irradiance P = 1.0 kW m⁻² = 1000 W m⁻²; area A = 1.0 m²; duration t = 1 hour = 3600 seconds.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Total energy E = P × A × t = 1000 J s⁻¹ m⁻² × 1 m² × 3600 s = 3,600,000 J = 3.6 × 10⁶ J.",
                    "Step 3: Verification & Environmental Equilibrium — 1 kWh is internationally defined as exactly 3.6 MJ (3.6 × 10⁶ J). Verified."
                ]
            },
            {
                "question": "What value defines the Solar Constant at the top of Earth's atmosphere?",
                "options": [
                    "0.7 kW m⁻²",
                    "1.0 kW m⁻²",
                    "1.4 kW m⁻²",
                    "2.4 kW m⁻²"
                ],
                "answer": 2,
                "hint": "It corresponds to roughly 1400 Joules per second received per square meter.",
                "explanation": "The Solar Constant is approximately 1.4 kW m⁻² (1400 J s⁻¹ m⁻²) measured perpendicular to rays at the mean Earth-Sun distance outside the atmosphere.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Solar luminosity L ≈ 3.828 × 10²⁶ W distributed over a sphere of radius 1 AU (r ≈ 1.496 × 10¹¹ m).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Solar constant S₀ = L / (4πr²) = 3.828 × 10²⁶ / [4π(1.496 × 10¹¹)²] ≈ 1361 W m⁻² ≈ 1.4 kW m⁻².",
                    "Step 3: Verification & Environmental Equilibrium — Atmospheric absorption and scattering reduce surface clear-sky insolation to ~1.0 kW m⁻²."
                ]
            },
            {
                "question": "In their 1982 atlas, Anna Mani and S. Rangarajan determined that most of India receives how much daily solar energy per square meter?",
                "options": [
                    "1 to 2 kWh m⁻²",
                    "4 to 7 kWh m⁻²",
                    "10 to 15 kWh m⁻²",
                    "20 to 25 kWh m⁻²"
                ],
                "answer": 1,
                "hint": "India enjoys high tropical insolation with 250 to 300 sunny days annually.",
                "explanation": "Anna Mani and S. Rangarajan's atlas documented that India receives an abundant 4 to 7 kWh m⁻² of solar energy daily, ideal for photovoltaic harvesting.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Meteorological radiation data compiled across India by Anna Mani and S. Rangarajan (1982).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Averaged over the year, daily horizontal global solar radiation across India ranges between 4.0 and 7.0 kWh m⁻² day⁻¹.",
                    "Step 3: Verification & Environmental Equilibrium — Western arid regions like Rajasthan exceed 6–7 kWh m⁻², making the Thar desert prime for solar mega-parks."
                ]
            },
            {
                "question": "Which surface has the highest albedo according to Table 13.1?",
                "options": [
                    "Deep ocean water (0.05–0.10)",
                    "Crushed basalt rock (0.25–0.30)",
                    "Moist black cotton soil (0.10–0.15)",
                    "Freshly fallen snow (0.80–0.90)"
                ],
                "answer": 3,
                "hint": "Albedo measures reflectivity; bright white cryospheric surfaces reflect up to 90% of sunlight.",
                "explanation": "Fresh snow reflects 80% to 90% (albedo 0.80–0.90) of incident solar radiation, preventing polar surfaces from absorbing significant heat.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Albedo α = reflected radiation / incident radiation (0 ≤ α ≤ 1).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Fresh snow has microscopic ice crystals that scatter sunlight across all visible wavelengths, yielding α = 0.80–0.90.",
                    "Step 3: Verification & Environmental Equilibrium — Liquid water absorbs sunlight (α ≈ 0.05–0.10), black soil absorbs (α ≈ 0.10), rock is intermediate (α ≈ 0.25). Fresh snow is highest."
                ]
            },
            {
                "question": "Why do traditional mud and thatch houses remain cooler during Indian summers than modern concrete buildings?",
                "options": [
                    "Mud generates cold geothermal energy continuously",
                    "Mud has high porosity and low thermal conductivity, slowing heat penetration",
                    "Concrete reflects 100% of solar radiation into the interior rooms",
                    "Thatch roofs pull moisture from the stratosphere"
                ],
                "answer": 1,
                "hint": "Mud walls act as natural thermal insulators and store heat with a significant time lag.",
                "explanation": "Mud and thatch possess low thermal conductivity and high porosity, delaying heat transfer into the interior until evening hours when ventilation cools the home.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Compare thermal properties of building materials: concrete/asphalt vs porous mud/straw composites.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Concrete has high thermal conductivity and volumetric heat capacity, storing immense solar heat and re-radiating it indoors. Mud is porous with low conductivity.",
                    "Step 3: Verification & Environmental Equilibrium — Traditional bio-climatic construction prevents indoor thermal peaking during maximum afternoon insolation."
                ]
            },
            {
                "question": "Why does a given quantity of solar energy spread over a larger surface area at the poles than at the equator?",
                "options": [
                    "Due to Earth's spherical curvature causing rays to strike at oblique angles",
                    "Because gravitational pull is weaker at the poles",
                    "Because polar winds blow the light rays horizontally",
                    "Because the ozone layer is thinner over equatorial latitudes"
                ],
                "answer": 0,
                "hint": "Think of shining a flashlight straight down versus at an angle on a curved ball.",
                "explanation": "Earth's spherical shape means equatorial rays strike perpendicularly (small footprint), whereas polar rays arrive obliquely, spreading the same energy over a larger area.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Solar rays travel in essentially parallel beams toward the spherical Earth.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — At solar elevation angle θ, beam width w intercepts ground length L = w / sin(θ). At equator, θ ≈ 90° so L ≈ w; near poles, θ is small so L is large.",
                    "Step 3: Verification & Environmental Equilibrium — Flux density (W m⁻²) drops by sin(θ), causing dramatic polar cooling and driving global atmospheric circulation."
                ]
            }
        ]
    },
    {
        "id": 18,
        "title": "Atmosphere & Winds",
        "subtitle": "Challenge Quiz: Atmospheric Layers, Greenhouse & Planetary Winds",
        "speech": "",
        "questions": [
            {
                "question": "What is the average environmental lapse rate in the troposphere?",
                "options": [
                    "1.5 °C per kilometer",
                    "6.5 °C per kilometer",
                    "15.0 °C per kilometer",
                    "25.0 °C per kilometer"
                ],
                "answer": 1,
                "hint": "Temperature drops by roughly six and a half degrees Celsius for every 1000 meters of altitude.",
                "explanation": "In the troposphere, temperature decreases with altitude at an average environmental lapse rate of ~6.5 °C km⁻¹.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Identify vertical thermal gradient dT/dz in the standard international troposphere (0 to 12 km).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — The ground is heated by sunlight and warms the troposphere from below; as air ascends, it expands adiabatically and cools at ~6.5 °C km⁻¹.",
                    "Step 3: Verification & Environmental Equilibrium — At 10 km altitude (cruising altitude), temperature drops from +15 °C to approximately -50 °C. Verified."
                ]
            },
            {
                "question": "Which atmospheric layer exhibits a thermal inversion where temperature increases with altitude due to ozone absorption?",
                "options": ["Troposphere", "Stratosphere", "Mesosphere", "Exosphere"],
                "answer": 1,
                "hint": "This layer lies between 12 km and 50 km and houses the protective ozone shield.",
                "explanation": "In the stratosphere, ozone absorbs energetic ultraviolet rays, transforming photon energy into heat and causing temperature to increase with altitude.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Review thermal profile of atmospheric strata: Troposphere (cooling), Stratosphere (warming), Mesosphere (cooling), Thermosphere (warming).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Ozone (O₃) photodissociation by UV radiation (O₃ + hν → O₂ + O) releases thermal kinetic energy, heating the upper stratosphere.",
                    "Step 3: Verification & Environmental Equilibrium — This positive vertical temperature gradient (dT/dz > 0) creates exceptional atmospheric stability, suppressing vertical storm convection."
                ]
            },
            {
                "question": "What milestone did Indian scientist K. R. Ramanathan achieve in 1934?",
                "options": [
                    "Synthesized artificial urea in a laboratory",
                    "Measured atmospheric ozone at 18,000 feet in the Himalayas",
                    "Discovered the speed of light using rotating mirrors",
                    "Proved that plants respire through leaf stomata"
                ],
                "answer": 1,
                "hint": "He used a Dobson spectrophotometer at high Himalayan altitudes to pioneer Indian atmospheric science.",
                "explanation": "K. R. Ramanathan conducted pioneering high-altitude ozone measurements at 18,000 feet in the Himalayas in 1934, discovering fundamental links between ozone and upper atmospheric circulation.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Identify the contributions of K. R. Ramanathan highlighted in Chapter 13 'Meet a Scientist'.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — In 1934, Ramanathan took a Dobson spectrophotometer up to 18,000 feet in the Himalayas, obtaining the first clear vertical ozone profiles in South Asia.",
                    "Step 3: Verification & Environmental Equilibrium — His work aided early monsoon forecasting and earned him international acclaim as the 'Father of Indian Atmospheric Sciences'."
                ]
            },
            {
                "question": "What would be Earth's surface temperature without the natural greenhouse effect?",
                "options": ["+15 °C", "0 °C", "-18 °C", "-80 °C"],
                "answer": 2,
                "hint": "Without heat-trapping gases, Earth would radiate all absorbed heat directly to space.",
                "explanation": "Without greenhouse gases trapping infrared radiation, Earth's radiative balance would drop average surface temperatures to approximately -18 °C (a 33 °C deficit).",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Earth radiation balance: (1 - α)S₀(πR²) = 4πR²σT_eff⁴.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Substituting albedo α ≈ 0.30 and solar constant S₀ ≈ 1361 W m⁻² yields effective radiating temperature T_eff = 255 K = -18 °C.",
                    "Step 3: Verification & Environmental Equilibrium — Atmospheric greenhouse gases absorb upward infrared and re-radiate it downward, raising actual average temperature to 288 K (+15 °C)."
                ]
            },
            {
                "question": "Why is planet Venus an alarming example of a runaway greenhouse effect?",
                "options": [
                    "Its 96% CO₂ atmosphere traps extreme heat, raising surface temperature to ~460 °C",
                    "It has lost its atmosphere completely to solar wind",
                    "It is covered in high-albedo ice sheets that reflect all heat",
                    "Its core produces nuclear explosions that vaporized its oceans"
                ],
                "answer": 0,
                "hint": "A dense atmosphere dominated by carbon dioxide creates extreme planetary thermal trapping.",
                "explanation": "Venus possesses a dense atmosphere containing 96% CO₂, creating an extreme greenhouse trap that drives surface temperatures to ~460 °C—hot enough to melt lead.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Compare Earth's 0.04% CO₂ atmosphere with Venus's dense CO₂ atmosphere (surface pressure ~92 bar).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Extreme concentrations of CO₂ and sulfur dioxide absorb nearly all outgoing infrared radiation, preventing planetary thermal escape.",
                    "Step 3: Verification & Environmental Equilibrium — Despite reflecting 70% of sunlight (albedo ~0.7), Venus reaches 735 K (460 °C), hotter than Mercury."
                ]
            },
            {
                "question": "What is the direction and mechanism of a daytime valley breeze (anabatic wind)?",
                "options": [
                    "Cold air sinks down mountain slopes into the valley floor",
                    "Sun-warmed air on mountain slopes rises, drawing cooler air up from the valley floor",
                    "Ocean water pushes moist air horizontally through deep valleys",
                    "Earth's rotation pulls valley air sideways toward the west"
                ],
                "answer": 1,
                "hint": "Slopes heat faster than valleys in daytime; rising warm air draws air up the valley.",
                "explanation": "Sunlit mountain slopes heat rapidly, causing air to expand and rise; cooler, denser air from the valley floor moves upward along the slopes as a valley breeze.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Mountain-valley diurnal heating cycle in regions like Shimla or Dehradun during clear daytime.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Solar rays warm mountain slopes more directly than the shadowed valley basin. Buoyant warm air ascends (anabatic flow), drawing replacement air up from the valley.",
                    "Step 3: Verification & Environmental Equilibrium — By afternoon, this moist upslope air cools adiabatically, often forming cumulus clouds along mountain ridges."
                ]
            },
            {
                "question": "What causes cold nighttime mountain breezes (katabatic winds) to drain down slopes?",
                "options": [
                    "Rapid radiational cooling at high altitudes makes air dense and heavy",
                    "Strong sunlight warming the valley basin at midnight",
                    "Magnetic repulsion from mountain rock formations",
                    "High evaporation rates on mountain peaks pushing air downward"
                ],
                "answer": 0,
                "hint": "At night, elevated slopes lose heat quickly into space, creating heavy, sinking air.",
                "explanation": "At night, high mountain slopes lose thermal energy rapidly via infrared radiation; the resulting cold, dense air flows downhill under gravity into valleys.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Nighttime radiative cooling across steep mountain topography.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Thin mountain air allows rapid net radiational heat loss. Surface air cools, contracts, increases in density (ρ = P/RT), and drains downslope under gravity (katabatic flow).",
                    "Step 3: Verification & Environmental Equilibrium — Cold air pools in the valley floor, frequently creating morning temperature inversions and valley fog."
                ]
            },
            {
                "question": "What causes the apparent deflection of moving winds known as the Coriolis force?",
                "options": [
                    "Gravitational pull of the Moon on atmospheric gases",
                    "Earth's rotation from west to east on its axis",
                    "Thermal expansion of oceanic water at the equator",
                    "Fluctuations in Earth's geomagnetic field"
                ],
                "answer": 1,
                "hint": "It is an apparent inertial force experienced in a rotating reference frame.",
                "explanation": "Because Earth rotates eastward, surface linear velocity is faster at the equator (~1670 km/h) than at the poles, causing moving fluids to veer relative to the ground.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Fluid motion over a rotating spherical reference frame with angular velocity Ω ≈ 7.292 × 10⁻⁵ rad s⁻¹.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — The Coriolis acceleration is a_c = -2(Ω × v). In the Northern Hemisphere, this acceleration deflects air to the right; in the Southern Hemisphere, to the left.",
                    "Step 3: Verification & Environmental Equilibrium — The Coriolis force is zero at the equator (latitude φ = 0) and reaches maximum strength at the geographic poles (sin 90° = 1)."
                ]
            },
            {
                "question": "Which global pressure belt is situated around 30° North and South latitudes where cooled tropical air descends?",
                "options": [
                    "Equatorial Low Pressure Belt",
                    "Sub-tropical High Pressure Belt",
                    "Sub-polar Low Pressure Belt",
                    "Polar High Pressure Belt"
                ],
                "answer": 1,
                "hint": "Descending dry air creates high atmospheric pressure, known historically as the horse latitudes.",
                "explanation": "Air rising from the equator travels poleward in the upper troposphere, cools, and subsides at ~30° N/S, creating the Sub-tropical High Pressure Belts.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Hadley cell circulation in the tropical atmosphere.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Equatorial warm air ascends and moves poleward, losing heat. Around 30° latitude, conservation of angular momentum and radiative cooling force air to subside.",
                    "Step 3: Verification & Environmental Equilibrium — Sinking air warms adiabatically and prevents cloud formation, creating major world deserts (Thar, Sahara) under Sub-tropical Highs."
                ]
            },
            {
                "question": "How are surface winds deflected in the Southern Hemisphere by the Coriolis force?",
                "options": [
                    "To the right of their direction of motion",
                    "To the left of their direction of motion",
                    "Directly upward toward the mesosphere",
                    "They experience zero deflection at any latitude"
                ],
                "answer": 1,
                "hint": "Recall that deflection is to the right in the north, and the opposite in the south.",
                "explanation": "In the Southern Hemisphere, Earth's rotation causes the Coriolis force to deflect winds toward the left of their path of travel.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Coriolis parameter f = 2Ω sin(φ). In the Southern Hemisphere, latitude φ is negative, making f negative.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — A negative Coriolis parameter generates an acceleration vector directed 90° to the left of the fluid velocity vector.",
                    "Step 3: Verification & Environmental Equilibrium — Consequently, southern trade winds blow from the southeast (Southeast Trades) rather than the northeast."
                ]
            }
        ]
    },
    {
        "id": 19,
        "title": "Biogeochemical Cycles Review",
        "subtitle": "Challenge Quiz: Ocean Gyres, Hydrological & Carbon Fluxes",
        "speech": "",
        "questions": [
            {
                "question": "How do major surface ocean currents circulate in the Northern and Southern Hemispheres?",
                "options": [
                    "Clockwise in the North, Counter-clockwise in the South",
                    "Counter-clockwise in the North, Clockwise in the South",
                    "Clockwise in both hemispheres",
                    "Counter-clockwise in both hemispheres"
                ],
                "answer": 0,
                "hint": "Surface gyres follow the direction of Coriolis wind deflection in each hemisphere.",
                "explanation": "Ocean gyres turn clockwise in the Northern Hemisphere and counter-clockwise in the Southern Hemisphere due to prevailing winds and Coriolis deflection.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Interaction between planetary wind belts, continental margins, and oceanic surface water layers.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Trade winds push water westward at low latitudes; westerlies push water eastward at mid-latitudes; Coriolis deflection turns water right in the North (clockwise) and left in the South (counter-clockwise).",
                    "Step 3: Verification & Environmental Equilibrium — Major gyres (North Atlantic Gyre, South Pacific Gyre) confirm this hemispheric symmetry."
                ]
            },
            {
                "question": "What climatic effect does the warm Gulf Stream and North Atlantic Drift have on northwestern Europe?",
                "options": [
                    "It causes perpetual sub-zero blizzards across Britain",
                    "It keeps high-latitude ports ice-free and moderates winter temperatures",
                    "It completely stops all oceanic evaporation across the Atlantic",
                    "It cools the European continent into an arctic tundra"
                ],
                "answer": 1,
                "hint": "This current carries tropical equatorial heat thousands of kilometers northward.",
                "explanation": "The Gulf Stream transports warm tropical water across the Atlantic, releasing heat that keeps northwestern European coastal harbors ice-free in winter.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Western boundary current (Gulf Stream) transitioning into North Atlantic Drift.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Warm, saline equatorial water carries ~1.3 × 10¹⁵ W of heat poleward. Westerly winds transfer this ocean heat to the European atmosphere.",
                    "Step 3: Verification & Environmental Equilibrium — Cities like London and Bergen maintain winter temperatures ~15 °C warmer than corresponding Canadian latitudes."
                ]
            },
            {
                "question": "What critical modeling role does the Indian Institute of Tropical Meteorology (IITM) in Pune perform?",
                "options": [
                    "Mining lithium deposits from the Deccan plateau",
                    "Running supercomputer coupled ocean-atmosphere models to forecast the Indian monsoon",
                    "Purifying industrial wastewater using synthetic polymers",
                    "Monitoring satellite television broadcasts across Asia"
                ],
                "answer": 1,
                "hint": "IITM operates high-performance computing systems for atmospheric and oceanic monsoon prediction.",
                "explanation": "IITM Pune deploys supercomputing systems to simulate coupled ocean-atmosphere interactions, forecasting the Indian summer monsoon and seasonal weather.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Identify the role of IITM Pune in Section 13.2.3 'India's Scientific Contributions'.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Supercomputers solve non-linear Navier-Stokes and thermodynamic equations across coupled oceanic and atmospheric grids.",
                    "Step 3: Verification & Environmental Equilibrium — Accurate monsoon forecasting protects India's agrarian economy, food security, and water reservoir management."
                ]
            },
            {
                "question": "Which of the following processes in the water cycle involves the conversion of liquid water to vapor directly from plant foliage?",
                "options": ["Precipitation", "Infiltration", "Transpiration", "Condensation"],
                "answer": 2,
                "hint": "It combines biological root uptake with evaporation through leaf stomata.",
                "explanation": "Transpiration is the biological process whereby moisture is carried through plants from roots to small pores (stomata) on leaves, where it evaporates into the atmosphere.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Identify components of the terrestrial water cycle: Evaporation, Transpiration, Condensation, Precipitation, Infiltration.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Plants extract liquid soil moisture via root xylem and evaporate it into the boundary layer through open stomata during photosynthetic gas exchange.",
                    "Step 3: Verification & Environmental Equilibrium — A mature tree can transpire hundreds of liters of water per day, directly cooling regional microclimates."
                ]
            },
            {
                "question": "How does accelerating cryospheric melt impact coastal cities like Mumbai and Chennai?",
                "options": [
                    "It causes sudden drops in sea level, stranding ships inland",
                    "It causes sea level rise, increasing coastal inundation, erosion, and storm surge risks",
                    "It freezes seawater in tropical harbors into solid ice sheets",
                    "It increases oceanic salinity to lethal crystallization levels"
                ],
                "answer": 1,
                "hint": "Melting land ice adds liquid volume to oceans, raising sea levels globally.",
                "explanation": "Melting glaciers and polar ice sheets transfer water mass from the cryosphere to the hydrosphere, causing global sea level rise that threatens low-lying coastal cities with flooding.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Cryosphere-to-hydrosphere mass transfer due to global planetary warming.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Melting land-based ice (glaciers and ice sheets) plus thermal expansion of warming ocean water increases total oceanic volume.",
                    "Step 3: Verification & Environmental Equilibrium — Global sea levels rise by ~3.7 mm/year, intensifying high-tide flooding, saltwater intrusion, and storm surge damage in Mumbai and Chennai."
                ]
            },
            {
                "question": "What is the primary difference between the fast biological and slow geological carbon cycles?",
                "options": [
                    "Fast cycle occurs only in winter; slow cycle occurs only in summer",
                    "Fast cycle involves photosynthesis and respiration over days/years; slow cycle stores carbon in rocks and fossil fuels over millions of years",
                    "Fast cycle produces radioactive isotopes; slow cycle produces stable isotopes",
                    "Fast cycle operates only on Mars; slow cycle operates on Earth"
                ],
                "answer": 1,
                "hint": "Fast cycle recycles carbon biologically; slow cycle locks carbon in sedimentary rocks and fossil deposits.",
                "explanation": "The fast carbon cycle moves carbon through living organisms (photosynthesis, respiration) within days to decades; the slow cycle traps carbon in rocks and fossil fuels for millions of years.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Compare temporal scales of carbon fluxes: biological exchanges vs geological lithospheric reservoirs.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Fast cycle: CO₂ + H₂O ↔ C₆H₁₂O₆ + O₂ (turnover rate 10⁰–10² years). Slow cycle: weathering, sedimentation, fossilization, volcanism (turnover rate 10⁵–10⁸ years).",
                    "Step 3: Verification & Environmental Equilibrium — Human combustion of fossil fuels extracts slow-cycle carbon and dumps it into the fast cycle, causing atmospheric CO₂ buildup."
                ]
            },
            {
                "question": "What was the atmospheric carbon dioxide concentration in 1960 according to the Keeling Curve, and what has it exceeded today?",
                "options": [
                    "150 ppm in 1960; exceeds 200 ppm today",
                    "315 ppm in 1960; exceeds 420 ppm today",
                    "400 ppm in 1960; exceeds 600 ppm today",
                    "500 ppm in 1960; exceeds 800 ppm today"
                ],
                "answer": 1,
                "hint": "Charles Keeling began measurements at Mauna Loa when CO₂ was around 315 ppm; it now surpasses 420 ppm.",
                "explanation": "Continuous atmospheric monitoring at Mauna Loa documented CO₂ rising from 315 ppm in 1960 to over 420 ppm in recent years.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Keeling Curve historical records of atmospheric CO₂ mole fraction.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — In 1958–1960, background baseline was ~315 ppm. Relentless global fossil fuel emissions and deforestation drove it past 420 ppm by 2024.",
                    "Step 3: Verification & Environmental Equilibrium — This represents an unprecedented >33% increase within six decades, driving modern anthropogenic climate change."
                ]
            },
            {
                "question": "What percentage of Earth's total mobile carbon is stored in the oceanic carbon sink compared to the atmosphere?",
                "options": [
                    "Oceans hold 10%, Atmosphere holds 90%",
                    "Oceans hold 50%, Atmosphere holds 50%",
                    "Oceans hold ~71%, Atmosphere holds ~1%",
                    "Oceans hold 0%, Atmosphere holds 100%"
                ],
                "answer": 2,
                "hint": "Oceans are by far the dominant reservoir, holding over 70 times more carbon than the atmosphere.",
                "explanation": "Earth's oceans store approximately 71% of global carbon (mostly as dissolved bicarbonate and carbonate ions), whereas the atmosphere holds only ~1%.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Quantitative mass balance of Earth's active carbon reservoirs (Atmosphere, Oceans, Biosphere, Soils).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Oceanic reservoir contains ~38,000 to 40,000 gigatons of carbon (GtC); atmosphere contains ~850 GtC (~1% of total).",
                    "Step 3: Verification & Environmental Equilibrium — Oceans buffer atmospheric changes, but excessive absorption causes acidification."
                ]
            },
            {
                "question": "Which symbiotic bacterium fixes atmospheric nitrogen within the root nodules of leguminous plants?",
                "options": ["Rhizobium", "Nitrobacter", "Lactobacillus", "Saccharomyces"],
                "answer": 0,
                "hint": "Found in peas, beans, and lentils, it forms mutualistic nitrogen-fixing root nodules.",
                "explanation": "Rhizobium forms symbiotic associations inside the root nodules of legumes, using the enzyme nitrogenase to convert atmospheric N₂ into ammonia.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Biological nitrogen fixation in terrestrial agro-ecosystems.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Legume roots secrete flavonoids attracting Rhizobium. Bacteria infect root hairs, form nodules, and produce nitrogenase enzyme to reduce N₂ to NH₃.",
                    "Step 3: Verification & Environmental Equilibrium — The plant provides carbohydrates; the bacterium supplies fixed nitrogen. Nitrobacter is a nitrifier, not a nodule fixer."
                ]
            },
            {
                "question": "In the soil nitrification process, which bacterium converts toxic nitrite ions (NO₂⁻) into plant-accessible nitrate ions (NO₃⁻)?",
                "options": ["Nitrosomonas", "Nitrobacter", "Azotobacter", "Pseudomonas"],
                "answer": 1,
                "hint": "Nitrosomonas handles ammonia to nitrite; Nitrobacter performs the second oxidation step to nitrate.",
                "explanation": "Nitrobacter is a chemoautotrophic bacterium that oxidizes nitrite (NO₂⁻) into nitrate (NO₃⁻), the primary nitrogen form assimilated by plant roots.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Soil nitrification: two-step biological oxidation of ammonia.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Step 1: 2NH₃ + 3O₂ → 2NO₂⁻ + 2H⁺ + 2H₂O (by Nitrosomonas). Step 2: 2NO₂⁻ + O₂ → 2NO₃⁻ (by Nitrobacter).",
                    "Step 3: Verification & Environmental Equilibrium — Nitrobacter prevents the accumulation of toxic intermediate nitrites, providing stable nitrates for crop nutrition."
                ]
            }
        ]
    },
    {
        "id": 20,
        "title": "Ecosystems & Conservation",
        "subtitle": "Challenge Quiz: Nitrogen Denitrification, Oxygen Cycle & Mission LiFE",
        "speech": "",
        "questions": [
            {
                "question": "Which bacterium converts soil nitrates back into inert atmospheric nitrogen gas (N₂) during denitrification?",
                "options": ["Rhizobium", "Nitrosomonas", "Pseudomonas", "Azotobacter"],
                "answer": 2,
                "hint": "It operates in waterlogged, anaerobic soils to complete the nitrogen cycle.",
                "explanation": "Pseudomonas is a denitrifying bacterium that converts soil nitrates back into atmospheric N₂ under anaerobic conditions.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Denitrification: the final reductive stage of the nitrogen cycle.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — In oxygen-depleted soils, facultative anaerobic bacteria like Pseudomonas use nitrate (NO₃⁻) as a terminal electron acceptor: NO₃⁻ → NO₂⁻ → NO → N₂O → N₂.",
                    "Step 3: Verification & Environmental Equilibrium — Denitrification prevents excessive nitrate toxicity in ecosystems and replenishes atmospheric N₂ reserves."
                ]
            },
            {
                "question": "What extreme physical conditions are required in the industrial Haber-Bosch ammonia synthesis?",
                "options": [
                    "Room temperature (25 °C), 1 atmosphere pressure, and copper catalyst",
                    "~450 °C temperature, ~200 atmospheres pressure, and an iron catalyst",
                    "-50 °C sub-zero temperature, vacuum chamber, and platinum catalyst",
                    "1000 °C temperature, 10 atmospheres pressure, and carbon catalyst"
                ],
                "answer": 1,
                "hint": "Breaking the triple covalent bond of N₂ requires high heat, extreme pressure, and an iron catalyst.",
                "explanation": "The Haber-Bosch process reacts N₂ and H₂ at ~450 °C and ~200 atm over an iron catalyst to achieve economical ammonia yield.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Industrial reaction: N₂(g) + 3H₂(g) ⇌ 2NH₃(g) (ΔH = -92.4 kJ mol⁻¹).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — High pressure (200 atm) shifts equilibrium toward products (fewer gas moles); high temperature (450 °C) accelerates kinetics across the iron catalyst bed.",
                    "Step 3: Verification & Environmental Equilibrium — This synthetic process currently feeds nearly half the human population via chemical fertilizers."
                ]
            },
            {
                "question": "How did synthetic nitrogen fertilizers impact Indian agriculture during the 1960s Green Revolution?",
                "options": [
                    "They eliminated all insect pests completely without pesticides",
                    "They dramatically increased wheat and rice crop yields, preventing famines",
                    "They permanently reduced agricultural water requirements by 90%",
                    "They converted all arable land into certified organic orchards"
                ],
                "answer": 1,
                "hint": "Combined with semi-dwarf high-yielding seeds and irrigation, fertilizers multiplied grain harvests.",
                "explanation": "Synthetic nitrogen fertilizers (urea, DAP) provided essential nutrients that allowed high-yielding wheat and rice varieties to multiply output, ensuring Indian national food self-sufficiency.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Historical agricultural transition in India during the mid-20th century.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — High-yielding crop varieties (HYVs) bred for responsiveness to chemical nitrogen dramatically increased grain-to-biomass conversion ratios.",
                    "Step 3: Verification & Environmental Equilibrium — India overcame chronic food deficits and attained granary surpluses in Punjab, Haryana, and Uttar Pradesh."
                ]
            },
            {
                "question": "Which of the following processes continually consumes atmospheric oxygen?",
                "options": [
                    "Cellular respiration, organic decay, and fuel combustion",
                    "Oxygenic photosynthesis by green plants",
                    "Atmospheric nitrogen fixation by lightning",
                    "Transpiration of water vapor from leaf stomata"
                ],
                "answer": 0,
                "hint": "Look for processes that oxidize organic carbon or burn materials in air.",
                "explanation": "Atmospheric oxygen is steadily consumed by cellular respiration in aerobic organisms, microbial decomposition of organic matter, and industrial combustion of fuels.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Mass balance of atmospheric oxygen (21% reservoir).",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Sinks: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O (respiration/decay); CH₄ + 2O₂ → CO₂ + 2H₂O (combustion); 4FeO + O₂ → 2Fe₂O₃ (weathering).",
                    "Step 3: Verification & Environmental Equilibrium — Photosynthesis is the sole major replenishing source; all others listed in Option A are consumptive sinks."
                ]
            },
            {
                "question": "What marine organisms are responsible for generating over 50% of planet Earth's photosynthetic oxygen?",
                "options": [
                    "Deep-sea anglerfish and giant squids",
                    "Microscopic phytoplankton, cyanobacteria, and marine algae",
                    "Coral reef calcium carbonate skeletons",
                    "Bottom-dwelling sea cucumbers and marine sponges"
                ],
                "answer": 1,
                "hint": "Microscopic drifting photosynthetic single-celled organisms in the upper ocean euphotic zone.",
                "explanation": "Oceanic phytoplankton, microalgae, and cyanobacteria in the marine euphotic zone produce more than 50% of global atmospheric oxygen.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Global photosynthetic primary production apportioned between terrestrial and marine biomes.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Microscopic marine phytoplankton (diatoms, dinoflagellates, Prochlorococcus) inhabit the sunlit upper 200 meters of oceans covering 71% of Earth.",
                    "Step 3: Verification & Environmental Equilibrium — Their aggregate photosynthesis exceeds all tropical rainforests combined, generating every second breath humans take."
                ]
            },
            {
                "question": "What chemical chain reaction occurs during ocean acidification?",
                "options": [
                    "Absorbed CO₂ reacts with seawater to form carbonic acid (H₂CO₃), lowering pH and dissolving carbonate shells",
                    "Dissolved nitrogen gas creates liquid nitric acid that turns the oceans green",
                    "Oxygen gas dissolves to form liquid ozone that bleaches ocean water",
                    "Salt crystals decompose into chlorine gas that acidifies coastal beaches"
                ],
                "answer": 0,
                "hint": "Carbon dioxide dissolves to form a weak acid, releasing hydrogen ions that react with carbonate.",
                "explanation": "CO₂ dissolves in seawater to form carbonic acid (H₂CO₃), which dissociates into H⁺ ions; these ions lower ocean pH and consume carbonate ions needed by corals and shell-builders.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Carbonate chemistry in marine hydrosphere: CO₂(aq) + H₂O ⇌ H₂CO₃ ⇌ H⁺ + HCO₃⁻.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Excess H⁺ reacts with carbonate ions: H⁺ + CO₃²⁻ ⇌ HCO₃⁻. This depletes the free CO₃²⁻ needed for calcification: Ca²⁺ + CO₃²⁻ → CaCO₃.",
                    "Step 3: Verification & Environmental Equilibrium — Seawater becomes corrosive to aragonite and calcite, causing coral reef degradation and plankton shell thinning."
                ]
            },
            {
                "question": "What sequence of events defines agricultural eutrophication in aquatic ecosystems?",
                "options": [
                    "Pesticide poisoning kills all plants → water turns clear → fish multiply rapidly",
                    "Fertilizer runoff → explosive algal bloom → algal death → bacterial decomposition exhausts dissolved oxygen → fish die",
                    "Glacier melt freezes lake water → ice blocks sunlight → plants perish",
                    "Excess acid rain dissolves fish scales → fish sink to the lake floor"
                ],
                "answer": 1,
                "hint": "Nutrient surge causes rapid algal proliferation, followed by bacterial decomposition and severe hypoxia.",
                "explanation": "Excess nitrogen/phosphorus runoff triggers explosive algal blooms; when the algae die, decomposing bacteria consume all dissolved oxygen, creating hypoxic dead zones.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Anthropogenic nutrient loading in freshwater lakes, ponds, and estuaries.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Nitrates/phosphates stimulate algal overgrowth (bloom). Algal mat blocks sunlight, killing benthic plants. Massive algal die-off fuels aerobic bacterial decomposers.",
                    "Step 3: Verification & Environmental Equilibrium — Biological Oxygen Demand (BOD) skyrockets, driving dissolved oxygen below 2 mg/L (hypoxia), resulting in massive fish kills."
                ]
            },
            {
                "question": "How does large-scale deforestation impact the regional hydrological cycle and climate?",
                "options": [
                    "It dramatically increases transpiration and regional rainfall",
                    "It reduces transpiration, disrupts rainfall patterns, and accelerates soil erosion",
                    "It causes glaciers to advance rapidly into agricultural plains",
                    "It permanently cools the regional climate by 10 °C"
                ],
                "answer": 1,
                "hint": "Trees recycle immense volumes of moisture; removing them weakens atmospheric humidity and destabilizes soil.",
                "explanation": "Removing forest cover reduces transpiration, cutting atmospheric moisture recycling and disrupting rainfall, while leaving topsoil vulnerable to heavy water and wind erosion.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Biosphere-Hydrosphere-Geosphere couplings in forested catchments.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Trees pump groundwater into the atmosphere via transpiration, seeding clouds. Without tree canopies, rainfall drops, surface runoff surges, and topsoil is stripped.",
                    "Step 3: Verification & Environmental Equilibrium — Deforestation also reduces carbon sequestration and raises local surface albedo, driving regional desertification."
                ]
            },
            {
                "question": "What is the core philosophy of India's Mission LiFE (Lifestyle for Environment) launched at COP26?",
                "options": [
                    "Replacing all human agriculture with automated subterranean hydroponic factories",
                    "Promoting sustainable individual and community behaviors rooted in mindful conservation",
                    "Relocating coastal populations into floating ocean barges",
                    "Building a giant space mirror to deflect all incoming solar radiation"
                ],
                "answer": 1,
                "hint": "Mission LiFE mobilizes grassroots behavioral shifts toward conscious, non-wasteful consumption.",
                "explanation": "Mission LiFE advocates individual and collective lifestyle changes that prioritize conscious resource utilization and circular sustainability over mindless consumption.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — India's climate policy initiative introduced at the 2021 Glasgow COP26 summit.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Shifting from a 'use-and-dispose' extractive economic model to a circular, regenerative model driven by individual sustainable choices (saving water, energy efficiency, waste reduction).",
                    "Step 3: Verification & Environmental Equilibrium — Connects modern climate action with traditional Indian ethos of living in harmony with nature."
                ]
            },
            {
                "question": "Why is the 1987 Montreal Protocol widely cited as the most successful international environmental treaty?",
                "options": [
                    "It successfully eradicated all greenhouse gas emissions worldwide by the year 2000",
                    "It united all global nations to phase out ozone-depleting substances, initiating ozone layer recovery",
                    "It banned all fossil fuel extraction across the entire planet",
                    "It established an international treaty to colonize the Moon"
                ],
                "answer": 1,
                "hint": "It achieved universal ratification and phased out 99% of chlorofluorocarbons.",
                "explanation": "The Montreal Protocol successfully phased out nearly 99% of ozone-depleting chlorofluorocarbons globally, putting the Antarctic ozone hole on a projected path to full recovery.",
                "solution_steps": [
                    "Step 1: System, Variables & Spheres Setup — Global diplomatic treaty addressing stratospheric ozone depletion.",
                    "Step 2: Physical/Chemical Mechanism & Transfer — Mandated legally binding phase-out schedules for CFCs, halons, and carbon tetrachloride, replacing them with benign alternatives.",
                    "Step 3: Verification & Environmental Equilibrium — Scientific assessment confirms stratospheric chlorine levels are declining and the ozone layer is projected to heal to 1980 levels by mid-century."
                ]
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides_part3:
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: title='{s['title']}' ({tw} words), questions={len(s['questions'])}")
        assert 1 <= tw <= 3, f"Title length {tw} not 1-3 words"
        assert len(s["questions"]) == 10, "Must have 10 questions"
        for q in s["questions"]:
            assert len(q["options"]) == 4, "Must have 4 options"
            assert "hint" in q and "explanation" in q, "Missing hint/explanation"
            assert len(q["solution_steps"]) == 3, "Must have 3 solution steps"
    print("Part 3 verified successfully!")
