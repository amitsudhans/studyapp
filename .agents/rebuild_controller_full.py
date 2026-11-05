"""
Rebuild app/Http/Controllers/MultimediaController.php with complete NCERT Class 5 (Ch 1-8)
and NCERT Class 6 (Ch 1-12) reconstructed from session logs.
"""

import json
import subprocess
import sys

transcript_path = '/home/lead-programmer/.gemini/antigravity/brain/a82d247f-53b7-4d46-bc5c-c38667735695/.system_generated/logs/transcript_full.jsonl'

# 1. Read clean HEAD
content = subprocess.check_output(['git', 'show', 'HEAD:app/Http/Controllers/MultimediaController.php']).decode('utf-8')

# 2. Extract Class 6 chapters 2 to 12 from transcript
c6_blocks = []
with open(transcript_path) as f:
    for line in f:
        data = json.loads(line)
        calls = data.get('tool_calls', [])
        for c in calls:
            args = c.get('args', {})
            rep = args.get('Replacement', '')
            for ch in range(2, 13):
                needle = f"'chapter_num' => {ch},"
                if needle in rep and 'class6-science' in rep:
                    pos = rep.find(needle)
                    start = rep.rfind('[', 0, pos)
                    end_marker = "'4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',"
                    pos_em = rep.find(end_marker, pos)
                    if pos_em != -1:
                        end = rep.find('],', pos_em)
                        end = rep.find('],', end + 2)
                        block = rep[start:end+2].strip()
                        c6_blocks.append((ch, block))

# Deduplicate C6 blocks keeping latest
c6_dict = {}
for ch, b in c6_blocks:
    c6_dict[ch] = b

assert len(c6_dict) == 11, f"Expected 11 C6 chapters (2-12), got {len(c6_dict)}"

# 3. Extract Class 5 chapters 1 to 5 from step 21198
with open('/home/lead-programmer/.gemini/antigravity/brain/a82d247f-53b7-4d46-bc5c-c38667735695/.system_generated/steps/21198/output.txt') as f:
    text_21198 = f.read()

start_idx = text_21198.find("'ncert-science-class5' => [")
part_1_to_5 = text_21198[start_idx:].strip()
ch5_closing = """
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],"""

# 4. Extract Class 5 Chapter 6 from step 21020
with open(transcript_path) as f:
    for line in f:
        data = json.loads(line)
        if data.get('step_index') == 21020:
            rep_21020 = data['tool_calls'][0]['args']['Replacement']
            break

ch6_start = rep_21020.find("[\n                    'chapter_num' => 6")
ch6_end = rep_21020.find("            ],\n\n            // NCERT Science Class 6")
c5_ch6_code = rep_21020[ch6_start:ch6_end].strip()

# 5. Extract Class 5 Chapter 7 from step 21092
with open(transcript_path) as f:
    for line in f:
        data = json.loads(line)
        if data.get('step_index') == 21092:
            rep_21092 = data['tool_calls'][0]['args']['Replacement']
            break

ch7_start = rep_21092.find("[\n                    'chapter_num' => 7")
ch7_end = rep_21092.find("            ],\n\n            // NCERT Science Class 6")
c5_ch7_code = rep_21092[ch7_start:ch7_end].strip()

