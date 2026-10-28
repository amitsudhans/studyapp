# -*- coding: utf-8 -*-
"""
Class 8 Science - Chapter 13: Our Home: Earth, a Unique Life Sustaining Planet
Curriculum Dataset: 20 Slides, 32 Checkpoints, 40 Mastery Quiz Questions
Mentor Avatar: Dr. Kalpana Chawla (Astronaut & Aerospace Scientist)
"""

SLIDES_DATA = [
    # Slide 1 (13.1)
    {
        "id": 1,
        "title": "Earth: The Unique Living Oasis",
        "tag": "13.1 Why Is Earth Unique?",
        "narration": "Hello, young explorers of the cosmos! I am Dr. Kalpana Chawla. When you gaze down upon Earth from space, drifting in the silent, velvet blackness of the universe, you are struck by an overwhelming realization: our planet is a breathtaking, fragile blue jewel! Out of all the billions of celestial bodies in our solar system and beyond, Earth is the only known planet that harbors life! With sparkling liquid water oceans covering over seventy percent of its surface, a protective blanket of breathable air, and millions of thriving species, Earth is humanity's only home in the cosmos!",
        "points": [
            ("The 'Blue Planet' Identity", "Over 71% of Earth's surface is draped in liquid water oceans, reflecting vibrant blue light that distinguishes Earth from every other world in our solar system."),
            ("The Only Known Living World", "Earth sustains millions of diverse species—from microscopic deep-sea vent archaea to towering redwood trees and intelligent humans."),
            ("Four Interconnected Spheres", "Life thrives because of the dynamic harmony between the Lithosphere (land/rocks), Hydrosphere (liquid water), Atmosphere (gaseous envelope), and Biosphere (the zone of life)."),
        ],
        "fact": "Earth is the only planet in the Solar System not named after a Greek or Roman deity; its name originates from the Old English and Germanic word 'eorðe', meaning ground or soil!",
        "sim_id": "earth_unique_oasis_sim",
        "checkpoints": [
            {
                "question": "Why is planet Earth widely referred to as the 'Blue Planet' when viewed from space?",
                "options": [
                    "Its atmosphere is composed of pure liquid blue nitrogen",
                    "Liquid water oceans cover approximately 71% of its surface, scattering blue light",
                    "The entire land surface is covered in blue grass and flowers",
                    "Giant blue neon lights shine from all major cities"
                ],
                "correct": 1,
                "explanation": "Over 71% of Earth's surface is covered by vast liquid water oceans, which reflect sunlight and give Earth its iconic blue glow when viewed from space."
            },
            {
                "question": "Which of the four major spheres of Earth represents the entire global realm where living organisms exist?",
                "options": [
                    "Lithosphere",
                    "Hydrosphere",
                    "Biosphere",
                    "Atmosphere"
                ],
                "correct": 2,
                "explanation": "The Biosphere is the global ecological system integrating all living beings and their relationships across the lithosphere, hydrosphere, and atmosphere."
            }
        ]
    },
    # Slide 2 (13.2)
    {
        "id": 2,
        "title": "Planets of Our Solar System",
        "tag": "13.2 Solar System Neighbors",
        "narration": "To appreciate why Earth is so uniquely hospitable, let us journey across our planetary neighborhood! Our solar system hosts eight major planets divided into two groups: four inner rocky Terrestrial planets and four outer Jovian Gas and Ice Giants. Look at our neighbors: Mercury is airless, baking at 430 degrees Celsius by day and freezing at minus 180 at night. Venus is a suffocating furnace at 465 degrees with crushing carbon dioxide pressure and sulfuric acid clouds! Mars is a frozen desert with a thin, unbreathable atmosphere. Beyond lie Jupiter, Saturn, Uranus, and Neptune—immense storms of swirling gas with no solid ground to stand on!",
        "points": [
            ("Terrestrial Planets (Inner Rocky Worlds)", "Mercury, Venus, Earth, and Mars possess solid rocky silicate crusts and metallic cores."),
            ("Gas & Ice Giants (Outer Jovian Worlds)", "Jupiter and Saturn (Gas Giants of hydrogen/helium) and Uranus and Neptune (Ice Giants of water, ammonia, methane) lack solid surfaces."),
            ("Extreme Inhospitality Elsewhere", "Mercury has no atmosphere; Venus suffers a runaway greenhouse furnace ($465^\\circ\\text{C}$); Mars has sub-zero average temperatures ($-60^\\circ\\text{C}$) with negligible pressure; outer giants have crushing gravity and toxic atmospheres."),
        ],
        "fact": "Venus is hotter than Mercury, even though it is nearly twice as far from the Sun! Its runaway greenhouse atmosphere of 96% carbon dioxide traps solar heat so intensely that it could melt lead!",
        "sim_id": "solar_system_planets_sim",
        "checkpoints": [
            {
                "question": "Why is Venus the hottest planet in the Solar System, even hotter than Mercury which is closer to the Sun?",
                "options": [
                    "Venus has thousands of active nuclear volcanoes",
                    "Its dense atmosphere of 96% carbon dioxide creates an extreme runaway greenhouse effect that traps heat",
                    "Venus absorbs all cosmic rays from deep space",
                    "The Sun is physically closer to Venus during summer"
                ],
                "correct": 1,
                "explanation": "Venus's dense carbon dioxide atmosphere acts as an impenetrable thermal blanket, producing a runaway greenhouse effect that pushes surface temperatures to $465^\\circ\\text{C}$."
            },
            {
                "question": "Which group of planets in our solar system lacks any solid rocky surface to stand on?",
                "options": [
                    "Terrestrial planets (Mercury, Venus, Earth, Mars)",
                    "Gas and Ice Giants (Jupiter, Saturn, Uranus, Neptune)",
                    "Dwarf planets and asteroids",
                    "The inner rocky planets"
                ],
                "correct": 1,
                "explanation": "Jupiter, Saturn, Uranus, and Neptune are composed almost entirely of thick layers of hydrogen, helium, ammonia, and methane gases surrounding dense liquid or small icy cores, lacking any solid surface."
            }
        ]
    },
    # Slide 3 (13.3.1)
    {
        "id": 3,
        "title": "Earth's Position in the Goldilocks Zone",
        "tag": "13.3.1 Habitable Zone",
        "narration": "What is the secret behind Earth's hospitable climate? The first fundamental reason is planetary real estate: Earth orbits in the Goldilocks Zone—also scientifically known as the Circumstellar Habitable Zone! Just like the porridge in the fairy tale, Earth's distance from the Sun—approximately 150 million kilometers, or 1 Astronomical Unit—is neither too hot nor too cold, but 'just right'! If Earth were closer, like Venus, our oceans would boil into vapor; if we were further, like Mars, all water would freeze into solid ice!",
        "points": [
            ("Circumstellar Habitable Zone Defined", "The orbital region around a star where ambient temperatures allow liquid water to persist stably on a planetary surface under normal atmospheric pressure."),
            ("1 Astronomical Unit (150 Million km)", "Earth's average orbital distance from the Sun provides a moderate solar radiant energy flux (solar constant $\\approx 1361\\text{ W/m}^2$)."),
            ("Water as the Universal Solvent of Life", "Because Earth resides in this sweet spot, water exists in all three phases: liquid oceans (the cradle of biochemistry), solid polar ice caps (climate regulators), and gaseous water vapor (weather and rain)."),
        ],
        "fact": "Liquid water is considered essential for all known biochemistry because its polar molecular structure allows it to dissolve and transport a wider variety of nutrients and biological compounds than any other liquid!",
        "sim_id": "goldilocks_zone_sim",
        "checkpoints": [
            {
                "question": "What is the primary astronomical definition of the 'Goldilocks Zone' (Habitable Zone)?",
                "options": [
                    "A region of space where gold asteroids are abundant",
                    "The orbital distance from a host star where planetary temperatures permit liquid water to exist stably",
                    "The space between the Moon and the Earth",
                    "A zone where gravity equals exactly zero"
                ],
                "correct": 1,
                "explanation": "The Habitable Zone is the orbital band around a star where stellar irradiance allows water to remain in liquid form on a planet's surface."
            },
            {
                "question": "What would happen to Earth's oceans if our planet were moved to the orbital position of Venus (0.72 AU from the Sun)?",
                "options": [
                    "The oceans would freeze into solid glaciers",
                    "The oceans would evaporate and boil away into steam due to extreme solar irradiance",
                    "The oceans would turn into liquid neon",
                    "The ocean level would rise by 500 meters without evaporating"
                ],
                "correct": 1,
                "explanation": "At Venus's distance, intense solar radiation would vaporize Earth's oceans, triggering a catastrophic runaway greenhouse effect."
            }
        ]
    },
    # Slide 4 (13.3.2)
    {
        "id": 4,
        "title": "Earth's Optimal Size & Gravity",
        "tag": "13.3.2 Planetary Size",
        "narration": "Position alone is not enough—a planet must also possess the proper size and mass! Earth's equatorial diameter of 12,742 kilometers and mass of nearly six sextillion metric tons generate an optimal surface gravitational acceleration of 9.8 meters per second squared. This surface gravity produces an escape velocity of 11.2 kilometers per second. This is strong enough to hold onto vital gases like nitrogen, oxygen, and water vapor, while allowing light, non-reactive hydrogen and helium to escape into space!",
        "points": [
            ("Optimal Planetary Mass", "Earth's mass generates sufficient surface gravity ($g = 9.8\\text{ m/s}^2$) to retain a protective, 100-km-thick atmospheric blanket."),
            ("Why the Moon and Mercury are Airless", "Smaller bodies have weak gravity (Moon's $g = 1.6\\text{ m/s}^2$, escape velocity $2.4\\text{ km/s}$); gas molecules easily reach thermal speeds and leak away into space."),
            ("Why Giant Planets are Inhospitable", "Massive gas giants like Jupiter ($g = 24.8\\text{ m/s}^2$) hold onto crushing atmospheres of dense hydrogen and methane, creating pressures millions of times higher than Earth's surface."),
        ],
        "fact": "Mars has only about 11% of Earth's mass. Because of its weak gravity, Mars lost most of its early thick atmosphere to space over billions of years, leaving a surface pressure less than 1% of Earth's!",
        "sim_id": "earth_size_gravity_sim",
        "checkpoints": [
            {
                "question": "Why is the Moon unable to retain an atmosphere like the Earth?",
                "options": [
                    "The Moon has too many craters",
                    "Its mass and surface gravity are too weak to prevent energetic gas molecules from escaping into space",
                    "The Moon is too cold for gases to exist",
                    "Solar wind pushes the Moon away from all gases"
                ],
                "correct": 1,
                "explanation": "Because the Moon's mass is only about 1/81 that of Earth, its escape velocity is low (2.4 km/s), allowing gas molecules to easily leak into outer space."
            },
            {
                "question": "What is the approximate Escape Velocity required to break free from Earth's gravitational pull?",
                "options": [
                    "1.6 km/s",
                    "5.5 km/s",
                    "11.2 km/s",
                    "60.0 km/s"
                ],
                "correct": 2,
                "explanation": "Earth's escape velocity from its surface is approximately 11.2 kilometers per second (about 40,300 km/h)."
            }
        ]
    },
    # Slide 5 (13.3.3)
    {
        "id": 5,
        "title": "Earth's Magnetic Shield (Magnetosphere)",
        "tag": "13.3.3 Planetary Magnetism",
        "narration": "Deep beneath our feet, nearly 3,000 kilometers down, lies a churning ocean of liquid iron and nickel: Earth's outer core! Convection currents in this molten metal, spun by Earth's rapid 24-hour rotation, function as a colossal dynamo generating an invisible planetary magnetic shield: the Magnetosphere! This magnetic bubble reaches tens of thousands of kilometers into space, deflecting lethal streams of charged plasma blasted by the Sun—the Solar Wind—and channeling energetic particles into spectacular polar Auroras!",
        "points": [
            ("The Geodynamo Mechanism", "Convection currents of electrical conducting molten iron-nickel in Earth's outer core create a massive magnetic dipole field."),
            ("Solar Wind Deflection", "The Sun continuously ejects high-energy ionized protons and electrons at 400 to 800 km/s. The magnetosphere acts as a cosmic forcefield, deflecting these particles safely around Earth."),
            ("Atmospheric & Ozone Preservation", "Without a magnetic field, the solar wind would physically strip away Earth's upper atmosphere and water vapor (as happened to Mars after its core cooled and solidified)."),
            ("Auroras (Northern & Southern Lights)", "Energetic charged particles guided along magnetic field lines collide with nitrogen and oxygen atoms in the upper atmosphere, producing ethereal green, purple, and red glowing lights."),
        ],
        "fact": "Billions of years ago, Mars had a liquid outer core and a magnetic field. When its smaller interior cooled and its geodynamo died, solar winds stripped away its thick atmosphere and evaporated its lakes!",
        "sim_id": "geomagnetic_shield_sim",
        "checkpoints": [
            {
                "question": "What generates Earth's planetary magnetic field (Magnetosphere)?",
                "options": [
                    "Giant permanent bar magnets buried in the Himalayan mountains",
                    "Convection currents of molten iron and nickel in Earth's outer core (the geodynamo)",
                    "Electrical currents produced by ocean tides",
                    "The rotation of the Moon around Earth"
                ],
                "correct": 1,
                "explanation": "Earth's magnetic field is generated by the geodynamo mechanism: swirling convection of electrically conducting molten iron and nickel in the outer core."
            },
            {
                "question": "What would happen to Earth's atmosphere if our planet completely lost its magnetic field?",
                "options": [
                    "The atmosphere would freeze into solid nitrogen ice",
                    "Solar wind plasma would strip away the upper atmosphere and erode the ozone layer over time",
                    "Gravity would instantly drop to zero",
                    "The Sun would stop emitting light"
                ],
                "correct": 1,
                "explanation": "Without the magnetic shield to deflect the charged solar wind, our atmosphere would be stripped away and water molecules split and lost, similar to the fate of Mars."
            }
        ]
    },
    # Slide 6 (13.4.1)
    {
        "id": 6,
        "title": "Air, Water, and Sunlight",
        "tag": "13.4.1 Life Support Pillars",
        "narration": "Life on Earth is sustained by three magnificent abiotic gifts: air, water, and sunlight! Our atmosphere consists of 78% nitrogen (which dilutes oxygen and provides protein building blocks), 21% life-giving oxygen for cellular respiration, and 0.04% carbon dioxide for plant photosynthesis. Trace greenhouse gases trap infrared heat, keeping Earth at a comfortable average temperature of +15 degrees Celsius instead of a frigid -18 degrees! Meanwhile, the global water cycle circulates fresh water across continents, energized by solar photons!",
        "points": [
            ("Breathable Atmospheric Composition", "78% Nitrogen ($N_2$), 21% Oxygen ($O_2$), 0.9% Argon ($Ar$), and 0.04% Carbon Dioxide ($CO_2$), protected by a stratospheric ozone ($O_3$) UV-absorption layer."),
            ("The Natural Greenhouse Thermostat", "Water vapor and $CO_2$ trap outbound thermal radiation, raising global mean temperature from $-18^\\circ\\text{C}$ (frozen ice ball) to a hospitable $+15^\\circ\\text{C}$."),
            ("The Dynamic Hydrological Cycle", "Solar energy evaporates ocean water; condensation produces clouds; precipitation deposits pure fresh water onto land, nourishing river basins and aquifers."),
        ],
        "fact": "The stratospheric Ozone Layer ($O_3$), located 15 to 35 km above the surface, absorbs over 98% of the Sun's harmful, high-frequency ultraviolet (UV-B and UV-C) rays, preventing lethal DNA damage to terrestrial life!",
        "sim_id": "air_water_sunlight_sim",
        "checkpoints": [
            {
                "question": "What would Earth's average global temperature be WITHOUT the natural greenhouse effect of water vapor and carbon dioxide?",
                "options": [
                    "+100°C (boiling hot)",
                    "Approximately -18°C (frozen ice ball)",
                    "Absolute Zero (-273°C)",
                    "+50°C (tropical desert everywhere)"
                ],
                "correct": 1,
                "explanation": "Without the natural greenhouse effect trapping heat, Earth's average surface temperature would plummet to approximately $-18^\\circ\\text{C}$, freezing all oceans solid."
            },
            {
                "question": "Which atmospheric gas shields life on Earth's surface by absorbing lethal ultraviolet (UV) radiation from the Sun?",
                "options": [
                    "Nitrogen gas ($N_2$)",
                    "Stratospheric Ozone ($O_3$)",
                    "Methane ($CH_4$)",
                    "Helium ($He$)"
                ],
                "correct": 1,
                "explanation": "The stratospheric ozone layer ($O_3$) absorbs high-energy UV radiation, safeguarding living cells from fatal genetic damage and skin cancers."
            }
        ]
    },
    # Slide 7 (13.4.2)
    {
        "id": 7,
        "title": "Soil, Rocks, and Essential Minerals",
        "tag": "13.4.2 The Lithosphere",
        "narration": "Beneath the green carpet of vegetation lies the solid crust of Earth: the Lithosphere! Over millions of years, physical weathering by rain, frost, and wind—coupled with biological action by lichens and roots—grinds barren rock into fertile, life-giving Soil! Soil is far more than mere dirt; it is a living biogeochemical pharmacy containing essential minerals like calcium for animal bones, iron for red blood hemoglobin, phosphorus for DNA and cell membranes, and potassium for nerve signals!",
        "points": [
            ("Soil Genesis by Weathering", "Physical, chemical, and biological breakdown of parent bedrock into fine mineral particles mixed with decomposing organic humus."),
            ("Soil Horizon Profile", "O-Horizon (organic litter) $\\rightarrow$ A-Horizon (nutrient-rich topsoil) $\\rightarrow$ B-Horizon (subsoil mineral accumulation) $\\rightarrow$ C-Horizon (partially weathered rock) $\\rightarrow$ R-Horizon (solid bedrock)."),
            ("Essential Mineral Reservoirs", "Rocks weather to release phosphorus ($PO_4^{3-}$), potassium ($K^+$), calcium ($Ca^{2+}$), magnesium ($Mg^{2+}$), and iron ($Fe^{2+}$), which dissolve in soil water and enter food webs via plant roots."),
        ],
        "fact": "It takes nature between 200 and 1,000 years to form just one single centimeter of fertile agricultural topsoil from weathered rock!",
        "sim_id": "soil_lithosphere_minerals_sim",
        "checkpoints": [
            {
                "question": "Roughly how long does it take natural ecological weathering to form just 1 centimeter of fertile agricultural topsoil?",
                "options": [
                    "1 to 2 weeks",
                    "About 1 year",
                    "200 to 1,000 years",
                    "Over 100 million years"
                ],
                "correct": 2,
                "explanation": "Topsoil formation is an extremely slow geological process taking several centuries (200 to 1,000 years per centimeter) of rock weathering and organic matter accumulation."
            },
            {
                "question": "Which vital mineral essential for building human bones and teeth is originally derived from weathered rock minerals in the soil?",
                "options": [
                    "Calcium",
                    "Argon",
                    "Lead",
                    "Mercury"
                ],
                "correct": 0,
                "explanation": "Calcium is weathered from rocks (like limestone and gypsum) into soil water, taken up by crops and fodder, and incorporated into human bones and teeth."
            }
        ]
    },
    # Slide 8 (13.4.3)
    {
        "id": 8,
        "title": "The Living Web: Microbes, Plants & Animals",
        "tag": "13.4.3 Biosphere Harmony",
        "narration": "Life on Earth is not a chaotic free-for-all; it is a masterfully choreographed symphony of three great biological kingdoms! Autotrophic plants act as the food producers: using sunlight, they manufacture billions of tons of glucose and oxygen. Heterotrophic animals act as consumers: grazing foliage, dispersing seeds, pollinating flowers, and transferring energy across food chains. And microscopic decomposers—bacteria and fungi—break down every fallen leaf and carcass, unlocking minerals to restart the perpetual cycle!",
        "points": [
            ("Producers (Autotrophic Foundation)", "Terrestrial plants, phytoplankton, and algae convert solar irradiance into edible chemical biomass and oxygen through photosynthesis."),
            ("Consumers (Heterotrophic Transfer)", "Herbivores consume plant biomass; carnivores control herbivore numbers; pollinators (bees, bats, birds) ensure floral cross-reproduction."),
            ("Decomposers (The Nutrient Resettlers)", "Microscopic bacteria and saprophytic fungi hydrolyze complex dead organic molecules into simple inorganic nitrates, phosphates, and $CO_2$."),
        ],
        "fact": "Over 50% of the oxygen you breathe does not come from land forests, but from microscopic marine phytoplankton (like diatoms and cyanobacteria) drifting in the sunlit surface waters of the ocean!",
        "sim_id": "biosphere_web_sim",
        "checkpoints": [
            {
                "question": "Where does more than 50% of the world's atmospheric oxygen supply originate?",
                "options": [
                    "From subterranean fungal caves",
                    "From microscopic marine phytoplankton drifting in ocean surface waters",
                    "From industrial oxygen factories",
                    "From volcanic steam vents"
                ],
                "correct": 1,
                "explanation": "Marine phytoplankton and ocean microalgae produce over half of Earth's oxygen via photosynthesis in surface waters."
            },
            {
                "question": "What is the primary ecological contribution of microscopic decomposers (bacteria and fungi)?",
                "options": [
                    "They hunt living birds in the canopy",
                    "They break down dead organic matter and recycle locked mineral nutrients back into the soil for plants",
                    "They absorb oxygen and create heavy stones",
                    "They stop all plant photosynthesis"
                ],
                "correct": 1,
                "explanation": "Decomposers break down dead biomass into simple inorganic ions, closing the nutrient cycle and preventing ecological stagnation."
            }
        ]
    },
    # Slide 9 (13.4.4)
    {
        "id": 9,
        "title": "The Importance of Natural Balance",
        "tag": "13.4.4 Dynamic Homeostasis",
        "narration": "Have you ever wondered why oxygen levels in our atmosphere remain near 21% and carbon dioxide near 0.04% year after year? Because Earth functions as a self-regulating, living planetary super-organism maintaining Dynamic Balance—or Homeostasis! Plants consume carbon dioxide and exhale oxygen during the day; all living things consume oxygen and exhale carbon dioxide during respiration. When human industrial chimneys and automobiles burn billions of tons of ancient fossil fuels, this delicate seesaw balance is destabilized!",
        "points": [
            ("Atmospheric Gas Homeostasis", "Photosynthesis ($6CO_2 + 6H_2O \\rightarrow C_6H_{12}O_6 + 6O_2$) perfectly balances cellular respiration ($C_6H_{12}O_6 + 6O_2 \\rightarrow 6CO_2 + 6H_2O$)."),
            ("The Carbon-Oxygen Seesaw", "Vegetation absorbs approximately 30% of anthropogenic $CO_2$ emissions annually, while oceans dissolve another 25%, buffering global temperature surges."),
            ("Anthropogenic Disruption", "Excessive combustion of ancient fossil coal, oil, and methane releases stored carbon millions of times faster than natural geological cycles can absorb it."),
        ],
        "fact": "British scientist James Lovelock formulated the 'Gaia Hypothesis' in the 1970s, proposing that living organisms interact with their inorganic surroundings to form a synergistic, self-regulating planetary system that maintains conditions for life!",
        "sim_id": "carbon_oxygen_balance_sim",
        "checkpoints": [
            {
                "question": "Which two complementary biological processes maintain the stable balance between Oxygen and Carbon Dioxide in Earth's atmosphere?",
                "options": [
                    "Combustion and Evaporation",
                    "Photosynthesis and Cellular Respiration",
                    "Transpiration and Condensation",
                    "Precipitation and Sublimation"
                ],
                "correct": 1,
                "explanation": "Photosynthesis produces oxygen while consuming carbon dioxide; cellular respiration consumes oxygen while releasing carbon dioxide, maintaining planetary equilibrium."
            },
            {
                "question": "What happens when humans burn billions of barrels of fossil fuels while simultaneously clearing vast tropical forests?",
                "options": [
                    "Atmospheric oxygen doubles instantly",
                    "Atmospheric carbon dioxide levels rise, trapping excess heat and driving global climate change",
                    "Earth's orbit around the Sun speeds up",
                    "The oceans lose all their salt"
                ],
                "correct": 1,
                "explanation": "Fossil fuel burning releases trapped carbon while deforestation reduces $CO_2$ absorption, tipping the balance and driving accelerated global warming."
            }
        ]
    },
    # Slide 10 (13.5.1)
    {
        "id": 10,
        "title": "Asexual Reproduction: Rapid Propagation",
        "tag": "13.5.1 Asexual Reproduction",
        "narration": "What prevents life on Earth from vanishing into extinction? Individual organisms are mortal—they age, succumb to predators, or perish from illness. Life survives across millions of years through Reproduction: the biological creation of new offspring! In Asexual Reproduction, a single parent produces genetically identical offspring without the involvement of gametes or fertilization. It is rapid, efficient, and requires no mate! Single-celled Amoeba divide by binary fission, Hydra produce buds, potatoes sprout from eye buds, and bread molds release millions of hardy spores!",
        "points": [
            ("Single Parent Inheritance", "Offspring inherit 100% of their genetic information from a single parent organism, creating biological clones."),
            ("Binary Fission in Bacteria & Amoeba", "The parent cell replicates its DNA and divides into two equal, fully formed daughter cells in under 20 minutes!"),
            ("Budding in Hydra & Yeast", "A small outward bulge (bud) develops by repetitive cell division, grows into a miniature individual, and detaches to live independently."),
            ("Vegetative Propagation", "Asexual reproduction in plants using vegetative parts (stem tubers in potatoes, rhizomes in ginger, leaf notches in Bryophyllum)."),
            ("Spore Formation in Fungi", "Microscopic, thick-walled protective spores produced in sporangia (like bread mold *Rhizopus*) drift in the air and germinate upon moist food."),
        ],
        "fact": "Under optimal temperature and nutrient conditions, a single bacterium dividing by binary fission every 20 minutes could theoretically produce a population of over 2 million bacteria in less than seven hours!",
        "sim_id": "asexual_reproduction_sim",
        "checkpoints": [
            {
                "question": "Which of the following is a fundamental characteristic of ASEXUAL reproduction?",
                "options": [
                    "It requires the fusion of male and female gametes",
                    "A single parent produces genetically identical offspring without fertilization",
                    "Offspring always display a wide variety of new genetic traits",
                    "It takes nine months of embryonic gestation"
                ],
                "correct": 1,
                "explanation": "Asexual reproduction involves only a single parent and produces genetically identical clones without the fusion of gametes."
            },
            {
                "question": "In which organism does asexual reproduction occur by 'Budding'—where an outgrowth develops on the parent body and detaches?",
                "options": [
                    "Human beings",
                    "Hydra and Yeast",
                    "Bengal tiger",
                    "Mango tree"
                ],
                "correct": 1,
                "explanation": "Hydra and single-celled yeast cells reproduce asexually by budding: developing an external bud that matures and separates from the parent."
            }
        ]
    },
    # Slide 11 (13.5.2)
    {
        "id": 11,
        "title": "Sexual Reproduction: Genetic Diversity",
        "tag": "13.5.2 Sexual Reproduction",
        "narration": "While asexual reproduction is fast, it produces identical clones with no genetic variety. What happens if a deadly new virus strikes? Clones could all perish together! Nature's genius solution is Sexual Reproduction! In sexual reproduction, two parents contribute specialized reproductive sex cells called gametes: a male sperm (or pollen grain in plants) and a female egg (ovum). When these two haploid cells fuse in fertilization, their chromosomes recombine to create a unique single-celled zygote. This genetic variation fuels evolution and enables species to survive changing environments!",
        "points": [
            ("Gametic Fusion (Fertilization)", "Male gamete ($n$, haploid) + Female gamete ($n$, haploid) $\\rightarrow$ Single-celled Zygote ($2n$, diploid)."),
            ("Genetic Recombination & Variation", "Offspring inherit a unique blend of traits from both mother and father; no two sexually reproduced offspring (except identical twins) are ever genetically alike."),
            ("Evolutionary Adaptability", "High genetic variation provides a biological reservoir of diverse traits, ensuring that some individuals survive novel diseases, droughts, or changing climates."),
        ],
        "fact": "In humans, the random crossing over of chromosomes during meiosis and fertilization can produce over 70 trillion unique genetic combinations from a single pair of parents!",
        "sim_id": "sexual_reproduction_sim",
        "checkpoints": [
            {
                "question": "What is the primary evolutionary advantage of SEXUAL reproduction over asexual reproduction?",
                "options": [
                    "It takes much less time and requires zero energy",
                    "It produces rich genetic variation among offspring, helping species adapt to diseases and changing environments",
                    "It eliminates the need for water in living cells",
                    "It produces 100% identical clones"
                ],
                "correct": 1,
                "explanation": "Sexual reproduction shuffles genes from two parents, creating unique genetic diversity that provides resistance against epidemics and environmental shifts."
            },
            {
                "question": "What is the single fertilized diploid cell formed by the fusion of a male sperm and a female ovum called?",
                "options": [
                    "Spore",
                    "Zygote",
                    "Bud",
                    "Pollen grain"
                ],
                "correct": 1,
                "explanation": "Fertilization produces a single-celled diploid ($2n$) entity termed the Zygote, which subsequently divides by mitosis to form an embryo."
            }
        ]
    },
    # Slide 12 (13.5)
    {
        "id": 12,
        "title": "Reproduction: The Generational Bridge",
        "tag": "13.5 Continuity of Life",
        "narration": "Step back and view the grand tapestry of geological time! Four billion years ago, the first microscopic single-celled microbes emerged in Earth's primeval oceans. Every single living organism alive today—from the sparrow perched on your windowsill to the grass under your feet—is connected to those primordial ancestors through an unbroken, four-billion-year chain of reproduction! Individual organisms are ephemeral mortal messengers, but reproduction is the immortal generational bridge that prevents life from disappearing!",
        "points": [
            ("Unbroken 4-Billion-Year Continuum", "Every living cell today was generated by pre-existing cells through an uninterrupted chain of reproductive cell division (*Omnis cellula e cellula*)."),
            ("Species Perpetuation", "Birth rates must balance or exceed mortality rates; if a species fails to reproduce successfully across successive generations, it enters the irreversible abyss of extinction."),
            ("Generational Information Transfer", "DNA (deoxyribonucleic acid) functions as the molecular instruction manual, replicating and passing genetic codes from generation to generation."),
        ],
        "fact": "All life on Earth shares the exact same fundamental genetic code—the four nucleotide bases Adenine (A), Thymine (T), Guanine (G), and Cytosine (C)—proving our universal common ancestry!",
        "sim_id": "reproduction_continuity_sim",
        "checkpoints": [
            {
                "question": "What would happen to any species if ALL its living members permanently stopped reproducing?",
                "options": [
                    "The individuals would live forever",
                    "The species would inevitably decline and become completely extinct as current individuals die",
                    "The species would transform into another animal immediately",
                    "Nothing would change in its population"
                ],
                "correct": 1,
                "explanation": "Reproduction is the sole biological mechanism for replacing deceased individuals; without it, population numbers fall to zero and extinction is permanent."
            },
            {
                "question": "Which master molecular chemical carries the genetic blueprint of life passed from parents to offspring during reproduction?",
                "options": [
                    "DNA (Deoxyribonucleic Acid)",
                    "Sulfuric Acid",
                    "Sodium Chloride",
                    "Calcium Hydroxide"
                ],
                "correct": 0,
                "explanation": "DNA contains the hereditary chemical code that directs cellular development, metabolism, and traits across generations."
            }
        ]
    },
    # Slide 13 (13.6)
    {
        "id": 13,
        "title": "The Threat of Climate Change & Global Warming",
        "tag": "13.6 Threats to Life",
        "narration": "Today, our precious planetary home faces unprecedented perils driven by human activities! The foremost global threat is Climate Change and the Enhanced Greenhouse Effect. Over the past century, industrial factories, coal-fired power stations, and billions of automobiles have poured hundreds of billions of tons of carbon dioxide, methane, and nitrous oxide into the atmosphere. This excess blanket traps thermal radiation, causing global temperatures to spike, polar glaciers to retreat, sea levels to rise, and triggering devastating heatwaves, unseasonal droughts, and super-cyclones!",
        "points": [
            ("Enhanced Greenhouse Effect", "Pre-industrial $CO_2$ levels were ~280 ppm; human fossil fuel burning has pushed atmospheric concentrations beyond 425 ppm—higher than any time in the past 3 million years!"),
            ("Melting Cryosphere & Rising Oceans", "Himalayan glaciers (the 'Water Towers of Asia') and polar ice sheets in Greenland and Antarctica are melting at record rates, raising global sea levels and threatening coastal megacities."),
            ("Extreme Weather Amplification", "Higher thermal energy in atmospheric and oceanic systems supercharges monsoonal storms, fuels catastrophic flash floods, and prolongs agricultural droughts."),
        ],
        "fact": "Over the past 50 years, the Arctic has been warming nearly four times faster than the global average—a dangerous climate phenomenon known as Arctic Amplification!",
        "sim_id": "greenhouse_global_warming_sim",
        "checkpoints": [
            {
                "question": "What is the primary cause of modern human-induced global warming?",
                "options": [
                    "Increased heat generated by the Earth's molten core",
                    "Massive emissions of greenhouse gases ($CO_2$, methane) from burning fossil fuels like coal, petrol, and gas",
                    "The Sun moving closer to the Earth every decade",
                    "The friction of satellites orbiting in space"
                ],
                "correct": 1,
                "explanation": "The burning of ancient fossil fuels releases billions of tons of $CO_2$ and $CH_4$ annually, intensifying the greenhouse effect and trapping excess heat."
            },
            {
                "question": "Why is the rapid melting of Himalayan glaciers a catastrophic threat to hundreds of millions of people in South Asia?",
                "options": [
                    "The glaciers are made of dangerous salt",
                    "Himalayan glaciers feed major perennial river systems (Ganga, Indus, Brahmaputra) providing freshwater for drinking and agricultural food security",
                    "The mountains will sink below sea level",
                    "Melting glaciers stop the rotation of the Earth"
                ],
                "correct": 1,
                "explanation": "The Himalayan cryosphere feeds rivers that supply freshwater to over 1.5 billion people; glacier retreat threatens seasonal water supply and agriculture."
            }
        ]
    },
    # Slide 14 (13.6)
    {
        "id": 14,
        "title": "Deforestation & The Biodiversity Crisis",
        "tag": "13.6 Habitat Destruction",
        "narration": "Every two seconds, an area of forest the size of a football field is cleared somewhere on Earth! Forests are Earth's living lungs and the cradle of terrestrial biodiversity. When forests are razed for commercial logging, monoculture palm oil plantations, and cattle ranches, wildlife habitats are violently fragmented. Driven from their homes, countless species face extinction. Scientists warn that humanity is triggering the Sixth Mass Extinction in planetary history—with species vanishing at hundreds of times the natural background extinction rate!",
        "points": [
            ("Rampant Deforestation", "Approximately 10 to 15 billion trees are cut down worldwide every year, transforming biodiverse tropical canopies into degraded pastureland."),
            ("Habitat Fragmentation & Edge Effects", "Chopping continuous forests into isolated patches divides wildlife populations, halts genetic exchange, and exposes animals to poachers and vehicular collisions."),
            ("The Sixth Mass Extinction Event", "Over one million animal and plant species face imminent extinction within decades due to human habitat destruction, overexploitation, and invasive species."),
        ],
        "fact": "The five previous mass extinctions in Earth's history (including the asteroid impact that ended the dinosaurs 66 million years ago) were caused by natural cosmic and geological cataclysms; the Sixth Mass Extinction is the first caused entirely by a single biological species: humans!",
        "sim_id": "deforestation_biodiversity_loss_sim",
        "checkpoints": [
            {
                "question": "What is the primary driving cause behind the accelerating extinction of terrestrial animal species worldwide?",
                "options": [
                    "Natural aging of the animals",
                    "Destruction and fragmentation of natural forest habitats by human expansion",
                    "Meteor showers hitting animal burrows",
                    "Animals forgetting how to find food"
                ],
                "correct": 1,
                "explanation": "Habitat loss through deforestation, agricultural conversion, and urban sprawl is the leading driver of species endangerment and extinction globally."
            },
            {
                "question": "What is meant by 'Habitat Fragmentation' in wildlife conservation?",
                "options": [
                    "Splitting a large contiguous forest into smaller, isolated patches separated by roads, farms, and cities",
                    "Animals migrating together to new continents",
                    "Planting trees along roadsides",
                    "Animals building smaller nests"
                ],
                "correct": 0,
                "explanation": "Habitat fragmentation divides large natural habitats into disconnected fragments, disrupting migration, gene flow, and breeding for large wildlife."
            }
        ]
    },
    # Slide 15 (13.6)
    {
        "id": 15,
        "title": "Pollution: Choking Air, Water & Soil",
        "tag": "13.6 Pollution Crisis",
        "narration": "Beyond climate change and habitat loss, humanity's synthetic wastes are poisoning the planet's life-support veins! Our skies are choked with microscopic particulate matter ($PM_{2.5}$) and toxic smog from industrial chimneys and vehicular tailpipes. Our sacred rivers and oceans are choked with millions of tons of non-biodegradable single-use plastics, toxic industrial heavy metals, and untreated sewage. And chemical pesticides and synthetic fertilizers sprayed on farmlands kill beneficial earthworms, poison pollinators, and leach into drinking water!",
        "points": [
            ("Air Smog & Toxic Particulates ($PM_{2.5}$)", "Microscopic particles smaller than 2.5 micrometers bypass nasal filters, penetrating deep into human lung alveoli and bloodstream, causing cardiovascular disease."),
            ("Plastic Ocean Pollution Crisis", "Over 14 million metric tons of plastic enter oceans annually; UV radiation breaks plastic down into microscopic microplastics, which bioaccumulate up marine food webs into human food!"),
            ("Chemical Soil Contamination", "Excessive synthetic chemical pesticides and fertilizers kill beneficial soil bacteria and earthworms, causing groundwater nitrate toxicity and aquatic eutrophication dead zones."),
        ],
        "fact": "Plastic takes between 400 and 1,000 years to decompose in nature! Virtually every piece of non-recycled plastic ever manufactured since the 1950s still exists somewhere on Earth today!",
        "sim_id": "pollution_threats_sim",
        "checkpoints": [
            {
                "question": "Why are fine particulate matter particles known as $PM_{2.5}$ so hazardous to human respiratory health?",
                "options": [
                    "They are too large to breathe in",
                    "They are microscopic (under 2.5 µm), allowing them to bypass nasal filters, penetrate deep into lung alveoli, and enter the bloodstream",
                    "They make your teeth turn green",
                    "They are made of heavy iron bars"
                ],
                "correct": 1,
                "explanation": "Because $PM_{2.5}$ particles are microscopic (under 2.5 micrometers), they evade natural upper-respiratory defense mechanisms and enter pulmonary capillaries directly."
            },
            {
                "question": "Roughly how long does it take for a conventional petroleum-based plastic bottle to break down naturally in the environment?",
                "options": [
                    "2 to 3 days",
                    "About 1 month",
                    "400 to 1,000 years",
                    "It never breaks down at all under any conditions"
                ],
                "correct": 2,
                "explanation": "Conventional plastics have robust synthetic chemical polymer chains that resist biological enzymes, requiring 400 to 1,000 years to break down."
            }
        ]
    },
    # Slide 16 (13.6 & Summary)
    {
        "id": 16,
        "title": "Ecological Healing & Sustainable Living",
        "tag": "13.6 Ecological Conservation",
        "narration": "Is the future of Earth doomed? Absolutely not! The power to heal our planet rests in our hands! Across the world, humanity is awakening to ecological stewardship. By transitioning rapidly to clean renewable solar and wind energy, practicing agroforestry and sustainable farming, banishing single-use plastics in favor of circular recycling, restoring degraded forests, and designating protected wildlife corridors, we can regenerate Earth's living harmony. Remember: we did not inherit the Earth from our ancestors; we are borrowing it from our children!",
        "points": [
            ("Clean Renewable Energy Transition", "Replacing polluting coal and petroleum with solar photovoltaics, wind turbines, and green hydrogen eliminates fossil emissions at the source."),
            ("Reforestation & Agroforestry", "Planting native multi-species trees acts as natural carbon sinks, restores depleted water tables, and revitalizes lost wildlife corridors."),
            ("Circular Economy & Waste Elimination", "Adopting the 5 R's of sustainability: Refuse, Reduce, Reuse, Repurpose, and Recycle, striving for zero synthetic waste."),
            ("Protected Biosphere Sanctuaries", "Preserving biodiversity hotspots and national parks provides safe havens where endangered species and natural ecological balance can thrive undisturbed."),
        ],
        "fact": "In 2022, the United Nations General Assembly officially declared that access to a clean, healthy, and sustainable environment is a universal Human Right!",
        "sim_id": "ecological_healing_conservation_sim",
        "checkpoints": [
            {
                "question": "Which of the following actions directly helps in restoring Earth's natural ecological balance and curbing global warming?",
                "options": [
                    "Burning large quantities of coal in open fields",
                    "Massive reforestation using native tree species and transitioning to solar and wind clean energy",
                    "Dumping chemical plastic wastes into deep river channels",
                    "Cutting down all forest trees to build concrete parking lots"
                ],
                "correct": 1,
                "explanation": "Reforestation absorbs excess atmospheric $CO_2$ while clean renewable energy replaces greenhouse-gas emitting fossil fuels, healing the climate."
            },
            {
                "question": "What is the core principle of a 'Circular Economy' in environmental sustainability?",
                "options": [
                    "Throwing all waste into circular pits",
                    "Designing products so materials are continuously reused, repaired, and recycled, eliminating waste from entering landfills",
                    "Making cars that only drive in circles",
                    "Using plastic once and burying it immediately"
                ],
                "correct": 1,
                "explanation": "A circular economy mimics nature's closed loops by designing products for durability, reuse, and complete recycling, eliminating wasteful extraction and disposal."
            }
        ]
    },
    # Slide 17: Mastery Challenge Part I
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "tag": "Earth's Uniqueness & Solar System",
        "narration": "Welcome to Part 1 of your Earth & Planetary Science Mastery Challenge! Test your deep understanding of Earth's unique living status, comparative planetary conditions, the Goldilocks Habitable Zone, and planetary mass/gravity dynamics.",
        "points": [
            ("Questions 1 to 10", "Covering Earth's 71% liquid ocean cover, planetary spheres, Venus's runaway greenhouse effect, terrestrial vs Jovian planets, Goldilocks Zone distance, and atmospheric escape velocity."),
            ("Real-Time Assessment", "Select your answer and view immediate feedback. Score points as you advance through the challenge!"),
            ("Step-by-Step Insights", "Click 'View Step-by-Step Solution' on any question to examine detailed astronomical equations and planetary data."),
        ],
        "fact": "Tip: Earth's 1 AU orbital distance and 11.2 km/s escape velocity are the twin physical guardians that keep our water liquid and our atmosphere intact!",
        "sim_id": "mastery_quiz_1",
        "is_quiz": True,
        "quiz_range": (1, 10)
    },
    # Slide 18: Mastery Challenge Part II
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "tag": "Magnetic Shield & Life Support Systems",
        "narration": "Welcome to Part 2! Here we explore Earth's geodynamo magnetic shield, deflecting the solar wind, the composition of our atmosphere, the natural greenhouse effect, and soil genesis from rock weathering.",
        "points": [
            ("Questions 11 to 20", "Investigating outer core liquid iron convection, magnetosphere deflection, ozone UV absorption, natural $-18^\\circ\\text{C}$ vs $+15^\\circ\\text{C}$ thermostat, and lithospheric mineral weathering."),
            ("Sharp Conceptual Focus", "Differentiate clearly between beneficial natural greenhouse warming and harmful anthropogenic climate disruption."),
            ("Interactive Modal Solutions", "Full explanations with geological and physical principles are available via the solution popup modal."),
        ],
        "fact": "Tip: Without the molten iron geodynamo, solar wind would strip our atmosphere just like it did on Mars!",
        "sim_id": "mastery_quiz_2",
        "is_quiz": True,
        "quiz_range": (11, 20)
    },
    # Slide 19: Mastery Challenge Part III
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "tag": "Biosphere Harmony & Reproduction",
        "narration": "Welcome to Part 3! Dive into the biological engines of Earth: producers, consumers, decomposers, gas homeostasis, and the reproductive mechanisms that prevent life from disappearing.",
        "points": [
            ("Questions 21 to 30", "Covering ocean phytoplankton oxygen generation, carbon-oxygen balance, binary fission, budding in Hydra, sexual gametic fertilization, and genetic diversity in adaptation."),
            ("Evolutionary Significance", "Understand why sexual reproduction is nature's superpower for long-term species survival against shifting environmental threats."),
            ("Comprehensive Solutions", "Click the solution button to review genetic recombination steps and biological equations."),
        ],
        "fact": "Tip: Asexual reproduction produces identical clones rapidly, while sexual reproduction produces diverse variations for evolution!",
        "sim_id": "mastery_quiz_3",
        "is_quiz": True,
        "quiz_range": (21, 30)
    },
    # Slide 20: Mastery Challenge Part IV
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "tag": "Planetary Threats & Ecological Healing",
        "narration": "Congratulations on reaching the final frontier! In Part 4, master the critical modern environmental threats facing our planet—global warming, deforestation, plastic pollution, biodiversity crisis—and explore the inspiring solutions for sustainable ecological healing!",
        "points": [
            ("Questions 31 to 40", "Exploring $CO_2$ atmospheric greenhouse trapping, melting Himalayan cryospheres, habitat fragmentation, microplastics, circular economies, and renewable energy conservation."),
            ("Chapter Completion", "Submit your final answers to view your aggregate mastery score across all 40 questions!"),
            ("Detailed Step-by-Step Keys", "Full explanations provided for every climate science and environmental conservation challenge."),
        ],
        "fact": "Celebration: Upon completing Slide 20, you have mastered the entire curriculum of NCERT Class 8 Science Chapter 13: Our Home: Earth, a Unique Life Sustaining Planet!",
        "sim_id": "mastery_quiz_4",
        "is_quiz": True,
        "quiz_range": (31, 40)
    }
]

