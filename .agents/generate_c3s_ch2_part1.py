#!/usr/bin/env python3
"""
NCERT Class 3 Science (Our Wondrous World) - Chapter 2: Going to the Mela
Part 1: Slides 1 to 8 Data Generator
Strict Constraints:
- Titles: Strictly 1-3 words each
- Spoken text: Strictly 195-215 words each
- Zero human character names
- Zero lecturer personas (Dr, Sir, Madam, Mr, Mrs)
- Exactly 2 checkpoints per slide with 4 options each
"""

slides_part1 = [
    {
        "id": 1,
        "title": "Excitement And Planning",
        "subtitle": "Anticipating community celebrations, distant travel planning, and route decisions",
        "speech": "Welcome, curious young learners, to our science exploration of community journeys and village fairs. Community fairs, or melas, are magnificent cultural gatherings where families, friends, and neighbors come together to celebrate shared traditions, crafts, and games. Planning a journey to a distant town mela requires thoughtful preparation and practical organization. When children hear that a grand annual mela has opened at the expansive central parade ground several kilometers away, their hearts fill with boundless excitement. However, because the fairground is located far beyond walking distance, the family must carefully discuss and plan transportation options. Walking several kilometers along busy highways is exhausting for growing children and physically impossible for aging elders. Therefore, family members gather around the kitchen table to examine local public transit schedules, deciding to travel together by city bus. Planning ahead teaches young learners about spatial distance, travel time, and the importance of budgeting transit fares before stepping out of the house. Successful journeys depend on collaborative decision-making, where everyone's opinions and physical capabilities are lovingly considered. Preparing for a shared family outing develops practical life skills, responsibility, and mutual cooperation that make community excursions safe, organized, and truly delightful for all participants.",
        "checkpoints": [
            {
                "question": "Why is careful pre-travel planning essential before visiting a distant town mela?",
                "options": [
                    "It ensures safe transportation, budgets travel time, and considers everyone's physical needs",
                    "It ensures that children can walk along railway tracks without tickets",
                    "It prevents family members from enjoying any rides or games at the fair",
                    "It allows families to travel without knowing where the destination is located"
                ],
                "answer": 0,
                "hint": "Planning considers distance, transport, schedules, and elder comfort.",
                "explanation": "Pre-travel planning identifies the right transportation, estimates transit time, and ensures every family member travels comfortably."
            },
            {
                "question": "What is the primary reason for choosing a public bus over walking to a distant fairground?",
                "options": [
                    "Buses cover long kilometers safely without exhausting children and elderly grandparents",
                    "Walking on busy highways at night is completely safe for toddlers",
                    "Buses are meant exclusively for carrying heavy market livestock",
                    "City buses travel underground through deep mountain tunnels only"
                ],
                "answer": 0,
                "hint": "Long distances tire out little legs and fragile knees.",
                "explanation": "Public buses allow families to travel long distances safely and comfortably together without physical exhaustion."
            }
        ]
    },
    {
        "id": 2,
        "title": "Elder Care Inclusivity",
        "subtitle": "Supportive familial reassurance, addressing physical discomfort, and universal access",
        "speech": "A truly loving and compassionate family ensures that no member is left behind during joyous community celebrations. When plans for the annual mela are finalized, elderly grandparents often hesitate to participate because aging joints and aching knees make prolonged walking painful and exhausting. In a thoughtful household, family members immediately step forward to offer comforting reassurance, gentle encouragement, and practical assistance. Parents explain that visiting relatives arriving by morning passenger train and helpful next-door neighbors will travel alongside the family as a united, supportive group. Furthermore, parents reassure the hesitant grandmother that modern public venues provide specialized amenities, including comfortable resting benches and free wheelchairs available at the entrance gate. Knowing that caring hands will support her every step of the way, the grandmother happily agrees to join the excursion. In environmental science, we learn that inclusivity means actively adapting activities so individuals of all ages and physical abilities can participate with dignity. Caring for aging elders fosters intergenerational warmth, teaching young children that empathy, patient listening, and cooperative teamwork transform daunting obstacles into joyful collective experiences. Every family milestone becomes immensely richer when celebrated in the cherished company of our wise, smiling grandparents. Respectful family consideration ensures that aging grandparents feel profoundly valued, comforted, and included.",
        "checkpoints": [
            {
                "question": "Why did the elderly grandmother initially hesitate to visit the town mela?",
                "options": [
                    "Because painful joints and aching knees made walking long distances difficult",
                    "Because she disliked traditional music and delicious festive sweets",
                    "Because the town mela only allowed entry to young school children",
                    "Because she preferred sleeping outside in the cold garden shed"
                ],
                "answer": 0,
                "hint": "Joint pain makes prolonged walking on hard ground uncomfortable for seniors.",
                "explanation": "Aging joints and leg pain make walking long distances difficult, causing seniors to worry about being an inconvenience."
            },
            {
                "question": "How can families ensure elderly grandparents participate comfortably in community outings?",
                "options": [
                    "By providing physical support, utilizing entrance wheelchairs, and taking frequent rest pauses",
                    "By demanding that grandparents run fast to catch the early bus",
                    "By leaving grandparents alone at home locked inside a dark room",
                    "By forcing elders to carry all the heavy luggage on their heads"
                ],
                "answer": 0,
                "hint": "Look for loving assistance, wheelchairs, and gentle rest pauses.",
                "explanation": "Offering physical assistance, borrowing wheelchairs, and taking resting breaks allows elders to enjoy family celebrations comfortably."
            }
        ]
    },
    {
        "id": 3,
        "title": "Pedestrian Road Safety",
        "subtitle": "Navigating streets safely, footpath discipline, and observing road traffic",
        "speech": "Stepping out from the quiet neighborhood lane onto the bustling main road to reach the public bus stop requires strict pedestrian safety discipline. Roads are shared public spaces filled with fast-moving automobiles, heavy freight trucks, motorcycles, and bicycles. Young learners must always walk on the raised pedestrian footpath or sidewalk, keeping safely away from the roadway edge where motorized vehicles travel. When walking alongside family elders and younger siblings, children should hold an adult's hand firmly and remain alert to their surroundings, never running ahead impulsively or chasing a dropped ball into traffic. At intersections where pedestrians must cross, everyone should use painted zebra crossings, looking carefully to the right, then to the left, and once again to the right to verify that all approaching vehicles have come to a complete halt. In environmental studies, road safety education empowers children to recognize traffic signals, directional road signs, and the vital role of alert traffic police officers who direct traffic flows. Cultivating keen spatial awareness, avoiding distractions like mobile screens while walking, and obeying road safety rules guarantees that every journey begins and concludes without avoidable mishaps or injuries. Mindful road discipline ensures pedestrians navigate complex community thoroughfares safely and arrive without mishap.",
        "checkpoints": [
            {
                "question": "Where should pedestrians always walk when moving alongside busy vehicular roads?",
                "options": [
                    "On the designated raised sidewalk or pedestrian footpath",
                    "In the middle of the road directly between speeding trucks",
                    "Along the slippery sloped drainage gutters beneath bridges",
                    "On top of parked cars and delivery vans along the street"
                ],
                "answer": 0,
                "hint": "Footpaths are designed specifically to separate walking people from motor vehicles.",
                "explanation": "Sidewalks and footpaths provide a secure, elevated path that isolates pedestrians from motorized traffic."
            },
            {
                "question": "What is the proper safety procedure before stepping onto a pedestrian zebra crossing?",
                "options": [
                    "Look right, then left, and right again to ensure all vehicles have fully stopped",
                    "Close your eyes tightly and sprint across the street as fast as possible",
                    "Throw your school backpack into the road to see if cars will swerve",
                    "Sit down in the center of the road to tie your shoelaces slowly"
                ],
                "answer": 0,
                "hint": "Look both ways carefully to confirm traffic has yielded.",
                "explanation": "Checking traffic in both directions confirms that vehicles have stopped, allowing pedestrians to cross the street safely."
            }
        ]
    },
    {
        "id": 4,
        "title": "Public Bus Journey",
        "subtitle": "Public transit etiquette, reserved seating courtesy, and passenger safety",
        "speech": "Arriving at the bus stop shelter, the family spots Bus Number 401 approaching the curb, clearly displaying its route number and destination board on the front windshield. Boarding a public bus teaches children valuable lessons in civic etiquette and passenger safety. Passengers wait patiently in a neat queue, allowing disembarking passengers to step off before boarding calmly without pushing or shoving. Inside the bus, thoughtful passengers immediately notice designated reserved seats labeled specifically for senior citizens, expectant mothers, and persons with disabilities. A courteous passenger graciously stands up, offering their seat to the elderly grandmother so she can sit comfortably near the front entrance without losing her balance as the bus maneuvers through city traffic. Once the bus begins moving, strict in-transit safety rules must be followed: all passengers must remain seated or hold firmly onto overhead grab rails, and children must never lean out of windows or stick hands and heads outside. Moving buses pass close to roadside signposts, tree branches, and oncoming vehicles, making leaning out extraordinarily dangerous. Public transit connects communities affordably, and following safety guidelines ensures every passenger enjoys a smooth, pleasant journey. Responsible public transit behavior fosters a harmonious, comfortable atmosphere where all passengers travel securely.",
        "checkpoints": [
            {
                "question": "Why must passengers never extend their hands or heads out of moving bus windows?",
                "options": [
                    "Passing trees, electric poles, and oncoming vehicles can cause severe injuries",
                    "Because moving air outside causes bus tickets to turn into butterflies",
                    "Because bus windows are designed to be used only as emergency exits",
                    "Because bus drivers are not permitted to drive while windows are open"
                ],
                "answer": 0,
                "hint": "Roadside poles and passing trucks are inches away from moving windows.",
                "explanation": "Extending body parts outside moving vehicle windows risks fatal collisions with roadside poles, branches, or passing traffic."
            },
            {
                "question": "What civic duty should young, healthy passengers practice when elderly citizens board a crowded bus?",
                "options": [
                    "Offer their seat courteously to ensure the elder sits safely",
                    "Pretend to be asleep so they do not have to move from their seat",
                    "Demand that the elderly passenger pay double the normal fare",
                    "Ask the driver to stop the bus and make the elder step off"
                ],
                "answer": 0,
                "hint": "Courtesy and safety mean helping elders sit comfortably.",
                "explanation": "Offering seats to seniors protects them from falls during sudden vehicle braking and demonstrates civic respect."
            }
        ]
    },
    {
        "id": 5,
        "title": "Transit Ticketing Rules",
        "subtitle": "Fare calculations, ticket verification, and public transport economics",
        "speech": "As the bus rolls steadily along the suburban route, the uniformed bus conductor makes his way down the central aisle with an electronic ticketing machine slung over his shoulder. Purchasing public transit tickets is a fundamental civic duty that funds vehicle maintenance, fuel costs, and driver salaries. The father calculates the fare for the combined travel party, requesting five full tickets for the adults and four half-rate concession tickets for the school-aged children. In public transportation systems, transport corporations offer discounted half-tickets for young children, recognizing that growing families need affordable access to urban transit. The conductor enters the passenger count into the digital terminal, issues printed paper tickets with QR codes, and hands back the exact change. Children closely examine the printed ticket slip, observing important recorded details including the boarding point, destination stop, date, timestamp, bus route number, and total fare amount. Keeping travel tickets safe until reaching the destination is essential because ticket examiners board intermittently to verify compliance. Learning how ticketing works introduces young students to practical arithmetic, consumer transactions, and the shared responsibility of supporting public services that make modern community travel possible. Preserving travel tickets until arrival upholds legal compliance and supports vital community transportation infrastructure.",
        "checkpoints": [
            {
                "question": "Why do public bus corporations offer half-price concession tickets for school children?",
                "options": [
                    "To support growing families with affordable, subsidized public transportation",
                    "Because children are only allowed to occupy half of a bus seat cushion",
                    "Because children are required to get off the bus halfway along the route",
                    "To discourage young children from ever using public transportation systems"
                ],
                "answer": 0,
                "hint": "Concessions help families afford essential public transport.",
                "explanation": "Subsidized half-fares provide affordable mobility for school children and families, encouraging public transit usage."
            },
            {
                "question": "What important travel information is recorded on a printed bus ticket?",
                "options": [
                    "Route number, boarding and destination stops, fare amount, and timestamp",
                    "The personal home phone number of every passenger on board",
                    "The names of all favorite television cartoon characters",
                    "A detailed scientific weather forecast for the upcoming winter month"
                ],
                "answer": 0,
                "hint": "Tickets record essential legal transaction data.",
                "explanation": "Bus tickets print route numbers, origin and destination stages, date, time, and fare paid for verification."
            }
        ]
    },
    {
        "id": 6,
        "title": "Fair Entrance Amenities",
        "subtitle": "Wayfinding orientation, schematic maps, and lost-and-found security",
        "speech": "The bus arrives at the grand festival stop, where the family alights safely and walks toward the festive entrance gates of the vast parade ground. At the entry plaza, extended family members arriving from the railway station by three-wheeled autorickshaw greet them with warm embraces and cheerful smiles. Before plunging into the bustling crowds, wise adults gather the entire group at the entrance information hub to study a large, illuminated schematic map of the fairground. The map outlines major pathways, identifying the locations of amusement rides, craft pavilions, restrooms, drinking water taps, and food courts. Right beside the map board stands an official 'Lost and Found' assistance booth equipped with public address loudspeakers. Family elders instruct all children to memorize this booth as the designated meeting landmark in case anyone accidentally gets separated in the crowd. Children are reminded to remain calm, approach a uniformed police officer or booth volunteer, and clearly state their parents' contact phone numbers. Organizing wayfinding landmarks and knowing emergency rendezvous points before entering a crowded public venue prevents panic, ensuring that children navigate vast community spaces with safety, self-assurance, and peace of mind. Preparing emergency rendezvous points gives young explorers confidence to navigate large festive venues without fear.",
        "checkpoints": [
            {
                "question": "Why should families study the schematic mela map at the entrance gate before exploring?",
                "options": [
                    "To orient themselves, locate essential amenities, and plan safe pathways",
                    "To find out where they can purchase live wild zoo animals",
                    "To discover secret underground tunnels leading out of the city",
                    "Because the map is a puzzle game that must be solved to enter"
                ],
                "answer": 0,
                "hint": "Maps display exits, water taps, first aid, and attraction zones.",
                "explanation": "Schematic maps show the layout of attractions, restrooms, water points, and exits, allowing visitors to navigate safely."
            },
            {
                "question": "What should a child immediately do if separated from family in a crowded fair?",
                "options": [
                    "Go to the 'Lost and Found' booth or approach a uniformed police officer for help",
                    "Run out into the highway traffic searching for family members",
                    "Hide under a food stall table and cry without speaking to anyone",
                    "Follow an unknown stranger who offers to buy them sugary candy"
                ],
                "answer": 0,
                "hint": "Uniformed officers and official assistance booths are safe places for help.",
                "explanation": "Approaching official personnel or the 'Lost and Found' booth allows trained staff to broadcast announcements and reunite families."
            }
        ]
    },
    {
        "id": 7,
        "title": "Emergency Service Vehicles",
        "subtitle": "Public safety lifelines, emergency sirens, and medical first responders",
        "speech": "Stationed prominently near the main entrance gates, children notice a fleet of specialized emergency service vehicles standing on high alert. These include a white hospital ambulance equipped with flashing red roof beacons, a navy-blue police patrol jeep with communication antennae, and a bright red municipal fire engine fitted with high-pressure water hoses and extendable ladders. Large public gatherings like town melas attract tens of thousands of visitors, creating high risks of sudden medical emergencies, heat exhaustion, accidental fires from cooking stalls, and crowd congestion. Trained paramedics inside the ambulance are prepared with oxygen cylinders, stretchers, and emergency first aid supplies to treat injured or fainting visitors immediately. The fire engine crew stands ready to extinguish accidental kitchen flare-ups, while alert police personnel coordinate perimeter security and manage crowd flows. Observing these vital emergency vehicles teaches young students about civic infrastructure, disaster preparedness, and the selfless community helpers who work tirelessly behind the scenes to safeguard human life. Recognizing the distinctive emergency siren sounds, flashing beacon colors, and national emergency contact phone numbers empowers children to stay calm and respond responsibly whenever unexpected emergencies occur in public spaces. Respecting emergency personnel highlights our shared civic responsibility in maintaining a secure, compassionate society.",
        "checkpoints": [
            {
                "question": "Why are ambulances, police jeeps, and fire engines stationed at large public fairgrounds?",
                "options": [
                    "To provide rapid medical aid, maintain public order, and respond immediately to fires",
                    "To provide amusement joyrides for visitors around the parade ground",
                    "To sell hot snacks, tea, and souvenirs to passing tourists",
                    "To block the entrance so that no visitors can enter the mela"
                ],
                "answer": 0,
                "hint": "Emergency vehicles protect lives during sudden medical or fire incidents.",
                "explanation": "Emergency vehicles guarantee immediate first aid, fire containment, and crowd safety during massive public gatherings."
            },
            {
                "question": "What critical medical equipment is carried inside a public emergency ambulance?",
                "options": [
                    "Oxygen cylinders, stretchers, bandages, and vital emergency first aid kits",
                    "Cotton candy machines and ice cream dispensing freezers",
                    "Heavy iron construction tools for building brick houses",
                    "Musical brass instruments for marching band parades"
                ],
                "answer": 0,
                "hint": "Ambulances carry life-support equipment for urgent medical treatment.",
                "explanation": "Ambulances are mobile healthcare units stocked with oxygen, stretchers, bandages, and medications for emergency care."
            }
        ]
    },
    {
        "id": 8,
        "title": "Accessible Wheelchair Mobility",
        "subtitle": "Universal barrier-free design, assistive mobility ramps, and dignified participation",
        "speech": "At the entrance accessibility counter, the family gratefully requests an assistive mobility wheelchair provided free of charge by the mela organizing committee. The elderly grandmother, whose knees were aching from the bus ride, is comfortably seated in the sturdy, padded wheelchair. Her son and younger family members take turns gently pushing the chair along the paved, barrier-free pathways that crisscross the fairground. In modern environmental planning and civic science, barrier-free accessibility ensures that public recreational spaces are welcoming to senior citizens, people recovering from illnesses, and individuals with physical disabilities. Rather than facing steep brick steps, fairground pavilions feature gentle sloping access ramps with sturdy handrails, allowing wheeled mobility devices to roll smoothly between exhibit halls and food courts. Seated comfortably at eye level with the vibrant surroundings, the grandmother enjoys every colorful spectacle, laughing at clown antics and admiring handcrafted textiles without enduring excruciating physical pain. Ensuring barrier-free accessibility demonstrates that a compassionate society values every citizen equally. When public spaces remove physical barriers, they foster social inclusion, dignity, and intergenerational joy, allowing families to celebrate cherished cultural milestones together in complete comfort. Inclusive public architecture ensures that public cultural celebrations remain accessible, welcoming, and joyful for every citizen.",
        "checkpoints": [
            {
                "question": "How do gentle sloping access ramps help individuals using assistive wheelchairs at fairgrounds?",
                "options": [
                    "They allow wheeled mobility devices to roll smoothly without encountering steep stairs",
                    "They make the pathways slippery so that wheelchairs slide downhill fast",
                    "They prevent children from walking alongside their elderly grandparents",
                    "They are designed exclusively as drainage ditches for monsoon rainwater"
                ],
                "answer": 0,
                "hint": "Ramps replace stair steps with gradual slopes for smooth rolling.",
                "explanation": "Access ramps eliminate stair barriers, enabling wheelchairs, strollers, and carts to navigate public spaces easily."
            },
            {
                "question": "What is the primary goal of barrier-free design in public parks and fairgrounds?",
                "options": [
                    "To ensure people of all ages and physical abilities can participate with dignity",
                    "To make fairgrounds look like modern industrial automobile factories",
                    "To charge higher admission ticket prices for visitors who use wheelchairs",
                    "To force all visitors to travel exclusively inside motorized vehicles"
                ],
                "answer": 0,
                "hint": "Barrier-free design provides universal access and dignified inclusion for all.",
                "explanation": "Universal barrier-free design guarantees that public environments are accessible, welcoming, and safe for everyone."
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part1)} slides for Part 1.")
    for s in slides_part1:
        wc = len(s["speech"].split())
        tw = len(s["title"].split())
        print(f"Slide {s['id']}: '{s['title']}' ({tw} words) - Speech: {wc} words")
        assert 1 <= tw <= 3, f"Title length violation on slide {s['id']}"
        assert 195 <= wc <= 215, f"Speech word count violation on slide {s['id']}: {wc} words"
        assert len(s["checkpoints"]) == 2, f"Checkpoints violation on slide {s['id']}"
    print("ALL SLIDES 1-8 STRICTLY PASSED VALIDATION!")
