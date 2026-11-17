#!/usr/bin/env python3
# -*- coding: utf-8 -*-
"""
Class 9 Science Chapter 13 Part 1 Data Generator (Slides 1-8)
Chapter Title: Earth as a System: Energy, Matter, and Life
Strict constraints:
- All slide titles 1-3 words
- Speech word count strictly 195-215 words on Slides 1-8
- Pure Indian male teacher voice
- Zero forbidden character names or persona titles
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Earth's Five Spheres",
        "subtitle": "Introduction & Five Coupled Planetary Domains",
        "speech": (
            "Welcome, students, to Chapter 13, Earth as a System: Energy, Matter, and Life! Look around at our vast, "
            "vibrant planet. Earth is not a static, disconnected pile of dirt, rocks, and water. Instead, it operates "
            "as a single, magnificently coupled thermodynamic engine driven by a continuous influx of solar energy and "
            "internal heat! Scientists organize Earth into five deeply interconnected primary spheres. The geosphere comprises "
            "solid rocks, minerals, soils, and landforms from the rugged Deccan plateau to the shifting Thar desert. "
            "The hydrosphere holds liquid surface water, majestic river networks like the Ganga-Brahmaputra basin, lakes, "
            "and deep underground aquifers. Next, the cryosphere represents our frozen realm: colossal Himalayan glaciers, "
            "snow across Ladakh, and polar ice caps. Surrounding everything is the atmosphere, our protective gaseous blanket. "
            "Finally, the biosphere encompasses every living organism, from deep oceanic plankton to lush Sundarban mangroves. "
            "In Activity 13.1, we trace direct connections across these domains. When winter snow melts in the cryosphere, "
            "it feeds freshwater streams in the hydrosphere, irrigating fertile soil in the geosphere and nourishing grass "
            "in the biosphere. A disturbance in any single sphere ripples dynamically through the entire planetary web! "
            "Use the interactive simulator to perturb individual spheres and witness how cascading thermodynamic feedbacks unfold."
        ),
        "checkpoints": [
            {
                "question": "Which Earth sphere specifically encompasses Himalayan glaciers, Ladakh snowfields, and polar ice?",
                "options": ["Hydrosphere", "Cryosphere", "Geosphere", "Atmosphere"],
                "answer": 1,
                "hint": "Think of the Greek prefix 'kryos' meaning icy cold or frost.",
                "explanation": "The cryosphere consists of all frozen water on Earth, including glaciers, ice sheets, snow cover, and permafrost, distinct from liquid hydrosphere water."
            },
            {
                "question": "Thermodynamically, how is planet Earth characterized with respect to energy and matter?",
                "options": [
                    "Closed for both energy and matter",
                    "Open for both energy and matter",
                    "Open for energy, largely closed for matter",
                    "Closed for energy, open for matter"
                ],
                "answer": 2,
                "hint": "Solar radiation arrives and heat radiates out, but physical atoms stay inside Earth's gravity.",
                "explanation": "Earth receives solar energy and radiates infrared heat to space (open for energy), while its chemical elements are recycled internally (closed for matter)."
            }
        ]
    },
    {
        "id": 2,
        "title": "Solar Energy Spectrum",
        "subtitle": "Electromagnetic Radiation & Spectral Bands",
        "speech": (
            "Every biological and physical process across our planet is energized by radiant sunlight traveling through the "
            "vacuum of space at three hundred thousand kilometers per second! Solar radiation arrives as electromagnetic waves, "
            "spanning an immense continuum of wavelengths. Remarkably, ninety-nine percent of all solar energy reaching the "
            "top of our atmosphere is concentrated into three primary spectral bands: ultraviolet, visible light, and infrared radiation. "
            "Each band plays a unique, specialized ecological role. High-energy ultraviolet rays, with wavelengths between one "
            "hundred and four hundred nanometers, carry sufficient photon energy to damage living tissues and cause cataracts; "
            "fortunately, our stratospheric ozone layer filters out the most hazardous ultraviolet wavelengths. Visible light, "
            "occupying wavelengths from four hundred to seven hundred nanometers, penetrates our clear atmosphere to power "
            "plant photosynthesis and warm the planetary surface. Infrared radiation, possessing longer wavelengths beyond "
            "seven hundred nanometers, represents direct thermal energy. When Earth's surface absorbs sunlight, it re-radiates "
            "longer-wavelength infrared waves, which greenhouse gases trap to maintain a hospitable global climate. Without this "
            "balanced incoming electromagnetic spectrum, life could never have emerged or flourished on Earth! Explore the interactive "
            "simulator to filter wavelengths and observe how incoming solar photons interact with atmospheric gases."
        ),
        "checkpoints": [
            {
                "question": "Approximately what percentage of solar energy reaching Earth falls within UV, visible, and IR spectrums?",
                "options": ["50 percent", "75 percent", "90 percent", "99 percent"],
                "answer": 3,
                "hint": "The Sun behaves almost like an ideal blackbody radiator peaking strongly in these three bands.",
                "explanation": "Nearly 99% of extraterrestrial solar radiation falls within the ultraviolet, visible, and infrared bands, with visible and near-infrared carrying the vast bulk."
            },
            {
                "question": "Which electromagnetic spectral band is primarily absorbed by Earth's surface and re-emitted as thermal heat?",
                "options": ["Gamma rays", "Infrared radiation", "X-rays", "Ultraviolet radiation"],
                "answer": 1,
                "hint": "These are long-wavelength, lower-energy heat waves trapped by greenhouse gases.",
                "explanation": "Solar energy absorbed by land and water is re-radiated as thermal infrared radiation, which interacts directly with atmospheric greenhouse gases."
            }
        ]
    },
    {
        "id": 3,
        "title": "Insolation & Atlas",
        "subtitle": "Solar Constant & Indian Energy Transition",
        "speech": (
            "The term insolation stands for incoming solar radiation intercepted by our planet. Scientists measure this continuous "
            "energy torrent using a standardized metric termed the Solar Constant. It is defined as the radiant energy received "
            "per unit area per unit time on a surface perpendicular to the Sun's rays at the outer boundary of the atmosphere, "
            "averaging approximately one point four kilowatts per square meter, or fourteen hundred joules per second per square "
            "meter! As sunlight traverses our dense atmosphere, scattering and absorption by aerosols and clouds reduce peak clear-sky "
            "surface insolation to around one kilowatt per square meter. In Example 13.1, a single square meter of ground receiving "
            "one kilowatt collects three point six megajoules of energy every hour! In 1982, pioneering meteorologists Anna Mani "
            "and S. Rangarajan published the landmark insolation atlas Solar Radiation Over India. Their meticulous nationwide data "
            "revealed that India receives between four and seven kilowatt-hours of solar energy per square meter daily. Today, "
            "this foundational research powers India's ambitious clean energy transition, demonstrating that covering a modest fraction "
            "of the arid Thar desert with photovoltaic arrays could generate enough electricity to power our entire national grid! "
            "Use the simulator to compute real-time solar harvest across various Indian states."
        ),
        "checkpoints": [
            {
                "question": "What is the approximate value of the Solar Constant at the outer boundary of Earth's atmosphere?",
                "options": ["0.5 kW/m²", "1.0 kW/m²", "1.4 kW/m²", "2.8 kW/m²"],
                "answer": 2,
                "hint": "It corresponds to roughly 1400 Joules per second received on each square meter.",
                "explanation": "The Solar Constant is approximately 1.4 kW/m² (or 1400 J s⁻¹ m⁻²) measured perpendicular to the Sun's rays at the top of Earth's atmosphere."
            },
            {
                "question": "Whose pioneering 1982 research provided the foundational solar radiation atlas for India?",
                "options": [
                    "C. V. Raman and Homi Bhabha",
                    "Anna Mani and S. Rangarajan",
                    "Birbal Sahni and K. R. Ramanathan",
                    "Jagadish Chandra Bose and Meghnad Saha"
                ],
                "answer": 1,
                "hint": "These scientists mapped India's insolation patterns in their book 'Solar Radiation Over India'.",
                "explanation": "Anna Mani and S. Rangarajan published the authoritative 1982 atlas 'Solar Radiation Over India', establishing quantitative benchmarks for Indian solar engineering."
            }
        ]
    },
    {
        "id": 4,
        "title": "Albedo & Surfaces",
        "subtitle": "Reflectance Dynamics & Urban Heat Islands",
        "speech": (
            "Not all solar radiation striking Earth is absorbed and converted into thermal energy. A significant fraction bounces "
            "directly back into space, quantified by a fundamental optical property called albedo. Albedo is the ratio of reflected "
            "solar radiation to total incident radiation, ranging from zero for a perfect absorber to one for a perfect reflector. "
            "In Activity 13.2, Table 13.1 highlights dramatic contrasts across natural landscapes. Fresh snow reflects eighty to "
            "ninety percent of incoming sunlight, having an albedo of zero point eight to zero point nine. Glacial ice reflects fifty "
            "to seventy percent, crushed rock reflects twenty-five to thirty percent, while dark ocean water and moist black soils "
            "absorb nearly ninety-five percent, reflecting only five to ten percent! This explains why polar ice caps remain bitterly "
            "cold while tropical oceans absorb massive amounts of heat. In human habitats, material choices alter microclimates. "
            "Traditional Indian homes built with mud, straw, and lime reflect sunlight and breathe naturally, whereas modern cities "
            "built of dark asphalt, dense concrete, and steel absorb enormous thermal energy. Re-radiating this heat at night creates "
            "the Urban Heat Island effect, raising city temperatures significantly above surrounding countryside! Use the simulator "
            "to adjust surface albedo and track localized heating."
        ),
        "checkpoints": [
            {
                "question": "Which of the following natural surfaces possesses the highest albedo?",
                "options": ["Deep ocean water", "Moist black cotton soil", "Freshly fallen snow", "Crushed basalt rock"],
                "answer": 2,
                "hint": "This bright white surface reflects 80% to 90% of incoming sunlight back into space.",
                "explanation": "Fresh snow has an albedo of 0.80 to 0.90, reflecting the vast majority of incident solar radiation, while oceans and dark soils absorb almost everything."
            },
            {
                "question": "What causes the Urban Heat Island effect in modern metropolitan cities?",
                "options": [
                    "Decreased gravity inside crowded urban zones",
                    "Low albedo concrete and asphalt absorbing and re-radiating heat",
                    "Increased plant transpiration in city parks",
                    "Higher atmospheric pressure over tall skyscrapers"
                ],
                "answer": 1,
                "hint": "Consider the thermal properties of dark building materials compared to natural vegetation.",
                "explanation": "Urban materials like asphalt and concrete have low albedo and high thermal mass, trapping heat and elevating city temperatures over rural surroundings."
            }
        ]
    },
    {
        "id": 5,
        "title": "Latitude & Seasons",
        "subtitle": "Planetary Geometry & Axial Tilt",
        "speech": (
            "Why is the equator sweltering hot while the north and south poles are locked in eternal ice? The answer lies in the "
            "spherical geometry of our planet! Because Earth is curved, solar rays do not strike all latitudes at the same angle. "
            "Near the equator, sunlight arrives nearly perpendicular to the surface. Perpendicular beams concentrate immense radiant "
            "energy over a very small surface footprint, while passing through a minimal atmospheric path length with little scattering. "
            "Moving toward higher latitudes and the poles, sunlight strikes at an increasingly shallow, oblique angle. The exact same "
            "amount of solar energy is forced to spread out over a much larger land area, while traversing a far thicker slice of "
            "atmosphere that scatters and weakens the beam! Furthermore, Earth does not spin upright; its rotational axis is tilted "
            "at twenty-three point five degrees relative to its orbital plane around the Sun. As Earth completes its annual revolution, "
            "this permanent axial tilt causes alternating hemispheres to lean toward the Sun, producing seasonal changes, shifting "
            "daytime lengths, and unequal thermal heating. This latitudinal thermal gradient is the master thermodynamic engine that "
            "drives planetary winds! Experiment with the simulator to alter orbital tilt and witness season changes."
        ),
        "checkpoints": [
            {
                "question": "Why do equatorial regions receive far more intense solar heating than polar regions?",
                "options": [
                    "The Sun is physically much closer to the equator",
                    "Solar rays strike at direct perpendicular angles over a smaller surface area",
                    "The equator possesses no atmospheric gases to block sunlight",
                    "The poles have stronger gravitational fields that repel heat"
                ],
                "answer": 1,
                "hint": "Direct sunlight concentrates energy over a compact area with less atmospheric scattering.",
                "explanation": "At the equator, solar rays arrive perpendicularly, concentrating energy over a small footprint; near the poles, oblique rays spread energy over a large area."
            },
            {
                "question": "What is the primary cause of changing seasons on Earth?",
                "options": [
                    "Changes in the distance between the Earth and the Sun during orbit",
                    "Earth's 23.5-degree axial tilt combined with its revolution around the Sun",
                    "Fluctuations in the Sun's internal nuclear fusion rate",
                    "Periodic reversals of Earth's magnetic poles"
                ],
                "answer": 1,
                "hint": "Earth's tilted axis points toward the Sun in summer and away in winter.",
                "explanation": "Earth's constant 23.5° axial tilt causes different hemispheres to receive direct sunlight at different points in its orbit, creating annual seasons."
            }
        ]
    },
    {
        "id": 6,
        "title": "Atmosphere's Layered Structure",
        "subtitle": "Thermal Inversions & Ramanathan's Legacy",
        "speech": (
            "Earth's atmosphere is a protective multi-layered envelope retained by gravity, composed of seventy-eight percent "
            "nitrogen, twenty-one percent oxygen, and trace gases like argon, carbon dioxide, and water vapor. Crucially, the atmosphere "
            "is stratified into distinct thermal layers based on temperature trends. The lowest layer, the troposphere, extends from "
            "sea level to approximately twelve kilometers. It contains seventy-five percent of all atmospheric mass and virtually all "
            "water vapor, making it the turbulent theatre for all clouds, storms, and weather! In the troposphere, temperature decreases "
            "steadily with altitude at an environmental lapse rate of about six point five degrees Celsius per kilometer. Above the "
            "tropopause lies the stratosphere, extending to fifty kilometers. Here, temperature reverses and increases with height "
            "because the ozone layer absorbs lethal solar ultraviolet radiation, creating a stable thermal inversion that suppresses "
            "vertical turbulence. In 1934, distinguished Indian meteorologist K. R. Ramanathan performed historic pioneering measurements of "
            "atmospheric ozone at eighteen thousand feet in the Himalayas, advancing global atmospheric physics and Indian monsoon forecasting! "
            "Higher up, the mesosphere, thermosphere, and exosphere shield Earth from meteors, burning them up, and block harmful cosmic rays. "
            "Test the interactive simulator to launch a virtual weather balloon through each of these atmospheric strata."
        ),
        "checkpoints": [
            {
                "question": "In which atmospheric layer does virtually all weather, cloud formation, and rainfall occur?",
                "options": ["Stratosphere", "Mesosphere", "Troposphere", "Thermosphere"],
                "answer": 2,
                "hint": "It is the lowest, densest layer extending from the ground up to roughly 12 kilometers.",
                "explanation": "The troposphere contains ~75% of atmospheric mass and almost all water vapor, driving all planetary weather phenomena."
            },
            {
                "question": "Why does temperature increase with altitude in the stratosphere?",
                "options": [
                    "Because it is closer to the hot molten interior of Earth",
                    "Due to intense friction from high-speed passenger jet engines",
                    "Due to the absorption of solar ultraviolet radiation by the ozone layer",
                    "Because heavy greenhouse gases settle into the upper stratosphere"
                ],
                "answer": 2,
                "hint": "Ozone molecules absorb solar UV rays and convert that radiation into thermal energy.",
                "explanation": "Ozone (O₃) in the stratosphere absorbs high-energy UV radiation, causing an inversion where temperature rises with altitude."
            }
        ]
    },
    {
        "id": 7,
        "title": "Greenhouse & Ozone",
        "subtitle": "Thermal Equilibrium & The Montreal Protocol",
        "speech": (
            "Life on Earth exists within a delicate thermal balance governed by the natural greenhouse effect. Shortwave solar radiation "
            "passes easily through atmospheric gases and warms our continents and oceans. The warmed Earth re-emits this energy as longwave "
            "infrared radiation. Naturally occurring greenhouse gases—principally water vapor, carbon dioxide, and methane—absorb and "
            "re-radiate these infrared waves back downward toward the planetary surface. This natural insulating blanket elevates Earth's average surface temperature "
            "from a frozen minus eighteen degrees Celsius to a comfortable plus fifteen degrees Celsius! However, our planetary neighbor "
            "Venus warns us of the catastrophe of a runaway greenhouse effect, where a ninety-six percent carbon dioxide atmosphere "
            "traps extreme heat, elevating surface temperatures to four hundred and sixty degrees Celsius! Simultaneously, the stratospheric "
            "ozone layer acts as Earth's natural sunblock against hazardous radiation. In the late twentieth century, synthetic chlorofluorocarbons used in air "
            "conditioners escaped into the stratosphere, where solar ultraviolet rays released chlorine atoms that catalytically destroyed "
            "ozone, opening a seasonal hole over Antarctica. Recognizing this planetary crisis, the global community signed the 1987 "
            "Montreal Protocol, phasing out harmful chemicals and enabling gradual ozone recovery! Use the interactive widget to model "
            "greenhouse gas concentrations and observe planetary temperatures."
        ),
        "checkpoints": [
            {
                "question": "Without the natural greenhouse effect, what would Earth's average surface temperature be?",
                "options": ["0 °C", "-18 °C", "-50 °C", "+5 °C"],
                "answer": 1,
                "hint": "Without heat-trapping gases, Earth would be a frozen, uninhabitable ice ball.",
                "explanation": "Without greenhouse gases trapping infrared heat, Earth's radiative equilibrium would drop its average temperature to approximately -18 °C instead of +15 °C."
            },
            {
                "question": "Which international environmental treaty successfully phased out ozone-depleting chlorofluorocarbons?",
                "options": ["Kyoto Protocol", "Paris Agreement", "Montreal Protocol", "Ramsar Convention"],
                "answer": 2,
                "hint": "Adopted in 1987, it is widely considered the most successful global environmental treaty.",
                "explanation": "The 1987 Montreal Protocol mandated the phase-out of ozone-depleting substances like CFCs, successfully stabilizing the stratospheric ozone layer."
            }
        ]
    },
    {
        "id": 8,
        "title": "Local Mountain Breezes",
        "subtitle": "Thermal Pressure Gradients & Diurnal Cycles",
        "speech": (
            "Uneven thermal heating does not merely alter temperatures; it generates air pressure differences that set our atmosphere "
            "into motion! When air is heated, its molecules absorb kinetic energy, expand, become less dense, and rise upward, forming "
            "a localized low-pressure zone. Surrounding cooler, denser air naturally rushes in to replace it, creating wind. A classic "
            "demonstration occurs in rugged mountainous terrains like Shimla and Dehradun, producing diurnal mountain and valley breezes. "
            "During the daytime, steep sun-facing mountain slopes absorb intense solar radiation and heat up much faster than the shaded, "
            "sheltered valley floor. Warm air over the mountain slopes expands rapidly and ascends toward the summits. To balance this "
            "upward convection, cooler, denser air from the valley floor flows upward along the incline, establishing an anabatic or "
            "valley breeze. At nighttime, the thermodynamic cycle reverses completely! Under clear skies, elevated mountain slopes "
            "radiate thermal energy into space rapidly, chilling the mountain air. This cold, heavy air becomes dense and drains downward "
            "under gravity along the slopes into the valley floor, creating a katabatic or mountain breeze! Local topography and altitude "
            "thus profoundly govern regional microclimates. Use the interactive simulator to toggle between day and night, observing airflow vectors in Himalayan valleys."
        ),
        "checkpoints": [
            {
                "question": "What is the primary driving force behind localized valley breezes during the daytime?",
                "options": [
                    "Rapid gravitational sliding of dense cold air down mountain slopes",
                    "Mountain slopes heating faster than the valley floor, causing warm air to rise",
                    "Evaporation of glaciers pushing high-pressure air upward",
                    "Geothermal steam venting from deep underground mountain fissures"
                ],
                "answer": 1,
                "hint": "Sunlight warms slopes quickly, causing air to expand, rise, and draw valley air upward.",
                "explanation": "During daytime, mountain slopes warm faster than the valley floor; the rising warm air creates an upslope anabatic valley breeze."
            },
            {
                "question": "At nighttime, why does cold air flow down mountain slopes into valleys as a mountain breeze?",
                "options": [
                    "Cold air expands and pushes against surrounding atmosphere",
                    "Rapid radiational cooling makes mountain air dense, causing it to sink under gravity",
                    "Atmospheric ozone pulls nighttime air toward sea level",
                    "Plant transpiration in valleys pulls dry air down from the summits"
                ],
                "answer": 1,
                "hint": "Radiative cooling at high altitudes makes air dense and heavy, draining down like fluid.",
                "explanation": "High-altitude slopes lose heat rapidly at night, creating dense, chilled air that drains into the valley under gravity (katabatic breeze)."
            }
        ]
    }
]

if __name__ == "__main__":
    for s in slides_part1:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: title='{s['title']}' ({tw} words), speech={wc} words")
        assert 1 <= tw <= 3, f"Title length {tw} not 1-3 words"
        assert 195 <= wc <= 215, f"Speech length {wc} not 195-215 words"
        assert len(s["checkpoints"]) == 2, "Must have 2 checkpoints"
    print("Part 1 verified successfully!")
