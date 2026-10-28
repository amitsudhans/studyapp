# -*- coding: utf-8 -*-
"""
Class 8 Science - Chapter 11: Astronomy and Calendars
Curriculum Dataset: 20 Slides, 32 Checkpoints, 40 Mastery Quiz Questions
Mentor Avatar: Prof. Meghnad Saha (Pioneering Astrophysicist & Chairman of Calendar Reform Committee)
"""

SLIDES_DATA = [
    # Slide 1 (11.1)
    {
        "id": 1,
        "title": "Moon's Illuminated Hemisphere & Reflection",
        "tag": "11.1 The Moon's Appearance",
        "narration": "Welcome, young astronomers! I am Professor Meghnad Saha. Look up at the night sky. The Moon shines with enchanting radiance, yet it produces no light of its own! Like a colossal rocky mirror, the Moon reflects sunlight towards Earth. Because the Moon is spherical, the Sun always illuminates exactly one hemisphere—50 percent of its surface—while the other half remains in nocturnal shadow. What we see from Earth is simply that portion of the sunlit hemisphere turned towards our vantage point!",
        "points": [
            ("Non-Luminous Rocky Satellite", "The Moon is Earth's only natural satellite. It does not produce nuclear fusion or emit light; it is visible purely through reflected solar radiation."),
            ("Constant 50% Illumination", "At every moment in time, exactly half (50%) of the Moon's spherical body is bathed in direct sunlight, while the opposite hemisphere experiences night."),
            ("Changing Earthly Perspective", "As the Moon orbits Earth every month, the fraction of its illuminated surface visible from Earth continuously changes, producing the celestial phases."),
        ],
        "fact": "The Moon reflects only about 7% to 12% of the sunlight striking its surface—an optical reflectance (albedo) comparable to worn asphalt or dark rock!",
        "sim_id": "moon_illumination_sim",
        "checkpoints": [
            {
                "question": "Why does the Moon shine brightly in the night sky?",
                "options": [
                    "It generates light through nuclear fusion like the Sun",
                    "It reflects sunlight falling on its rocky surface",
                    "It absorbs ultraviolet light and fluoresces at night",
                    "It has glowing volcanic magma rivers across its surface"
                ],
                "correct": 1,
                "explanation": "The Moon is a non-luminous rocky body with no internal light source; it shines exclusively by reflecting incident sunlight toward Earth."
            },
            {
                "question": "How much of the Moon's spherical surface is illuminated by the Sun at any given time?",
                "options": [
                    "Only the portion visible from Earth",
                    "Always exactly half (50%) of its surface",
                    "100% during Full Moon and 0% during New Moon",
                    "It changes depending on the lunar season"
                ],
                "correct": 1,
                "explanation": "Because the Moon is a sphere illuminated by the distant Sun, exactly half (50%) of its surface is always illuminated, regardless of how much of that lit half is visible from Earth."
            }
        ]
    },
    # Slide 2 (11.1.1)
    {
        "id": 2,
        "title": "The Eight Phases of the Moon",
        "tag": "11.1.1 Lunar Phases",
        "narration": "Over approximately four weeks, the Moon transitions through eight classical phases. We begin at New Moon (Amavasya), when the dark, unlit side faces Earth. As it journeys eastward, the illuminated crescent grows—this is Waxing Crescent. At First Quarter, half the visible disk is lit. It swells through Waxing Gibbous until the entire face shines as the brilliant Full Moon (Purnima). Then, it wanes through Waning Gibbous, Third Quarter, and Waning Crescent before renewing the eternal cycle!",
        "points": [
            ("Primary Milestone Phases", "New Moon (Amavasya - 0% visible), First Quarter (50% right half lit), Full Moon (Purnima - 100% visible disk), and Third Quarter (50% left half lit)."),
            ("Intermediate Transition Phases", "Waxing Crescent (growing sliver), Waxing Gibbous (more than half lit), Waning Gibbous (shrinking from full), and Waning Crescent (thinning morning sliver)."),
            ("Waxing vs. Waning Terminology", "'Waxing' denotes increasing illumination (from New to Full Moon, growing from right in Northern Hemisphere); 'Waning' denotes decreasing illumination (from Full to New Moon)."),
        ],
        "fact": "In Sanskrit and Indian tradition, the waxing fortnight of increasing light is celebrated as 'Shukla Paksha' (bright fortnight), while the waning fortnight is 'Krishna Paksha' (dark fortnight).",
        "sim_id": "eight_moon_phases_sim",
        "checkpoints": [
            {
                "question": "What is the phase called when the illuminated portion of the Moon is increasing from New Moon to Full Moon?",
                "options": [
                    "Waning phase (Krishna Paksha)",
                    "Waxing phase (Shukla Paksha)",
                    "Gibbous descent",
                    "Total penumbral transition"
                ],
                "correct": 1,
                "explanation": "'Waxing' refers to the progressive increase in the visible sunlit portion of the Moon from New Moon up to Full Moon."
            },
            {
                "question": "When more than half—but not the whole—visible face of the Moon is illuminated, the phase is termed:",
                "options": [
                    "Crescent",
                    "First Quarter",
                    "Gibbous",
                    "Penumbral"
                ],
                "correct": 2,
                "explanation": "The term 'Gibbous' describes the lunar phase when more than half but less than the fully illuminated disk is visible from Earth."
            }
        ]
    },
    # Slide 3 (11.1.1)
    {
        "id": 3,
        "title": "The Synodic Month & Lunar Orbit",
        "tag": "11.1.1 Orbit & Period",
        "narration": "Have you ever wondered how long a lunar month lasts? Astronomers distinguish between two key periods! The Moon completes one physical 360-degree revolution around Earth in 27.3 days—called the Sidereal Month. However, while the Moon is revolving, Earth is simultaneously traveling along its orbit around the Sun! To realign with the Sun and reach the same phase (such as New Moon to New Moon), the Moon must travel an extra 2.2 days. Thus, the Synodic Month—the cycle of phases—lasts approximately 29.53 days!",
        "points": [
            ("Sidereal Month (27.3 Days)", "The true physical orbital period of the Moon around Earth relative to the fixed distant background stars."),
            ("Earth's Orbital Advance", "During those 27.3 days, Earth travels roughly 27 degrees along its annual orbit around the Sun (~1° per day)."),
            ("Synodic Month (29.53 Days)", "The time required for the Moon to cycle through all phases (e.g., from one New Moon to the next New Moon). This ~29.5-day cycle forms the bedrock of lunar calendars."),
        ],
        "fact": "The difference between 27.3 days and 29.53 days is roughly 2.2 extra days, during which the Moon must travel an additional ~27° in orbit to catch up with the moving Sun!",
        "sim_id": "synodic_vs_sidereal_sim",
        "checkpoints": [
            {
                "question": "Why is the synodic month (phase cycle: 29.5 days) longer than the sidereal month (revolution: 27.3 days)?",
                "options": [
                    "The Moon slows down its speed during Full Moon",
                    "Earth moves along its orbit around the Sun, requiring the Moon to travel further to realign with the Sun",
                    "Gravitational friction from the ocean tides lengthens the orbit every week",
                    "Solar flares push the Moon further away from the Earth"
                ],
                "correct": 1,
                "explanation": "Because Earth travels around the Sun, the Moon must complete its 360° orbit plus an extra ~27° (taking about 2.2 extra days) to return to the exact same Sun-Earth alignment."
            },
            {
                "question": "The time taken for the Moon to go from one New Moon to the next New Moon is approximately:",
                "options": [
                    "24 hours",
                    "27.3 days",
                    "29.5 days",
                    "365.25 days"
                ],
                "correct": 2,
                "explanation": "The synodic month—the complete cycle of lunar phases from New Moon to New Moon—takes approximately 29.53 days."
            }
        ]
    },
    # Slide 4 (11.1.2)
    {
        "id": 4,
        "title": "Locating the Moon in the Sky",
        "tag": "11.1.2 Daily Motion",
        "narration": "If you observe the Moon on successive evenings at the exact same hour, you will notice a fascinating pattern! The Moon shifts eastward by about 12 to 13 degrees every single day. Because Earth rotates 360 degrees in 24 hours (15 degrees per hour), this daily orbital advance means the Moon rises approximately 50 minutes later each day! Furthermore, the Moon is not strictly a nighttime object—the crescent Moon is often visible in daylight afternoon or morning skies!",
        "points": [
            ("Eastward Daily Orbital Shift", "The Moon completes a 360° orbit in ~27.3 days, advancing eastward through the sky by roughly 360° / 27.3 ≈ 13.2° every 24 hours."),
            ("The 50-Minute Daily Delay", "Because Earth rotates at 15° per hour, it takes approximately (13° / 15°) × 60 ≈ 50 additional minutes each day for Earth's rotation to bring the Moon back above the eastern horizon."),
            ("Daytime Lunar Visibility", "Except during Full Moon (which rises at sunset) and New Moon (which is lost in solar glare), intermediate phases are frequently visible during broad daylight!"),
        ],
        "fact": "A Full Moon always rises in the East almost precisely at sunset and sets in the West at sunrise, because it is directly opposite the Sun in our sky!",
        "sim_id": "locating_moon_sky_sim",
        "checkpoints": [
            {
                "question": "On average, how much later does the Moon rise each successive day?",
                "options": [
                    "About 5 minutes later",
                    "About 50 minutes later",
                    "About 3 hours later",
                    "It rises at the exact same time every day"
                ],
                "correct": 1,
                "explanation": "Because the Moon moves eastward in its orbit by roughly 13° each day, Earth must rotate for about 50 additional minutes for the Moon to rise again."
            },
            {
                "question": "At what time of day does a Full Moon rise above the eastern horizon?",
                "options": [
                    "Around sunrise",
                    "Around noon",
                    "Around sunset",
                    "At midnight"
                ],
                "correct": 2,
                "explanation": "During Full Moon, the Moon is situated directly opposite the Sun from Earth's vantage point; therefore, as the Sun sets in the west, the Full Moon rises in the east."
            }
        ]
    },
    # Slide 5 (11.1.3)
    {
        "id": 5,
        "title": "Sun-Earth-Moon Orbital Geometry",
        "tag": "11.1.3 Spatial Geometry",
        "narration": "To truly comprehend lunar phases, we must step outside our Earth-bound perspective and visualize the celestial dance from space! Imagine looking down from above Earth's North Pole. The Sun illuminates the entire solar system from one direction. The Moon orbits Earth in a counter-clockwise direction. At position 1, between Sun and Earth, its dark side faces us (New Moon). At 90 degrees, we see half the lit face (First Quarter). At 180 degrees, the fully lit face faces Earth (Full Moon)!",
        "points": [
            ("Top-Down Space View vs. Terrestrial View", "From space, the Sun always lights the side facing it. From Earth's surface, our line of sight catches varying proportions of that illuminated side as the Moon revolves."),
            ("Elongation Angle", "The angular separation between Sun and Moon in our sky. At 0° elongation = New Moon; at 90° = First Quarter; at 180° = Full Moon; at 270° = Third Quarter."),
            ("Illumination Consistency", "The Moon never physically expands or shrinks. The varying shape is entirely an optical perspective determined by the relative geometric angles of Sun, Earth, and Moon."),
        ],
        "fact": "Ancient Greek astronomer Anaxagoras (c. 500–428 BCE) was among the first in the Mediterranean to realize that the Moon does not emit light, but reflects sunlight, explaining both phases and eclipses!",
        "sim_id": "orbital_geometry_sim",
        "checkpoints": [
            {
                "question": "What is the relative position of Earth, Moon, and Sun during a Full Moon?",
                "options": [
                    "The Moon is directly between the Earth and the Sun",
                    "The Earth is located between the Sun and the Moon",
                    "The Sun is located between the Earth and the Moon",
                    "The Moon forms a 45-degree angle with the Sun"
                ],
                "correct": 1,
                "explanation": "During Full Moon, Earth is situated between the Sun and the Moon, allowing observers on Earth's night side to gaze upon the fully sunlit lunar hemisphere."
            },
            {
                "question": "When the Moon forms a 90-degree angle relative to the Sun as seen from Earth, which phase occurs?",
                "options": [
                    "New Moon",
                    "Quarter Moon (First or Third Quarter)",
                    "Full Moon",
                    "Solar Eclipse"
                ],
                "correct": 1,
                "explanation": "At an elongation angle of 90 degrees, an observer on Earth sees exactly half of the sunlit hemisphere—constituting a First or Third Quarter Moon."
            }
        ]
    },
    # Slide 6 (11.1.3)
    {
        "id": 6,
        "title": "Synchronous Rotation & Tidal Locking",
        "tag": "11.1.3 The Far Side",
        "narration": "Here is one of astronomy's greatest marvels: throughout all of human history, humanity only ever saw one face of the Moon! Why? Because the Moon is tidally locked to Earth in synchronous rotation! The Moon rotates on its own internal axis in exactly the same amount of time it takes to complete one revolution around Earth: 27.3 days. As it turns around Earth, it rotates just enough to keep the same lunar face permanently oriented toward us. The Far Side remained completely invisible until spacecraft photographed it in 1959!",
        "points": [
            ("Synchronous Rotation Defined", "Rotation period on axis (27.3 days) = Revolution period around Earth (27.3 days). The ratio of rotation to revolution is exactly 1:1."),
            ("Tidal Friction Origin", "Over billions of years, Earth's immense gravitational tidal forces created bulges on the Moon, acting as a gravitational brake until its spin matched its orbital period."),
            ("The 'Far Side' is Not Dark", "The Far Side is often erroneously called the 'Dark Side'. In reality, when we experience a New Moon, the Far Side is bathed in brilliant 100% sunlight!"),
        ],
        "fact": "Humanity first saw the lunar far side in October 1959, when the Soviet Union's Luna 3 probe transmitted historic photographs revealing heavily cratered terrain devoid of large lunar 'seas' (maria)!",
        "sim_id": "synchronous_rotation_sim",
        "checkpoints": [
            {
                "question": "Why do we always observe the same side of the Moon from Earth?",
                "options": [
                    "The Moon does not rotate on its axis at all",
                    "The Moon's rotation period on its axis exactly equals its orbital period around Earth",
                    "The far side of the Moon is physically attached to deep space",
                    "Earth's magnetic field locks the Moon completely rigid"
                ],
                "correct": 1,
                "explanation": "Due to tidal locking, the Moon rotates on its axis in 27.3 days—the exact same duration as its orbit around Earth—keeping the same hemisphere permanently facing us."
            },
            {
                "question": "Is the far side of the Moon permanently dark?",
                "options": [
                    "Yes, sunlight never reaches the far side of the Moon",
                    "No, during New Moon on Earth, the far side is fully illuminated by sunlight",
                    "Yes, because the Moon is shaped like a flat shield",
                    "No, but it only receives light from Earthshine"
                ],
                "correct": 1,
                "explanation": "The far side receives just as much sunlight as the near side; during a New Moon on Earth, the far side of the Moon is in full daylight."
            }
        ]
    },
    # Slide 7 (11.1.3)
    {
        "id": 7,
        "title": "Solar and Lunar Eclipses",
        "tag": "11.1.3 Celestial Shadows",
        "narration": "If the Moon passes between Earth and the Sun every New Moon, and Earth passes between Sun and Moon every Full Moon, why don't eclipses occur every single month? The answer lies in orbital tilt! The Moon's orbital plane is tilted by approximately 5.14 degrees with respect to Earth's orbital plane around the Sun (the ecliptic). Most months, the Moon passes slightly above or below the direct shadow line. Eclipses can only occur when the Moon crosses the plane of the ecliptic at specific intersection points called nodes!",
        "points": [
            ("Solar Eclipse (Surya Grahan)", "Occurs during New Moon when the Moon passes directly between Sun and Earth, casting its shadow (umbra and penumbra) onto Earth's surface."),
            ("Lunar Eclipse (Chandra Grahan)", "Occurs during Full Moon when Earth passes directly between Sun and Moon, casting Earth's massive shadow onto the Moon and giving it a coppery-red tint."),
            ("The 5.14° Orbital Tilt", "Because of the Moon's 5.14° tilt, the shadows usually miss their celestial targets. Only when Sun, Earth, and Moon align near orbital nodes do eclipses occur (2 to 5 times a year)."),
        ],
        "fact": "During a total lunar eclipse, the Moon does not turn completely black. Earth's atmosphere bends (refracts) red wavelengths of sunlight into Earth's shadow, turning the Moon a dramatic 'Blood Moon' red!",
        "sim_id": "eclipses_geometry_sim",
        "checkpoints": [
            {
                "question": "Why does a solar or lunar eclipse not happen every single month?",
                "options": [
                    "The Moon's orbit is tilted at about 5.14 degrees relative to Earth's orbit around the Sun",
                    "The Moon is too small to cast a shadow most of the year",
                    "The Sun's light bends around the Earth due to gravity",
                    "Eclipses only occur during leap years"
                ],
                "correct": 0,
                "explanation": "The Moon's orbital plane is inclined by ~5.14° to the ecliptic plane; therefore, the Moon usually passes slightly above or below the direct shadow alignment line."
            },
            {
                "question": "A Solar Eclipse can only happen during which lunar phase?",
                "options": [
                    "Full Moon (Purnima)",
                    "First Quarter",
                    "New Moon (Amavasya)",
                    "Third Quarter"
                ],
                "correct": 2,
                "explanation": "A Solar Eclipse requires the Moon to be directly between the Earth and the Sun, which only occurs during the New Moon phase (Amavasya)."
            }
        ]
    },
    # Slide 8 (11.2 & 11.2.1)
    {
        "id": 8,
        "title": "Origin of Calendars & The Lunar Calendar",
        "tag": "11.2 / 11.2.1 Calendars",
        "narration": "Since the dawn of civilization, humans needed a dependable way to track time for agriculture, sowing crops, anticipating floods, and scheduling cultural festivities. The Moon's distinct, easily observable phases provided humanity with nature's first cosmic clock! A pure lunar calendar uses 12 synodic months as one year. However, 12 lunar months equal 12 × 29.53 ≈ 354.36 days—roughly 11 days shorter than the 365.24-day solar year! As a result, pure lunar calendars gradually drift across the solar seasons!",
        "points": [
            ("Nature's First Celestial Clock", "The regular 29.5-day cycle from New Moon to New Moon is readily visible without any optical tools, making it the most ancient timekeeping standard."),
            ("The Pure Lunar Year (~354 Days)", "Composed of 12 alternating months of 29 and 30 days, totaling approximately 354 days per year."),
            ("The 11-Day Seasonal Drift", "Because a solar year is ~365.25 days, a pure lunar calendar falls behind by ~11 days each solar year, causing lunar months and festivals to cycle through all four seasons over a 33-year period (e.g., the Islamic Hijri calendar)."),
        ],
        "fact": "Because the Islamic Hijri calendar is purely lunar, the sacred fasting month of Ramadan drifts backward through the solar seasons by about 11 days every Gregorian year, returning to the same season every 33 years!",
        "sim_id": "lunar_calendar_drift_sim",
        "checkpoints": [
            {
                "question": "How many days are in a typical pure lunar year consisting of 12 synodic lunar months?",
                "options": [
                    "365 days",
                    "354 days",
                    "300 days",
                    "366 days"
                ],
                "correct": 1,
                "explanation": "A pure lunar year of 12 synodic months (12 × 29.53 days) equals approximately 354 days—roughly 11 days shorter than the solar year."
            },
            {
                "question": "What is the primary characteristic of a purely lunar calendar over many years?",
                "options": [
                    "Its months remain permanently fixed to identical weather seasons",
                    "Its months drift through all seasons over roughly a 33-year cycle",
                    "It automatically inserts 10 days every month",
                    "It has exactly 365 days every year"
                ],
                "correct": 1,
                "explanation": "Because it is ~11 days shorter than the solar year, months in a pure lunar calendar advance across all seasons, cycling completely through the seasonal year every ~33 solar years."
            }
        ]
    },
    # Slide 9 (11.2.2)
    {
        "id": 9,
        "title": "Solar Calendars & The Tropical Year",
        "tag": "11.2.2 Solar Calendars",
        "narration": "To keep agricultural sowing, harvests, and seasonal weather strictly synchronized with the calendar, ancient societies developed solar calendars! A solar calendar tracks Earth's complete orbital journey around the Sun. This duration—from one vernal equinox to the next—is called the Tropical Solar Year, measuring 365.2422 days. Because of that stubborn fraction of nearly a quarter day (0.2422 days), solar calendars require leap years! In the Gregorian calendar, we add February 29th every 4 years, with a special century leap rule!",
        "points": [
            ("The Tropical Solar Year", "Measures 365 days, 5 hours, 48 minutes, and 45 seconds (365.2422 days). It precisely governs Earth's four seasons: spring, summer, autumn, and winter."),
            ("The Julian Calendar Reform", "Introduced by Julius Caesar in 45 BCE, assuming a year of 365.25 days by adding one leap day every 4 years. Over 16 centuries, it drifted by about 10 days!"),
            ("The Gregorian Leap Year Rule", "Introduced in 1582 CE: a year is a leap year if divisible by 4, except end-of-century years (ending in 00), which must be divisible by 400 (e.g., 2000 was a leap year, but 1900 was not)."),
        ],
        "fact": "The 400-year Gregorian leap rule keeps the calendar remarkably accurate: it accumulates an error of merely 1 day in approximately 3,300 years!",
        "sim_id": "solar_calendar_seasons_sim",
        "checkpoints": [
            {
                "question": "What is the precise astronomical length of Earth's tropical solar year?",
                "options": [
                    "Exactly 365.00 days",
                    "Approximately 365.2422 days",
                    "Exactly 354.36 days",
                    "Approximately 366.50 days"
                ],
                "correct": 1,
                "explanation": "Earth's tropical solar year is approximately 365.2422 days (365 days, 5 hours, 48 minutes, and 45 seconds)."
            },
            {
                "question": "According to the Gregorian calendar rules, which of the following century years was a leap year?",
                "options": [
                    "Year 1700",
                    "Year 1800",
                    "Year 1900",
                    "Year 2000"
                ],
                "correct": 3,
                "explanation": "Under Gregorian rules, century years must be divisible by 400 to be leap years. 2000 is divisible by 400 (2000 ÷ 400 = 5), making it a leap year, whereas 1700, 1800, and 1900 were not."
            }
        ]
    },
    # Slide 10 (11.2.3)
    {
        "id": 10,
        "title": "Luni-Solar Calendars & Adhik Maas",
        "tag": "11.2.3 Luni-Solar Harmony",
        "narration": "What if you wish to honor the sacred beauty of lunar phases while ensuring that agricultural festivals never drift away from their natural seasons? The brilliant solution is the Luni-Solar calendar! In India, calendars like Vikram Samvat and Shalivahana Shaka use lunar months. To bridge the ~11-day annual gap between 354 lunar days and 365 solar days, an entire intercalary thirteenth month—known as Adhik Maas, Purushottam Maas, or Mala Masa—is inserted approximately every 2.5 to 3 years!",
        "points": [
            ("Harmonizing Moon and Sun", "Luni-solar calendars reckon months by the Moon's phases, but adjust their years so that harvest festivals remain firmly locked to the solar seasons."),
            ("The Mathematical Deficit", "In 3 solar years, the 11-day annual deficit accumulates to roughly 33 days—slightly longer than one complete lunar month (29.5 days)."),
            ("Adhik Maas (Intercalary Month)", "By adding an extra 13th month every 32 to 33 months (roughly 7 times in 19 years), the calendar resynchronizes with the Sun, ensuring festivals like Diwali remain in autumn and Holi in spring!"),
        ],
        "fact": "The 19-year cycle reconciling 235 lunar months with 19 solar years is known in global astronomy as the Metonic Cycle, discovered independently by Indian, Babylonian, and Greek astronomers!",
        "sim_id": "lunisolar_adhik_maas_sim",
        "checkpoints": [
            {
                "question": "What is the purpose of adding an 'Adhik Maas' (extra month) in traditional Indian calendars?",
                "options": [
                    "To celebrate extra holidays during the summer season",
                    "To reconcile the 11-day annual difference between lunar and solar years so seasons remain aligned",
                    "To adjust for the slowing rotation of the Earth's core",
                    "To match the 24-hour day with the Moon's orbital period"
                ],
                "correct": 1,
                "explanation": "Adhik Maas is an intercalary month added roughly every 2.5 to 3 years to make up for the 11-day annual deficit of the lunar calendar, keeping festivals aligned with solar seasons."
            },
            {
                "question": "Roughly how often is an extra intercalary month (Adhik Maas) inserted into a luni-solar calendar?",
                "options": [
                    "Every single year",
                    "Every 2.5 to 3 years (about 7 times in 19 years)",
                    "Once every 10 years",
                    "Once every 50 years"
                ],
                "correct": 1,
                "explanation": "Because an 11-day deficit accumulates to ~33 days after roughly 32.5 months, an extra month is inserted every 2.5 to 3 years."
            }
        ]
    },
    # Slide 11 (11.2.4)
    {
        "id": 11,
        "title": "The Indian National Calendar (Saka Era)",
        "tag": "11.2.4 National Calendar",
        "narration": "After Indian independence, our nation had over thirty regional calendars! In 1952, Prime Minister Jawaharlal Nehru appointed the Calendar Reform Committee under my chairmanship. We standardized a scientific, unified solar calendar based on the historic Saka Era (which began in 78 CE). Adopted on March 22, 1957, the Indian National Calendar begins its year on Chaitra 1st, coinciding with the Vernal Equinox (March 22 in normal years, March 21 in leap years), followed by 12 standardized months!",
        "points": [
            ("Calendar Reform Committee (1952–1955)", "Chaired by astrophysicist Prof. Meghnad Saha, the committee harmonized ancient astronomical wisdom with modern precision science."),
            ("The Saka Era Standard", "Year 1 of the Saka Era corresponds to 78 CE of the Gregorian calendar. To find the Saka year, subtract 78 from the current Gregorian year (e.g., 2026 CE − 78 = 1948 Saka Era)."),
            ("Structure of the Year", "Contains 365 days (366 in leap years). Month 1 is Chaitra (30/31 days), followed by Vaisakha, Jyeshtha, Ashadha, Shravana, Bhadra (each 31 days), and then Ashvina, Kartika, Agrahayana, Pausha, Magha, Phalguna (each 30 days)."),
        ],
        "fact": "The Indian National Calendar is published alongside the Gregorian calendar in official Gazettes of India, All India Radio news broadcasts, and official Government of India communications!",
        "sim_id": "indian_national_calendar_sim",
        "checkpoints": [
            {
                "question": "When does the first day of the year (Chaitra 1) occur in the Indian National Calendar in a normal year?",
                "options": [
                    "January 1",
                    "March 22 (Vernal Equinox)",
                    "August 15",
                    "October 2"
                ],
                "correct": 1,
                "explanation": "In the Indian National Calendar, Chaitra 1 falls on March 22 in normal years (and March 21 in leap years), precisely matching the Vernal Equinox."
            },
            {
                "question": "Which historic era forms the astronomical basis of the Indian National Calendar?",
                "options": [
                    "Vikram Era (57 BCE)",
                    "Saka Era (78 CE)",
                    "Kalyug Era",
                    "Harsha Era"
                ],
                "correct": 1,
                "explanation": "The Indian National Calendar is based on the historic Saka Era, which began in 78 CE."
            }
        ]
    },
    # Slide 12 (11.3)
    {
        "id": 12,
        "title": "Astronomical Origins of Festivals",
        "tag": "11.3 Cultural Astronomy",
        "narration": "Have you ever marveled at how closely our cultural festivals mirror cosmic events? Across cultures, celebrations were born from sky observations! Diwali, the festival of lights, is celebrated on the darkest night of the year—the New Moon (Amavasya) of the month of Kartika. Holi, Buddha Purnima, and Guru Nanak Jayanti occur on the luminous Full Moon (Purnima). Eid-ul-Fitr is heralded by the first sighting of the delicate crescent Moon (Hilal), while Makar Sankranti marks the Sun entering the zodiac sign of Capricorn (Makara)!",
        "points": [
            ("New Moon Festivals (Amavasya)", "Diwali illuminates the darkest night of Kartika with clay diyas, welcoming prosperity and inner light amidst cosmic darkness."),
            ("Full Moon Festivals (Purnima)", "Holi (Phalguna Purnima), Buddha Purnima (Vaisakha Purnima), Raksha Bandhan (Shravana Purnima), and Guru Purnima celebrate peak illumination."),
            ("Solar Transit & Equinox Celebrations", "Makar Sankranti and Pongal celebrate the Sun's northward transit (Uttarayan) into Makara rashi; Baisakhi, Vishu, and Puthandu celebrate the solar New Year!"),
        ],
        "fact": "Makar Sankranti is one of the rare Indian festivals calculated directly according to the Sun's transit (solar calendar), which is why it almost always falls on January 14th or 15th every year!",
        "sim_id": "festival_astronomy_sim",
        "checkpoints": [
            {
                "question": "On which astronomical lunar phase is the festival of Diwali celebrated?",
                "options": [
                    "Full Moon (Purnima)",
                    "New Moon (Amavasya) of Kartika month",
                    "First Quarter Moon",
                    "During a Total Solar Eclipse"
                ],
                "correct": 1,
                "explanation": "Diwali is celebrated on the New Moon (Amavasya) night of the Hindu month of Kartika, lighting lamps against the darkest night of the month."
            },
            {
                "question": "Why does Makar Sankranti occur on nearly the same date (January 14/15) in the Gregorian calendar each year?",
                "options": [
                    "It is based on the solar transit of the Sun rather than the lunar phase cycle",
                    "It is scheduled by modern international treaties",
                    "The Moon stops orbiting on that particular night",
                    "It always coincides with a lunar eclipse"
                ],
                "correct": 0,
                "explanation": "Makar Sankranti is governed by the solar cycle (the Sun's transit into the zodiac sign of Makara), which aligns closely with the solar Gregorian calendar."
            }
        ]
    },
    # Slide 13 (11.4)
    {
        "id": 13,
        "title": "Artificial Satellites & Orbital Mechanics",
        "tag": "11.4 Satellites & Orbits",
        "narration": "While the Moon is Earth's only natural satellite, humanity has launched thousands of man-made marvels into space: artificial satellites! How does a satellite stay in orbit without falling back to Earth? Sir Isaac Newton imagined firing a cannon from a mountain top. If fired with sufficient forward speed—approximately 7.9 kilometers per second (28,000 km/h)—the cannonball falls towards Earth at the exact same rate that Earth's curved surface curves away beneath it! It enters continuous free fall: an orbit!",
        "points": [
            ("Natural vs. Artificial Satellites", "Natural satellite: A celestial body orbiting a planet (the Moon). Artificial satellite: A human-engineered spacecraft placed in orbit by multi-stage rockets."),
            ("Newton's Orbital Cannon Principle", "An orbiting satellite is actually falling freely toward Earth, but possesses enough forward tangential velocity that it continually misses Earth's curvature!"),
            ("Orbital Velocities", "Low Earth Orbit requires ~7.9 km/s. If velocity exceeds 11.2 km/s (Escape Velocity), the craft breaks free of Earth's gravity entirely and ventures into interplanetary space!"),
        ],
        "fact": "The world's first artificial satellite, Sputnik 1, was launched by the Soviet Union on October 4, 1957. India entered space on April 19, 1975, with its first satellite, named Aryabhata!",
        "sim_id": "newton_orbital_cannon_sim",
        "checkpoints": [
            {
                "question": "What keeps an artificial satellite in continuous orbit around Earth without falling to the ground?",
                "options": [
                    "Rocket engines fire non-stop every second in space",
                    "Its high forward horizontal speed balances the downward gravitational pull, keeping it in continuous free fall",
                    "There is zero gravity in space so objects naturally float",
                    "Giant solar sails push against solar wind to hold it up"
                ],
                "correct": 1,
                "explanation": "A satellite in orbit is in continuous free fall toward Earth, but its immense tangential velocity causes the surface of spherical Earth to curve away at the exact same rate."
            },
            {
                "question": "What was the name of India's very first indigenously designed artificial satellite launched in 1975?",
                "options": [
                    "Mangalyaan",
                    "Aryabhata",
                    "Chandrayaan-1",
                    "INSAT-1A"
                ],
                "correct": 1,
                "explanation": "India's first satellite was named 'Aryabhata', launched on April 19, 1975, honoring the legendary 5th-century Indian astronomer and mathematician."
            }
        ]
    },
    # Slide 14 (11.4)
    {
        "id": 14,
        "title": "Communications, Weather & NavIC Satellites",
        "tag": "11.4 Practical Applications",
        "narration": "Where are satellites placed, and what do they do for us every day? Satellites occupy distinct orbital highways based on their mission! Low Earth Orbit (LEO, 160–2,000 km) hosts the International Space Station and earth monitoring sensors. At an altitude of 35,786 km lies Geostationary Orbit (GEO), where a satellite takes exactly 24 hours to orbit Earth—appearing permanently stationary over one spot on the equator! These power television broadcasts, weather monitoring, and India's regional navigation system, NavIC!",
        "points": [
            ("Geostationary Orbit (GEO at 35,786 km)", "Orbital period exactly matches Earth's 24-hour rotation. Ground dishes stay pointed at one spot without moving. Ideal for communication and continuous cyclone tracking."),
            ("Weather & Disaster Monitoring", "Satellites like INSAT and Kalpana-1 track atmospheric moisture, ocean temperatures, and monsoon clouds, providing life-saving early warnings for devastating cyclones."),
            ("NavIC (Navigation with Indian Constellation)", "India's autonomous regional satellite navigation system consisting of 7 satellites providing real-time positioning accuracy across India and 1,500 km beyond its borders!"),
        ],
        "fact": "Geostationary orbit was popularized in 1945 by science-fiction author and scientist Arthur C. Clarke, which is why this unique 35,786 km orbit is also called the 'Clarke Orbit'!",
        "sim_id": "satellite_orbits_navic_sim",
        "checkpoints": [
            {
                "question": "At what approximate altitude above Earth's equator do Geostationary Satellites (GEO) orbit?",
                "options": [
                    "400 km",
                    "2,000 km",
                    "35,786 km",
                    "384,400 km"
                ],
                "correct": 2,
                "explanation": "Geostationary satellites orbit at an altitude of approximately 35,786 kilometers, where their orbital period is exactly 24 hours, matching Earth's rotation."
            },
            {
                "question": "What is 'NavIC' developed by the Indian Space Research Organisation (ISRO)?",
                "options": [
                    "A weather radar on the Himalayas",
                    "India's independent regional satellite navigation system",
                    "A deep-sea submarine navigation probe",
                    "A space telescope orbiting Mars"
                ],
                "correct": 1,
                "explanation": "NavIC (Navigation with Indian Constellation) is India's independent regional satellite navigation system operated by ISRO."
            }
        ]
    },
    # Slide 15 (11.4)
    {
        "id": 15,
        "title": "Earth Remote Sensing & Deep Space Missions",
        "tag": "11.4 Exploration",
        "narration": "Beyond communications, satellites serve as Earth's watchful guardians through Remote Sensing! Indian Remote Sensing satellites (IRS series, Cartosat, and RISAT) photograph our planet in visible, infrared, and radar wavelengths. They estimate crop yields, locate underground water, map deforestation, and assess flood damage. Furthermore, satellites travel into deep space: ISRO's Chandrayaan missions discovered water molecules on the Moon, Mangalyaan reached Mars, and Aditya-L1 observes our Sun!",
        "points": [
            ("Multispectral Remote Sensing", "Sensors detect electromagnetic radiation reflected from Earth's surface. Infrared sensors reveal crop health, moisture content, and mineral deposits."),
            ("Chandrayaan Lunar Exploration", "Chandrayaan-1 (2008) made the historic discovery of water molecules ($H_2O$ / $OH$) on the lunar surface. Chandrayaan-3 (2023) achieved humanity's first soft landing near the lunar South Pole!"),
            ("Aditya-L1 Solar Observatory", "Positioned at the Sun-Earth Lagrange Point 1 (1.5 million km from Earth), Aditya-L1 continuously studies solar flares, coronal mass ejections, and space weather without any eclipses!"),
        ],
        "fact": "On August 23, 2023, India's Chandrayaan-3 lander 'Vikram' touched down near the lunar South Pole, making India the 4th country to soft-land on the Moon and the 1st near the South Pole, celebrated annually as National Space Day!",
        "sim_id": "remote_sensing_space_sim",
        "checkpoints": [
            {
                "question": "What major breakthrough did India's Chandrayaan-1 mission discover on the Moon in 2008?",
                "options": [
                    "Evidence of active volcanic eruptions",
                    "Presence of water molecules ($H_2O$ and hydroxyl) on the lunar surface",
                    "Deposits of liquid fossil fuels",
                    "An ancient alien radio beacon"
                ],
                "correct": 1,
                "explanation": "Chandrayaan-1's Moon Mineralogy Mapper instrument conclusively confirmed the widespread presence of water molecules on the lunar surface."
            },
            {
                "question": "Where is ISRO's solar observatory satellite, Aditya-L1, stationed to observe the Sun continuously?",
                "options": [
                    "In Low Earth Orbit around the equator",
                    "On the surface of the Moon",
                    "At the Sun-Earth Lagrange Point 1 (L1), 1.5 million km from Earth",
                    "In an orbit around the planet Venus"
                ],
                "correct": 2,
                "explanation": "Aditya-L1 is stationed in a halo orbit around the Sun-Earth Lagrange Point 1 (L1), about 1.5 million km from Earth, offering an uninterrupted view of the Sun without eclipses."
            }
        ]
    },
    # Slide 16 (Review & Heritage)
    {
        "id": 16,
        "title": "Ancient Indian Astronomy & Jantar Mantar",
        "tag": "Review & Scientific Heritage",
        "narration": "India has a glorious astronomical heritage spanning millennia! Long before modern telescopes, visionary astronomers like Aryabhata (who established that Earth rotates on its axis and calculated the year as 365.258 days), Varahamihira, and Brahmagupta mapped celestial motions with astonishing accuracy. In the early 1700s, Maharaja Sawai Jai Singh II built magnificent monumental stone observatories—the Jantar Mantar at Delhi, Jaipur, Ujjain, and Varanasi. Their giant sundials measure local time to within two seconds!",
        "points": [
            ("Aryabhata's Revolutionary Insights (476–550 CE)", "Asserted in the 'Aryabhatiya' that day and night are caused by Earth's rotation on its axis, and that the Moon and planets shine by reflected sunlight."),
            ("Brahmagupta & Gravitation (598–668 CE)", "Stated in the 'Brahmasphutasiddhanta' that all heavy objects are naturally drawn toward the center of the Earth by an attractive force ('Gurutvakarshan')."),
            ("Jantar Mantar Stone Observatories (1724–1734 CE)", "Built by Maharaja Sawai Jai Singh II; the giant Vrihat Samrat Yantra sundial in Jaipur stands 27 meters tall, casting a shadow that moves at 1 mm per second to tell time with 2-second precision!"),
        ],
        "fact": "The name 'Jantar Mantar' derives from the Sanskrit words 'Yantra' (instrument) and 'Mantra' (calculation or formula)—literally meaning 'Calculation Instruments'!",
        "sim_id": "jantar_mantar_sundial_sim",
        "checkpoints": [
            {
                "question": "Which ancient Indian astronomer first proposed that the apparent rotation of the heavens is caused by the actual rotation of Earth on its own axis?",
                "options": [
                    "Aryabhata",
                    "Charaka",
                    "Panini",
                    "Sushruta"
                ],
                "correct": 0,
                "explanation": "In his seminal 499 CE treatise 'Aryabhatiya', Aryabhata boldly explained that Earth rotates daily on its axis, making the stars appear to revolve around us."
            },
            {
                "question": "What is the primary function of the giant 'Samrat Yantra' at the Jantar Mantar observatories?",
                "options": [
                    "A water reservoir for cooling telescopes",
                    "A massive equinoctial sundial for measuring local solar time and celestial declination",
                    "A launching ramp for ancient firework rockets",
                    "A ceremonial victory gate for military parades"
                ],
                "correct": 1,
                "explanation": "The Samrat Yantra is a giant equinoctial sundial whose triangular gnomon and curved marble quadrants measure local solar time with an accuracy of approximately two seconds."
            }
        ]
    },
    # Slide 17: Mastery Challenge Part I
    {
        "id": 17,
        "title": "Mastery Challenge • Part I",
        "tag": "Lunar Dynamics & Illumination",
        "narration": "Welcome to Part 1 of your Astronomy & Calendars Mastery Challenge! Test your deep understanding of lunar illumination, phase progression, and orbital periods across these 10 rigorous conceptual questions.",
        "points": [
            ("Questions 1 to 10", "Covering the source of Moon's light, spherical illumination geometry, the 8 distinct lunar phases, sidereal vs synodic month definitions, and the 2.2-day orbital realignment delay."),
            ("Real-Time Assessment", "Select your answer and view immediate feedback. Score points as you advance through the challenge!"),
            ("Step-by-Step Insights", "Click 'View Step-by-Step Solution' on any question to examine detailed astronomical diagrams and derivations."),
        ],
        "fact": "Tip: Remember that exactly 50% of the Moon's spherical body is always lit by the Sun; the phase depends solely on how much of that 50% we can view from Earth!",
        "sim_id": "mastery_quiz_1",
        "is_quiz": True,
        "quiz_range": (1, 10)
    },
    # Slide 18: Mastery Challenge Part II
    {
        "id": 18,
        "title": "Mastery Challenge • Part II",
        "tag": "Celestial Motions & Shadow Geometry",
        "narration": "Welcome to Part 2! Here we explore the daily motion of the Moon across the sky, why it rises 50 minutes later each day, the physics of synchronous rotation, and the precise orbital tilt that governs solar and lunar eclipses.",
        "points": [
            ("Questions 11 to 20", "Investigating daily eastward lunar drift, the ~50-minute daily rising delay, tidal locking, the truth about the 'Far Side', and the 5.14-degree orbital tilt preventing monthly eclipses."),
            ("Sharp Conceptual Focus", "Distinguish between physical orbital revolution and visible phase cycles from Earth's moving reference frame."),
            ("Interactive Modal Solutions", "Every question includes full mathematical and spatial reasoning available via the solution popup."),
        ],
        "fact": "Tip: An eclipse requires three celestial bodies—Sun, Earth, and Moon—to align along the line of nodes where their tilted orbital planes intersect!",
        "sim_id": "mastery_quiz_2",
        "is_quiz": True,
        "quiz_range": (11, 20)
    },
    # Slide 19: Mastery Challenge Part III
    {
        "id": 19,
        "title": "Mastery Challenge • Part III",
        "tag": "Calendars, Adhik Maas & Festivals",
        "narration": "Welcome to Part 3! Dive into the science of human timekeeping. We test your mastery of pure lunar calendars, tropical solar years, leap year mechanics, the mathematical necessity of Adhik Maas in luni-solar calendars, and the Indian National Calendar.",
        "points": [
            ("Questions 21 to 30", "Covering the 354-day lunar year, the 11-day annual seasonal drift, Gregorian 400-year century leap rules, Adhik Maas calculation, the Saka Era, and astronomical festival timing."),
            ("Bridging Culture and Science", "Discover how traditional festivals like Diwali, Eid, and Makar Sankranti directly reflect cosmic alignments."),
            ("Comprehensive Solutions", "Click the solution button to review calendar equations and historical milestones."),
        ],
        "fact": "Tip: A luni-solar calendar uses the Moon for its months and the Sun for its seasons, bridging the gap with an extra month every ~2.5 to 3 years!",
        "sim_id": "mastery_quiz_3",
        "is_quiz": True,
        "quiz_range": (21, 30)
    },
    # Slide 20: Mastery Challenge Part IV
    {
        "id": 20,
        "title": "Mastery Challenge • Part IV",
        "tag": "Satellites, Space Missions & Heritage",
        "narration": "Congratulations on reaching the final frontier! In Part 4, test your knowledge of artificial satellites, orbital velocity, Low Earth Orbit vs. Geostationary Orbit, ISRO's flagship missions NavIC, Chandrayaan, and Aditya-L1, and India's ancient astronomical heritage!",
        "points": [
            ("Questions 31 to 40", "Exploring Newton's orbital cannon, orbital vs escape velocity, Geostationary 35,786 km orbits, NavIC GPS constellation, remote sensing, and Jantar Mantar observatories."),
            ("Chapter Completion", "Submit your final answers to view your aggregate mastery score across all 40 questions!"),
            ("Detailed Step-by-Step Keys", "Full explanations provided for every orbital mechanics and historical astronomy challenge."),
        ],
        "fact": "Celebration: Upon completing Slide 20, you have mastered the entire curriculum of NCERT Class 8 Science Chapter 11: Astronomy and Calendars!",
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
        "question": "Which of the following statements correctly explains why the Moon is visible from Earth?",
        "options": [
            "The Moon generates light by internal nuclear fusion of hydrogen atoms",
            "The Moon is a non-luminous rocky body that reflects light emitted by the Sun",
            "The Moon's atmosphere glows due to high-energy cosmic ray ionization",
            "The Moon absorbs heat during the day and emits visible phosphorescence at night"
        ],
        "correct": 1,
        "solution": "Step 1: The Moon is an inert rocky natural satellite with no internal nuclear reactions or energy generation mechanisms.\nStep 2: The Sun is the sole primary light source in the Solar System.\nStep 3: Incident sunlight strikes the Moon's regolith surface, and roughly 7% to 12% is scattered and reflected towards Earth.\nConclusion: The Moon is visible exclusively because it reflects sunlight."
    },
    # Q2
    {
        "id": 2,
        "question": "At any given instant, what fraction of the Moon's spherical surface is illuminated by the Sun?",
        "options": [
            "It varies between 0% at New Moon to 100% at Full Moon",
            "Exactly 50% (one hemisphere) is always illuminated by the Sun",
            "Only 25% because of shadows cast by mountain craters",
            "75% on average throughout the lunar month"
        ],
        "correct": 1,
        "solution": "Step 1: The Moon is an approximately spherical celestial body.\nStep 2: Parallel rays of light from the distant Sun illuminate exactly half of any sphere facing the Sun at all times.\nStep 3: While an Earth-based observer views varying portions of that sunlit hemisphere depending on orbital geometry, the physical sunlit fraction of the Moon is always constant at 50% (one hemisphere)."
    },
    # Q3
    {
        "id": 3,
        "question": "What is the correct chronological sequence of lunar phases following the New Moon (Amavasya)?",
        "options": [
            "New Moon → Waning Crescent → Third Quarter → Waning Gibbous → Full Moon",
            "New Moon → Waxing Crescent → First Quarter → Waxing Gibbous → Full Moon",
            "New Moon → Full Moon → Waxing Crescent → Waning Crescent",
            "New Moon → First Quarter → Waxing Crescent → Full Moon → Third Quarter"
        ],
        "correct": 1,
        "solution": "Step 1: The cycle begins at New Moon (0% illumination visible from Earth).\nStep 2: Illumination increases (waxing): thin Waxing Crescent appears on the right.\nStep 3: At 90° orbital angle, First Quarter occurs (half the visible disk lit).\nStep 4: As it continues growing past half, it becomes Waxing Gibbous.\nStep 5: At 180° opposition, the full disk is illuminated (Full Moon / Purnima)."
    },
    # Q4
    {
        "id": 4,
        "question": "The time taken by the Moon to complete one physical 360-degree revolution around Earth relative to the distant stars is called:",
        "options": [
            "A Synodic Month (~29.53 days)",
            "A Sidereal Month (~27.32 days)",
            "A Solar Year (~365.24 days)",
            "An Anomalistic Month (~27.55 days)"
        ],
        "correct": 1,
        "solution": "Step 1: A revolution measured against the fixed background stars represents the true 360° orbital period of the Moon around Earth.\nStep 2: This period is scientifically defined as the 'Sidereal Month' (from Latin 'sidus' meaning star).\nStep 3: Its exact duration is approximately 27.32 days (27 days, 7 hours, 43 minutes)."
    },
    # Q5
    {
        "id": 5,
        "question": "Why is a Synodic Month (phase cycle of 29.53 days) longer than a Sidereal Month (orbital period of 27.32 days)?",
        "options": [
            "The Moon slows down its orbital speed due to lunar ocean tidal drag",
            "Earth is also moving around the Sun, so the Moon must travel an extra ~27° in orbit to realign with the Sun",
            "Solar radiation pressure pushes the Moon outward every month",
            "Earth's magnetic field periodically halts the Moon's rotation"
        ],
        "correct": 1,
        "solution": "Step 1: During the 27.32 days the Moon takes to orbit Earth 360°, Earth has moved ~27° along its annual orbit around the Sun (~1° per day).\nStep 2: Because Earth's position relative to the Sun has shifted, the Moon is not yet aligned between Earth and Sun.\nStep 3: The Moon must travel an additional ~27° along its orbit, which takes roughly 2.2 days.\nConclusion: 27.32 days + 2.21 days = 29.53 days (Synodic Month)."
    },
    # Q6
    {
        "id": 6,
        "question": "What is the traditional Indian astronomical name for the waning fortnight of the Moon (from Full Moon to New Moon)?",
        "options": [
            "Shukla Paksha (Bright Fortnight)",
            "Krishna Paksha (Dark Fortnight)",
            "Adhik Paksha",
            "Sankranti Paksha"
        ],
        "correct": 1,
        "solution": "Step 1: In Indian astronomy and calendar systems, a lunar month is split into two fortnights (pakshas).\nStep 2: The waxing period of increasing moonlight from New Moon to Full Moon is called Shukla Paksha (bright fortnight).\nStep 3: The waning period of diminishing moonlight from Full Moon to New Moon is called Krishna Paksha (dark fortnight)."
    },
    # Q7
    {
        "id": 7,
        "question": "When the Moon is at the 'First Quarter' phase, what fraction of its visible disk as seen from Earth appears illuminated?",
        "options": [
            "25% (one quarter of the disk)",
            "50% (exactly half of the disk)",
            "75% (three quarters of the disk)",
            "100% (the entire disk)"
        ],
        "correct": 1,
        "solution": "Step 1: 'First Quarter' refers to the Moon having completed one-quarter (25%) of its total 360° orbital journey around Earth.\nStep 2: Geometrically, at 90° elongation, an observer on Earth sees exactly half of the sunlit hemisphere and half of the shadowed hemisphere.\nConclusion: Exactly 50% of the visible disk is illuminated."
    },
    # Q8
    {
        "id": 8,
        "question": "If you observe the crescent Moon setting in the western sky shortly after sunset, the phase is:",
        "options": [
            "Waning Crescent",
            "Waxing Crescent",
            "Third Quarter",
            "Full Moon"
        ],
        "correct": 1,
        "solution": "Step 1: A crescent Moon visible in the western sky just after sunset is trailing slightly behind the Sun in its daily motion.\nStep 2: This means the Moon has just emerged past the New Moon phase and is situated east of the Sun.\nStep 3: As night falls, the illuminated sliver is growing each day.\nConclusion: It is a Waxing Crescent Moon."
    },
    # Q9
    {
        "id": 9,
        "question": "Which ancient Indian term refers to the New Moon day when the Moon is invisible from Earth?",
        "options": [
            "Purnima",
            "Amavasya",
            "Ekadashi",
            "Ashtami"
        ],
        "correct": 1,
        "solution": "Step 1: 'Amavasya' in Sanskrit denotes the conjunction of the Sun and Moon, signifying the New Moon day when the illuminated side faces away from Earth.\nStep 2: 'Purnima' refers to the Full Moon day.\nStep 3: 'Ekadashi' and 'Ashtami' refer to the 11th and 8th lunar days (tithis) respectively."
    },
    # Q10
    {
        "id": 10,
        "question": "What is the average albedo (reflectivity) of the Moon's surface?",
        "options": [
            "0.85 (highly reflective like fresh snow)",
            "0.50 (moderately reflective like concrete)",
            "0.12 (low reflectivity like dark rock or asphalt)",
            "0.01 (near-total light absorption like black velvet)"
        ],
        "correct": 2,
        "solution": "Step 1: Albedo measures the fraction of incident electromagnetic radiation reflected by a surface.\nStep 2: Fresh snow has an albedo of ~0.85; Earth has an average albedo of ~0.30.\nStep 3: The Moon's dry basaltic and anorthositic regolith reflects only about 7% to 12% (average albedo ~0.12) of incident sunlight, surprisingly similar to dark charcoal or weathered asphalt."
    },
    # Q11
    {
        "id": 11,
        "question": "By approximately how many degrees does the Moon travel eastward across the celestial sphere in 24 hours?",
        "options": [
            "About 1° per day",
            "About 13° per day",
            "About 45° per day",
            "About 90° per day"
        ],
        "correct": 1,
        "solution": "Step 1: The Moon completes a 360° orbit around Earth in approximately 27.32 days.\nStep 2: Calculate daily angular motion: $360^\\circ / 27.32 \\approx 13.18^\\circ$ per day.\nConclusion: The Moon advances eastward across the background stars by roughly 13 degrees every 24 hours."
    },
    # Q12
    {
        "id": 12,
        "question": "Why does the Moon rise approximately 50 minutes later every day?",
        "options": [
            "Earth's rotation slows down by 50 minutes every night",
            "The Moon moves eastward in orbit by ~13°, so Earth must rotate an extra ~50 minutes for the Moon to rise",
            "Atmospheric refraction delays the visual rising time by 50 minutes",
            "The Moon is moving further away from the Sun each hour"
        ],
        "correct": 1,
        "solution": "Step 1: The Moon moves eastward in its orbit by roughly 13.2° every day.\nStep 2: Earth rotates on its axis at a rate of $360^\\circ / 24\\text{ hours} = 15^\\circ$ per hour (or $1^\\circ$ every 4 minutes).\nStep 3: To cover the extra 13.2° that the Moon has advanced, Earth must rotate for an additional duration:\n$\\text{Delay} = 13.2^\\circ \\times 4\\text{ minutes/degree} \\approx 52.8\\text{ minutes} \\approx 50\\text{ minutes}$.\nConclusion: The Moon rises roughly 50 minutes later each day."
    },
    # Q13
    {
        "id": 13,
        "question": "At what time of day does a Full Moon rise and set?",
        "options": [
            "Rises at sunrise and sets at sunset",
            "Rises at noon and sets at midnight",
            "Rises around sunset and sets around sunrise",
            "Rises at midnight and sets at noon"
        ],
        "correct": 2,
        "solution": "Step 1: At Full Moon, the Moon is at 180° elongation, directly opposite the Sun with Earth in the middle.\nStep 2: As Earth rotates, when the Sun sets in the west, the point opposite the Sun rises in the east.\nConclusion: A Full Moon rises in the east approximately at sunset and sets in the west around sunrise."
    },
    # Q14
    {
        "id": 14,
        "question": "What is 'Synchronous Rotation' of the Moon?",
        "options": [
            "The Moon revolves around the Sun in sync with Mars",
            "The Moon rotates on its axis in the exact same duration as it takes to revolve around Earth (1:1 spin-orbit resonance)",
            "The Moon's phases synchronize with Earth's 24-hour day",
            "The Moon's tides synchronize with the seasons"
        ],
        "correct": 1,
        "solution": "Step 1: Synchronous rotation (or tidal locking) means the orbital revolution period and rotational spin period are identical.\nStep 2: The Moon takes ~27.3 days to rotate once on its axis and ~27.3 days to complete one orbit around Earth.\nConclusion: Because of this 1:1 ratio, the exact same hemisphere of the Moon faces Earth at all times."
    },
    # Q15
    {
        "id": 15,
        "question": "What caused the Moon to become tidally locked to Earth over geological time?",
        "options": [
            "Powerful magnetic fields anchoring the Moon's crust to Earth's core",
            "Gravitational tidal friction from Earth acting on the Moon's tidal bulges, slowing its spin down to match its orbital period",
            "Solar radiation pressure creating friction on the lunar mountains",
            "Repeated meteorite bombardments hitting only one side of the Moon"
        ],
        "correct": 1,
        "solution": "Step 1: In the early Solar System, the Moon rotated much faster than its orbit.\nStep 2: Earth's immense gravitational gradient exerted differential pull on the near and far sides, distorting the Moon into an oblate shape with tidal bulges.\nStep 3: As the Moon spun through these bulges, internal friction dissipated kinetic energy as heat, slowing its rotation until the bulges remained permanently aligned toward Earth."
    },
    # Q16
    {
        "id": 16,
        "question": "Which space mission captured the very first photographs of the Far Side of the Moon in 1959?",
        "options": [
            "Apollo 11 (USA)",
            "Luna 3 (USSR)",
            "Chandrayaan-1 (India)",
            "Chang'e 4 (China)"
        ],
        "correct": 1,
        "solution": "Step 1: The lunar far side is permanently turned away from Earth and was never seen by human eyes throughout history.\nStep 2: On October 7, 1959, the Soviet robotic probe Luna 3 flew around the Moon and transmitted the first historic images of the far side.\nStep 3: The photos revealed a starkly different, heavily cratered surface with very few basaltic dark maria."
    },
    # Q17
    {
        "id": 17,
        "question": "By how many degrees is the Moon's orbital plane inclined relative to Earth's orbital plane (the ecliptic)?",
        "options": [
            "0.0 degrees (perfectly coplanar)",
            "Approximately 5.14 degrees",
            "23.5 degrees",
            "90.0 degrees"
        ],
        "correct": 1,
        "solution": "Step 1: The ecliptic plane is the geometric plane of Earth's orbit around the Sun.\nStep 2: The Moon does not orbit in the ecliptic plane; its orbit is tilted by approximately $5.14^\\circ$ ($5^\\circ 8'$).\nConclusion: This ~5.14° inclination is the crucial reason why eclipses do not occur at every New Moon and Full Moon."
    },
    # Q18
    {
        "id": 18,
        "question": "What is the dark central region of a shadow where the light source is completely blocked called?",
        "options": [
            "Penumbra",
            "Umbra",
            "Antumbra",
            "Corona"
        ],
        "correct": 1,
        "solution": "Step 1: A shadow cast by an extended light source has two main regions.\nStep 2: The 'Umbra' is the darkest, central cone where the light source is totally blocked from view.\nStep 3: The 'Penumbra' is the outer, lighter region where only a portion of the light source is occluded."
    },
    # Q19
    {
        "id": 19,
        "question": "Why does the Moon take on a reddish-copper hue during a Total Lunar Eclipse rather than becoming pitch black?",
        "options": [
            "Lava eruptions illuminate the lunar surface during eclipses",
            "Earth's atmosphere scatters short blue wavelengths and refracts longer red wavelengths into Earth's shadow cone",
            "The Moon's rocks absorb infrared light and glow red",
            "Solar flares directly hit the Moon from behind the Earth"
        ],
        "correct": 1,
        "solution": "Step 1: During a total lunar eclipse, direct sunlight is blocked by Earth.\nStep 2: However, sunlight passing through Earth's atmosphere undergoes Rayleigh scattering: blue light is scattered away, while red wavelengths pass through.\nStep 3: Earth's atmosphere refracts (bends) this filtered red light into the umbral shadow cone, bathing the Moon in a copper-red glow (the 'Blood Moon')."
    },
    # Q20
    {
        "id": 20,
        "question": "What are the two points where the Moon's tilted orbit crosses the plane of the ecliptic called?",
        "options": [
            "Apogee and Perigee",
            "Lunar Nodes (Ascending and Descending Nodes / Rahu and Ketu)",
            "Solstices and Equinoxes",
            "Perihelion and Aphelion"
        ],
        "correct": 1,
        "solution": "Step 1: The intersection of two tilted geometric planes forms a line.\nStep 2: The two points where the Moon's 5.14° inclined orbital path intersects the ecliptic plane are known as the Lunar Nodes.\nStep 3: In ancient Indian astronomy, these intersection points were famously named Rahu (Ascending Node) and Ketu (Descending Node). Eclipses can only occur when Sun and Moon are near these nodes."
    },
    # Q21
    {
        "id": 21,
        "question": "How many days are there in a pure lunar calendar year of 12 synodic months, and how does it compare to the solar year?",
        "options": [
            "365 days; it is identical to the solar year",
            "Approximately 354 days; it is about 11 days shorter than the solar year",
            "366 days; it is 1 day longer than the solar year",
            "300 days; it is 65 days shorter than the solar year"
        ],
        "correct": 1,
        "solution": "Step 1: One synodic month is approximately 29.5306 days.\nStep 2: $12 \\times 29.5306 \\approx 354.367$ days.\nStep 3: A solar year is ~365.2422 days.\nStep 4: Difference = $365.2422 - 354.367 \\approx 10.875$ days $\\approx 11$ days.\nConclusion: A pure lunar calendar has ~354 days and is roughly 11 days shorter than the solar year."
    },
    # Q22
    {
        "id": 22,
        "question": "Which of the following modern calendars is an example of a purely lunar calendar that does not add intercalary months?",
        "options": [
            "Gregorian Calendar",
            "Islamic Hijri Calendar",
            "Indian National Saka Calendar",
            "Hebrew Calendar"
        ],
        "correct": 1,
        "solution": "Step 1: The Islamic Hijri calendar is strictly lunar, consisting of 12 lunar months of 29 or 30 days totaling 354 or 355 days.\nStep 2: Because it never adds extra intercalary months, its calendar year is ~11 days shorter than the solar seasonal year.\nStep 3: Thus, events like Ramadan cycle through all four seasons over a 33-year period."
    },
    # Q23
    {
        "id": 23,
        "question": "What is the primary cause of Earth's annual cycle of seasons (spring, summer, autumn, winter)?",
        "options": [
            "Earth moving closer to the Sun in summer and farther in winter",
            "The 23.5-degree tilt of Earth's rotational axis as it revolves around the Sun",
            "Fluctuations in solar energy output from sunspots",
            "The gravitational pull of Jupiter pulling Earth sideways"
        ],
        "correct": 1,
        "solution": "Step 1: Earth's rotational axis is tilted by $23.5^\\circ$ relative to the perpendicular to its orbital plane.\nStep 2: As Earth orbits the Sun, this fixed tilt causes each hemisphere to lean toward the Sun for half the year (experiencing longer days and direct solar rays = summer) and away for the other half (shorter days and slanting rays = winter).\nConclusion: The axial tilt is the true cause of seasons."
    },
    # Q24
    {
        "id": 24,
        "question": "Under the Gregorian calendar leap year rules, why was the year 1900 NOT a leap year, while the year 2000 WAS a leap year?",
        "options": [
            "1900 was during an international astronomical conference",
            "Century years ending in '00' must be divisible by 400 to be leap years",
            "1900 had an extra leap second instead",
            "Queen Victoria signed a decree canceling leap year in 1900"
        ],
        "correct": 1,
        "solution": "Step 1: Earth's tropical year is 365.2422 days—slightly less than 365.25 days.\nStep 2: Adding a leap year every 4 years adds too many days (0.25 vs 0.2422).\nStep 3: The Gregorian reform rule specifies that century years (ending in 00) are leap years ONLY if divisible by 400.\nStep 4: $1900 / 400 = 4.75$ (not divisible by 400 $\\rightarrow$ common year of 365 days).\nStep 5: $2000 / 400 = 5$ (evenly divisible by 400 $\\rightarrow$ leap year of 366 days)."
    },
    # Q25
    {
        "id": 25,
        "question": "In traditional Indian luni-solar calendars, what is 'Adhik Maas' (also called Purushottam Maas or Mala Masa)?",
        "options": [
            "A special fasting week celebrated in winter",
            "An intercalary (extra) 13th month inserted roughly every 2.5 to 3 years to synchronize lunar months with solar seasons",
            "The first month of the spring harvest",
            "A leap day added to the end of Phalguna"
        ],
        "correct": 1,
        "solution": "Step 1: A lunar year of 354 days falls short of a solar year (365 days) by ~11 days per year.\nStep 2: Over roughly 32.5 months (about 2.7 years), this deficit accumulates to approximately 30 days (one full lunar month).\nStep 3: To prevent festivals from shifting seasons, an entire extra lunar month called 'Adhik Maas' is inserted.\nConclusion: Adhik Maas synchronizes the lunar calendar with the solar seasons."
    },
    # Q26
    {
        "id": 26,
        "question": "Who was the renowned Indian astrophysicist who chaired the Calendar Reform Committee appointed by the Government of India in 1952?",
        "options": [
            "Homi J. Bhabha",
            "Prof. Meghnad Saha",
            "Sir C. V. Raman",
            "Vikram Sarabhai"
        ],
        "correct": 1,
        "solution": "Step 1: In November 1952, Prime Minister Jawaharlal Nehru appointed the Calendar Reform Committee under the Council of Scientific and Industrial Research (CSIR).\nStep 2: Prof. Meghnad Saha, world-renowned for the Saha Ionization Equation in astrophysics, chaired the committee.\nStep 3: The committee standardized India's diverse regional calendars into the Indian National Calendar (Saka Calendar), adopted on March 22, 1957."
    },
    # Q27
    {
        "id": 27,
        "question": "On which day of the Gregorian calendar does the first day of the Indian National Calendar (Chaitra 1) begin in a common year?",
        "options": [
            "January 1",
            "March 22 (Vernal Equinox)",
            "April 14",
            "July 1"
        ],
        "correct": 1,
        "solution": "Step 1: The Indian National Calendar was scientifically anchored to the Vernal Equinox (the start of astronomical spring).\nStep 2: In a normal common year, Chaitra 1 falls precisely on March 22.\nStep 3: In a Gregorian leap year, Chaitra 1 falls on March 21, and Chaitra has 31 days instead of 30."
    },
    # Q28
    {
        "id": 28,
        "question": "If the current Gregorian year is 2026 CE, what is the corresponding year in the Saka Era of the Indian National Calendar?",
        "options": [
            "2083 Saka",
            "1948 Saka",
            "2026 Saka",
            "1447 Saka"
        ],
        "correct": 1,
        "solution": "Step 1: The Saka Era began in 78 CE of the Gregorian calendar.\nStep 2: To calculate the Saka year from the Gregorian year:\n$\\text{Saka Year} = \\text{Gregorian Year} - 78$.\nStep 3: For 2026 CE: $2026 - 78 = 1948$ Saka Era.\nConclusion: 1948 Saka."
    },
    # Q29
    {
        "id": 29,
        "question": "Which of the following festivals is celebrated on the Full Moon (Purnima) night?",
        "options": [
            "Diwali",
            "Holi",
            "Eid-ul-Fitr",
            "Maha Shivratri"
        ],
        "correct": 1,
        "solution": "Step 1: Holi is celebrated on the Full Moon day (Purnima) of the Hindu month of Phalguna.\nStep 2: Diwali is celebrated on the New Moon (Amavasya) of Kartika.\nStep 3: Eid-ul-Fitr is celebrated on the sighting of the new crescent moon (Hilal) at the start of Shawwal.\nStep 4: Maha Shivratri is celebrated on the 14th night of the dark fortnight (Krishna Paksha Chaturdashi) of Magha/Phalguna."
    },
    # Q30
    {
        "id": 30,
        "question": "Why is the festival of Eid-ul-Fitr celebrated on different dates of the solar Gregorian calendar each year, shifting by about 11 days earlier?",
        "options": [
            "It is decided by annual political votes in different countries",
            "The Islamic calendar is purely lunar (354 days), so its months shift 11 days earlier against the 365-day solar year",
            "It is celebrated only during leap years",
            "It follows the orbital period of the planet Jupiter"
        ],
        "correct": 1,
        "solution": "Step 1: The Islamic calendar is purely lunar with 354 or 355 days per year.\nStep 2: The Gregorian calendar is solar with 365 or 366 days per year.\nStep 3: Because the lunar year is ~11 days shorter, every Islamic month (including Shawwal and Ramadan) begins ~11 days earlier in the Gregorian calendar each year."
    },
    # Q31
    {
        "id": 31,
        "question": "In Newton's orbital cannon thought experiment, what minimum horizontal velocity must a projectile reach to enter circular Low Earth Orbit (neglecting air resistance)?",
        "options": [
            "About 1.2 km/s",
            "About 7.9 km/s (approx. 28,000 km/h)",
            "About 11.2 km/s",
            "Speed of light (300,000 km/s)"
        ],
        "correct": 1,
        "solution": "Step 1: Orbital velocity $v_o$ is derived by equating gravitational force to centripetal force:\n$\\frac{G M m}{R^2} = \\frac{m v_o^2}{R} \\implies v_o = \\sqrt{\\frac{G M}{R}}$.\nStep 2: Substituting $G = 6.674 \\times 10^{-11}\\text{ N m}^2/\\text{kg}^2$, $M = 5.972 \\times 10^{24}\\text{ kg}$, and $R = 6,371\\text{ km}$:\n$v_o \\approx 7,910\\text{ m/s} \\approx 7.9\\text{ km/s}$ (approx. 28,000 km/h).\nConclusion: The minimum orbital speed for Low Earth Orbit is ~7.9 km/s."
    },
    # Q32
    {
        "id": 32,
        "question": "What is the Escape Velocity from Earth's surface—the speed needed to break free of Earth's gravitational pull entirely?",
        "options": [
            "7.9 km/s",
            "9.8 km/s",
            "11.2 km/s (approx. 40,300 km/h)",
            "25.0 km/s"
        ],
        "correct": 2,
        "solution": "Step 1: Escape velocity $v_e$ is the speed at which kinetic energy equals gravitational potential energy:\n$\\frac{1}{2} m v_e^2 = \\frac{G M m}{R} \\implies v_e = \\sqrt{\\frac{2 G M}{R}} = \\sqrt{2} \\times v_o$.\nStep 2: $v_e = \\sqrt{2} \\times 7.91\\text{ km/s} \\approx 1.414 \\times 7.91 \\approx 11.2\\text{ km/s}$.\nConclusion: Escape velocity is ~11.2 km/s."
    },
    # Q33
    {
        "id": 33,
        "question": "What is the unique characteristic of a satellite placed in Geostationary Orbit (GEO) at an altitude of 35,786 km?",
        "options": [
            "It orbits Earth once every 90 minutes across the poles",
            "Its orbital period is exactly 24 hours, so it appears stationary relative to an observer on Earth's equator",
            "It is completely immune to Earth's gravity",
            "It reflects 100% of the sunlight hitting its solar arrays"
        ],
        "correct": 1,
        "solution": "Step 1: As orbital altitude increases, orbital speed decreases and the period lengthens (Kepler's Third Law).\nStep 2: At precisely 35,786 km above the equator, the orbital period equals Earth's rotational period: exactly 23 hours, 56 minutes, 4 seconds (one sidereal day).\nStep 3: Because the satellite travels east at the exact rate Earth rotates, it hovers over the same geographic longitude, appearing stationary in the sky."
    },
    # Q34
    {
        "id": 34,
        "question": "What type of satellite orbit passes over the North and South Poles and is typically used for Earth observation and remote sensing?",
        "options": [
            "Equatorial Geostationary Orbit",
            "Polar Sun-Synchronous Orbit (LEO)",
            "Geostationary Transfer Orbit",
            "Lagrange Point L2 Orbit"
        ],
        "correct": 1,
        "solution": "Step 1: Polar orbits have an inclination near 90°, passing over the polar regions.\nStep 2: As the satellite orbits from north to south, Earth rotates beneath it from west to east.\nStep 3: This allows the satellite's sensors to scan and photograph the entire surface of Earth strip by strip over several days, making it ideal for environmental mapping, meteorology, and military reconnaissance."
    },
    # Q35
    {
        "id": 35,
        "question": "How many operational satellites make up the core constellation of India's indigenous regional navigation system, NavIC?",
        "options": [
            "3 satellites",
            "7 satellites",
            "24 satellites",
            "100 satellites"
        ],
        "correct": 1,
        "solution": "Step 1: NavIC (Navigation with Indian Constellation, formerly IRNSS) is designed to provide high-precision positioning services across India and extending 1,500 km around its borders.\nStep 2: The baseline constellation consists of 7 satellites: 3 in geostationary orbit (GEO) and 4 in inclined geosynchronous orbit (GSO).\nConclusion: 7 satellites."
    },
    # Q36
    {
        "id": 36,
        "question": "Which branch of satellite technology uses sensors to record reflected electromagnetic radiation from Earth's surface to monitor agriculture, forests, and water bodies?",
        "options": [
            "Direct Satellite Broadcasting (DTH)",
            "Remote Sensing",
            "Satellite Telephony",
            "Laser Altimetry Astronomy"
        ],
        "correct": 1,
        "solution": "Step 1: Remote sensing is the acquisition of information about an object or phenomenon without making physical contact.\nStep 2: Earth observation satellites use multispectral cameras (detecting visible, near-infrared, and microwave bands) to assess crop health (NDVI), monitor forest cover, trace groundwater resources, and track flood inundation."
    },
    # Q37
    {
        "id": 37,
        "question": "What historic milestone did India's Chandrayaan-3 mission achieve on August 23, 2023?",
        "options": [
            "First human landing on Mars",
            "First spacecraft to soft-land near the lunar South Pole",
            "First sample return mission from an asteroid",
            "First probe to land on the rings of Saturn"
        ],
        "correct": 1,
        "solution": "Step 1: On August 23, 2023, ISRO's Chandrayaan-3 lander module 'Vikram' with the rover 'Pragyan' made a flawless soft landing on the Moon.\nStep 2: India became the fourth country in history to achieve a soft lunar landing (after the USSR, USA, and China) and the very first nation in human history to land in the rugged terrain near the lunar South Pole."
    },
    # Q38
    {
        "id": 38,
        "question": "What is the scientific significance of placing the Aditya-L1 solar observatory at the Sun-Earth Lagrange Point 1 (L1)?",
        "options": [
            "It is protected from solar radiation by Earth's magnetic tail",
            "It remains in an equilibrium position 1.5 million km from Earth with an uninterrupted 24/7 view of the Sun free from eclipses",
            "It is able to scoop solar wind gas directly into its fuel tanks",
            "It lands on the surface of Mercury every six months"
        ],
        "correct": 1,
        "solution": "Step 1: Lagrange Point 1 (L1) is a gravitational equilibrium point located ~1.5 million km from Earth directly along the Sun-Earth line.\nStep 2: At L1, the combined gravitational pull of the Sun and Earth provides precisely the centripetal force needed for the spacecraft to orbit the Sun in lockstep with Earth.\nStep 3: This vantage point ensures an uninterrupted view of the Sun with zero eclipses or occultations by Earth or Moon."
    },
    # Q39
    {
        "id": 39,
        "question": "In his landmark 499 CE astronomical treatise 'Aryabhatiya', what revolutionary explanation did Aryabhata provide for the day-night cycle?",
        "options": [
            "The Sun revolves around a stationary flat Earth once every 24 hours",
            "The spherical Earth rotates daily on its own internal axis, making the stars appear to revolve in the opposite direction",
            "Giant celestial serpents swallow and release the Sun daily",
            "The ocean tides push the Sun below the horizon each evening"
        ],
        "correct": 1,
        "solution": "Step 1: In Section IV, Verse 9 of 'Aryabhatiya', Aryabhata gave the famous boat analogy:\n'Just as a man in a boat moving forward sees stationary objects along the riverbank moving backward, so the stationary stars appear to move westward because Earth is rotating eastward on its axis.'\nConclusion: Aryabhata correctly discovered that Earth rotates daily on its axis."
    },
    # Q40
    {
        "id": 40,
        "question": "What is the world's largest stone sundial, located at the Jantar Mantar in Jaipur, called?",
        "options": [
            "Ram Yantra",
            "Jai Prakash Yantra",
            "Vrihat Samrat Yantra",
            "Misra Yantra"
        ],
        "correct": 2,
        "solution": "Step 1: The Jantar Mantar observatory at Jaipur was built by Maharaja Sawai Jai Singh II between 1724 and 1734 CE.\nStep 2: The centerpiece of the observatory is the 'Vrihat Samrat Yantra' (Supreme Instrument), standing 27 meters (88 feet) tall.\nStep 3: Its massive triangular gnomon casts a shadow onto graduated marble quadrants that moves at 1 millimeter per second, reading local solar time to an accuracy of 2 seconds."
    }
]

