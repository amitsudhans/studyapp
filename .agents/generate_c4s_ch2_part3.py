# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 2: Exploring Our Neighbourhood
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names (replaced with generic roles).
Zero lecturer personas.
Clean Unicode throughout.
"""

def make_sol_html(steps, note=None):
    items = "".join(f"<li class='mb-2 text-slate-700 leading-relaxed'>{s}</li>" for s in steps)
    html = f"<div class='space-y-3 font-sans'><div class='bg-blue-50 border-l-4 border-blue-500 p-3.5 rounded-r-lg'><h5 class='text-xs font-bold uppercase tracking-wider text-blue-800 mb-2'>Step-by-Step Solution</h5><ol class='list-decimal list-inside space-y-1.5 text-sm'>{items}</ol></div>"
    if note:
        html += f"<div class='bg-amber-50 border-l-4 border-amber-500 p-3 rounded-r-lg text-xs text-amber-900 leading-normal'><strong>Key Takeaway:</strong> {note}</div>"
    html += "</div>"
    return html

slides_part3 = [
    {
        "slide_num": 17,
        "title": "Challenge 1",
        "section": "Neighbourhood Life & Communication Evolution",
        "speech": "",
        "quizzes": [
            {
                "question": "What defines a neighbourhood most accurately?",
                "options": [
                    "A solitary building isolated in a forest",
                    "An interconnected local community of homes, markets, and shared public services",
                    "A single vehicle driving on a highway",
                    "An empty plot of land with no residents"
                ],
                "correct": 1,
                "hint": "Think about where families live, shop, and share facilities together.",
                "explanation": "A neighbourhood is an interconnected community where families share public roads, clinics, schools, and markets.",
                "sol": make_sol_html([
                    "Neighbourhoods consist of residential dwellings alongside essential service facilities.",
                    "Residents share common infrastructure including water supply, paved roads, and streetlights.",
                    "Community members interact daily, supporting local trade and mutual welfare."
                ], "A neighbourhood is a living network of shared facilities and mutual social support.")
            },
            {
                "question": "Which ancient method enabled early communities to transmit urgent warnings across hills before electrical wires existed?",
                "options": [
                    "Broadband optical fiber cables",
                    "Rhythmic acoustic drumbeats and visible smoke plumes",
                    "Digital video conferencing",
                    "Automated text messaging"
                ],
                "correct": 1,
                "explanation": "Before electricity, communities used sound from drums and visual smoke signals across high ground to warn of danger or announce news.",
                "sol": make_sol_html([
                    "Sound vibrations from large hollow drums travel across deep valleys.",
                    "Smoke plumes rising against the open sky provide long-range visual signals.",
                    "These traditional methods formed the earliest telecommunication systems."
                ], "Early acoustic and visual signals bridged geographical barriers before technology.")
            },
            {
                "question": "Why were homing pigeons chosen as reliable message carriers in historical times?",
                "options": [
                    "They can read handwritten alphabet letters",
                    "They possess an extraordinary natural instinct to navigate back to their home roosts over great distances",
                    "They fly faster than commercial aeroplanes",
                    "They can carry heavy wooden crates"
                ],
                "correct": 1,
                "explanation": "Homing pigeons have an innate magneto-reception and navigational ability that directs them back to their home lofts, carrying lightweight messages.",
                "sol": make_sol_html([
                    "Homing pigeons navigate using Earth's magnetic fields and solar position.",
                    "Lightweight parchment scrolls were tied securely to their legs.",
                    "Upon release, pigeons flew directly back to their home base with the attached dispatch."
                ], "Trained homing pigeons provided fast airborne message relays in ancient and medieval times.")
            },
            {
                "question": "What code of short and long electrical pulses was transmitted over telegram wires?",
                "options": [
                    "Barcode lines",
                    "Morse code (dots and dashes)",
                    "Binary computer code (zeros and ones)",
                    "Musical guitar tabs"
                ],
                "correct": 1,
                "explanation": "Telegrams used Morse code, consisting of dots (short pulses) and dashes (longer pulses), to represent letters of the alphabet.",
                "sol": make_sol_html([
                    "Invented by Samuel Morse, this system converted text into electrical pulses.",
                    "A receiving telegraph sounder clicked out corresponding dots and dashes.",
                    "Skilled telegraph operators translated the clicks back into written language."
                ], "Morse code revolutionized rapid intercity and transcontinental communication.")
            },
            {
                "question": "What is the primary function of the six-digit Postal Index Number (PIN code) in India?",
                "options": [
                    "It indicates the price of the postage stamp",
                    "It identifies the exact delivery post office and geographic zone to route mail efficiently",
                    "It represents the sender's mobile phone number",
                    "It shows the weight of the parcel"
                ],
                "correct": 1,
                "explanation": "A PIN code pinpoints the specific regional zone, sub-district, and sorting post office, preventing delivery delays.",
                "sol": make_sol_html([
                    "The first digit indicates the broad geographical region across India.",
                    "The second and third digits identify the sub-region and sorting district.",
                    "The final three digits designate the specific local post office responsible for doorstep delivery."
                ], "PIN codes streamline sorting and eliminate errors in mail delivery.")
            },
            {
                "question": "What happens to letters after they are cleared from a red street postbox?",
                "options": [
                    "They are discarded immediately into paper recycling bins",
                    "They are transported to a central mail sorting hub to be date-stamped and organized by destination zones",
                    "They are displayed in an art gallery",
                    "They are kept permanently inside the postbox"
                ],
                "correct": 1,
                "explanation": "Cleared letters are taken to a central sorting facility where they are postmarked with date stamps and sorted by destination.",
                "sol": make_sol_html([
                    "A postal carrier unlocks the postbox and empties letters into a mail bag.",
                    "At the sorting hub, postal workers cancel stamps with date and location postmarks.",
                    "Letters are organized into regional bundles for dispatch via road, rail, or air transit."
                ], "Central sorting hubs form the operational heart of national postal delivery networks.")
            },
            {
                "question": "Which modern device combines telephony, internet browsing, camera functions, and instant messaging into a single handheld tool?",
                "options": [
                    "A rotary dial landline telephone",
                    "A smartphone",
                    "A mechanical typewriter",
                    "A printed paperback atlas"
                ],
                "correct": 1,
                "explanation": "Smartphones integrate digital telephone calls, internet browsing, messaging applications, and cameras into one portable device.",
                "sol": make_sol_html([
                    "Smartphones connect to cellular towers and Wi-Fi networks.",
                    "They process voice, text, video, and digital photography simultaneously.",
                    "This represents the convergence of multiple communication technologies."
                ], "Smartphones have revolutionized communication by uniting multiple media in one device.")
            },
            {
                "question": "Why is conducting interviews with community elders valuable when studying communication history?",
                "options": [
                    "Elders share firsthand historical experiences of waiting for handwritten letters and using telegrams",
                    "Elders only know how to play computer games",
                    "Elders sell new mobile telephones",
                    "Elders manufacture television screens"
                ],
                "correct": 0,
                "explanation": "Interviews with elders provide living historical testimony about how communication felt before mobile phones and internet arrived.",
                "sol": make_sol_html([
                    "Elders recall the anticipation of receiving inland letters and aerogrammes.",
                    "They describe the urgency and brevity of sending telegrams for family milestones.",
                    "Firsthand oral history enriches textbook learning with emotional and cultural depth."
                ], "Elder oral histories bridge generational knowledge and preserve cultural heritage.")
            },
            {
                "question": "Where should a student look to verify the postage fee when preparing an envelope for mailing?",
                "options": [
                    "On the sole of their shoes",
                    "On the adhesive postage stamp affixed to the top-right corner of the envelope",
                    "Inside a dictionary",
                    "On the back of a classroom notebook"
                ],
                "correct": 1,
                "explanation": "Postage stamps affixed to envelopes display denominations representing prepayment for postal handling and transit.",
                "sol": make_sol_html([
                    "Postage stamps serve as official receipts proving postal charges were paid.",
                    "They are conventionally affixed to the upper right-hand corner of the address side.",
                    "Different mail weights and destination distances require varying stamp denominations."
                ], "Affixing the correct postage stamp ensures letters are processed without penalty.")
            },
            {
                "question": "Which of the following is a key advantage of modern digital electronic mail (email) over traditional postal letters?",
                "options": [
                    "Email travels in canvas bags on trains",
                    "Email delivers text and digital attachments across the world in seconds",
                    "Email requires buying paper and glue stamps",
                    "Email can only be sent once a month"
                ],
                "correct": 1,
                "explanation": "Email transmits electronic text, documents, and images across global internet networks almost instantaneously.",
                "sol": make_sol_html([
                    "Digital packets travel through high-speed fiber-optic cables and wireless links.",
                    "Delivery takes seconds regardless of geographical borders or distance.",
                    "Users can include formatted documents, digital spreadsheets, and photos."
                ], "Instantaneous digital delivery has made email a cornerstone of global communication.")
            }
        ]
    },
    {
        "slide_num": 18,
        "title": "Challenge 2",
        "section": "Modern Transit & Greener Infrastructure",
        "speech": "",
        "quizzes": [
            {
                "question": "How do elevated flyovers improve road safety and commuting times in urban neighbourhoods?",
                "options": [
                    "They block all sunlight permanently",
                    "They allow express traffic to cross over congested road junctions without stopping at ground-level signals",
                    "They force every vehicle to stop every ten metres",
                    "They eliminate all pedestrian sidewalks"
                ],
                "correct": 1,
                "explanation": "Flyovers carry continuous traffic above busy ground intersections, reducing waiting times and eliminating bottlenecks.",
                "sol": make_sol_html([
                    "Ground-level intersections experience heavy traffic delays due to multiple merging lanes.",
                    "Elevated flyovers provide an unobstructed roadway overhead for through traffic.",
                    "Bypassing ground signals reduces idling, fuel waste, and rear-end collisions."
                ], "Flyovers optimize vehicle flow and reduce junction congestion in expanding cities.")
            },
            {
                "question": "Why are electric metro rail networks considered environmentally friendly transport solutions?",
                "options": [
                    "They run on coal fires inside passenger coaches",
                    "They transport hundreds of passengers using electric power, generating zero direct tailpipe emissions",
                    "They emit thick black smoke clouds",
                    "They only carry five passengers per day"
                ],
                "correct": 1,
                "explanation": "Electric trains operate on clean electricity from overhead cables, carrying high passenger capacities with no local tailpipe emissions.",
                "sol": make_sol_html([
                    "High passenger capacity takes thousands of private cars off city streets.",
                    "Electric motors produce zero roadside emissions, preserving clean breathing air.",
                    "Energy regeneration during braking further enhances operational efficiency."
                ], "Electric metro systems reduce traffic congestion and city air pollution simultaneously.")
            },
            {
                "question": "What is a negative ecological consequence of cutting mature shade trees to build wider roads?",
                "options": [
                    "Increased bird nesting habitats",
                    "Loss of wildlife habitat, increased ambient ground temperatures, and higher airborne dust levels",
                    "Purification of local well water",
                    "More cooling shade for pedestrians"
                ],
                "correct": 1,
                "explanation": "Tree removal destroys animal shelters, creates urban heat islands, and removes natural dust filters from the air.",
                "sol": make_sol_html([
                    "Mature tree canopies shelter birds, bats, and beneficial pollinating insects.",
                    "Foliage absorbs solar radiation, keeping ground temperatures cooler.",
                    "Leaves trap suspended particulate matter (PM2.5 and PM10), purifying breathable air."
                ], "Preserving mature roadside trees protects local biodiversity and human health.")
            },
            {
                "question": "What principle requires planting several young trees for every single mature tree removed for construction?",
                "options": [
                    "Commercial logging trade",
                    "Compensatory afforestation and environmental stewardship",
                    "Agricultural grain harvesting",
                    "Mineral mining extraction"
                ],
                "correct": 1,
                "explanation": "Compensatory plantation ensures new green canopy is planted to replace and eventually exceed the foliage lost during construction.",
                "sol": make_sol_html([
                    "Development must not cause permanent environmental degradation.",
                    "Planting multiple native saplings compensates for the years needed for saplings to mature.",
                    "This maintains ecological balance and restores community green cover over time."
                ], "Compensatory tree plantation balances infrastructure growth with environmental preservation.")
            },
            {
                "question": "Which native Indian trees are especially valued along neighbourhood avenues for their broad shade and air-filtering qualities?",
                "options": [
                    "Cactus and prickly thorns",
                    "Neem, peepal, and banyan trees",
                    "Plastic ornamental shrubs",
                    "Tiny indoor bonsai plants"
                ],
                "correct": 1,
                "explanation": "Native trees like neem, peepal, and banyan thrive in local climates, providing expansive shade, oxygen, and natural air purification.",
                "sol": make_sol_html([
                    "Neem trees release beneficial phytoncides and offer dense, cooling shade.",
                    "Peepal and banyan trees have large canopies that trap atmospheric dust and provide bird roosts.",
                    "Native species require less artificial watering once established."
                ], "Planting native trees supports indigenous birds and purifies urban neighbourhood air.")
            },
            {
                "question": "What is the key purpose of green median strips planted with flowering shrubs along wide roads?",
                "options": [
                    "To hide traffic signals from drivers",
                    "To absorb headlight glare at night and create ecological pathways for pollinating insects and birds",
                    "To store construction waste piles",
                    "To prevent rain from falling"
                ],
                "correct": 1,
                "explanation": "Shrubs in median strips block dazzling oncoming headlight glare and offer nectar-rich resting stops for butterflies and bees.",
                "sol": make_sol_html([
                    "Dense shrubbery prevents blinding glare from headlights of vehicles in opposing lanes.",
                    "Flowering plants provide food corridors for bees, butterflies, and small urban birds.",
                    "Roots stabilize central soil embankments against monsoon water erosion."
                ], "Green medians enhance nighttime road safety and provide urban ecological corridors.")
            },
            {
                "question": "How do roadside rainwater harvesting channels benefit neighbourhood water resources?",
                "options": [
                    "By discharging dirty chemical waste into rivers",
                    "By capturing clean surface storm runoff to filter into and recharge underground aquifers",
                    "By evaporating water into steam",
                    "By turning paved roads into swimming pools"
                ],
                "correct": 1,
                "explanation": "Harvesting channels intercept surface runoff and divert it into filtration pits to replenish groundwater reserves.",
                "sol": make_sol_html([
                    "Roads and sidewalks prevent rainwater from naturally soaking into soil.",
                    "Constructed channels direct runoff into percolation pits filled with gravel and sand.",
                    "Filtered water recharges local borewells and deep groundwater aquifers."
                ], "Rainwater harvesting alongside roads replenishes vital underground water tables.")
            },
            {
                "question": "Why are dedicated bicycle lanes and wide pedestrian walkways important in urban transit planning?",
                "options": [
                    "They encourage active, non-polluting travel while keeping pedestrians and cyclists safe from heavy motor traffic",
                    "They allow large trucks to drive on sidewalks",
                    "They increase exhaust smoke emissions",
                    "They remove street lighting completely"
                ],
                "correct": 0,
                "explanation": "Protected bike lanes and sidewalks separate vulnerable non-motorized commuters from fast motor vehicles, promoting health and safety.",
                "sol": make_sol_html([
                    "Walking and cycling generate zero carbon emissions and promote cardiovascular fitness.",
                    "Physical curbs protect cyclists and pedestrians from speeding automobiles.",
                    "Safe walking environments make neighbourhoods child-friendly and accessible for all."
                ], "Protected pedestrian and cycling paths promote green mobility and community safety.")
            },
            {
                "question": "What feature on modern pedestrian footpaths assists visually impaired citizens in navigating neighbourhood streets safely?",
                "options": [
                    "Smooth slippery marble tiles",
                    "Tactile paving tiles with raised directional ridges and warning bumps",
                    "Deep open uncovered ditches",
                    "Bright neon advertising signs"
                ],
                "correct": 1,
                "explanation": "Tactile paving tiles feature raised tactile patterns detectable through walking canes or shoes, indicating safe paths or upcoming hazards.",
                "sol": make_sol_html([
                    "Long raised ridges indicate a clear, obstacle-free straight walking path.",
                    "Domed blister bumps warn pedestrians of street corners, road edges, or pedestrian crossings.",
                    "Tactile paving ensures universal accessibility and dignity for visually impaired citizens."
                ], "Tactile paving ensures public neighbourhood walkways are accessible to all citizens.")
            },
            {
                "question": "How does choosing shared public buses instead of driving separate private cars help the neighbourhood?",
                "options": [
                    "It causes more traffic congestion and uses more fuel",
                    "It reduces the total number of vehicles on the road, decreasing traffic jams and exhaust emissions",
                    "It makes bus stops empty",
                    "It eliminates all public transport routes"
                ],
                "correct": 1,
                "explanation": "One full bus replaces up to forty private cars, freeing road space and drastically reducing tailpipe pollution.",
                "sol": make_sol_html([
                    "A single bus transports 50 or more passengers at once.",
                    "Fewer vehicles on the road translates into less idling and fewer traffic jams.",
                    "Lower aggregate fuel consumption leads to cleaner, healthier neighbourhood air."
                ], "Mass public transit reduces traffic congestion, carbon footprints, and street smog.")
            }
        ]
    },
    {
        "slide_num": 19,
        "title": "Challenge 3",
        "section": "Community Healthcare, Roles & Banking",
        "speech": "",
        "quizzes": [
            {
                "question": "What is the primary role of a physician or doctor in a community hospital?",
                "options": [
                    "To construct hospital brick walls",
                    "To examine sick patients, diagnose physical conditions, and prescribe medical treatment",
                    "To operate public transport buses",
                    "To sell commercial grocery items"
                ],
                "correct": 1,
                "explanation": "Doctors assess symptoms, conduct clinical examinations, formulate diagnoses, and prescribe curative treatments.",
                "sol": make_sol_html([
                    "Physicians use diagnostic tools like stethoscopes, thermometers, and blood pressure monitors.",
                    "They interpret clinical findings to understand the underlying cause of an illness.",
                    "They design comprehensive treatment plans including medications and lifestyle care."
                ], "Doctors provide skilled clinical diagnoses and evidence-based healing therapies.")
            },
            {
                "question": "Which medical instrument is used by doctors to listen to internal heartbeats and breathing sounds?",
                "options": [
                    "A telescope",
                    "A stethoscope",
                    "A periscope",
                    "A kaleidoscope"
                ],
                "correct": 1,
                "explanation": "A stethoscope is an acoustic medical device used to listen to the internal sounds of the heart, lungs, and intestines.",
                "sol": make_sol_html([
                    "The stethoscope disc or diaphragm is placed directly against the patient's chest or back.",
                    "Sound waves travel through sealed hollow acoustic tubes directly to the physician's earpieces.",
                    "Unusual heart murmurs or chest congestion sounds indicate specific health conditions."
                ], "Stethoscopes allow non-invasive acoustic examination of heart and lung function.")
            },
            {
                "question": "How do nurses contribute critically to patient recovery inside healthcare wards?",
                "options": [
                    "By delivering postal mail",
                    "By administering prescribed medicines, dressing wounds, monitoring vital signs, and ensuring patient comfort",
                    "By manufacturing surgical tables",
                    "By designing road flyovers"
                ],
                "correct": 1,
                "explanation": "Nurses provide continuous bedside care, monitor vital recovery signs, administer treatments, and offer empathetic comfort.",
                "sol": make_sol_html([
                    "Nurses check temperature, pulse, respiration rate, and blood pressure regularly.",
                    "They ensure medications and intravenous fluids are delivered at exact prescribed intervals.",
                    "Their continuous observation allows early detection of any patient health changes."
                ], "Nurses are the compassionate backbone of patient recovery in healthcare institutions.")
            },
            {
                "question": "What is the main task of a hospital laboratory technician?",
                "options": [
                    "To clean the hospital garden",
                    "To analyze blood, urine, and fluid specimens under microscopes to identify bacteria and health indicators",
                    "To drive the emergency ambulance",
                    "To cook meals in the patient cafeteria"
                ],
                "correct": 1,
                "explanation": "Lab technicians analyze clinical specimens scientifically to provide accurate diagnostic data for physicians.",
                "sol": make_sol_html([
                    "Technicians prepare blood smears and biological cultures on glass slides.",
                    "They operate optical microscopes, centrifuges, and biochemical analyzers.",
                    "Precise test results reveal specific pathogens, hemoglobin counts, and blood sugar levels."
                ], "Laboratory technicians provide vital diagnostic evidence that guides targeted medical treatment.")
            },
            {
                "question": "Why is a qualified pharmacist necessary when dispensing prescribed medicines?",
                "options": [
                    "To ensure patients receive the correct medicine, precise strength, and clear instructions on dosage timing",
                    "To write creative storybooks",
                    "To repair dental equipment",
                    "To operate bank ATM kiosks"
                ],
                "correct": 0,
                "explanation": "Pharmacists verify prescriptions, prevent adverse drug interactions, and explain how and when medicines must be taken.",
                "sol": make_sol_html([
                    "Pharmacists check that medicine dosages align with patient age and medical needs.",
                    "They warn patients about whether medicines should be taken before or after meals.",
                    "Proper dispensing prevents dangerous overdoses and ensures therapeutic effectiveness."
                ], "Pharmacists ensure medicines are dispensed safely, accurately, and responsibly.")
            },
            {
                "question": "How do free community eye check-up camps directly benefit neighbourhood elders and schoolchildren?",
                "options": [
                    "By distributing expensive smartphones",
                    "By detecting cataracts, checking vision acuity, and providing corrective spectacles for clear vision",
                    "By building concrete park walls",
                    "By repairing broken bicycle chains"
                ],
                "correct": 1,
                "explanation": "Eye camps diagnose visual impairments early, distribute corrective glasses, and refer surgical cataract cases to hospitals.",
                "sol": make_sol_html([
                    "Specialists use Snellen letter charts to test distance and near vision acuity.",
                    "Corrective lenses restore clear sight for schoolchildren studying reading and writing.",
                    "Surgical cataract identification helps elderly citizens regain self-reliant mobility."
                ], "Community vision camps transform quality of life through accessible eye care.")
            },
            {
                "question": "What is the primary benefit of depositing money in a bank savings account instead of keeping cash at home?",
                "options": [
                    "The money disappears completely",
                    "The bank protects funds in secure vaults, insures deposits, and adds interest payments over time",
                    "The money is locked permanently and can never be withdrawn",
                    "The bank gives away the money to strangers"
                ],
                "correct": 1,
                "explanation": "Banks offer secure storage against theft or loss, provide digital tracking, and pay interest that increases savings.",
                "sol": make_sol_html([
                    "Keeping large cash sums at home carries risks of burglary, fire, or accidental damage.",
                    "Bank deposits are protected by strict institutional security and government insurance.",
                    "Interest credited periodically rewards savers and helps wealth grow over time."
                ], "Bank accounts provide safe security, legal protection, and interest growth for savings.")
            },
            {
                "question": "What does ATM stand for in everyday neighbourhood banking services?",
                "options": [
                    "Automated Teller Machine",
                    "Any Time Medicine",
                    "Automatic Train Motor",
                    "All Trade Market"
                ],
                "correct": 0,
                "explanation": "ATM stands for Automated Teller Machine, an electronic banking kiosk that performs cash dispensing and balance enquiries.",
                "sol": make_sol_html([
                    "The machine acts as an automated teller or cashier.",
                    "It communicates through secure computer networks with bank servers.",
                    "Customers can withdraw cash, deposit funds, or verify balances around the clock."
                ], "ATMs offer 24-hour access to basic banking services without visiting counter queues.")
            },
            {
                "question": "Why must an ATM cardholder never share their 4-digit PIN with anyone else?",
                "options": [
                    "Because numbers change into letters",
                    "Because the PIN is a confidential authentication code that protects the account from unauthorized withdrawals",
                    "Because the ATM machine will shut down",
                    "Because it is an illegal secret"
                ],
                "correct": 1,
                "explanation": "A Personal Identification Number (PIN) proves identity; keeping it confidential prevents financial theft and fraud.",
                "sol": make_sol_html([
                    "The PIN acts as a digital key unlocking the cardholder's funds.",
                    "If someone learns the PIN and obtains the card, they could drain savings.",
                    "Banks advise covering the keypad when entering numbers to protect personal privacy."
                ], "Confidentiality of your banking PIN is the first line of defence against financial theft.")
            },
            {
                "question": "How do banks support local neighbourhood business owners, farmers, and families?",
                "options": [
                    "By closing all doors to the public",
                    "By providing loans and credit to help buy equipment, build houses, and expand businesses",
                    "By selling grocery vegetables",
                    "By manufacturing motor vehicle tires"
                ],
                "correct": 1,
                "explanation": "Banks provide credit loans that allow entrepreneurs to purchase tools, farmers to buy seeds, and families to construct homes.",
                "sol": make_sol_html([
                    "Savings deposited by community members provide capital for lending.",
                    "Borrowers repay loans gradually over time with agreed interest charges.",
                    "This financial circulation fuels local employment, construction, and economic growth."
                ], "Bank loans stimulate community economic progress and help families achieve life goals.")
            }
        ]
    },
    {
        "slide_num": 20,
        "title": "Challenge 4",
        "section": "Money, Maps, Directions & Frontline Heroes",
        "speech": "",
        "quizzes": [
            {
                "question": "What major flaw made the ancient barter system inconvenient for daily trade?",
                "options": [
                    "It required both trading parties to desire exactly what the other offered at the same time (double coincidence of wants)",
                    "Items were too light to carry",
                    "Nobody owned any farm animals",
                    "It used too many paper banknotes"
                ],
                "correct": 0,
                "explanation": "Barter failed when mutual wants did not align or when perishable commodities like milk or fish spoiled before trade occurred.",
                "sol": make_sol_html([
                    "A person with grain had to find someone with cloth who specifically needed grain.",
                    "Perishable goods could not be stored indefinitely to trade in the future.",
                    "Standard money eliminated these problems by acting as a universal medium of exchange."
                ], "The double coincidence of wants and perishability made barter inefficient.")
            },
            {
                "question": "What does a 'debit' entry in a bank passbook indicate to the account owner?",
                "options": [
                    "Money that was added or deposited into the account",
                    "Money that was withdrawn or spent from the account balance",
                    "The total number of bank branches in the city",
                    "The date when the bank was founded"
                ],
                "correct": 1,
                "explanation": "A debit entry shows funds withdrawn, transferred out, or spent, reducing the account's total available balance.",
                "sol": make_sol_html([
                    "Debit entries are logged in the withdrawal column of the passbook.",
                    "Each debit reduces the accumulated running balance.",
                    "Credit entries, in contrast, indicate deposits that increase total savings."
                ], "Debit signifies withdrawals; credit signifies deposits into an account.")
            },
            {
                "question": "When framing a sensible family monthly budget, which expense should be given the highest priority?",
                "options": [
                    "Buying luxury collectible toys",
                    "Essential necessities like nutritious food, clean drinking water, school fees, and healthcare",
                    "Attending expensive weekend cinema parties",
                    "Purchasing video game consoles"
                ],
                "correct": 1,
                "explanation": "Budgets must prioritize survival and growth essentials (food, water, medicine, schooling) before spending on luxury wants.",
                "sol": make_sol_html([
                    "Needs are essential requirements without which health, learning, and life suffer.",
                    "Wants are non-essential luxuries that can be postponed or skipped.",
                    "Prudent budgeting funds all needs first, sets aside savings, and limits discretionary wants."
                ], "Prioritizing essential needs over optional wants creates stable financial security.")
            },
            {
                "question": "If you stand facing the morning rising sun, which cardinal direction is situated directly to your left side?",
                "options": [
                    "South",
                    "West",
                    "North",
                    "East"
                ],
                "correct": 2,
                "explanation": "Facing East (sunrise), your back points West, your right arm points South, and your left arm points North.",
                "sol": make_sol_html([
                    "The sun rises in the East, establishing the baseline reference orientation.",
                    "Turn your face toward the sunrise: East is directly ahead.",
                    "Extend both arms horizontally: the left arm points North, while the right arm points South."
                ], "Facing East aligns North to your left, South to your right, and West behind.")
            },
            {
                "question": "Which cardinal direction is universally positioned at the top of a standard printed map?",
                "options": [
                    "South",
                    "East",
                    "West",
                    "North"
                ],
                "correct": 3,
                "explanation": "Cartographers universally align maps with North pointing toward the top margin of the sheet.",
                "sol": make_sol_html([
                    "Standard orientation ensures maps from different regions can be easily aligned and compared.",
                    "North is top, South is bottom, East is to the right, and West is to the left.",
                    "A compass rose on the map margin confirms this orientation."
                ], "Standard geographical maps place North at the top margin for consistency.")
            },
            {
                "question": "What is the function of a map legend or symbol key?",
                "options": [
                    "It tells humorous bedtime stories",
                    "It explains what each symbol, color shading, and marker icon represents on the map",
                    "It keeps the paper flat in strong winds",
                    "It lists the names of every person in the town"
                ],
                "correct": 1,
                "explanation": "A map legend decodes symbols—such as blue lines for rivers, red crosses for clinics, and green patches for parks.",
                "sol": make_sol_html([
                    "Maps use compact symbols to represent complex real-world landmarks.",
                    "The legend key provides an illustrated directory explaining each icon.",
                    "Checking the legend ensures readers interpret features and boundaries accurately."
                ], "Map legends decode symbols, colors, and line styles into clear spatial information.")
            },
            {
                "question": "How does selecting a prominent central landmark assist in drawing or reading a neighbourhood map?",
                "options": [
                    "It serves as a familiar reference anchor from which other buildings and directions are measured",
                    "It makes the map completely invisible",
                    "It removes all roads from the drawing",
                    "It changes North to South"
                ],
                "correct": 0,
                "explanation": "A central landmark (such as a school, clock tower, or community park) acts as a base anchor to orient all other surrounding places.",
                "sol": make_sol_html([
                    "Everyone in the neighbourhood recognizes prominent central landmarks.",
                    "Using the landmark as the starting origin simplifies spatial descriptions.",
                    "Travelers can easily orient themselves by moving forward, backward, left, or right relative to it."
                ], "Central landmarks provide intuitive reference anchors for spatial navigation.")
            },
            {
                "question": "Why are sanitation workers regarded as frontline community heroes during epidemics and daily life?",
                "options": [
                    "They pilot commercial helicopters",
                    "They clean public streets, remove municipal refuse, and sanitize shared spaces to prevent dangerous disease outbreaks",
                    "They write computer software programs",
                    "They perform stage plays in theatres"
                ],
                "correct": 1,
                "explanation": "Sanitation workers remove accumulating waste, sweep public footpaths, and disinfect drains, stopping epidemic disease vectors.",
                "sol": make_sol_html([
                    "Uncollected refuse attracts disease vectors such as flies, rodents, and mosquitoes.",
                    "Sanitation workers risk health exposure to maintain community hygiene and clean public spaces.",
                    "Their tireless labour is essential for safeguarding public health and preventing epidemics."
                ], "Sanitation workers preserve public health and civic hygiene through selfless daily service.")
            },
            {
                "question": "Which emergency vehicle is equipped with water hoses, high-pressure pumps, hydraulic ladders, and rescue tools?",
                "options": [
                    "A postal delivery van",
                    "A fire engine",
                    "A mobile ice cream cart",
                    "A public library bookmobile"
                ],
                "correct": 1,
                "explanation": "Fire engines transport water hoses, high-pressure pumps, long ladders, and rescue tools to extinguish fires and rescue trapped citizens.",
                "sol": make_sol_html([
                    "Fire engines carry large onboard water tanks and foam retardants.",
                    "Hydraulic ladders extend high up to reach upper floors of multistory buildings.",
                    "Specialized cutting and extraction tools assist in vehicle accident rescues."
                ], "Fire engines carry specialized hydraulic equipment for fire suppression and rescue.")
            },
            {
                "question": "How can young citizens demonstrate active civic responsibility and gratitude toward neighbourhood helpers?",
                "options": [
                    "By throwing garbage on footpaths and ignoring traffic signals",
                    "By sorting household waste, using public amenities with care, and treating all community workers with respect",
                    "By blocking fire hydrant valves with rocks",
                    "By writing graffiti on public library books"
                ],
                "correct": 1,
                "explanation": "Respecting community workers, keeping public spaces tidy, and following civic rules builds a cooperative, thriving neighbourhood.",
                "sol": make_sol_html([
                    "Civic responsibility begins with personal habits like segregating waste and not littering.",
                    "Treating workers with dignity and gratitude honors their essential contributions.",
                    "Caring for shared infrastructure ensures community resources serve everyone for generations."
                ], "Respecting community workers and protecting public spaces strengthens community harmony.")
            }
        ]
    }
]

if __name__ == "__main__":
    total_q = sum(len(s["quizzes"]) for s in slides_part3)
    print(f"Total quiz questions across Slides 17-20: {total_q}")
    assert total_q == 40, f"Expected 40 quiz questions, got {total_q}"
    for s in slides_part3:
        print(f"Slide {s['slide_num']}: '{s['title']}' -> {len(s['quizzes'])} questions")
        assert len(s["quizzes"]) == 10
        for i, q in enumerate(s["quizzes"]):
            assert len(q["options"]) == 4, f"Slide {s['slide_num']} Q{i+1} does not have 4 options"
            assert 0 <= q["correct"] <= 3, f"Slide {s['slide_num']} Q{i+1} correct index out of range"
            assert "sol" in q, f"Slide {s['slide_num']} Q{i+1} missing sol"
    print("All slides 17-20 validated successfully!")