# 6. Chapter 8 of Class 5
c5_ch8_code = """[
                    'chapter_num' => 8,
                    'name' => 'Clothes - How Things are Made',
                    'has_multimedia' => true,
                    'media_key' => 'class5-science-clothes-how-things-are-made',
                    'media_title' => 'NCERT Class 5 Science • Chapter 8 • Clothes - How Things are Made Master Lab',
                    'media_url' => asset('animations/class5-science-clothes-how-things-are-made.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated laboratory for Grade 5 Science Chapter 8: Clothes - How Things are Made (Curiosity, NEP 2020) featuring comprehensive spoken classroom audio lectures in authentic Indian English narration, Web Speech API integration, and 16 bespoke SVG/HTML interactive simulators covering Nature\\'s Weavers (male baya weaverbird pouch nests woven from grass and palm ribbons with entrance tubes; spider silk webs), Warp and Weft (orthogonal crossing of vertical warp tana and horizontal weft bana; Activity 1 paper-strip weaving), Handloom Heritage (4,000+ years of Indian handlooms from the Indus Valley; Kanjeevaram mulberry silk with gold zari, Kashmiri Pashmina mountain goat down, and Odisha/Gujarat tie-dye Ikat), Charkha Spinning (drawing and twisting cotton fibres to create surface friction and tensile yarn; takli spindles, charkha wheels, and Mahatma Gandhi\\'s khadi self-reliance movement), Natural Fibres (plant cellulose from cotton seed hairs, flax/linen bast, jute, and bamboo vs animal protein from sheep wool crimp and silk fibroin), Silk Cocoon (Bombyx mori silkworm metamorphosis: tiny eggs, voracious mulberry caterpillars, figure-8 cocoon spinning yielding 1,000 m filaments, and adult silk moths), Synthetic Fibres (petroleum polymer synthetics nylon, polyester, and terylene; crucial flame safety rules and severe molten plastic burn hazards), Tailorbird Stitches (common tailorbird Orthotomus sutorius puncturing leaf margins with needle beaks and threading spider silk with rivet knots), Running Stitch (Activity 7 & 8: fundamental in-and-out running stitch kaccha tanka rhythm and piecing tailor scraps into functional mats), Chikankari Craft (historic Lucknow shadow-stitch Bakhiya worked on the reverse of translucent muslin with delicate front silhouettes), Kantha Quilts (traditional recycling craft of West Bengal and Odisha layering worn cotton sarees with thousands of rippling running stitches), Phulkari & Toda (Punjab floral silk floss darning from the reverse side of khaddar cloth vs Nilgiri Toda counted-thread red-and-black geometric buffalo horn shawls), Kashmiri & Khneng (Kashmir Chinar leaf crewel embroidery vs Meghalaya Mustoh village river fish-bone stitching on handspun Eri peace silk), Cloth Upcycling (Indian zero-waste circular life cycle: new garments, younger sibling hand-me-downs, Godhari quilts, cleaning mops, and soil compost), Fabric Testing (forensic flame burn tests identifying burning paper smell and soft ash for cotton, burning hair smell and crushable beads for wool/silk, and chemical smoke and hard plastic beads for synthetics), and Textile Guardians (honoring 20 km of spun thread in an adult shirt, learning basic mending, and supporting master handloom weavers), plus 32 in-slide checkpoints and 4 dedicated mastery quiz challenge slides with 40 questions and step-by-step solution modals.',
                    'topics' => [
                        'Nature\\'s Weavers: Baya Weaver Hanging Pouch Nests & Spider Web Geometry',
                        'Warp and Weft: Orthogonal Thread Crossing (Tana & Bana) & Activity 1 Paper Loom',
                        'Handloom Heritage: 4,000-Year Indian Legacy (Kanjeevaram, Pashmina & Ikat)',
                        'Charkha Spinning: Fibre Friction, Twist Physics, Takli & Gandhi\\'s Khadi Movement',
                        'Natural Fibres: Plant Cellulose (Cotton, Flax, Jute) vs Animal Protein (Wool, Silk)',
                        'Silk Cocoon: Bombyx Mori Metamorphosis & Figure-8 Spinning of 1,000m Filaments',
                        'Synthetic Fibres: Petrochemical Polymers & Molten Plastic Fire Safety Hazards',
                        'Tailorbird Stitches: Avian Needle Beaks, Leaf Punctures & Spider-Silk Rivet Knots',
                        'Running Stitch: Rhythmic In-and-Out Sewing & Activity 7-8 Patchwork Mats',
                        'Chikankari Craft: Lucknow Muslin Shadow-Work (Bakhiya) & Awadh Elegance',
                        'Kantha Quilts: Upcycling Saree Layers with Rippling Running-Stitch Waves',
                        'Phulkari & Toda: Punjab Floral Bagh Floss vs Nilgiri Geometric Buffalo Horn Shawls',
                        'Kashmiri & Khneng: Kashmir Chinar Motifs vs Meghalaya River Fish-Bone Eri Silk',
                        'Cloth Upcycling: 5-Stage Zero-Waste Circular Life Cycle (Garment to Compost)',
                        'Fabric Testing: Forensic Burn Analysis (Paper vs Hair vs Melting Plastic Residues)',
                        'Textile Guardians: Honoring 20 km of Spun Thread, Mending & Artisan Stewardship',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ]"""

full_c5_block = f"""            // NCERT Science Class 5
            {part_1_to_5}
{ch5_closing}
                {c5_ch6_code}
                {c5_ch7_code}
                {c5_ch8_code}
            ],"""

# 7. Insert Class 5 block before Class 6 header
c6_marker = """            // NCERT Science Class 6
            'ncert-science-class6' => ["""
content = content.replace(c6_marker, f"{full_c5_block}\n\n{c6_marker}", 1)

# 8. Insert Class 6 chapters 2 to 12 right after Chapter 1 of Class 6
# Find Chapter 1 of Class 6 ending
c6_ch1_target = """                        'Everyday Scientists: Mechanics, Cooks, Electricians & Becoming a Lifelong \\'Whys\\' Person',
                        '32 In-Slide Checkpoint Inquiries with Instant Mentor Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],"""

if c6_ch1_target not in content:
    # Try alternative quote escaping
    c6_ch1_target = """                        'Everyday Scientists: Mechanics, Cooks, Electricians & Becoming a Lifelong \'Whys\' Person',
                        '32 In-Slide Checkpoint Inquiries with Instant Mentor Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],"""

assert c6_ch1_target in content, "Class 6 Chapter 1 target not found in controller content!"

all_c6_rest = "\n                ".join([c6_dict[ch] for ch in range(2, 13)])
c6_replacement = f"""                        'Everyday Scientists: Mechanics, Cooks, Electricians & Becoming a Lifelong \\'Whys\\' Person',
                        '32 In-Slide Checkpoint Inquiries with Instant Mentor Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
                {all_c6_rest}
            ],"""

content = content.replace(c6_ch1_target, c6_replacement, 1)

with open('app/Http/Controllers/MultimediaController.php', 'w', encoding='utf-8') as f:
    f.write(content)

print("Controller rebuilt with Class 5 (Chapters 1-8) and Class 6 (Chapters 1-12)!")

