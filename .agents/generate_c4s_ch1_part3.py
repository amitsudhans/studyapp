# -*- coding: utf-8 -*-
"""
Class 4 Science Chapter 1: Living Together
Part 3: Slides 17 to 20 Data Generator (40 Quiz Questions)
Short headings: Challenge 1, Challenge 2, Challenge 3, Challenge 4.
Zero human names (replaced with generic roles).
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
        "id": 17,
        "title": "Challenge 1",
        "section": "Communities, Public Places & Van Mahotsav",
        "speech": "",
        "quizzes": [
            {
                "q": "What primarily distinguishes a vibrant community from a mere cluster of houses?",
                "options": ["The color of the house walls", "Mutual cooperation, shared public spaces, and social interdependence", "Having only tall apartment towers", "Having high boundary fences between neighbors"],
                "ans": 1,
                "hint": "Think about how people interact and help one another in daily life.",
                "exp": "A community is defined by mutual support, shared facilities, and collaborative living.",
                "sol": make_sol_html([
                    "Houses provide individual shelter, but a community represents people living together.",
                    "Community members share common resources like roads, health centers, and parks.",
                    "Mutual trust and cooperative action are the core pillars of community life."
                ], "Communities thrive through shared cooperation and interdependence.")
            },
            {
                "q": "Why has the village banyan tree historically served as a central community hub across rural India?",
                "options": ["It produces sweet edible fruits all year", "Its wide canopy and aerial roots offer sheltering shade for public gatherings and elder councils", "It is made of stone", "It requires no water"],
                "ans": 1,
                "exp": "The expansive banyan tree provides natural shade where villagers gather for discussions and decision-making.",
                "sol": make_sol_html([
                    "Banyan trees develop wide crowns supported by pillar-like aerial prop roots.",
                    "This creates a cool, covered outdoor pavilion suitable for large community meetings.",
                    "Historically, village councils (panchayats) and elders congregate under banyans to resolve issues."
                ], "The banyan tree symbolizes community wisdom, shelter, and unity.")
            },
            {
                "q": "Which public institution is primarily responsible for preventive vaccinations and treating sudden illnesses in a village?",
                "options": ["The post office", "The primary health center (PHC)", "The bus depot", "The weekly grocery bazaar"],
                "ans": 1,
                "hint": "Look for the healthcare facility staffed by medical professionals.",
                "exp": "Primary health centers provide vital medical treatments, immunizations, and healthcare guidance.",
                "sol": make_sol_html([
                    "Healthcare is an essential public service in every locality.",
                    "Primary health centers provide emergency first aid, maternity care, and immunizations.",
                    "They protect community health by preventing contagious disease outbreaks."
                ], "Healthcare centers are crucial for community physical well-being.")
            },
            {
                "q": "If a town's sheltered bus stop were removed, what immediate difficulty would daily commuters face?",
                "options": ["Buses would stop running forever", "Passengers would stand exposed to scorching heat, wind, and heavy monsoon rains", "Ticket prices would instantly double", "The roads would turn to mud"],
                "ans": 1,
                "hint": "Consider the primary physical protective function of a bus shelter.",
                "exp": "Bus shelters shield waiting passengers from adverse weather conditions.",
                "sol": make_sol_html([
                    "Public infrastructure is engineered to serve human comfort and safety.",
                    "Shelters protect commuters while waiting for scheduled public transit.",
                    "Without them, elderly citizens, workers, and students face severe weather exposure."
                ], "Public amenities provide comfort and dignity in daily civic life.")
            },
            {
                "q": "During which dates is the national tree planting festival, Van Mahotsav, celebrated throughout India?",
                "options": ["January 1 to January 7", "July 1 to July 7", "August 15 to August 22", "October 2 to October 9"],
                "ans": 1,
                "hint": "It coincides with the arrival of early monsoon rainfalls across India.",
                "exp": "Van Mahotsav is observed annually from July 1 to July 7 to utilize monsoon soil moisture.",
                "sol": make_sol_html([
                    "Van Mahotsav was established in 1950 by environmental visionary K. M. Munshi.",
                    "The first week of July coincides with active monsoon rains in most parts of India.",
                    "Plentiful rainwater helps young tree saplings establish root systems without artificial irrigation."
                ], "Timing tree plantations with natural seasonal rains ensures high sapling survival rates.")
            },
            {
                "q": "Why is the neem tree especially prized in community tree plantation drives?",
                "options": ["Its wood dissolves in water", "It releases abundant oxygen, purifies air, and possesses natural antiseptic properties", "It grows only inside glass greenhouses", "It flowers only in winter snow"],
                "ans": 1,
                "hint": "Think about the medicinal and ecological benefits of neem leaves and shade.",
                "exp": "Neem is a hardy native tree renowned for air purification, cooling shade, and antibacterial properties.",
                "sol": make_sol_html([
                    "Neem (Azadirachta indica) is indigenous to the Indian subcontinent.",
                    "It thrives in semi-arid soils and tolerates intense summer temperatures.",
                    "Its leaves and bark contain natural pest-repellent and medicinal compounds."
                ], "Native trees like neem offer unmatched ecological and health benefits.")
            },
            {
                "q": "How does keeping public parks clean directly benefit the physical health of neighborhood children?",
                "options": ["It eliminates open breeding grounds for disease-carrying flies and mosquitoes", "It makes grass grow purple", "It prevents children from running", "It increases homework hours"],
                "ans": 0,
                "hint": "Think about the link between stagnant waste and insect-borne diseases.",
                "exp": "Clean, unlittered parks prevent stagnant water puddles where mosquitoes breed, reducing dengue and malaria.",
                "sol": make_sol_html([
                    "Discarded plastics and food containers trap rainwater, creating mosquito breeding pools.",
                    "Rotting food waste attracts flies, stray rodents, and harmful pathogens.",
                    "Regular sanitation keeps open recreational spaces safe and disease-free."
                ], "Public hygiene directly suppresses insect vectors and infectious illnesses.")
            },
            {
                "q": "What civic action should a responsible student take upon noticing a leaking public drinking water tap in a park?",
                "options": ["Ignore it and walk away", "Close the tap firmly and inform the park caretaker or local authority if it continues leaking", "Break the valve further", "Wash shoes under the leak"],
                "ans": 1,
                "hint": "Consider water conservation and civic responsibility.",
                "exp": "Tightly closing taps and alerting caretakers saves precious treated drinking water.",
                "sol": make_sol_html([
                    "Treated municipal drinking water requires significant energy and resources to purify.",
                    "A single continuously dripping tap can waste thousands of liters of clean water monthly.",
                    "Reporting faults to maintenance staff reflects active civic stewardship."
                ], "Conserving shared water resources is every citizen's fundamental responsibility.")
            },
            {
                "q": "Why do tree roots play a vital role in preventing topsoil erosion during monsoon cloudbursts?",
                "options": ["Roots absorb all sunlight underground", "Dense subterranean root networks bind soil particles tightly together", "Roots turn soil into stone", "Roots push soil into rivers"],
                "ans": 1,
                "hint": "Think about how plant root hairs hold earth in place against rushing water.",
                "exp": "Root systems physically anchor loose topsoil, preventing rain runoff from washing away fertile earth.",
                "sol": make_sol_html([
                    "Heavy rainfall generates fast-flowing surface runoff that dislodges loose dirt.",
                    "Tree roots form an interlocking subterranean fibrous web that holds soil particles intact.",
                    "Leaves also intercept falling raindrops, softening their impact on the forest floor."
                ], "Trees prevent soil erosion and landslides on slopes and riverbanks.")
            },
            {
                "q": "What is the primary role of a local police post in a neighborhood?",
                "options": ["To sell fruits and vegetables", "To maintain public safety, regulate traffic, and protect residents from harm", "To conduct science experiments", "To build residential houses"],
                "ans": 1,
                "hint": "Think about law enforcement and community safety.",
                "exp": "Police personnel safeguard citizens, enforce laws, and assist during emergencies.",
                "sol": make_sol_html([
                    "Peaceful social life requires the fair enforcement of civic laws.",
                    "Police officers deter crime, assist lost children, and manage congested intersections.",
                    "Their presence ensures safety and security for all community members."
                ], "Public safety services provide the peaceful order necessary for community life.")
            }
        ]
    },
    {
        "id": 18,
        "title": "Challenge 2",
        "section": "Posters, Voluntary Labor, Tools & Plantation",
        "speech": "",
        "quizzes": [
            {
                "q": "What makes a public awareness poster for Van Mahotsav most effective?",
                "options": ["A very long paragraphs in tiny faint print", "A memorable slogan, eye-catching green visuals, and clear event details", "No dates or locations mentioned", "Blank white paper with no drawings"],
                "ans": 1,
                "hint": "Think about what grabs attention quickly on a busy street notice board.",
                "exp": "Strong slogans, vibrant pictures, and clear logistics motivate community participation.",
                "sol": make_sol_html([
                    "Posters must convey their message in just a few seconds to pedestrians.",
                    "Bold slogans like 'Plant Today, Breathe Tomorrow' create emotional resonance.",
                    "Clear details (date, time, venue) enable interested neighbors to attend."
                ], "Effective visual communication inspires public civic action.")
            },
            {
                "q": "What is the traditional Indian concept of voluntary collective labor for community welfare called?",
                "options": ["Shramdaan", "Bazaar", "Melawa", "Khel"],
                "ans": 0,
                "hint": "The term combines the words for labor/effort ('shram') and gift/donation ('daan').",
                "exp": "'Shramdaan' refers to voluntary donation of physical labor for public community improvement.",
                "sol": make_sol_html([
                    "'Shram' means physical labor, and 'Daan' means selfless donation or gift.",
                    "In Indian culture, shramdaan represents community members uniting to repair roads, clean ponds, or plant trees.",
                    "It fosters self-reliance and civic pride without relying solely on government funding."
                ], "Shramdaan embodies community self-help and cooperative volunteerism.")
            },
            {
                "q": "Which tool does a skilled carpenter use to smooth timber and cut precise joints for wooden park benches?",
                "options": ["A steel trowel and mortar tray", "A handsaw, measuring tape, and wood chisel", "A pipe wrench and Teflon tape", "An electrical voltage tester"],
                "ans": 1,
                "exp": "Carpenters use saws, chisels, mallets, and measuring tapes to shape and join wooden components.",
                "sol": make_sol_html([
                    "Different trades require specialized, task-specific instruments.",
                    "Carpentry requires woodworking tools: saws cut timber, chisels carve mortises, and tapes measure dimensions.",
                    "Trowels belong to masons, while pipe wrenches belong to plumbers."
                ], "Specialized tools enable craftspeople to build durable public infrastructure.")
            },
            {
                "q": "What is the primary function of a spirit level and plumb line in brick masonry?",
                "options": ["To color the bricks", "To ensure walls are perfectly horizontal and vertically upright", "To cut bricks in half", "To mix sand with water"],
                "ans": 1,
                "hint": "Think about what keeps a brick wall from leaning or toppling over.",
                "exp": "Plumb lines check vertical alignment (perpendicularity), while spirit levels ensure horizontal flatness.",
                "sol": make_sol_html([
                    "Gravity exerts downward pressure on structures.",
                    "A plumb line uses a hanging weight to establish a true vertical line.",
                    "A spirit level uses an air bubble in liquid to verify horizontal flatness.",
                    "Both tools guarantee that walls are structurally sound and plumb."
                ], "Precision measuring tools prevent architectural collapse and structural leaning.")
            },
            {
                "q": "Why is it essential to dig planting pits at least 50 to 60 centimeters deep before planting tree saplings?",
                "options": ["To hide rocks underground", "To loosen compacted subsoil so young roots can spread easily and anchor firmly", "To trap wild animals", "To make the tree shorter"],
                "ans": 1,
                "hint": "Think about how tender sapling roots penetrate hard-packed earth.",
                "exp": "Deep, loosened soil allows young root tips to penetrate downward and absorb moisture readily.",
                "sol": make_sol_html([
                    "Park ground is often compacted by foot traffic and heavy equipment.",
                    "Digging a deep pit breaks up hard subsoil barriers.",
                    "Loosened soil allows tender taproots to grow deeply, anchoring the tree against windstorms."
                ], "Proper pit preparation gives saplings the best foundation for rapid root establishment.")
            },
            {
                "q": "Why should the plastic nursery bag be carefully peeled off before placing a sapling into the soil pit?",
                "options": ["Plastic nursery bags dissolve instantly in water", "Non-biodegradable plastic restricts root expansion and traps stagnant water, suffocating roots", "Plastic bag makes the tree grow too fast", "To keep the bag inside the tree trunk"],
                "ans": 1,
                "hint": "Can roots grow through a sealed sheet of plastic?",
                "exp": "Plastic bags do not decompose and will strangle roots if left around the root ball.",
                "sol": make_sol_html([
                    "Polythene nursery bags are artificial polymers that do not degrade in soil.",
                    "Leaving the bag on coils the roots in a circle, eventually girdling and suffocating the sapling.",
                    "Removing the bag allows roots to establish direct contact with native surrounding soil."
                ], "Always unwrap root balls from plastic containers before planting in the earth.")
            },
            {
                "q": "What is the primary purpose of watering a newly planted sapling immediately after backfilling the soil?",
                "options": ["To wash the leaves", "To settle the soil, remove dry air pockets around roots, and provide immediate hydration", "To make mud pies", "To attract insects"],
                "ans": 1,
                "hint": "Air pockets around roots dry out sensitive root hairs.",
                "exp": "Immediate watering eliminates air pockets and establishes capillary water movement to roots.",
                "sol": make_sol_html([
                    "Backfilled soil contains loose voids and dry air pockets.",
                    "Thorough soaking causes fine soil particles to settle closely against root hairs.",
                    "This prevents transplanted roots from drying out and experiencing transplant shock."
                ], "Immediate watering bridges root-to-soil contact, ensuring transplant survival.")
            },
            {
                "q": "Why are bamboo tree guards installed around saplings in public village parks?",
                "options": ["To decorate the park for celebrations", "To protect tender young stems and leaves from browsing goats and cattle", "To stop rain from touching trees", "To keep children from playing"],
                "ans": 1,
                "hint": "Consider what roaming herbivores like goats do to fresh green leaves.",
                "exp": "Guards prevent wandering livestock from chewing and destroying vulnerable saplings.",
                "sol": make_sol_html([
                    "Young trees possess tender, nutrient-rich leaves that attract herbivores.",
                    "A single goat or cow can defoliate and kill an unprotected sapling within minutes.",
                    "Bamboo lattice guards provide physical protection while allowing sunlight and airflow."
                ], "Protective guards ensure planted saplings survive the vulnerable early growth years.")
            },
            {
                "q": "What does the term 'dignity of labor' mean in community ethics?",
                "options": ["Only wealthy professionals deserve respect", "All forms of honest work—manual or intellectual—are equally honorable and worthy of respect", "People should avoid physical work", "Machines should do all human jobs"],
                "ans": 1,
                "hint": "Think about how every worker contributes to making society functional.",
                "exp": "Dignity of labor teaches that every honest occupation deserves equal respect and gratitude.",
                "sol": make_sol_html([
                    "Society cannot function without plumbers, masons, sanitation workers, or farmers.",
                    "Dignity of labor rejects discrimination based on whether work is physical or intellectual.",
                    "Every ethical job that contributes to human welfare deserves honor and fair compensation."
                ], "True education teaches equal respect for all honest labor and crafts.")
            },
            {
                "q": "Why is division of labor into specialized task groups so successful during large plantation drives?",
                "options": ["It makes everyone do the same thing at once", "It matches skills to tasks and keeps operations moving without confusion or delay", "It allows most people to sleep", "It requires fewer trees"],
                "ans": 1,
                "hint": "Think of how an assembly line or sports team coordinates different roles.",
                "exp": "Assigning clearing, digging, planting, and watering to distinct groups ensures rapid, orderly progress.",
                "sol": make_sol_html([
                    "If everyone attempts to dig, no one brings saplings or water.",
                    "Dividing into specialized teams (diggers, planters, waterers) creates a continuous workflow.",
                    "This collective synergy multiplies efficiency and prevents fatigue."
                ], "Coordinated organization turns large civic goals into swift, successful achievements.")
            }
        ]
    },
    {
        "id": 19,
        "title": "Challenge 3",
        "section": "River Bridges, Social Insects, Feasts & Compost",
        "speech": "",
        "quizzes": [
            {
                "q": "In Kanker, Chhattisgarh, which swollen river submerged the culvert and prompted villagers to build a bamboo bridge in 2024?",
                "options": ["The Ganga river", "The Chinar river", "The Yamuna river", "The Narmada river"],
                "ans": 1,
                "hint": "Review the real-world case study from central India.",
                "exp": "The Chinar river overflowed its banks, cutting off several village hamlets in Kanker district.",
                "sol": make_sol_html([
                    "In 2024, monsoon flooding along the Chinar river submerged the local transport culvert.",
                    "Over a thousand villagers were isolated without access to emergency clinics or schools.",
                    "The community resolved the crisis by constructing a temporary sixty-foot bamboo bridge."
                ], "The Chinar river case study exemplifies rural Indian resilience and self-reliance.")
            },
            {
                "q": "What primary local materials did the Kanker villagers use to construct their emergency pedestrian bridge in 48 hours?",
                "options": ["Imported steel girders and concrete pre-casts", "Mature bamboo poles, river boulders, and wire ropes", "Plastic pipes and cardboard", "Wooden railroad ties"],
                "ans": 1,
                "hint": "Think about sustainable materials readily available in Indian rural landscapes.",
                "exp": "Farmers donated thick bamboo poles, while youth collected riverbed stones and wire ties.",
                "sol": make_sol_html([
                    "Bamboo provides exceptional tensile strength while being lightweight and flexible.",
                    "Heavy riverbed boulders formed the base ballast, anchoring bamboo trestles in rushing water.",
                    "Utilizing locally available natural materials allowed instant construction without waiting for imports."
                ], "Indigenous materials and local engineering often solve acute crises faster than external bureaucracy.")
            },
            {
                "q": "What role does the queen ant perform in an ant colony?",
                "options": ["She hunts for food across the forest", "She lays eggs to ensure the colony's continuous reproduction", "She guards the entrance against beetles", "She builds the honeycomb"],
                "ans": 1,
                "hint": "Think about the specialized reproductive role in social insect colonies.",
                "exp": "The queen ant's sole vital duty is laying eggs to sustain and expand colony population.",
                "sol": make_sol_html([
                    "Social insects feature distinct castes: reproductive, worker, and soldier castes.",
                    "The queen ant is the reproductive heart of the colony, laying thousands of eggs.",
                    "Worker ants care for her and feed the emerging larvae."
                ], "Specialized reproductive roles in insect colonies guarantee species survival.")
            },
            {
                "q": "How do honeybees communicate the direction and distance of distant nectar-rich flower meadows to other hive workers?",
                "options": ["By buzzing names", "By performing intricate figure-eight movements known as the waggle dance", "By blinking their eyes", "By changing color"],
                "ans": 1,
                "hint": "Think of the famous biological dance language discovered by Karl von Frisch.",
                "exp": "Forager bees perform the waggle dance inside the dark hive to encode the angle and distance to flowers.",
                "sol": make_sol_html([
                    "When a scout bee discovers rich blossom patches, she returns to the honeycomb.",
                    "She performs a figure-eight waggle run on the vertical wax combs.",
                    "The angle of the run relative to vertical indicates the flower direction relative to the sun.",
                    "The duration of the waggle buzz indicates the distance to the flower source."
                ], "The honeybee waggle dance is one of the animal kingdom's most sophisticated symbolic languages.")
            },
            {
                "q": "Why is eating a communal meal on fresh banana leaves considered both healthy and ecologically sustainable?",
                "options": ["Banana leaves are coated in plastic", "They are 100% natural, biodegradable, contain beneficial plant antioxidants, and create zero plastic pollution", "They cannot be composted", "They are made in factories"],
                "ans": 1,
                "hint": "Consider the natural properties of large tropical foliage.",
                "exp": "Banana leaves are chemical-free, hygienic, biodegradable, and enrich compost after disposal.",
                "sol": make_sol_html([
                    "Banana leaves have a natural waxy cuticle that repels water and prevents soaking.",
                    "Warm food placed on the leaf absorbs natural plant polyphenols like EGCG.",
                    "Unlike single-use plastic or thermocol plates, used banana leaves decompose naturally into manure."
                ], "Traditional dining on leaves harmonizes human health with environmental sustainability.")
            },
            {
                "q": "What is the dark, crumbly, nutrient-rich organic substance produced when decomposers break down plant waste in a compost pit?",
                "options": ["Sand", "Humus (organic manure)", "Plastic clay", "Gravel"],
                "ans": 1,
                "hint": "It smells like rich forest soil and feeds garden plants.",
                "exp": "Humus is fully decomposed organic matter that provides essential nutrients and moisture retention in soil.",
                "sol": make_sol_html([
                    "Decomposition of leaves, peels, and manure produces dark organic matter called humus.",
                    "Humus is rich in nitrogen, phosphorus, potassium, and beneficial soil microbes.",
                    "Adding humus to garden soil enhances water-holding capacity and aerates root zones."
                ], "Humus represents the biological gold standard of fertile, living soil.")
            },
            {
                "q": "Why is a sprinkle of cow dung slurry or garden soil added to a compost pit filled with dry leaves?",
                "options": ["To make the pit heavier", "To inoculate the pile with millions of beneficial decomposing bacteria and fungi", "To prevent leaves from touching each other", "To stop decomposition"],
                "ans": 1,
                "hint": "Think about what biological agents are needed to start the breakdown process.",
                "exp": "Soil and dung slurry introduce microbial populations that accelerate organic decomposition.",
                "sol": make_sol_html([
                    "Dry leaves alone take a long time to break down because they lack starter microbes.",
                    "Cow dung slurry contains billions of active cellulolytic bacteria and moisture.",
                    "Adding this starter culture jump-starts aerobic composting within days."
                ], "Microbial inoculation accelerates natural organic waste breakdown.")
            },
            {
                "q": "What happens if organic food waste is dumped into open burning garbage piles instead of being composted?",
                "options": ["It turns directly into fertilizer", "It emits toxic smoke, carbon dioxide, and foul air pollution while wasting valuable soil nutrients", "It produces clean oxygen", "It turns into drinking water"],
                "ans": 1,
                "hint": "Consider the difference between burning and composting for air quality.",
                "exp": "Burning organic waste releases harmful particulate matter and greenhouse gases into the air.",
                "sol": make_sol_html([
                    "Burning leaves produces carbon monoxide, smoke, and fine particulates (PM2.5).",
                    "It also permanently destroys the nitrogen and carbon that could have regenerated soil.",
                    "Composting captures nutrients in the ground safely without air contamination."
                ], "Composting turns waste into soil wealth, whereas burning creates harmful air pollution.")
            },
            {
                "q": "How does social division of labor in an ant colony mirror organized human community projects?",
                "options": ["Both have every individual doing every job at random", "Both assign specialized roles so that complex collective goals are achieved smoothly", "Neither cares about survival", "Both rely on electronic computers"],
                "ans": 1,
                "hint": "Think about how specialization improves collective efficiency in both nature and society.",
                "exp": "Specialized roles allow both insect colonies and human communities to accomplish massive undertakings.",
                "sol": make_sol_html([
                    "In an ant nest, foragers find food, soldiers defend tunnels, and nurses rear young.",
                    "In a village, farmers produce food, masons build homes, and doctors treat diseases.",
                    "Specialization prevents duplication and ensures all vital community needs are met."
                ], "Division of labor is a universal principle of successful social living.")
            },
            {
                "q": "What ecological lesson does the life cycle of a banana leaf—from tree to dining plate to compost pit to sapling food—teach students?",
                "options": ["Linear waste disposal", "The circular economy of nature, where nothing is wasted and everything nourishes new life", "That plants are useless", "That soil is made of chemicals"],
                "ans": 1,
                "hint": "Think of how materials cycle in natural ecosystems without leaving trash.",
                "exp": "Nature operates in closed loops where organic waste becomes the fertile foundation for future growth.",
                "sol": make_sol_html([
                    "Human industrial systems often follow a linear model: make, use, dispose as trash.",
                    "Natural biological systems follow a circular loop: grow, use, compost, nourish new life.",
                    "Emulating nature's zero-waste loops creates sustainable, resilient human settlements."
                ], "In nature's circular ecology, waste is simply raw food for the next generation.")
            }
        ]
    },
    {
        "id": 20,
        "title": "Challenge 4",
        "section": "Traditions, School Teams, Projects & Riddles",
        "speech": "",
        "quizzes": [
            {
                "q": "In Assam, what do communities build from bamboo and thatch on the harvest festival eve of Uruka?",
                "options": ["A Bhela Ghar", "A Shikara boat", "A Stone fortress", "A Metal tower"],
                "ans": 0,
                "hint": "It is a temporary pavilion where neighbors cook and celebrate before the morning meji bonfire.",
                "exp": "Bhela Ghar is a traditional temporary hut built for communal feasts during Magh Bihu in Assam.",
                "sol": make_sol_html([
                    "Magh Bihu celebrates the conclusion of the winter harvest in Assam.",
                    "On Uruka night, villagers build artistic temporary pavilions called Bhela Ghar from bamboo and straw.",
                    "Families dine together inside, celebrating agrarian fellowship and community harmony."
                ], "Bhela Ghar exemplifies northeastern India's vibrant tradition of communal harvest celebration.")
            },
            {
                "q": "What is the traditional agricultural labor-sharing system called among terrace farmers in Sikkim?",
                "options": ["Panchayat", "Khetala", "Shramdaan", "Sabha"],
                "ans": 1,
                "hint": "Review the indigenous reciprocal farming network in the eastern Himalayas.",
                "exp": "'Khetala' is Sikkim's traditional labor exchange where farming families help each other without wages.",
                "sol": make_sol_html([
                    "Terrace farming in steep Himalayan topography requires intense seasonal labor.",
                    "Under Khetala, farming households take turns providing collective labor on each other's terraces.",
                    "This mutual assistance ensures all crops are planted and harvested on time without cash debt."
                ], "Khetala preserves community solidarity and sustainable agriculture in mountainous Sikkim.")
            },
            {
                "q": "In a school community, who is responsible for safely transporting students across city traffic to school each morning?",
                "options": ["The school librarian", "The school bus driver and conductor", "The mathematics teacher", "The sports referee"],
                "ans": 1,
                "hint": "Identify the transportation personnel who navigate public roadways.",
                "exp": "Bus drivers and conductors ensure safe, punctual transit between homes and school gates.",
                "sol": make_sol_html([
                    "Educational access requires safe, dependable transportation infrastructure.",
                    "Bus drivers navigate congested streets with caution and vigilance.",
                    "Conductors ensure children board and disembark safely at designated stops."
                ], "Transportation staff provide an essential lifeline connecting students to education.")
            },
            {
                "q": "Why is waste segregation into separate wet and dry dustbins essential during a campus cleanliness project?",
                "options": ["To make bins look colorful", "To keep biodegradable wet waste clean for composting while dry recyclables like paper can be recycled", "To make bins harder to empty", "To stop students from eating fruit"],
                "ans": 1,
                "hint": "Can wet rotten food and clean paper be recycled together?",
                "exp": "Segregation prevents dry recyclables from getting contaminated and enables wet waste to compost cleanly.",
                "sol": make_sol_html([
                    "When wet food scraps mix with dry paper and plastic, both become foul and difficult to recycle.",
                    "Separating at source keeps wet organics clean for rapid composting in school gardens.",
                    "Clean dry paper and cardboard can be baled and sent directly to paper recycling mills."
                ], "Segregation at source is the golden rule of modern waste management.")
            },
            {
                "q": "Solve this public place riddle: 'I have many platforms, rumbling buses arrive and depart, and ticket booths guide commuters to destinations.' What am I?",
                "options": ["A Library", "A Bus Stand", "A Post Office", "A Police Station"],
                "ans": 1,
                "hint": "It is the transit depot where passenger buses congregate.",
                "exp": "A bus stand or depot is the designated public hub for boarding and alighting passenger buses.",
                "sol": make_sol_html([
                    "Platforms and waiting bays organize arriving and departing buses.",
                    "Ticket windows issue travel passes and route schedules.",
                    "This landmark is the public Bus Stand."
                ], "Public transport hubs facilitate regional mobility and economic connectivity.")
            },
            {
                "q": "Solve this riddle: 'I have red collection boxes, letters sorted into sacks, and stamps carrying messages far away.' What am I?",
                "options": ["A Post Office", "A Primary Health Clinic", "A Cinema Hall", "A Water Treatment Plant"],
                "ans": 0,
                "hint": "Look for postal boxes, letters, and delivery couriers.",
                "exp": "The Post Office is the public postal facility for sending mail, parcels, and savings services.",
                "sol": make_sol_html([
                    "Red post boxes collect handwritten letters and official documents.",
                    "Postal clerks sort mail according to PIN codes and dispatch carrier vehicles.",
                    "This public landmark is the Post Office."
                ], "Postal systems connect people across geography through dependable communication.")
            },
            {
                "q": "Solve this riddle: 'I have swings, green grass lawns, shade trees, and flowerbeds where young and old relax.' What am I?",
                "options": ["A Railway Junction", "A Community Park", "A Fire Brigade Station", "A Grocery Supermarket"],
                "ans": 1,
                "hint": "Think of the outdoor green recreational space in a neighborhood.",
                "exp": "A public park provides open green recreation, fresh air, and community leisure space.",
                "sol": make_sol_html([
                    "Parks feature open grass lawns, recreational equipment like swings, and trees.",
                    "Children play team games while senior citizens walk and socialize.",
                    "This cherished public area is the Community Park."
                ], "Parks are vital urban green lungs that support physical and mental well-being.")
            },
            {
                "q": "Which traditional regional craft uses natural clay, a spinning wheel, and a firing kiln to produce cooling water pots?",
                "options": ["Metal welding", "Pottery", "Carpet weaving", "Glass blowing"],
                "ans": 1,
                "hint": "Think of the craftsperson called a kumhar who molds earthenware matkas.",
                "exp": "Potters shape clay on rotating wheels and fire pots in kilns to create earthenware vessels.",
                "sol": make_sol_html([
                    "Pottery is one of humanity's ancient indigenous crafts.",
                    "Clay is kneaded, centered on a spinning wheel, and shaped by hand into pitchers and bowls.",
                    "Firing in a kiln hardens clay into durable, porous earthenware that cools water naturally."
                ], "Earthen pottery provides natural, electricity-free evaporative water cooling.")
            },
            {
                "q": "How does crafting decorative nature cards from fallen leaves and pine needles embody eco-friendly living?",
                "options": ["It cuts down living green trees", "It upcycles fallen natural biomass into art without generating plastic waste or pollution", "It requires petroleum paints", "It destroys garden soil"],
                "ans": 1,
                "hint": "Think about using fallen plant debris creatively instead of factory-made plastics.",
                "exp": "Nature-based crafts upcycle fallen plant parts into biodegradable, plastic-free works of art.",
                "sol": make_sol_html([
                    "Upcycling uses discarded or fallen natural materials without harming living flora.",
                    "Fallen leaves, dried seed pods, and pine cones provide beautiful natural textures.",
                    "This craft eliminates the need for synthetic glues, glitter, or plastic embellishments."
                ], "Nature crafts celebrate organic beauty while maintaining zero ecological footprint.")
            },
            {
                "q": "What is the ultimate scientific and civic takeaway of studying 'Living Together'?",
                "options": ["Humans should live completely isolated from nature and neighbors", "Human well-being and environmental health depend upon mutual cooperation, teamwork, and ecological stewardship", "That communities do not need rules", "That public places maintain themselves automatically"],
                "ans": 1,
                "hint": "Consider how individuals, society, and nature are interconnected.",
                "exp": "Living together means recognizing that cooperation, empathy, and environmental care sustain our world.",
                "sol": make_sol_html([
                    "Humans are deeply social beings who thrive through collective effort and shared knowledge.",
                    "Community institutions, public parks, and infrastructure require continuous mutual care.",
                    "Respecting the dignity of labor and nature's circular ecology ensures a joyful, sustainable future."
                ], "Living together unites human cooperation with responsible environmental stewardship.")
            }
        ]
    }
]

if __name__ == "__main__":
    print(f"Loaded {len(slides_part3)} slides for Part 3.")
    total_q = sum(len(s.get("quizzes", [])) for s in slides_part3)
    print(f"Total quizzes: {total_q}")
    for s in slides_part3:
        tw = len(s["title"].split())
        assert 1 <= tw <= 3, f"Title '{s['title']}' must be 1 to 3 words"
        assert len(s["quizzes"]) == 10, f"Slide {s['id']} must have 10 quizzes"
        for q in s["quizzes"]:
            assert len(q["options"]) == 4, f"Question must have 4 options: {q['q']}"
            assert 0 <= q["ans"] <= 3, f"Invalid answer index: {q['ans']}"
            assert "sol" in q and "<ol" in q["sol"], "Solution HTML must be valid"
    print("All Part 3 slide constraints validated successfully!")