# 40 Mastery Quiz Questions
QUIZ_QUESTIONS = [
    # Q1
    {
        "id": 1,
        "question": "What percentage of Earth's surface is covered by liquid water oceans, earning it the title of the 'Blue Planet'?",
        "options": [
            "About 29%",
            "About 50%",
            "Approximately 71%",
            "Over 95%"
        ],
        "correct": 2,
        "solution": "Step 1: Approximately 71% of Earth's surface area (roughly 361 million sq km out of 510 million sq km) is submerged beneath liquid oceans and seas.\nStep 2: When viewed from space, these liquid water reservoirs absorb red wavelengths and scatter blue light, imparting Earth's signature sapphire blue appearance.\nConclusion: Approximately 71%."
    },
    # Q2
    {
        "id": 2,
        "question": "Which of the following planets is characterized by a runaway greenhouse atmosphere of 96% carbon dioxide and surface temperatures exceeding 460°C?",
        "options": [
            "Mercury",
            "Venus",
            "Mars",
            "Jupiter"
        ],
        "correct": 1,
        "solution": "Step 1: Venus possesses a massive, super-dense atmosphere composed of 96.5% carbon dioxide and clouds of concentrated sulfuric acid.\nStep 2: This creates an impenetrable thermal blanket that traps infrared radiation in an extreme runaway greenhouse effect.\nStep 3: Surface temperatures reach approximately $465^\\circ\\text{C}$ (hot enough to melt lead), making Venus the hottest planet in the Solar System."
    },
    # Q3
    {
        "id": 3,
        "question": "What is the astronomical term for the orbital zone around a star where temperatures permit liquid water to persist stably on a planetary surface?",
        "options": [
            "Asteroid Belt",
            "Oort Cloud",
            "Circumstellar Habitable Zone (Goldilocks Zone)",
            "Kuiper Belt"
        ],
        "correct": 2,
        "solution": "Step 1: The Circumstellar Habitable Zone (often called the Goldilocks Zone) is the orbital corridor around a star where incoming radiant flux maintains surface temperatures between $0^\\circ\\text{C}$ and $100^\\circ\\text{C}$ under 1 atm pressure.\nStep 2: Earth sits comfortably inside this habitable band at an average distance of 1.0 Astronomical Unit (~150 million km)."
    },
    # Q4
    {
        "id": 4,
        "question": "What is the approximate Escape Velocity required for an object to overcome Earth's gravitational pull from its surface?",
        "options": [
            "2.4 km/s",
            "5.0 km/s",
            "11.2 km/s (approx. 40,300 km/h)",
            "25.0 km/s"
        ],
        "correct": 2,
        "solution": "Step 1: Escape velocity $v_e = \\sqrt{\\frac{2GM}{R}}$.\nStep 2: Substituting Earth's gravitational constant $G$, planetary mass $M = 5.97 \\times 10^{24}\\text{ kg}$, and radius $R = 6,371\\text{ km}$ yields:\n$v_e \\approx 11.186\\text{ km/s} \\approx 11.2\\text{ km/s}$.\nConclusion: 11.2 km/s."
    },
    # Q5
    {
        "id": 5,
        "question": "Why is the Moon completely devoid of a substantial atmosphere, unlike the Earth?",
        "options": [
            "The Moon is too close to the Sun",
            "Its smaller mass and weak surface gravity ($1.6\\text{ m/s}^2$) yield a low escape velocity ($2.4\\text{ km/s}$), allowing thermal gases to leak into space",
            "The Moon's craters absorb all nitrogen gases",
            "The Moon is made of frozen cheese"
        ],
        "correct": 1,
        "solution": "Step 1: Planetary gas retention depends on escape velocity versus the root-mean-square thermal velocity of gas molecules.\nStep 2: The Moon's surface gravity is only 1/6th that of Earth ($1.62\\text{ m/s}^2$), resulting in a low escape velocity of just $2.4\\text{ km/s}$.\nStep 3: Atmospheric gas molecules heated by the daytime Sun easily exceed this speed and escape into the vacuum of space."
    },
    # Q6
    {
        "id": 6,
        "question": "Which layer of the Earth's interior generates our planetary magnetic field through geodynamo convection currents?",
        "options": [
            "Crust",
            "Solid inner mantle",
            "Molten liquid iron-nickel outer core",
            "Oceanic tectonic lithosphere"
        ],
        "correct": 2,
        "solution": "Step 1: Earth's outer core is a 2,200-km-thick layer of molten iron and nickel.\nStep 2: Thermal and compositional convection currents in this electrically conductive liquid metal, coupled with Coriolis forces from Earth's 24-hour rotation, function as a self-sustaining geodynamo.\nConclusion: The molten outer core produces the geomagnetic field."
    },
    # Q7
    {
        "id": 7,
        "question": "What vital life-preserving role does Earth's Magnetosphere play against solar emissions?",
        "options": [
            "It reflects all visible sunlight back to the Sun",
            "It deflects dangerous streams of ionized solar wind plasma and cosmic radiation safely around the planet",
            "It slows down Earth's rotation to prevent earthquakes",
            "It produces fresh drinking water in the upper clouds"
        ],
        "correct": 1,
        "solution": "Step 1: The Sun continuously ejects high-energy charged particles (solar wind) at speeds up to 800 km/s.\nStep 2: Earth's magnetosphere deflects these charged particles along magnetic field lines, preventing them from bombarding the surface or stripping away our atmosphere and ozone layer."
    },
    # Q8
    {
        "id": 8,
        "question": "What is the primary atmospheric gas that constitutes approximately 78% of dry air on Earth?",
        "options": [
            "Oxygen ($O_2$)",
            "Carbon Dioxide ($CO_2$)",
            "Nitrogen ($N_2$)",
            "Argon ($Ar$)"
        ],
        "correct": 2,
        "solution": "Step 1: Earth's troposphere is comprised of:\n- Nitrogen ($N_2$): ~78.08%\n- Oxygen ($O_2$): ~20.95%\n- Argon ($Ar$): ~0.93%\n- Carbon Dioxide ($CO_2$): ~0.04%\nConclusion: Nitrogen gas ($N_2$) is the most abundant."
    },
    # Q9
    {
        "id": 9,
        "question": "What are the celestial light displays created when solar wind charged particles strike oxygen and nitrogen atoms in the polar upper atmosphere called?",
        "options": [
            "Solar flares",
            "Auroras (Aurora Borealis and Aurora Australis)",
            "Ball lightning",
            "Zodiacal light"
        ],
        "correct": 1,
        "solution": "Step 1: Charged solar wind electrons funneled along geomagnetic field lines toward the North and South magnetic poles collide with upper atmospheric gas atoms.\nStep 2: De-excitation of oxygen emits green and red light, while nitrogen emits blue and purple light.\nStep 3: These dynamic luminescent displays are known as Auroras (Northern and Southern Lights)."
    },
    # Q10
    {
        "id": 10,
        "question": "Which Jovian gas giant planet in our solar system has the largest mass and strongest surface gravity ($24.8\\text{ m/s}^2$)?",
        "options": [
            "Saturn",
            "Mars",
            "Jupiter",
            "Neptune"
        ],
        "correct": 2,
        "solution": "Step 1: Jupiter is more massive than all other seven planets combined (318 times Earth's mass).\nStep 2: Its immense mass creates a surface gravity of $24.79\\text{ m/s}^2$ (~2.5 times Earth's gravity), retaining a crushing, toxic atmosphere of hydrogen, helium, ammonia, and methane."
    },
    # Q11
    {
        "id": 11,
        "question": "What would Earth's global average surface temperature be if there were NO natural greenhouse gases (water vapor, $CO_2$) in the atmosphere?",
        "options": [
            "+100°C",
            "Approximately -18°C (a frozen world)",
            "+15°C",
            "Absolute Zero (-273°C)"
        ],
        "correct": 1,
        "solution": "Step 1: In the absence of an infrared-trapping greenhouse atmosphere, radiative equilibrium between incoming solar radiation ($S_0 = 1361\\text{ W/m}^2$) and planetary albedo ($A \\approx 0.30$) yields an effective blackbody temperature:\n$T_{eff} = \\left[\\frac{S_0 (1-A)}{4\\sigma}\\right]^{1/4} \\approx 255\\text{ K} \\approx -18^\\circ\\text{C}$.\nStep 2: The natural greenhouse effect elevates this by $33^\\circ\\text{C}$ to a comfortable $+15^\\circ\\text{C}$."
    },
    # Q12
    {
        "id": 12,
        "question": "Which atmospheric layer contains the Ozone Layer ($O_3$) that absorbs harmful high-frequency ultraviolet radiation?",
        "options": [
            "Troposphere",
            "Stratosphere",
            "Mesosphere",
            "Exosphere"
        ],
        "correct": 1,
        "solution": "Step 1: The Stratosphere extends from about 12 km to 50 km altitude.\nStep 2: Ozone ($O_3$) is concentrated between 15 km and 35 km within the stratosphere, where it absorbs over 98% of solar UV-B and UV-C rays via the Chapman photochemical cycle."
    },
    # Q13
    {
        "id": 13,
        "question": "Roughly how many years does it take natural geological weathering and biological action to form 1 centimeter of fertile agricultural topsoil from solid bedrock?",
        "options": [
            "1 to 2 months",
            "1 year",
            "200 to 1,000 years",
            "Over 10 million years"
        ],
        "correct": 2,
        "solution": "Step 1: Topsoil genesis is a slow, multi-stage process involving mechanical frost-cracking, chemical mineral hydration, acid etching by lichens, and organic humification by decomposers.\nStep 2: It requires between 200 and 1,000 years to produce just 1 centimeter of fertile topsoil."
    },
    # Q14
    {
        "id": 14,
        "question": "Which mineral nutrient, weathered from rocks in the lithosphere and absorbed by plant roots, is indispensable for building DNA, RNA, and cellular ATP energy molecules?",
        "options": [
            "Argon",
            "Phosphorus",
            "Helium",
            "Mercury"
        ],
        "correct": 1,
        "solution": "Step 1: Phosphorus ($P$) is a fundamental component of the sugar-phosphate backbone of nucleic acids (DNA and RNA) and the universal cellular energy currency ATP (Adenosine Triphosphate).\nStep 2: It originates from the geological weathering of apatite rock minerals in the crust."
    },
    # Q15
    {
        "id": 15,
        "question": "What microscopic marine organisms produce over 50% of the Earth's atmospheric oxygen supply through photosynthesis in surface waters?",
        "options": [
            "Giant kelp in deep underwater trenches",
            "Phytoplankton (diatoms, cyanobacteria, and microalgae)",
            "Deep-sea anglerfish",
            "Submarine coral polyps"
        ],
        "correct": 1,
        "solution": "Step 1: Oceanic phytoplankton drifting in the photic (sunlit) top 100 meters of the world's oceans perform vast photosynthetic carbon fixation.\nStep 2: They are responsible for generating over 50% of global biogenic oxygen output."
    },
    # Q16
    {
        "id": 16,
        "question": "What is the scientific hypothesis proposed by James Lovelock that states Earth functions as a self-regulating, synergistic system maintaining conditions for life?",
        "options": [
            "The Big Bang Theory",
            "The Gaia Hypothesis",
            "The Nebula Cloud Hypothesis",
            "The Continental Drift Theory"
        ],
        "correct": 1,
        "solution": "Step 1: Formulated by James Lovelock and Lynn Margulis in the 1970s, the Gaia Hypothesis posits that Earth's living organisms closely interact with inorganic components to form a complex, self-regulating feedback system that actively stabilizes climate and atmospheric chemistry."
    },
    # Q17
    {
        "id": 17,
        "question": "In the chemical balance of life, what gas is absorbed by autotrophic plants during daytime photosynthesis and released by animals during respiration?",
        "options": [
            "Nitrogen ($N_2$)",
            "Carbon Dioxide ($CO_2$)",
            "Oxygen ($O_2$)",
            "Hydrogen ($H_2$)"
        ],
        "correct": 1,
        "solution": "Step 1: Photosynthesis: $6CO_2 + 6H_2O + \\text{light} \\rightarrow C_6H_{12}O_6 + 6O_2$.\nStep 2: Cellular Respiration: $C_6H_{12}O_6 + 6O_2 \\rightarrow 6CO_2 + 6H_2O + \\text{energy}$.\nConclusion: Carbon Dioxide ($CO_2$) is absorbed by plants and released by respiring organisms."
    },
    # Q18
    {
        "id": 18,
        "question": "Which of the following is an example of an organism reproducing by 'Binary Fission'—splitting into two equal, identical daughter cells?",
        "options": [
            "Amoeba and Bacteria",
            "Hydra",
            "Potato tuber",
            "Human being"
        ],
        "correct": 0,
        "solution": "Step 1: Binary fission is a form of asexual reproduction typical in prokaryotes (bacteria) and protozoa (*Amoeba*).\nStep 2: The organism replicates its genetic material and divides into two identical daughter cells of equal size."
    },
    # Q19
    {
        "id": 19,
        "question": "How does vegetative propagation occur in potato plants?",
        "options": [
            "Through wind-blown seeds",
            "Through specialized vegetative buds ('eyes') on the subterranean stem tuber",
            "Through spores on the flower petals",
            "Through taproot splitting"
        ],
        "correct": 1,
        "solution": "Step 1: A potato is an underground modified stem tuber.\nStep 2: It possesses nodes termed 'eyes', which contain dormant vegetative buds that sprout into genetically identical clone plants under moist conditions."
    },
    # Q20
    {
        "id": 20,
        "question": "In sexual reproduction, what is the single-celled diploid entity formed immediately upon the fusion of a male sperm and a female egg called?",
        "options": [
            "Spore",
            "Bud",
            "Zygote",
            "Embryo"
        ],
        "correct": 2,
        "solution": "Step 1: The male gamete ($n$) fuses with the female gamete ($n$) in the process of fertilization (syngamy).\nStep 2: The resulting fertilized single cell with restored diploid chromosome number ($2n$) is scientifically called a Zygote."
    },
    # Q21
    {
        "id": 21,
        "question": "Why is sexual reproduction evolutionary superior to asexual cloning when a species encounters a novel, lethal infectious disease?",
        "options": [
            "Sexual reproduction occurs ten times faster than cloning",
            "Genetic recombination creates diverse combinations of immune resistance alleles, ensuring some individuals survive the epidemic",
            "Sexually reproduced animals do not have cells",
            "It eliminates all bacteria from the ecosystem"
        ],
        "correct": 1,
        "solution": "Step 1: Asexual cloning produces uniform genetic populations; if a pathogen exploits a weakness, all clones succumb.\nStep 2: Sexual reproduction involves meiotic crossing over and random fertilization, producing diverse genetic varieties where resistant individuals survive and perpetuate the species."
    },
    # Q22
    {
        "id": 22,
        "question": "What chemical molecule carries the double-helix hereditary instructions passed from generation to generation across billions of years of reproduction?",
        "options": [
            "ATP",
            "DNA (Deoxyribonucleic Acid)",
            "Cellulose",
            "Chlorophyll"
        ],
        "correct": 1,
        "solution": "Step 1: DNA is the double-stranded polymer composed of nucleotide base pairs (A-T, G-C).\nStep 2: It encodes the universal genetic blueprint replicated and transmitted during cellular reproduction."
    },
    # Q23
    {
        "id": 23,
        "question": "Which of the following is a classic example of an organism reproducing asexually by 'Budding'?",
        "options": [
            "Bread mold (*Rhizopus*)",
            "Freshwater *Hydra* and baker's *Yeast*",
            "Spotted deer",
            "*Amoeba*"
        ],
        "correct": 1,
        "solution": "Step 1: In *Hydra* and *Yeast*, a specialized external bulge (bud) arises through localized mitotic cell division.\nStep 2: The bud develops tiny tentacles/structures, matures, and constricts at its base to separate as an independent clone."
    },
    # Q24
    {
        "id": 24,
        "question": "What would be the inevitable fate of ANY biological species if 100% of its individuals permanently ceased reproducing?",
        "options": [
            "The individuals would become immortal",
            "The species would experience total, irreversible biological extinction as mortal individuals die off",
            "The species would split into three different animals automatically",
            "The species would enter permanent hibernation without dying"
        ],
        "correct": 1,
        "solution": "Step 1: Individual organisms have finite lifespans.\nStep 2: Without reproduction generating successive generations, death rates exceed birth rates until the last surviving individual dies, leading to permanent Extinction."
    },
    # Q25
    {
        "id": 25,
        "question": "What is the primary driver of modern global climate change and the Enhanced Greenhouse Effect?",
        "options": [
            "Natural cosmic rays from exploding supernovas",
            "Anthropogenic emissions of $CO_2$ and methane from burning fossil fuels (coal, oil, gas) and mass deforestation",
            "The Moon drifting 3.8 cm farther away each year",
            "Geothermal boiling of deep ocean trenches"
        ],
        "correct": 1,
        "solution": "Step 1: Since the Industrial Revolution, human combustion of fossil fuels has added over 1.5 trillion tons of $CO_2$ to the atmosphere.\nStep 2: Atmospheric $CO_2$ concentrations have soared from 280 ppm to over 425 ppm, amplifying the greenhouse effect and trapping excess thermal energy."
    },
    # Q26
    {
        "id": 26,
        "question": "Why are the Himalayan mountain glaciers often referred to as the 'Water Towers of Asia'?",
        "options": [
            "They store vast quantities of water inside artificial concrete tanks",
            "Their seasonal meltwaters feed major perennial rivers (Ganga, Indus, Brahmaputra, Yangtze) supplying freshwater to over 1.5 billion people",
            "They pump water to the clouds using steam pressure",
            "They are the highest waterfalls in the world"
        ],
        "correct": 1,
        "solution": "Step 1: The Hindu Kush Himalayan ice sheets hold the largest volume of permanent ice outside the polar regions.\nStep 2: They sustain ten major Asian river basins that provide drinking water, irrigation, and hydropower to more than 1.5 billion people."
    },
    # Q27
    {
        "id": 27,
        "question": "What is 'Habitat Fragmentation' caused by road construction, agriculture, and urban development?",
        "options": [
            "Animals building larger homes across mountains",
            "The division of large, continuous natural ecosystems into small, isolated patches, isolating wildlife populations",
            "The natural growth of trees along riverbanks",
            "The seasonal migration of birds to warmer countries"
        ],
        "correct": 1,
        "solution": "Step 1: Habitat fragmentation occurs when human infrastructure (highways, railways, farm fields) carves up continuous natural forests into disconnected habitat islands.\nStep 2: This restricts wildlife mobility, reduces gene pool diversity, and heightens mortality rates."
    },
    # Q28
    {
        "id": 28,
        "question": "Roughly how many years does it take for a conventional synthetic plastic bottle to decompose naturally in the environment?",
        "options": [
            "6 months",
            "2 to 5 years",
            "400 to 1,000 years",
            "It decomposes in less than 24 hours under rain"
        ],
        "correct": 2,
        "solution": "Step 1: Petroleum-based plastics (like polyethylene terephthalate / PET) contain sturdy synthetic carbon-carbon bonds that natural biological decomposers lack enzymes to break.\nStep 2: Under environmental weathering, they require approximately 400 to 1,000 years to break down into microplastics."
    },
    # Q29
    {
        "id": 29,
        "question": "Why are fine particulate matter air pollutants smaller than 2.5 micrometers ($PM_{2.5}$) particularly lethal to human health?",
        "options": [
            "They are so heavy that they break human bones",
            "They easily evade nasal hair filtration, penetrate deep into alveolar lung tissues, and cross into pulmonary capillaries to trigger heart attacks and strokes",
            "They only affect people when they are swimming",
            "They produce poisonous sound waves"
        ],
        "correct": 1,
        "solution": "Step 1: Particles $\\le 2.5\\,\\mu\\text{m}$ ($PM_{2.5}$) are thirty times smaller than the width of a human hair.\nStep 2: They bypass the cilia and mucous membranes of the upper airway, reaching the deepest lung alveoli where they trigger systemic vascular inflammation, asthma, and cardiovascular disease."
    },
    # Q30
    {
        "id": 30,
        "question": "What is the 'Sixth Mass Extinction' currently occurring on planet Earth?",
        "options": [
            "The extinction of dinosaurs 66 million years ago",
            "The ongoing rapid global loss of biodiversity driven directly by human activities (habitat destruction, pollution, poaching, climate change)",
            "A volcanic eruption in the Pacific Ocean",
            "The drying up of an underground desert lake"
        ],
        "correct": 1,
        "solution": "Step 1: Earth has experienced five major mass extinction events in deep geological time, all triggered by natural cataclysms (volcanism, asteroid impacts).\nStep 2: The ongoing Anthropocene extinction (the Sixth Mass Extinction) is unique because it is driven entirely by human industrial and agricultural expansion."
    },
    # Q31
    {
        "id": 31,
        "question": "In a sustainable 'Circular Economy', what is the ultimate goal regarding synthetic materials and resources?",
        "options": [
            "Burn all products in open municipal bonfires",
            "Design products for durability, reuse, refurbishment, and complete recycling to eliminate waste from entering landfills or oceans",
            "Manufacture products that break within one week",
            "Bury all plastic in deep mountain caves"
        ],
        "correct": 1,
        "solution": "Step 1: A linear economy follows an unsustainable 'take-make-waste' model.\nStep 2: A circular economy mirrors nature's zero-waste loops: keeping technical and biological materials circulating at highest utility and value through repair, reuse, remanufacture, and closed-loop recycling."
    },
    # Q32
    {
        "id": 32,
        "question": "Which clean, renewable energy source generates electricity directly from solar photons without releasing greenhouse gas emissions?",
        "options": [
            "Diesel generators",
            "Coal-fired thermal power plants",
            "Solar Photovoltaic (PV) cells",
            "Kerosene lamps"
        ],
        "correct": 2,
        "solution": "Step 1: Solar photovoltaic panels utilize semiconductor materials (like doped silicon) to convert incident sunlight photons directly into electric current via the photoelectric effect.\nStep 2: They operate with zero operational carbon emissions."
    },
    # Q33
    {
        "id": 33,
        "question": "How do protected wildlife corridors connecting isolated national parks help save endangered species?",
        "options": [
            "They provide roads for tourist buses to drive faster",
            "They allow wildlife to safely migrate, disperse, find food, and interbreed across fragmented landscapes, preventing inbreeding depression",
            "They keep animals locked inside concrete fences permanently",
            "They prevent animals from drinking river water"
        ],
        "correct": 1,
        "solution": "Step 1: Wildlife corridors are continuous strips of natural habitat bridging disconnected protected reserves.\nStep 2: They enable gene flow between separate populations, reduce human-wildlife conflict, and allow animals to track shifting resources during droughts or climate change."
    },
    # Q34
    {
        "id": 34,
        "question": "What is the primary ecological hazard of 'Microplastics' in the world's oceans?",
        "options": [
            "They turn seawater into sweet fruit juice",
            "They are ingested by plankton, fish, and filter-feeders, bioaccumulating toxic chemical additives up the marine food chain into humans",
            "They cause ocean waves to stop moving entirely",
            "They make marine animals grow three times faster"
        ],
        "correct": 1,
        "solution": "Step 1: Microplastics (particles $< 5\\text{ mm}$) absorb toxic persistent organic pollutants (POPs) from seawater.\nStep 2: Ingested by zooplankton and small fish, they bioaccumulate and biomagnify up the marine food web, eventually entering human seafood diets."
    },
    # Q35
    {
        "id": 35,
        "question": "Which of the following agricultural practices restores soil biodiversity and reduces synthetic chemical contamination?",
        "options": [
            "Spraying heavy chemical insecticides every single day",
            "Agroforestry, organic composting, crop rotation, and integrated biological pest management",
            "Burning all crop residues and clearing all trees",
            "Paving the farmland with asphalt"
        ],
        "correct": 1,
        "solution": "Step 1: Sustainable ecological agriculture utilizes organic compost, legume nitrogen fixers, and beneficial predatory insects.\nStep 2: This regenerates soil microbial health, preserves beneficial earthworms, and prevents toxic runoff into groundwater."
    },
    # Q36
    {
        "id": 36,
        "question": "What is the historic 2022 United Nations declaration regarding human rights and the environment?",
        "options": [
            "Access to private airplanes is a universal right",
            "Access to a clean, healthy, and sustainable environment is a universal Human Right",
            "Every person must own three plastic factories",
            "Cutting down trees is declared mandatory for all citizens"
        ],
        "correct": 1,
        "solution": "Step 1: On July 28, 2022, the UN General Assembly adopted a historic resolution declaring that living in a clean, healthy, and sustainable environment is a universal human right, obligating nations to protect planetary ecosystems."
    },
    # Q37
    {
        "id": 37,
        "question": "How does the massive planting of native multi-species trees directly fight climate change?",
        "options": [
            "Trees absorb solar heat and turn it into solid ice",
            "Trees act as biological carbon sinks, absorbing atmospheric $CO_2$ through photosynthesis and sequestering it in woody biomass and soil",
            "Trees emit nitrogen gas to push the Sun away",
            "Trees stop all cloud formation"
        ],
        "correct": 1,
        "solution": "Step 1: Growing trees actively absorb $CO_2$ from the air during photosynthesis: $6CO_2 + 6H_2O \\rightarrow C_6H_{12}O_6 + 6O_2$.\nStep 2: They convert carbon into long-term solid cellulose and lignin in trunks and roots, functioning as natural terrestrial carbon sinks."
    },
    # Q38
    {
        "id": 38,
        "question": "What is the famous environmental proverb reminding us of our intergenerational responsibility toward the Earth?",
        "options": [
            "The Earth belongs only to those who can buy it",
            "We do not inherit the Earth from our ancestors; we borrow it from our children",
            "Use all resources as fast as possible before they disappear",
            "Nature will fix all problems without human action"
        ],
        "correct": 1,
        "solution": "Step 1: The proverb 'We do not inherit the Earth from our ancestors; we borrow it from our children' embodies the philosophy of intergenerational equity.\nStep 2: It emphasizes our ethical duty to preserve a living, thriving planetary biosphere for future generations."
    },
    # Q39
    {
        "id": 39,
        "question": "What is the main biological reason that monoculture tree plantations (like vast eucalyptus or pine plantations) cannot replace natural old-growth forests?",
        "options": [
            "Monocultures do not grow any leaves",
            "They support extremely low biodiversity, lack complex multi-tier ecological niches, and are vulnerable to catastrophic pest outbreaks",
            "Monocultures produce too much rain",
            "Animals refuse to walk on grass in plantations"
        ],
        "correct": 1,
        "solution": "Step 1: Natural old-growth forests have diverse canopy layers, varied tree species, dead fallen logs, and thousands of symbiotic organisms.\nStep 2: Single-species plantations represent ecological 'green deserts' with minimal niche diversity and low ecological resilience."
    },
    # Q40
    {
        "id": 40,
        "question": "Which international astronaut famously reflected that gazing at Earth from space reveals our planet as a fragile, borders-less oasis of life in the blackness of space?",
        "options": [
            "Dr. Kalpana Chawla",
            "Christopher Columbus",
            "Vasco da Gama",
            "Ferdinand Magellan"
        ],
        "correct": 0,
        "solution": "Step 1: Dr. Kalpana Chawla, the first Indian-born woman in space, flew on space shuttle missions STS-87 and STS-107.\nStep 2: She eloquently spoke of seeing Earth as an interconnected, fragile oasis without geopolitical boundaries, inspiring global environmental stewardship."
    }
]

