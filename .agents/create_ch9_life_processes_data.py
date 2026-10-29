# -*- coding: utf-8 -*-
"""
Generator script for Class 7 Science Chapter 9: Life Processes in Animals Data
Outputs .agents/class7_science_life_processes_data.py
"""

import json

def sanitize(text):
    if not isinstance(text, str):
        return text
    forbidden = [r'\text{', r'\frac{', r'\circ', r'\approx', r'\cdot', r'\times', r'\degree', r'\dots',
                 r'\alpha', r'\beta', r'\Delta', r'\pm', r'\rightarrow', r'\left', r'\right', r'\quad',
                 r'\ge', r'\le', r'\neq', r'\sim', r'\infty', r'\sqrt']
    for f in forbidden:
        if f in text:
            raise ValueError(f"Raw LaTeX detected in slide data: {f} in {text[:50]}")
    return text

SLIDES_DATA = [
    # -------------------------------------------------------------
    # SLIDE 1: Nutrition in Animals: Breakdown of Complex Nutrients
    # -------------------------------------------------------------
    {
        "id": 1,
        "type": "theory_slide",
        "title": "Nutrition in Animals: Breaking Down the Complex",
        "subtitle": "Section 9.1 • Heterotrophic Feeding & Macromolecular Cleavage",
        "formula": "Carbohydrates → Glucose • Proteins → Amino Acids • Fats → Fatty Acids + Glycerol",
        "content": "<p>Unlike green plants that manufacture their own food through photosynthesis, all animals are <strong>heterotrophic</strong>: they must obtain energy and structural matter by consuming plants or other animals. Animal nutrition encompasses food requirement, the mode of food intake, and the body's utilization of nutrients.</p><p>The food consumed by animals consists of complex, insoluble organic macromolecules that cannot be directly absorbed into the bloodstream. Therefore, food must be broken down into simpler, soluble substances through the process called <strong>digestion</strong>:</p><ul><li><strong>Carbohydrates (Starches & Sugars):</strong> Broken down into simple monosaccharide sugars like <strong>glucose</strong> for cellular energy.</li><li><strong>Proteins:</strong> Broken down into building blocks called <strong>amino acids</strong> for muscle growth, tissue repair, and enzymatic synthesis.</li><li><strong>Fats (Lipids):</strong> Broken down into <strong>fatty acids</strong> and <strong>glycerol</strong> for long-term energy storage and cell membranes.</li></ul><p>This magnificent chemical disassembly takes place inside a specialized, continuous internal tube: the <strong>alimentary canal</strong>.</p>",
        "key_takeaways": [
            "Animals are heterotrophs that depend on ingested organic food for energy and growth.",
            "Digestion is the chemical and mechanical breakdown of complex insoluble nutrients into simple soluble forms.",
            "Carbohydrates yield glucose, proteins yield amino acids, and fats yield fatty acids and glycerol.",
            "The alimentary canal and associated digestive glands perform this coordinated breakdown."
        ],
        "checkpoints": [
            {
                "question": "What is the primary biological reason food must undergo digestion before being utilized by animal cells?",
                "options": [
                    "Complex nutrients are insoluble and too large to pass through cell membranes into the bloodstream",
                    "To change the color of food so that blood cells can recognize it",
                    "To convert all solid food into boiling steam inside the body",
                    "Food must be turned into pure carbon dioxide before entering cells"
                ],
                "correct": 0,
                "explanation": "Food macromolecules like starch and protein are insoluble and too large to cross the intestinal wall into the blood capillaries. Digestion breaks them into tiny, soluble molecules like glucose and amino acids."
            },
            {
                "question": "Which of the following correctly pairs a complex nutrient with its simplest digested product?",
                "options": [
                    "Proteins → Amino Acids",
                    "Fats → Glucose",
                    "Carbohydrates → Fatty Acids",
                    "Proteins → Dietary Fiber"
                ],
                "correct": 0,
                "explanation": "Proteins are long polymers of amino acids; digestion cleaves peptide bonds to release free amino acids. Carbohydrates break down into glucose, and fats break down into fatty acids and glycerol."
            }
        ],
        "simulator_type": "macronutrient_breakdown_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 2: The Alimentary Canal: The Master Journey of Food
    # -------------------------------------------------------------
    {
        "id": 2,
        "type": "theory_slide",
        "title": "The Alimentary Canal: The Continuous Food Tube",
        "subtitle": "Section 9.1 • Anatomical Roadmap: From Ingestion to Egestion",
        "formula": "Tract: Mouth → Oesophagus → Stomach → Small Intestine → Large Intestine → Rectum → Anus",
        "content": "<p>In human beings and higher animals, digestion occurs within a continuous muscular tube extending from the mouth to the anus, known as the <strong>alimentary canal</strong> (or gastrointestinal tract). In an adult human, this remarkable pathway stretches nearly <strong>9 metres (30 feet)</strong> in total length!</p><p><strong>The Sequential Digestive Compartments:</strong></p><ol><li><strong>Buccal Cavity (Mouth):</strong> Where food is ingested, chewed by teeth, and mixed with saliva.</li><li><strong>Oesophagus (Food Pipe):</strong> Muscular conduit transporting food to the stomach via peristalsis.</li><li><strong>Stomach:</strong> J-shaped muscular reservoir churning food with acid and protein-digesting enzymes.</li><li><strong>Small Intestine:</strong> Longest section (~6 metres) where primary chemical digestion and nutrient absorption occur.</li><li><strong>Large Intestine:</strong> Absorbs water and minerals from residual undigested matter, forming semi-solid stool.</li><li><strong>Rectum & Anus:</strong> Stores faeces temporarily and expels waste via egestion.</li></ol><p>Along this journey, three vital accessory glands—the <strong>salivary glands</strong>, <strong>liver</strong>, and <strong>pancreas</strong>—pour powerful digestive juices into the canal to accelerate chemical breakdown.</p>",
        "key_takeaways": [
            "The alimentary canal is a continuous muscular tube measuring roughly 9 metres in adult humans.",
            "It consists of the buccal cavity, oesophagus, stomach, small intestine, large intestine, rectum, and anus.",
            "Food moves in one direction through coordinated muscular contractions called peristalsis.",
            "Accessory glands (salivary glands, liver, and pancreas) secrete digestive juices into the tract."
        ],
        "checkpoints": [
            {
                "question": "Which of the following represents the correct sequential order of organs through which food travels in the human alimentary canal?",
                "options": [
                    "Mouth → Oesophagus → Stomach → Small Intestine → Large Intestine",
                    "Mouth → Stomach → Oesophagus → Large Intestine → Small Intestine",
                    "Mouth → Small Intestine → Stomach → Oesophagus → Large Intestine",
                    "Oesophagus → Mouth → Stomach → Large Intestine → Rectum"
                ],
                "correct": 0,
                "explanation": "Food enters the mouth, passes down the oesophagus into the stomach, proceeds into the small intestine, and finally enters the large intestine."
            },
            {
                "question": "Which of the following organs is an associated digestive gland that secretes juices rather than a compartment food passes through?",
                "options": [
                    "Pancreas",
                    "Oesophagus",
                    "Stomach",
                    "Small Intestine"
                ],
                "correct": 0,
                "explanation": "The pancreas (along with the liver and salivary glands) is an accessory digestive gland. Food does not pass inside the pancreas; rather, the pancreas injects pancreatic juice into the small intestine."
            }
        ],
        "simulator_type": "alimentary_canal_map_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 3: The Buccal Cavity: Teeth & Salivary Digestion
    # -------------------------------------------------------------
    {
        "id": 3,
        "type": "theory_slide",
        "title": "The Mouth Cavity: Mastication & Salivary Amylase",
        "subtitle": "Section 9.1.1 • Mechanical Grinding & Chemical Breakdown of Starch",
        "formula": "Starch (Complex Carbohydrate) + Salivary Amylase → Simple Sugars (Maltose)",
        "content": "<p>Digestion begins the moment food enters the <strong>buccal cavity</strong>. Here, mechanical and chemical digestion happen simultaneously:</p><p><strong>1. Mechanical Digestion (The Teeth):</strong><br>Humans have four distinct types of teeth specialized for processing diverse foods:</p><ul><li><strong>Incisors (8):</strong> Chisel-shaped front teeth for biting and cutting food.</li><li><strong>Canines (4):</strong> Pointed, dagger-like teeth for piercing and tearing food.</li><li><strong>Premolars (8) & Molars (12):</strong> Broad, ridged surface teeth for crushing and grinding food into a moist pulp.</li></ul><p><strong>2. Chemical Digestion (Saliva & The Tongue):</strong><br>Three pairs of salivary glands pour watery saliva into the mouth. Saliva contains the enzyme <strong>salivary amylase</strong> (ptyalin), which initiates the chemical breakdown of complex starch (such as in rice or chapati) into sweet, simple sugars (maltose). This is why a piece of plain bread tastes noticeably sweeter after being chewed for two minutes!</p><p>The muscular tongue rolls the food into a soft, lubricated sphere called a <strong>bolus</strong>, ready for swallowing.</p>",
        "key_takeaways": [
            "Digestion begins in the mouth through both mechanical chewing and chemical enzyme action.",
            "Four types of teeth perform specific mechanical roles: incisors (cut), canines (tear), premolars and molars (grind).",
            "Salivary amylase chemically converts insoluble starch into sweet, soluble simple sugars.",
            "The tongue mixes food with saliva, tastes through taste buds, and shapes the food into a lubricated bolus."
        ],
        "checkpoints": [
            {
                "question": "Why does a piece of plain chapati or boiled rice begin to taste sweet after being chewed thoroughly for several minutes?",
                "options": [
                    "Salivary amylase converts tasteless starch into sweet simple sugars",
                    "Teeth release natural sugar crystals stored inside their enamel",
                    "The tongue secretes glucose syrup directly onto the food",
                    "Bacteria in the mouth turn protein into honey"
                ],
                "correct": 0,
                "explanation": "Saliva contains the digestive enzyme amylase, which breaks down complex starch molecules into simple, sweet-tasting sugars like maltose."
            },
            {
                "question": "Which type of teeth are specifically adapted with sharp, pointed tips to pierce and tear tough food?",
                "options": [
                    "Canines",
                    "Incisors",
                    "Molars",
                    "Premolars"
                ],
                "correct": 0,
                "explanation": "Canines are pointed and dagger-shaped, located beside incisors, specifically designed for tearing and piercing food."
            }
        ],
        "simulator_type": "mouth_saliva_starch_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 4: The Oesophagus: Peristalsis Defies Gravity
    # -------------------------------------------------------------
    {
        "id": 4,
        "type": "theory_slide",
        "title": "The Food Pipe: Peristaltic Wave Mechanics",
        "subtitle": "Section 9.1.1 • Rhythmic Muscular Contractions of the Oesophagus",
        "formula": "Peristalsis = Circular Muscle Contraction (Behind Bolus) + Longitudinal Relaxation (Ahead)",
        "content": "<p>Once swallowed, the food bolus enters the <strong>oesophagus</strong> (food pipe), a flexible muscular tube approximately <strong>25 cm long</strong> connecting the pharynx to the stomach. No digestive enzymes are secreted in the oesophagus; its primary function is rapid, safe transport.</p><p>How does food travel down the tube? It does <em>not</em> simply fall by gravity! If you were to drink water or swallow food while hanging upside down from a gymnastics bar, the food would still travel smoothly toward your stomach. This is accomplished by a rhythmic muscular mechanism called <strong>peristalsis</strong>:</p><ul><li>The circular muscles in the oesophageal wall immediately behind the bolus contract forcefully, pinching the tube inward.</li><li>Simultaneously, the longitudinal muscles ahead of the bolus relax and widen the passage.</li><li>This coordinated, wave-like contraction sweeps downward, pushing the bolus steadily along the alimentary canal.</li></ul><p>At the base of the oesophagus, the lower oesophageal sphincter opens like a one-way security valve to admit food into the stomach while preventing corrosive acid from splashing back upward.</p>",
        "key_takeaways": [
            "The oesophagus is a 25 cm muscular tube connecting the throat to the stomach.",
            "Peristalsis is the involuntary wave-like contraction and relaxation of muscular walls that propels food forward.",
            "Peristalsis works independently of gravity, allowing food transit even when lying down or upside down.",
            "A muscular sphincter at the base prevents stomach acid from flowing backward into the food pipe."
        ],
        "checkpoints": [
            {
                "question": "What is the term for the wave-like muscular contractions that push food along the human digestive tract?",
                "options": [
                    "Peristalsis",
                    "Photosynthesis",
                    "Circulation",
                    "Transpiration"
                ],
                "correct": 0,
                "explanation": "Peristalsis is the rhythmic involuntary contraction and relaxation of muscles along the alimentary canal that propels the food bolus forward."
            },
            {
                "question": "If an astronaut in zero gravity swallows food inside the International Space Station, what happens to the food bolus?",
                "options": [
                    "Peristalsis propels the food bolus into the stomach normally",
                    "The food floats indefinitely in the throat and cannot reach the stomach",
                    "The food reverses direction and exits through the ears",
                    "The food instantly dissolves into thin air"
                ],
                "correct": 0,
                "explanation": "Because peristalsis is driven by active muscular contractions rather than gravity, food travels efficiently to the stomach even in zero gravity."
            }
        ],
        "simulator_type": "peristalsis_wave_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 5: The Stomach: Churning, Acid & Protein Digestion
    # -------------------------------------------------------------
    {
        "id": 5,
        "type": "theory_slide",
        "title": "The Stomach: Acid, Mucus & Gastric Churning",
        "subtitle": "Section 9.1.1 • Gastric Proteolysis & Dr. William Beaumont's Fistula Discovery",
        "formula": "Pepsinogen + HCl (pH 1.5–2.0) → Active Pepsin • Proteins + Pepsin → Peptides",
        "content": "<p>The <strong>stomach</strong> is a thick-walled, expandable J-shaped muscular organ located on the left side of the upper abdominal cavity. It serves as both a temporary storage reservoir and a vigorous chemical reaction vessel.</p><p>The stomach's muscular walls contract rhythmically, churning solid food into a smooth, semi-liquid acidic puree called <strong>chyme</strong>. The inner gastric lining secretes three vital substances:</p><ul><li><strong>Hydrochloric Acid (HCl):</strong> Creates an intensely acidic environment (pH 1.5 to 2.0). This strong acid kills harmful bacteria and micro-organisms ingested with food, and provides the necessary acidic medium to activate the protein-digesting enzyme <strong>pepsin</strong>.</li><li><strong>Pepsin:</strong> A powerful protease enzyme that breaks down complex dietary protein chains into smaller, soluble fragments called peptides.</li><li><strong>Mucus:</strong> A thick, protective alkaline coating that shields the stomach's delicate inner wall from being corroded and digested by its own acid and pepsin!</li></ul><p><strong>Historic Insight:</strong> In 1822, American army surgeon <strong>Dr. William Beaumont</strong> treated a Canadian trapper named Alexis St. Martin, who survived a shotgun wound leaving an open window (fistula) directly into his stomach. Through direct observation, Beaumont proved that digestion is a chemical process driven by gastric acid and juices rather than simple mechanical grinding.</p>",
        "key_takeaways": [
            "The stomach churns food mechanically into a semi-liquid mass known as chyme.",
            "Hydrochloric acid (HCl) creates a low pH (1.5-2.0) that sterilizes food by killing microbes and activates pepsin.",
            "Pepsin begins the chemical breakdown of complex proteins into smaller peptides.",
            "A protective mucus barrier prevents the stomach wall from being digested by its own acid."
        ],
        "checkpoints": [
            {
                "question": "What is the crucial biological function of the thick mucus layer secreted by the inner stomach lining?",
                "options": [
                    "To protect the stomach wall from being eroded and digested by hydrochloric acid and pepsin",
                    "To convert proteins into simple sugars",
                    "To freeze the food so bacteria cannot multiply",
                    "To absorb all vitamins directly into the lungs"
                ],
                "correct": 0,
                "explanation": "Stomach acid is strong enough to dissolve tissue (pH ~1.5). The alkaline mucus layer acts as an essential physical and chemical shield protecting the stomach lining."
            },
            {
                "question": "What dual role does hydrochloric acid (HCl) play in the human stomach?",
                "options": [
                    "It kills ingested bacteria and creates the acidic medium needed to activate pepsin",
                    "It digests fats and turns water into blood",
                    "It cools down hot food and absorbs dietary calcium",
                    "It produces oxygen gas for cellular respiration"
                ],
                "correct": 0,
                "explanation": "Hydrochloric acid has two main duties: killing harmful pathogens swallowed with food, and providing the acidic pH necessary for pepsin to break down proteins."
            }
        ],
        "simulator_type": "stomach_churning_acid_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 6: The Small Intestine: Liver Bile & Pancreatic Juice
    # -------------------------------------------------------------
    {
        "id": 6,
        "type": "theory_slide",
        "title": "The Small Intestine: Secretions of Liver & Pancreas",
        "subtitle": "Section 9.1.1 • Fat Emulsification & Complete Chemical Digestion",
        "formula": "Bile: Large Fat Globules → Emulsified Micelles • Pancreatic Enzymes: Complete Breakdown",
        "content": "<p>From the stomach, acidic chyme squirts in controlled spurts through the pyloric sphincter into the <strong>small intestine</strong>. Measuring about <strong>6 metres (20 feet)</strong> in length, this coiled organ is the longest component of the alimentary canal and the true powerhouse of chemical digestion.</p><p>Because stomach chyme is intensely acidic, enzymes in the intestine cannot function until the acid is neutralized. Two magnificent accessory organs step in:</p><ul><li><strong>The Liver (Reddish-Brown Gland):</strong> The largest gland in the body. It manufactures greenish-yellow <strong>bile</strong>, which is stored in the <strong>gall bladder</strong>. Bile contains no enzymes, but it contains alkaline bile salts that neutralize stomach acid and break down large fat globules into microscopic droplets through <strong>emulsification</strong>.</li><li><strong>The Pancreas (Cream-Coloured Gland):</strong> Secretes <strong>pancreatic juice</strong> containing three master enzymes: <em>amylase</em> (breaks starch to glucose), <em>trypsin</em> (cleaves proteins to amino acids), and <em>lipase</em> (digests emulsified fats into fatty acids and glycerol).</li></ul>",
        "key_takeaways": [
            "The small intestine is the longest section of the alimentary canal (~6 metres) and the site of final chemical breakdown.",
            "The liver produces bile (stored in the gall bladder), which neutralizes acid and emulsifies fats.",
            "Emulsification breaks large fat globules into microscopic droplets, accelerating enzymatic digestion.",
            "Pancreatic juice contains amylase, trypsin, and lipase to digest carbohydrates, proteins, and fats completely."
        ],
        "checkpoints": [
            {
                "question": "Which organ produces bile, and where is this digestive liquid temporarily stored before entering the small intestine?",
                "options": [
                    "Produced by the Liver; stored in the Gall Bladder",
                    "Produced by the Pancreas; stored in the Stomach",
                    "Produced by the Kidneys; stored in the Bladder",
                    "Produced by the Oesophagus; stored in the Tongue"
                ],
                "correct": 0,
                "explanation": "Bile is continuously synthesized by the liver and stored in concentrated form in the gall bladder until fatty food enters the small intestine."
            },
            {
                "question": "What is the biological significance of fat emulsification by bile salts?",
                "options": [
                    "It breaks large oil droplets into microscopic droplets, dramatically increasing the surface area for lipase enzymes",
                    "It turns liquid fats into solid bone calcium",
                    "It evaporates all fats out of the body as sweat",
                    "It converts fats directly into carbon dioxide inside the intestine"
                ],
                "correct": 0,
                "explanation": "Fats do not mix with water. Bile acts like natural detergent, breaking large fat globules into tiny droplets (emulsification) so water-soluble lipase can digest them rapidly."
            }
        ],
        "simulator_type": "liver_pancreas_bile_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 7: Absorption in Small Intestine: The Villi Marvel
    # -------------------------------------------------------------
    {
        "id": 7,
        "type": "theory_slide",
        "title": "Absorption in Small Intestine: The Architecture of Villi",
        "subtitle": "Section 9.1.1 • Microscopic Villi & Massive Surface Area Expansion",
        "formula": "Surface Area Factor: Foldings + Villi + Microvilli Expand Surface Area by 600× (> 250 m²)",
        "content": "<p>Digestion without absorption is futile. Once food is dismantled into elementary soluble molecules (glucose, amino acids, fatty acids), it must cross the intestinal wall into the circulatory system to nourish trillions of living body cells. This process is called <strong>absorption</strong>.</p><p>To absorb nutrients efficiently, the inner lining of the small intestine is engineered with millions of microscopic, finger-like projections called <strong>villi</strong> (singular: <em>villus</em>):</p><ul><li><strong>Massive Surface Area:</strong> If the inside of the human small intestine were completely smooth, its surface area would barely cover 0.5 square metres. Thanks to circular folds, millions of villi, and billions of microscopic <strong>microvilli</strong>, the absorptive surface area is expanded to over <strong>250 square metres</strong>—the size of an entire tennis court!</li><li><strong>Ultra-Thin Barrier:</strong> Each villus is covered by an epithelial membrane only one cell thick, minimizing diffusion distance.</li><li><strong>Rich Capillary Mesh:</strong> Directly beneath the membrane lies a dense network of blood capillaries that absorb glucose and amino acids directly into the bloodstream.</li><li><strong>Lacteal (Lymph Vessel):</strong> A central lymphatic vessel in each villus specifically absorbs digested fatty acids and glycerol.</li></ul><p>The absorbed nutrients travel via the portal vein to the liver and cells, where they are built into cellular structures—a process called <strong>assimilation</strong>.</p>",
        "key_takeaways": [
            "Absorption is the passage of digested soluble nutrients through the intestinal wall into the blood and lymph.",
            "Millions of finger-like projections called villi expand the absorptive area to over 250 m².",
            "Each villus has a one-cell-thin wall and contains blood capillaries (for sugars and amino acids) and a lacteal (for fats).",
            "Assimilation is the utilization of absorbed nutrients by body cells for energy, growth, and tissue repair."
        ],
        "checkpoints": [
            {
                "question": "What is the primary architectural purpose of the millions of finger-like villi lining the small intestine?",
                "options": [
                    "To vastly increase the internal surface area for rapid absorption of digested nutrients",
                    "To chew solid food into tiny bits inside the belly",
                    "To store undigested food for several weeks",
                    "To pump blood directly into the kidneys"
                ],
                "correct": 0,
                "explanation": "Villi, along with microvilli, expand the absorptive surface area of the small intestine more than 600-fold (to over 250 m²), allowing rapid, complete nutrient absorption."
            },
            {
                "question": "Which microscopic vessel inside a villus is specifically responsible for absorbing digested fatty acids and glycerol?",
                "options": [
                    "The Lacteal (central lymphatic vessel)",
                    "The Blood Capillary",
                    "The Tracheal Air Tube",
                    "The Ureter"
                ],
                "correct": 0,
                "explanation": "Water-soluble glucose and amino acids enter blood capillaries, whereas hydrophobic fatty acids and glycerol are absorbed into the central lymph vessel called the lacteal."
            }
        ],
        "simulator_type": "intestinal_villi_absorption_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 8: Large Intestine, Rectum & Egestion
    # -------------------------------------------------------------
    {
        "id": 8,
        "type": "theory_slide",
        "title": "Large Intestine & Egestion: Reclaiming Water & Salts",
        "subtitle": "Section 9.1.1 • Compaction of Stool & Expulsion of Undigested Waste",
        "formula": "Ingestion → Digestion → Absorption → Assimilation → Egestion (The 5 Nutritional Pillars)",
        "content": "<p>All food that cannot be digested or absorbed—such as insoluble cellulose plant fibers (roughage)—passes out of the small intestine and enters the <strong>large intestine</strong> (colon). Although wider in diameter than the small intestine, it is considerably shorter, measuring approximately <strong>1.5 metres</strong> in length.</p><p><strong>Vital Functions of the Large Intestine:</strong></p><ul><li><strong>Water Reabsorption:</strong> Digestion requires liters of water secreted in saliva, gastric juice, bile, and pancreatic fluid. The primary duty of the colon is to reabsorb nearly 90% of this water and vital mineral salts back into the body. Without this reabsorption, severe dehydration would occur rapidly.</li><li><strong>Formation of Faeces:</strong> As water is extracted, the liquid waste is compacted into a semi-solid material known as <strong>faeces</strong> (stool).</li><li><strong>Symbiotic Gut Microbiota:</strong> Billions of beneficial bacteria thrive in the colon, synthesizing essential vitamins (like Vitamin K and B-complex) and fermenting residual fibers.</li></ul><p>The semi-solid faeces pass into the <strong>rectum</strong>, where they are stored temporarily. When sensory stretch receptors signal fullness, the waste is eliminated from the body through the <strong>anus</strong> in the final stage of animal nutrition, called <strong>egestion</strong> (defaecation).</p>",
        "key_takeaways": [
            "The large intestine (~1.5 m long) is wider than the small intestine and specializes in water and salt reabsorption.",
            "Water recovery prevents critical dehydration and consolidates unabsorbed waste into semi-solid faeces.",
            "Faeces are temporarily stored in the rectum before being expelled through the anus.",
            "Egestion is the discharge of undigested food matter (distinct from excretion, which removes cellular metabolic wastes)."
        ],
        "checkpoints": [
            {
                "question": "What is the primary physiological function of the human large intestine?",
                "options": [
                    "To reabsorb water and mineral salts from undigested food, forming semi-solid faeces",
                    "To chemically digest proteins into amino acids",
                    "To secrete hydrochloric acid and bile",
                    "To filter nitrogenous waste from the blood"
                ],
                "correct": 0,
                "explanation": "The large intestine does not secrete digestive enzymes; its main job is to recover water and mineral salts from leftover undigested matter, preventing dehydration."
            },
            {
                "question": "What is the key scientific distinction between 'egestion' and 'excretion'?",
                "options": [
                    "Egestion removes undigested food waste through the anus, while excretion removes cellular metabolic waste like urea through kidneys",
                    "Egestion produces urine, while excretion produces sweat",
                    "Egestion occurs only in plants, while excretion occurs only in animals",
                    "They are identical terms with no difference whatsoever"
                ],
                "correct": 0,
                "explanation": "Egestion is the elimination of undigested, unabsorbed food residue via the anus. Excretion is the removal of chemical metabolic waste products (like urea in urine and CO₂ in exhaled air) generated inside body cells."
            }
        ],
        "simulator_type": "large_intestine_egestion_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 9: Digestion in Ruminants: Cud-Chewing Herbivores
    # -------------------------------------------------------------
    {
        "id": 9,
        "type": "theory_slide",
        "title": "Digestion in Ruminants: The Mystery of Cellulose",
        "subtitle": "Section 9.1.2 • Four-Chambered Stomachs & Microbial Fermentation in Cud-Chewers",
        "formula": "Cellulose (Grass) + Rumen Bacteria/Protozoa → Cellobiose → Glucose → Absorbed Energy",
        "content": "<p>Have you ever noticed grazing herbivores like cows, buffaloes, deer, and sheep continuously chewing even when resting peacefully under a tree? These animals are <strong>ruminants</strong>, and they possess a fascinating digestive adaptation to consume grass rich in <strong>cellulose</strong>—a tough structural carbohydrate that humans and carnivores cannot digest!</p><p>Humans lack the enzyme <em>cellulase</em> required to cleave cellulose bonds. Ruminants overcome this challenge through a specialized, four-compartment stomach:</p><ol><li><strong>Rumen (Largest Chamber):</strong> Grazing animals quickly bite and swallow grass without thorough chewing. In the rumen, millions of symbiotic anaerobic bacteria and ciliate protozoa begin fermenting and breaking down cellulose. The partially digested food is called <strong>cud</strong>.</li><li><strong>Reticulum (Honeycomb):</strong> Directs cud back into the mouth in small lumps when the animal is resting. The ruminant chews this cud thoroughly—a process called <strong>rumination</strong> (chewing the cud)—mixing it with vast volumes of saliva.</li><li><strong>Omasum (Book-Leaves):</strong> The re-swallowed cud enters this chamber, where excess water is squeezed out and reabsorbed.</li><li><strong>Abomasum (The True Stomach):</strong> Gastric juices and enzymes digest the food proteins and the fermented bacteria themselves, exactly like the human stomach!</li></ol>",
        "key_takeaways": [
            "Ruminants (cows, buffaloes, sheep) possess specialized stomachs to digest tough plant cellulose.",
            "The four stomach chambers are the Rumen, Reticulum, Omasum, and Abomasum (true stomach).",
            "Swallowed food is partially digested in the rumen into 'cud', which is regurgitated to the mouth for thorough chewing (rumination).",
            "Symbiotic microbes in the rumen ferment cellulose into absorbable nutrients, a capability humans lack."
        ],
        "checkpoints": [
            {
                "question": "Why can ruminant animals like cows digest grass and leaves, while humans cannot obtain energy from eating grass?",
                "options": [
                    "Ruminants harbor symbiotic rumen microbes that break down tough cellulose; humans lack cellulase enzymes",
                    "Cows have steel teeth that turn grass into sugar",
                    "Grass contains no nutrients at all",
                    "Human stomachs contain too much acid which freezes plant cells"
                ],
                "correct": 0,
                "explanation": "Plant cell walls are made of cellulose. Ruminants rely on trillions of symbiotic bacteria and protozoa in their rumen to ferment cellulose; humans lack these microbes and enzymes."
            },
            {
                "question": "What is 'cud' in the digestive cycle of a grazing ruminant animal?",
                "options": [
                    "Partially digested grass brought back from the rumen into the mouth for re-chewing",
                    "Poisonous matter rejected by the stomach",
                    "Water stored in the animal's hump",
                    "The outer horn covering of sheep"
                ],
                "correct": 0,
                "explanation": "Cud is the partially fermented, softened food mass in the rumen that is regurgitated back to the mouth for thorough chewing when the animal is resting."
            }
        ],
        "simulator_type": "ruminant_digestion_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 10: Digestion in Birds: The Muscular Gizzard & Crop
    # -------------------------------------------------------------
    {
        "id": 10,
        "type": "theory_slide",
        "title": "Digestion in Birds: The Crop & Toothless Gizzard",
        "subtitle": "Section 9.1.2 • Mechanical Grinding via Swallowed Grit (Gastroliths)",
        "formula": "Swallowed Hard Grain + Swallowed Stones (Grit) + Thick Muscular Gizzard Churning → Crushed Meal",
        "content": "<p>Did you know that birds have <strong>no teeth</strong>? Heavy jawbones and dense teeth would make birds far too heavy to fly efficiently! Yet seed-eating birds like pigeons, sparrows, chickens, and ostriches consume rock-hard seeds, grains, and nuts. How do birds grind their food without teeth?</p><p>Avian evolution solved this puzzle by developing two specialized digestive chambers:</p><ul><li><strong>The Crop:</strong> An expandable pouch at the base of the bird's neck. Because birds must feed rapidly in the open to avoid predators, they quickly swallow grains whole. The crop serves as a safe temporary storage silo where food is moistened and softened by secretions.</li><li><strong>The Proventriculus:</strong> The glandular first part of the stomach that secretes digestive acid and enzymes onto the softened food.</li><li><strong>The Gizzard (Ventriculus):</strong> A thick, extremely powerful muscular organ lined with a tough, sandpaper-like keratin layer (koilin). Birds deliberately swallow small <strong>pebbles, sand grains, and grit</strong> (gastroliths), which remain stored inside the gizzard. When the gizzard's muscular walls contract with immense crushing force, the hard pebbles grind the seeds into fine meal, acting exactly like internal stone millstones!</li></ul>",
        "key_takeaways": [
            "Birds have no teeth to reduce body weight for efficient flight.",
            "The crop is a pouch in the gullet used for rapid food collection, temporary storage, and softening.",
            "The gizzard is a powerful muscular grinding organ lined with tough keratin.",
            "Swallowed small stones and grit (gastroliths) inside the gizzard grind seeds mechanically, replacing the function of teeth."
        ],
        "checkpoints": [
            {
                "question": "Why do grain-eating birds like hens and pigeons deliberately swallow small pebbles, sand, and grit?",
                "options": [
                    "The swallowed grit stays in the muscular gizzard to grind hard seeds and grains mechanically",
                    "To add mineral flavors to their food",
                    "Because they mistake colorful stones for fruit",
                    "To make themselves too heavy for cats to catch"
                ],
                "correct": 0,
                "explanation": "Since birds lack teeth, the swallowed stones (gastroliths) lodge inside the muscular gizzard, where powerful churning contractions grind hard grains into digestible meal."
            },
            {
                "question": "Which organ in a bird's digestive tract serves as an expandable storage pouch to moisten and soften swallowed food?",
                "options": [
                    "Crop",
                    "Gizzard",
                    "Liver",
                    "Kidney"
                ],
                "correct": 0,
                "explanation": "The crop is an elastic pouch along the oesophagus where birds store and soften quickly swallowed food before it passes to the stomach and gizzard."
            }
        ],
        "simulator_type": "bird_gizzard_mechanics_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 11: Respiration in Animals: Cellular Powerhouse
    # -------------------------------------------------------------
    {
        "id": 11,
        "type": "theory_slide",
        "title": "Respiration in Animals: Unlocking Cellular Energy",
        "subtitle": "Section 9.2 • Breathing (Physical) vs Cellular Respiration (Chemical)",
        "formula": "C₆H₁₂O₆ (Glucose) + 6O₂ (Oxygen) → 6CO₂ (Carbon Dioxide) + 6H₂O (Water) + Energy (ATP)",
        "content": "<p>Digestion delivers glucose into the blood, but glucose itself is like unburned fuel in a car's tank. To perform vital life activities—running, thinking, maintaining body warmth, cell repair—the chemical energy locked inside glucose bonds must be liberated. This life process is <strong>respiration</strong>.</p><p>Many students confuse <em>breathing</em> with <em>respiration</em>, but in science they represent two distinct steps of a single life-sustaining chain:</p><ul><li><strong>Breathing (External Respiration):</strong> A physical, mechanical process where an animal takes in oxygen-rich air from the environment (inhalation) and expels carbon dioxide-rich air (exhalation). It involves respiratory organs like lungs, gills, or skin, and produces no chemical energy.</li><li><strong>Cellular Respiration (Internal Respiration):</strong> A biochemical reaction that occurs inside the <strong>mitochondria</strong> of every single living body cell. Here, oxygen reacts with glucose to break its carbon backbone, releasing usable biochemical energy in the form of <strong>ATP</strong>, while water and carbon dioxide are produced as by-products.</li></ul><p>The circulatory system acts as the courier bridge: red blood cells pick up oxygen from respiratory surfaces, deliver it to cells, and collect carbon dioxide waste to carry back for exhalation.</p>",
        "key_takeaways": [
            "Respiration is the cellular biochemical breakdown of glucose using oxygen to release vital energy (ATP).",
            "Breathing is the physical gas-exchange mechanism (inhaling O₂ and exhaling CO₂).",
            "Cellular respiration equation: Glucose + Oxygen → Carbon Dioxide + Water + Usable Energy.",
            "The circulatory system (blood) connects the breathing organs to every living cell in the body."
        ],
        "checkpoints": [
            {
                "question": "What is the primary scientific difference between breathing and cellular respiration?",
                "options": [
                    "Breathing is the physical intake and release of gases; cellular respiration is the chemical breakdown of glucose inside cells to release energy",
                    "Breathing produces glucose, while cellular respiration destroys water",
                    "Breathing occurs only at night, while respiration occurs only during the day",
                    "Breathing happens in plants, while respiration happens only in fish"
                ],
                "correct": 0,
                "explanation": "Breathing is the mechanical ventilation of respiratory organs (lungs/gills). Cellular respiration is the enzymatic chemical oxidation of glucose inside mitochondria to generate ATP energy."
            },
            {
                "question": "What are the two waste by-products produced during aerobic cellular respiration?",
                "options": [
                    "Carbon dioxide and water",
                    "Oxygen and glucose",
                    "Hydrochloric acid and bile",
                    "Nitrogen gas and protein crystals"
                ],
                "correct": 0,
                "explanation": "When glucose is oxidized with oxygen (C₆H₁₂O₆ + 6O₂), the products are energy plus the by-products carbon dioxide (CO₂) and water (H₂O)."
            }
        ],
        "simulator_type": "cellular_respiration_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 12: Human Respiratory Anatomy: Nostrils to Lungs
    # -------------------------------------------------------------
    {
        "id": 12,
        "type": "theory_slide",
        "title": "Human Respiratory System: The Pathway of Air",
        "subtitle": "Section 9.2.1 • From Nasal Conditioning to the Bronchial Tree",
        "formula": "Air Pathway: Nostrils → Nasal Cavity → Pharynx → Larynx → Trachea → Bronchi → Bronchioles → Alveoli",
        "content": "<p>The human respiratory tract is an intricately engineered air conditioning and delivery network that protects delicate lung tissues while channeling atmospheric oxygen deep into the chest.</p><p><strong>Tracing the Airway Step-by-Step:</strong></p><ol><li><strong>Nostrils & Nasal Cavity:</strong> Air enters through two external nostrils into the nasal cavity, lined with fine hairs (cilia) and sticky mucus. These act as electrostatic air filters, trapping airborne dust, soot, pollen, and microbes. Blood vessels warm and humidify the air to 37°C before it reaches the lungs. This is why <em>breathing through the nose is far healthier than breathing through the mouth</em>!</li><li><strong>Pharynx & Larynx:</strong> Air passes down the throat into the voice box (larynx). A flap of cartilage called the <strong>epiglottis</strong> automatically covers the windpipe during swallowing, ensuring food enters only the oesophagus and never the lungs.</li><li><strong>Trachea (Windpipe):</strong> A 12 cm long flexible tube strengthened by 16–20 <strong>C-shaped rings of cartilage</strong>. These stiff rings prevent the windpipe from collapsing inward when internal air pressure drops during deep inhalation.</li><li><strong>Bronchi & Bronchioles:</strong> At its base, the trachea divides into left and right <strong>bronchi</strong>, which enter the left and right lungs and branch repeatedly into thousands of microscopic twigs called <strong>bronchioles</strong>.</li></ol>",
        "key_takeaways": [
            "Air travels from nostrils → nasal cavity → pharynx → larynx → trachea → bronchi → bronchioles → alveoli.",
            "Nasal hairs and mucus filter, warm, and humidify incoming air, protecting lung tissue from dust and cold.",
            "The epiglottis prevents food and liquids from entering the respiratory windpipe during swallowing.",
            "C-shaped rings of cartilage keep the trachea open and prevent it from collapsing under negative pressure."
        ],
        "checkpoints": [
            {
                "question": "Why is the human trachea (windpipe) reinforced along its entire length with C-shaped rings of cartilage?",
                "options": [
                    "To prevent the windpipe from collapsing shut when air pressure drops during inhalation",
                    "To help digest food as it passes down to the stomach",
                    "To make the neck look wider to scare predators",
                    "To store extra oxygen reserves for running"
                ],
                "correct": 0,
                "explanation": "During inhalation, negative pressure is generated inside the airway. Stiff cartilage rings maintain an open lumen, preventing the trachea from collapsing closed."
            },
            {
                "question": "What is the function of the tiny leaf-like cartilage flap called the epiglottis located above the larynx?",
                "options": [
                    "It closes over the windpipe during swallowing to prevent food from entering the lungs",
                    "It filters dust out of nasal air",
                    "It cools the blood flowing to the heart",
                    "It vibrates to produce vocal sound"
                ],
                "correct": 0,
                "explanation": "The epiglottis acts like a safety trapdoor, tilting backward during swallowing to seal off the larynx and trachea, directing food safely into the oesophagus."
            }
        ],
        "simulator_type": "human_respiratory_tract_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 13: Breathing Mechanics: Diaphragm & Pressure Laws
    # -------------------------------------------------------------
    {
        "id": 13,
        "type": "theory_slide",
        "title": "Breathing Mechanics: Inhalation & Exhalation",
        "subtitle": "Section 9.2.1 • Boyle's Pressure-Volume Physics of the Thoracic Cage",
        "formula": "Inhalation: Diaphragm Flattens + Ribs Rise → Volume Expands → Pressure Drops → Air Enters",
        "content": "<p>Lungs do not possess muscles of their own; they cannot contract or expand by themselves! Instead, breathing is driven by pressure differences created by two muscle groups enclosing the thoracic (chest) cavity: the dome-shaped muscular <strong>diaphragm</strong> at the floor of the chest, and the <strong>intercostal muscles</strong> between the ribs.</p><p><strong>1. Inhalation (Breathing In):</strong></p><ul><li>The diaphragm contracts and flattens downward.</li><li>The rib muscles contract, pulling the ribs upward and outward.</li><li>These combined movements expand the volume of the chest cavity.</li><li>According to physics, when volume increases, <em>air pressure inside the chest drops below outside atmospheric pressure</em>.</li><li>Atmospheric air rushes through the nostrils into the lungs like air filling an expanding syringe!</li></ul><p><strong>2. Exhalation (Breathing Out):</strong></p><ul><li>The diaphragm relaxes and arches upward into its resting dome shape.</li><li>The rib muscles relax, allowing the ribs to move down and inward.</li><li>The chest cavity volume decreases, raising the internal air pressure above atmospheric pressure.</li><li>Air is squeezed out of the lungs into the environment.</li></ul><p>A simple laboratory model using a bell jar, two rubber balloons (lungs), and a flexible rubber sheet at the bottom (diaphragm) demonstrates this pressure mechanism flawlessly.</p>",
        "key_takeaways": [
            "Lungs cannot move independently; breathing is driven by changes in chest cavity volume and air pressure.",
            "Inhalation: diaphragm flattens, ribs lift, chest volume increases, internal pressure drops, and air rushes in.",
            "Exhalation: diaphragm arches up, ribs lower, chest volume decreases, internal pressure rises, and air is pushed out.",
            "The bell-jar model proves that expanding cavity volume creates negative pressure that inflates the lungs."
        ],
        "checkpoints": [
            {
                "question": "What happens to the muscular diaphragm during active inhalation (breathing in)?",
                "options": [
                    "It contracts and moves downward, becoming flatter to increase chest volume",
                    "It relaxes and bulges upward into a tall dome",
                    "It stops moving completely and turns into bone",
                    "It spins around in a circle to stir up air"
                ],
                "correct": 0,
                "explanation": "During inhalation, the diaphragm contracts and flattens downward while ribs move upward, expanding the chest cavity and pulling air into the lungs."
            },
            {
                "question": "In a bell-jar lung demonstration model, what happens to the internal balloons when the bottom rubber sheet (diaphragm) is pulled downward?",
                "options": [
                    "The balloons inflate with air because volume increases and internal pressure drops",
                    "The balloons burst and catch fire",
                    "The balloons deflate completely and shrivel up",
                    "Nothing happens because air cannot move"
                ],
                "correct": 0,
                "explanation": "Pulling the rubber sheet downward increases the internal volume of the jar, lowering the pressure inside. Outside air rushes in through the tube to inflate the balloons."
            }
        ],
        "simulator_type": "breathing_diaphragm_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 14: Gas Exchange at Alveoli: The Microscopic Frontier
    # -------------------------------------------------------------
    {
        "id": 14,
        "type": "theory_slide",
        "title": "Alveolar Gas Exchange: Oxygen & Hemoglobin",
        "subtitle": "Section 9.2.1 • 300 Million Balloon Sacs & Capillary Diffusion",
        "formula": "Hb (Hemoglobin) + 4O₂ ⇌ Hb(O₂)₄ (Oxyhemoglobin in Pulmonary Capillaries)",
        "content": "<p>Deep inside the human lungs, each microscopic bronchiole terminates in clusters of tiny, hollow balloon-like air sacs called <strong>alveoli</strong> (singular: <em>alveolus</em>). An adult human pair of lungs houses an astronomical <strong>300 to 500 million alveoli</strong>, providing a staggering surface area of roughly <strong>80 square metres</strong>—nearly 40 times the surface area of our external skin!</p><p><strong>The Physics of Alveolar Gas Exchange:</strong></p><ul><li><strong>Ultra-Thin Diffusion Boundary:</strong> The wall of each alveolus is only one squamous epithelial cell thick. Each alveolus is wrapped in a dense web of microscopic pulmonary blood capillaries, whose walls are also only one cell thick!</li><li><strong>Oxygen Uptake:</strong> Fresh inhaled air in the alveoli has a high concentration of oxygen. Oxygen readily dissolves in the thin moisture film on the alveolar wall and diffuses across the micro-thin barrier into blood capillaries.</li><li><strong>Hemoglobin Binding:</strong> Inside red blood cells, iron-rich protein molecules called <strong>hemoglobin</strong> bind with oxygen to form bright crimson <strong>oxyhemoglobin</strong>, which circulates to every body tissue.</li><li><strong>Carbon Dioxide Release:</strong> Simultaneously, cellular carbon dioxide waste dissolved in blood plasma diffuses down its concentration gradient in the opposite direction—from blood into the alveolus—to be exhaled.</li></ul>",
        "key_takeaways": [
            "Alveoli are microscopic balloon-like sacs (300+ million) where gas exchange occurs.",
            "The total alveolar surface area exceeds 80 m², with ultra-thin walls only one cell thick.",
            "Oxygen diffuses from alveoli into capillary red blood cells and binds with iron-rich hemoglobin to form oxyhemoglobin.",
            "Carbon dioxide diffuses from blood into alveoli to be expelled during exhalation."
        ],
        "checkpoints": [
            {
                "question": "What is the primary iron-rich respiratory pigment in human red blood cells that binds and transports oxygen?",
                "options": [
                    "Hemoglobin",
                    "Chlorophyll",
                    "Insulin",
                    "Pepsin"
                ],
                "correct": 0,
                "explanation": "Hemoglobin is the specialized iron-containing protein in red blood cells that binds oxygen in lung capillaries to form oxyhemoglobin, delivering O₂ throughout the body."
            },
            {
                "question": "Why can oxygen and carbon dioxide diffuse so rapidly between alveolar air and capillary blood in human lungs?",
                "options": [
                    "The combined diffusion barrier is only two cells thick and the total alveolar surface area exceeds 80 square metres",
                    "The lungs use high-voltage electrical shocks to force gases across",
                    "Blood flows backwards during every breath",
                    "Alveoli have large muscular valves that swallow gas molecules"
                ],
                "correct": 0,
                "explanation": "The barrier between alveolar air and capillary blood is exceptionally thin (sub-micron, just two single-cell layers), and the massive surface area (80 m²) allows instantaneous gas diffusion."
            }
        ],
        "simulator_type": "alveoli_gas_exchange_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 15: Diversity of Respiration in Animals: Gills, Skin & Spiracles
    # -------------------------------------------------------------
    {
        "id": 15,
        "type": "theory_slide",
        "title": "Breathing Diversity: Gills, Moist Skin & Tracheal Tubes",
        "subtitle": "Section 9.2.2 • Specialized Evolutionary Adaptations Across Animal Phyla",
        "formula": "Fish: Gills + Operculum • Earthworm: Moist Cutaneous Skin • Insect: Spiracles + Tracheae",
        "content": "<p>Humans and mammals breathe using lungs, but animals inhabit diverse environments—deep oceans, moist underground burrows, arid deserts, and mountain peaks. Over evolutionary history, animals have developed distinct respiratory organs tailored to extract oxygen from their surroundings:</p><p><strong>1. Gills in Fish (Aquatic Respiration):</strong><br>Water contains less than 1% dissolved oxygen by volume (compared to 21% in atmospheric air). Fish take water in through their mouth and pump it over feathery respiratory organs called <strong>gills</strong>, protected by the bony <strong>operculum</strong>. Each gill consists of thin arches fringed with thousands of blood-rich lamellae. As water sweeps past, oxygen diffuses into blood vessels while carbon dioxide exits into the water.</p><p><strong>2. Moist Skin in Earthworms (Cutaneous Respiration):</strong><br>An earthworm has neither lungs nor gills! It absorbs oxygen directly through its thin, moist skin into an underlying capillary network. Glands secrete mucus to keep the skin slimy; <em>if an earthworm's skin dries out in the sun, it suffocates</em> because oxygen cannot dissolve to diffuse inward.</p><p><strong>3. Spiracles & Tracheal Tubes in Insects (Tracheal Respiration):</strong><br>Insects like cockroaches and grasshoppers do not use blood to carry oxygen! Instead, air enters small lateral pores called <strong>spiracles</strong> on the sides of their body, leading into a network of branching air pipes called <strong>tracheae</strong>. These tubes deliver gaseous oxygen directly to every individual cell.</p>",
        "key_takeaways": [
            "Fish extract dissolved oxygen from water using feathery, vascularized gills beneath the operculum.",
            "Earthworms breathe through their thin, moist, mucus-covered skin directly into dermal capillaries.",
            "Insects breathe through lateral body pores (spiracles) connected to a branching internal network of tracheal tubes.",
            "Insect blood (hemolymph) does not carry oxygen; tracheae deliver oxygen directly to tissues."
        ],
        "checkpoints": [
            {
                "question": "How does an earthworm absorb oxygen from its underground soil environment?",
                "options": [
                    "Through its thin, moist, mucus-covered skin directly into blood capillaries",
                    "Through a pair of large lungs in its chest",
                    "Through bony gills located behind its ears",
                    "Through a hard beak like a bird"
                ],
                "correct": 0,
                "explanation": "Earthworms practice cutaneous respiration: atmospheric oxygen dissolves in the moist mucus coating their outer skin and diffuses directly into blood capillaries."
            },
            {
                "question": "What is the function of the tiny lateral openings called spiracles found along the body walls of insects like cockroaches?",
                "options": [
                    "They allow atmospheric air to enter the internal branching network of tracheal tubes",
                    "They squirt poison to deter predators",
                    "They absorb water from muddy soil",
                    "They are ears used to hear sounds"
                ],
                "correct": 0,
                "explanation": "Spiracles are the external breathing pores of insects. Air passes through spiracles into branching tracheal tubes that transport oxygen directly to living cells."
            }
        ],
        "simulator_type": "animal_respiration_diversity_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 16: Amphibian Adaptations & Ancient Indian Heritage
    # -------------------------------------------------------------
    {
        "id": 16,
        "type": "theory_slide",
        "title": "Amphibian Versatility & Ancient Indian Heritage",
        "subtitle": "Section 9.2.2 • Frog Triple-Breathing & Ayurveda's Jatharagni & Prana",
        "formula": "Frog: Aquatic = Cutaneous Skin • Terrestrial = Buccal Pumping + Pulmonary Lungs",
        "content": "<p>Amphibians like frogs lead dual lives—beginning life in water and transitioning to land—and have evolved the most versatile respiratory toolkit in the animal kingdom:</p><ul><li><strong>Tadpole Stage:</strong> Young aquatic tadpoles swim with a tail and breathe exclusively through feathery external and internal <strong>gills</strong>, exactly like fish.</li><li><strong>Adult Underwater:</strong> When diving in ponds or hibernating in winter mud (winter sleep / aestivation), adult frogs breathe entirely through their thin, moist, highly vascularized <strong>skin</strong> (cutaneous respiration).</li><li><strong>Adult on Land:</strong> On land, adult frogs breathe using simple sac-like <strong>lungs</strong> (pulmonary respiration) assisted by rhythmic pumping of the throat floor in the <strong>buccal cavity</strong>.</li></ul><p><strong>Ancient Indian Medical Heritage (Ayurveda):</strong><br>Centuries before modern physiology, ancient Indian physicians <strong>Maharishi Sushruta</strong> (Father of Surgery, ~600 BCE) and <strong>Maharishi Charaka</strong> (~300 BCE) documented foundational insights into animal life processes:</p><ul><li><strong>Jatharagni (The Digestive Fire):</strong> Described as the central metabolic flame in the stomach and duodenum that cooks and transforms ingested food (*Ahara*) into nutrient essence (*Ahararasa*) to nourish the seven bodily tissues (*Sapta Dhatus*).</li><li><strong>Prana Vayu (The Vital Breath):</strong> Recognized as the supreme life force flowing through the respiratory channels to energize the heart and brain, prefiguring our understanding of cellular respiration and oxygen transport!</li></ul>",
        "key_takeaways": [
            "Frogs possess triple breathing mechanisms: gills as tadpoles, moist skin underwater, and lungs + buccal cavity on land.",
            "During hibernation in mud, adult frogs survive solely through cutaneous skin respiration.",
            "Ancient Indian Ayurveda recognized 'Jatharagni' as the internal metabolic fire transforming food into nutrient essence.",
            "'Prana Vayu' was identified in ancient texts as the vital respiratory energy that sustains life and powers body tissues."
        ],
        "checkpoints": [
            {
                "question": "How does an adult frog breathe while submerged underwater or hibernating deep in winter mud?",
                "options": [
                    "Through its thin, moist skin (cutaneous respiration)",
                    "Using its lungs like a scuba diver",
                    "By drinking vast amounts of water into its liver",
                    "By holding its breath for four months without any oxygen"
                ],
                "correct": 0,
                "explanation": "Underwater, a frog relies exclusively on cutaneous respiration: dissolved oxygen in water diffuses directly across its moist, vascularized skin into the bloodstream."
            },
            {
                "question": "In ancient Indian Ayurvedic physiology (Charaka and Sushruta Samhitas), what is 'Jatharagni'?",
                "options": [
                    "The vital internal digestive fire responsible for breaking down food and nourishing body tissues",
                    "A medicinal plant used to clean teeth",
                    "A surgical knife used to operate on eyes",
                    "The morning dew found on lotus leaves"
                ],
                "correct": 0,
                "explanation": "In Ayurveda, 'Jatharagni' represents the metabolic digestive fire centered in the stomach and intestine that converts food into absorbable nutrient essence to build the body's tissues."
            }
        ],
        "simulator_type": "frog_metamorphosis_ayurveda_sim"
    },

    # -------------------------------------------------------------
    # SLIDE 17: Mastery Assessment Challenge 1 (Questions 1 to 10)
    # -------------------------------------------------------------
    {
        "id": 17,
        "type": "quiz_slide",
        "title": "Mastery Challenge I: Nutrition, Mouth & Stomach Digestion",
        "subtitle": "Diagnostic Inquiries 1 to 10 • Step-by-Step Pop-up Solutions",
        "questions": [
            {
                "question": "Which of the following is the final digested product of dietary carbohydrates?",
                "options": ["Glucose", "Amino acids", "Fatty acids", "Glycerol"],
                "correct": 0,
                "solution": "Carbohydrates are complex polysaccharide chains. Digestion by amylase and intestinal enzymes breaks them down into simple monosaccharide sugars, predominantly glucose."
            },
            {
                "question": "Which enzyme present in human saliva initiates the chemical digestion of starch in the mouth?",
                "options": ["Salivary amylase (ptyalin)", "Pepsin", "Lipase", "Trypsin"],
                "correct": 0,
                "solution": "Salivary amylase (also known as ptyalin) is secreted by salivary glands in the mouth and initiates the cleavage of complex starch into simpler sugars like maltose."
            },
            {
                "question": "What is the primary role of the rhythmic wave-like muscular contractions called peristalsis in the oesophagus?",
                "options": [
                    "To push the food bolus downward toward the stomach regardless of body orientation",
                    "To chew the food into smaller particles",
                    "To secrete hydrochloric acid into the mouth",
                    "To absorb glucose directly into the heart"
                ],
                "correct": 0,
                "solution": "Peristalsis consists of circular muscle contractions behind the bolus and longitudinal relaxation ahead, propelling food toward the stomach even in zero gravity."
            },
            {
                "question": "Which acid is secreted by the gastric glands in the human stomach, and what is its pH range?",
                "options": [
                    "Hydrochloric acid (HCl), pH 1.5 to 2.0",
                    "Sulfuric acid (H₂SO₄), pH 7.0",
                    "Citric acid, pH 9.5",
                    "Acetic acid, pH 12.0"
                ],
                "correct": 0,
                "solution": "The stomach lining contains parietal cells that secrete strong hydrochloric acid (HCl), generating an intensely acidic environment with a pH between 1.5 and 2.0."
            },
            {
                "question": "Why does the inner lining of the stomach not get corroded by its own hydrochloric acid and pepsin?",
                "options": [
                    "It is coated with a thick protective layer of alkaline mucus",
                    "The stomach is made of solid stainless steel",
                    "The acid is neutralized immediately by cold drinking water",
                    "The stomach contains no nerves or living cells"
                ],
                "correct": 0,
                "solution": "Mucous cells in the gastric mucosa secrete a thick, bicarbonate-rich alkaline mucus gel that forms a physical and chemical barrier against acid and proteolytic digestion."
            },
            {
                "question": "Which historical scientist observed the living human stomach through an accidental gunshot fistula in Alexis St. Martin?",
                "options": [
                    "Dr. William Beaumont",
                    "Sir Isaac Newton",
                    "Antonie van Leeuwenhoek",
                    "Edward Jenner"
                ],
                "correct": 0,
                "solution": "In 1822, American army surgeon Dr. William Beaumont conducted pioneering physiological experiments through the healed stomach fistula of patient Alexis St. Martin."
            },
            {
                "question": "How many total permanent teeth are found in a healthy adult human mouth, and how many are molars?",
                "options": [
                    "32 total teeth, including 12 molars (with 4 wisdom teeth)",
                    "20 total teeth, including 4 molars",
                    "40 total teeth, including 20 molars",
                    "28 total teeth, with zero molars"
                ],
                "correct": 0,
                "solution": "An adult human has 32 permanent teeth: 8 incisors, 4 canines, 8 premolars, and 12 molars (which include the four wisdom teeth)."
            },
            {
                "question": "What is the semi-liquid acidic mass of partially digested food formed in the stomach called?",
                "options": ["Chyme", "Bolus", "Bile", "Roughage"],
                "correct": 0,
                "solution": "Food swallowed from the mouth is a bolus; once it has been churned and mixed with gastric acid and enzymes in the stomach, it becomes a semi-liquid mixture called chyme."
            },
            {
                "question": "Which enzyme in the stomach initiates the breakdown of proteins into smaller peptides?",
                "options": ["Pepsin", "Salivary amylase", "Lipase", "Cellulase"],
                "correct": 0,
                "solution": "Pepsinogen secreted by gastric chief cells is activated by hydrochloric acid into pepsin, an endopeptidase that hydrolyzes complex protein bonds into peptides."
            },
            {
                "question": "Which teeth in the human mouth are shaped with broad, flat, cusped surfaces specifically to crush and grind food?",
                "options": [
                    "Premolars and Molars",
                    "Incisors",
                    "Canines",
                    "Wisdom incisors"
                ],
                "correct": 0,
                "solution": "Premolars and molars have broad chewing surfaces with ridges and cusps, engineered specifically for crushing and grinding tough food particles."
            }
        ]
    },

    # -------------------------------------------------------------
    # SLIDE 18: Mastery Assessment Challenge 2 (Questions 11 to 20)
    # -------------------------------------------------------------
    {
        "id": 18,
        "type": "quiz_slide",
        "title": "Mastery Challenge II: Intestinal Secretions, Absorption & Animal Adaptations",
        "subtitle": "Diagnostic Inquiries 11 to 20 • Step-by-Step Pop-up Solutions",
        "questions": [
            {
                "question": "Where is bile synthesized in the human body, and where is it stored prior to release?",
                "options": [
                    "Synthesized by the Liver; stored in the Gall Bladder",
                    "Synthesized by the Pancreas; stored in the Spleen",
                    "Synthesized by the Stomach; stored in the Colon",
                    "Synthesized by the Kidneys; stored in the Bladder"
                ],
                "correct": 0,
                "solution": "Bile is continuously produced by liver hepatocytes and flows through the hepatic duct to be stored and concentrated in the gall bladder."
            },
            {
                "question": "What is the primary action of bile on dietary fats in the small intestine?",
                "options": [
                    "Emulsification: breaking large fat droplets into microscopic micelles to increase surface area",
                    "Converting fats directly into amino acids",
                    "Solidifying fats into hard kidney stones",
                    "Freezing fats so they cannot be absorbed"
                ],
                "correct": 0,
                "solution": "Bile salts act like biological detergents. Through emulsification, they disperse large lipid globules into tiny micelles, dramatically increasing the surface area for pancreatic lipase."
            },
            {
                "question": "What are the millions of microscopic finger-like projections on the small intestine lining called?",
                "options": ["Villi", "Alveoli", "Spiracles", "Cilia"],
                "correct": 0,
                "solution": "The small intestine wall is covered with millions of finger-like projections called villi (and microvilli), which expand the absorptive area to over 250 square metres."
            },
            {
                "question": "Which vessel inside an intestinal villus absorbs digested fatty acids and glycerol?",
                "options": ["Lacteal (lymph vessel)", "Blood capillary", "Artery", "Vein"],
                "correct": 0,
                "solution": "Water-soluble glucose and amino acids enter the blood capillaries, whereas lipid digestion products (fatty acids and glycerol) are absorbed into the central lymphatic vessel called the lacteal."
            },
            {
                "question": "What is the primary role of the human large intestine?",
                "options": [
                    "Absorption of water and mineral salts from undigested residue to form semi-solid faeces",
                    "Digestion of protein into amino acids",
                    "Secretion of bile and pancreatic enzymes",
                    "Filtering oxygen from swallowed air"
                ],
                "correct": 0,
                "solution": "The large intestine does not secrete digestive enzymes; its vital duty is the reabsorption of water and dissolved salts, consolidating waste into semi-solid stool."
            },
            {
                "question": "Which chamber of a cow's four-chambered stomach is considered the 'true stomach' where gastric juices digest food?",
                "options": ["Abomasum", "Rumen", "Reticulum", "Omasum"],
                "correct": 0,
                "solution": "The abomasum is the fourth chamber and the true glandular stomach of ruminants, secreting hydrochloric acid and proteases just like a human stomach."
            },
            {
                "question": "What allows ruminants like cows and buffaloes to digest the cellulose in grass that humans cannot digest?",
                "options": [
                    "Symbiotic anaerobic bacteria and protozoa in the rumen that ferment cellulose",
                    "Heavy iron teeth that melt grass into sugar",
                    "Drinking boiling water from ponds",
                    "A special venom gland in their horns"
                ],
                "correct": 0,
                "solution": "Ruminants host billions of specialized anaerobic microorganisms in their rumen that produce cellulase enzymes, fermenting cellulose into absorbable fatty acids."
            },
            {
                "question": "Why do seed-eating birds like hens and pigeons swallow small pebbles and grit into their gizzard?",
                "options": [
                    "To mechanically grind hard seeds and grains inside the muscular gizzard, compensating for having no teeth",
                    "To build calcium for eggshells in the liver",
                    "To quench their thirst during summer",
                    "Because they cannot see what they are eating"
                ],
                "correct": 0,
                "solution": "Birds lack teeth. Swallowed stones (gastroliths) remain in the thick muscular gizzard, where vigorous contractions grind hard grains into a digestible pulp."
            },
            {
                "question": "What is the temporary food storage and softening pouch located along a bird's oesophagus called?",
                "options": ["Crop", "Gizzard", "Rumen", "Proventriculus"],
                "correct": 0,
                "solution": "The crop is an expanded muscular pouch along the bird's gullet used to store food quickly and soften it with secretions before it enters the stomach."
            },
            {
                "question": "What is the five-stage sequence representing the complete nutrition cycle in animals?",
                "options": [
                    "Ingestion → Digestion → Absorption → Assimilation → Egestion",
                    "Egestion → Ingestion → Assimilation → Digestion → Absorption",
                    "Absorption → Ingestion → Digestion → Egestion → Assimilation",
                    "Digestion → Ingestion → Absorption → Egestion → Respiration"
                ],
                "correct": 0,
                "solution": "The five universal stages of animal nutrition are: Ingestion (taking food in), Digestion (breakdown), Absorption (uptake into blood), Assimilation (cellular utilization), and Egestion (expulsion of unabsorbed waste)."
            }
        ]
    },

    # -------------------------------------------------------------
    # SLIDE 19: Mastery Assessment Challenge 3 (Questions 21 to 30)
    # -------------------------------------------------------------
    {
        "id": 19,
        "type": "quiz_slide",
        "title": "Mastery Challenge III: Respiration Chemistry & Human Breathing Mechanics",
        "subtitle": "Diagnostic Inquiries 21 to 30 • Step-by-Step Pop-up Solutions",
        "questions": [
            {
                "question": "What is the balanced summary word equation for aerobic cellular respiration inside animal cells?",
                "options": [
                    "Glucose + Oxygen → Carbon Dioxide + Water + Usable Energy (ATP)",
                    "Carbon Dioxide + Water + Sunlight → Glucose + Oxygen",
                    "Glucose + Carbon Dioxide → Oxygen + Alcohol",
                    "Protein + Water → Hydrochloric Acid + Energy"
                ],
                "correct": 0,
                "solution": "Cellular respiration oxidizes glucose using oxygen: C₆H₁₂O₆ + 6O₂ → 6CO₂ + 6H₂O + chemical energy stored in ATP molecules."
            },
            {
                "question": "In which cellular organelle does the majority of aerobic energy release occur during respiration?",
                "options": ["Mitochondria", "Ribosome", "Chloroplast", "Vacuole"],
                "correct": 0,
                "solution": "Mitochondria are known as the 'powerhouses of the cell' because the enzymatic Krebs cycle and oxidative phosphorylation take place within their membranes."
            },
            {
                "question": "What physical change occurs in the human chest cavity during active inhalation (breathing in)?",
                "options": [
                    "The diaphragm moves downward, ribs lift outward, cavity volume increases, and internal air pressure drops",
                    "The diaphragm moves upward, ribs move down, and air is pushed out",
                    "The chest cavity fills with liquid bile",
                    "The lungs shrink to zero volume"
                ],
                "correct": 0,
                "solution": "During inhalation, contraction of the diaphragm (moving downward) and external intercostals (lifting ribs) increases thoracic volume, dropping pressure below atmospheric level so air rushes in."
            },
            {
                "question": "Why is breathing through the nose significantly healthier than breathing through the mouth?",
                "options": [
                    "Nasal hairs and mucus filter dust and microbes, while blood vessels warm and humidify the air",
                    "The mouth can only breathe carbon dioxide",
                    "The nose contains teeth that kill bacteria",
                    "Nose breathing stops people from talking"
                ],
                "correct": 0,
                "solution": "The nasal cavity is lined with ciliated epithelial cells, sticky mucus to trap airborne contaminants, and a dense vascular plexus that warms and humidifies air to body temperature."
            },
            {
                "question": "What structure keeps the human trachea (windpipe) from collapsing when internal air pressure falls?",
                "options": [
                    "C-shaped rings of cartilage",
                    "Bones called ribs",
                    "Layers of fat",
                    "Strands of hair"
                ],
                "correct": 0,
                "solution": "The trachea is reinforced with 16 to 20 C-shaped cartilaginous rings that keep the airway lumen permanently open during changes in intratracheal pressure."
            },
            {
                "question": "What is the small flap of cartilage that covers the entrance to the trachea during swallowing to prevent choking?",
                "options": ["Epiglottis", "Uvula", "Larynx", "Pharynx"],
                "correct": 0,
                "solution": "The epiglottis folds downward over the glottis (the opening of the larynx) during swallowing, guiding food safely into the oesophagus and preventing aspiration into the airway."
            },
            {
                "question": "What is the normal breathing rate of an adult human at rest?",
                "options": [
                    "15 to 18 breaths per minute",
                    "60 to 72 breaths per minute",
                    "1 to 2 breaths per minute",
                    "120 to 150 breaths per minute"
                ],
                "correct": 0,
                "solution": "A healthy adult at rest breathes approximately 15 to 18 times per minute (each breath consisting of one inhalation and one exhalation)."
            },
            {
                "question": "In the classic bell-jar demonstration model of human breathing, what component represents the muscular diaphragm?",
                "options": [
                    "The thin rubber sheet tied across the open bottom of the jar",
                    "The glass bell-jar itself",
                    "The Y-shaped glass tube",
                    "The two small rubber balloons inside"
                ],
                "correct": 0,
                "solution": "In the bell-jar model: the glass jar represents the chest cavity, the Y-tube represents the trachea and bronchi, the balloons represent the lungs, and the bottom rubber sheet represents the diaphragm."
            },
            {
                "question": "What percentage of oxygen is present in normal inhaled atmospheric air compared to exhaled air in humans?",
                "options": [
                    "Inhaled: ~21% oxygen; Exhaled: ~16.4% oxygen",
                    "Inhaled: 100% oxygen; Exhaled: 0% oxygen",
                    "Inhaled: 0.04% oxygen; Exhaled: 21% oxygen",
                    "Inhaled: ~78% oxygen; Exhaled: ~21% oxygen"
                ],
                "correct": 0,
                "solution": "Inhaled air contains about 21% oxygen and 0.04% carbon dioxide. Exhaled air contains about 16.4% oxygen and 4.4% carbon dioxide, showing that oxygen was extracted and CO₂ was added."
            },
            {
                "question": "How does lime water (calcium hydroxide solution) behave when someone exhales breath through it using a straw?",
                "options": [
                    "It turns milky white due to the formation of insoluble calcium carbonate precipitate by carbon dioxide",
                    "It turns bright blue like ink",
                    "It freezes into solid ice",
                    "It remains completely crystal clear with no change"
                ],
                "correct": 0,
                "solution": "Exhaled air contains carbon dioxide, which reacts with clear lime water [Ca(OH)₂] to form a white precipitate of insoluble calcium carbonate (CaCO₃), turning the solution milky."
            }
        ]
    },

    # -------------------------------------------------------------
    # SLIDE 20: Mastery Assessment Challenge 4 (Questions 31 to 40)
    # -------------------------------------------------------------
    {
        "id": 20,
        "type": "quiz_slide",
        "title": "Mastery Challenge IV: Gas Exchange, Animal Diversity & Heritage",
        "subtitle": "Diagnostic Inquiries 31 to 40 • Step-by-Step Pop-up Solutions",
        "questions": [
            {
                "question": "In which microscopic lung structures does gas exchange between air and blood capillaries take place?",
                "options": ["Alveoli", "Bronchi", "Nostrils", "Trachea"],
                "correct": 0,
                "solution": "Alveoli are tiny, thin-walled air sacs (300+ million in humans) enveloped in capillaries, where oxygen diffuses into blood and carbon dioxide diffuses out."
            },
            {
                "question": "What is the name of the iron-containing protein in human red blood cells that transports oxygen to body tissues?",
                "options": ["Hemoglobin", "Chlorophyll", "Keratin", "Collagen"],
                "correct": 0,
                "solution": "Hemoglobin is the red, iron-rich protein in red blood cells that reversibly binds oxygen in pulmonary capillaries to form oxyhemoglobin, which is transported to all tissues."
            },
            {
                "question": "How does a fish breathe underwater to extract dissolved oxygen from water?",
                "options": [
                    "Water taken into the mouth is forced over vascular gill filaments beneath the operculum",
                    "It swims to the surface to swallow bubbles into lungs",
                    "It breathes through nostrils on the tip of its tail",
                    "It splits water into hydrogen and oxygen using stomach acid"
                ],
                "correct": 0,
                "solution": "Fish take water into the mouth and pump it across feathery, capillary-rich gill filaments. Dissolved oxygen diffuses across the thin gill membranes into the bloodstream."
            },
            {
                "question": "How does an earthworm exchange respiratory gases with its soil environment?",
                "options": [
                    "Through its thin, moist skin covered in mucus (cutaneous respiration)",
                    "Through large spiracles on its head",
                    "Using a single air lung in its belly",
                    "Through feathery gills inside its mouth"
                ],
                "correct": 0,
                "solution": "Earthworms have no specialized breathing organs. Atmospheric oxygen dissolves in the moist mucus on their skin and diffuses directly into the superficial blood capillary network."
            },
            {
                "question": "What is the respiratory system of insects like cockroaches and grasshoppers composed of?",
                "options": [
                    "External body pores called spiracles connected to an internal branching network of tracheal tubes",
                    "A pair of moist lungs surrounded by ribs",
                    "Feathery gills in their legs",
                    "Diffusion through solid shell scales"
                ],
                "correct": 0,
                "solution": "Insects have lateral openings called spiracles that connect to an extensive network of air-filled tracheal tubes, delivering oxygen gas directly to cells without using blood as a carrier."
            },
            {
                "question": "How does an adult frog breathe when submerged underwater at the bottom of a pond?",
                "options": [
                    "Exclusively through its thin, moist skin (cutaneous respiration)",
                    "Using its lungs like land mammals",
                    "Using gills located on its neck",
                    "By storing air in its bladder"
                ],
                "correct": 0,
                "solution": "When submerged in water or hibernating in winter mud, adult frogs rely entirely on cutaneous respiration, absorbing dissolved oxygen directly through their thin, vascularized, moist skin."
            },
            {
                "question": "What respiratory organ do young frog tadpoles use to breathe before undergoing metamorphosis into adult frogs?",
                "options": ["Gills", "Lungs", "Spiracles", "Tracheae"],
                "correct": 0,
                "solution": "Young aquatic frog tadpoles possess feathery gills (both external and internal) to extract dissolved oxygen from water, exactly like fish."
            },
            {
                "question": "In ancient Indian Ayurvedic medicine (Charaka and Sushruta Samhitas), what is 'Jatharagni'?",
                "options": [
                    "The central digestive metabolic fire in the stomach that cooks food into nutrient essence (Ahararasa)",
                    "A poisonous plant found in forests",
                    "A type of surgical incision on the arm",
                    "A breathing meditation practiced at sunrise"
                ],
                "correct": 0,
                "solution": "In Ayurvedic classics, 'Jatharagni' is the digestive metabolic flame located in the stomach and duodenum that breaks down food into nutrient essence (Ahararasa) to nourish the body's seven tissues (Sapta Dhatus)."
            },
            {
                "question": "What does ancient Indian physiological science refer to as 'Prana Vayu'?",
                "options": [
                    "The vital life breath flowing through respiratory pathways to sustain consciousness and vitality",
                    "Water vapor exhaled during running",
                    "The smoke produced by burning incense",
                    "The breeze that blows from the ocean"
                ],
                "correct": 0,
                "solution": "In ancient Indian medicine, 'Prana Vayu' represents the vital life energy and respiratory breath taken in through inhalation, sustaining cardiac and neural function."
            },
            {
                "question": "If an earthworm's skin is coated with dry talcum powder and kept in dry air, why does it quickly die?",
                "options": [
                    "It suffocates because oxygen cannot dissolve and diffuse through dry skin into its blood vessels",
                    "It becomes too heavy to crawl",
                    "The powder dissolves its heart",
                    "It falls into a deep sleep and starves"
                ],
                "correct": 0,
                "solution": "Earthworms require a layer of moisture on their skin to dissolve atmospheric oxygen. If the skin dries out, oxygen cannot dissolve to diffuse across the cuticle, leading to asphyxiation."
            }
        ]
    }
]

# Verify zero raw LaTeX across all slides
for slide in SLIDES_DATA:
    sanitize(slide.get("title", ""))
    sanitize(slide.get("subtitle", ""))
    sanitize(slide.get("content", ""))
    sanitize(slide.get("formula", ""))
    for t in slide.get("key_takeaways", []):
        sanitize(t)
    for cp in slide.get("checkpoints", []):
        sanitize(cp.get("question", ""))
        sanitize(cp.get("explanation", ""))
        for opt in cp.get("options", []):
            sanitize(opt)
    for q in slide.get("questions", []):
        sanitize(q.get("question", ""))
        sanitize(q.get("solution", ""))
        for opt in q.get("options", []):
            sanitize(opt)

with open('.agents/class7_science_life_processes_data.py', 'w', encoding='utf-8') as f:
    f.write('# -*- coding: utf-8 -*-\n"""Generated Slide Data for Class 7 Science Chapter 9: Life Processes in Animals"""\n\nSLIDES_DATA = ' + json.dumps(SLIDES_DATA, ensure_ascii=False, indent=2) + '\n')

print(f"Generated .agents/class7_science_life_processes_data.py with {len(SLIDES_DATA)} slides cleanly.")
