"""
Patch script for Class 5 Science Chapter 10: Earth - Our Shared Home
1. Updates app/Http/Controllers/MultimediaController.php
2. Updates resources/views/components/layouts/app.blade.php
3. Updates tests/Unit/MultimediaCurriculumTreeUnitTest.php
"""

import sys
import re

# 1. Update MultimediaController.php
controller_path = 'app/Http/Controllers/MultimediaController.php'
with open(controller_path, 'r', encoding='utf-8') as f:
    ctrl_content = f.read()

ch10_entry = '''                [
                    'chapter_num' => 10,
                    'name' => 'Earth - Our Shared Home',
                    'has_multimedia' => true,
                    'media_key' => 'class5-science-earth-our-shared-home',
                    'media_title' => 'NCERT Class 5 Science • Chapter 10 • Earth - Our Shared Home Master Lab',
                    'media_url' => asset('animations/class5-science-earth-our-shared-home.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated laboratory for Grade 5 Science Chapter 10: Earth - Our Shared Home (Curiosity, NEP 2020) featuring comprehensive spoken classroom audio lectures in authentic Indian English narration, Web Speech API integration, and 16 bespoke SVG/HTML interactive simulators covering One Shared Home (space perspective from Group Captain Shubhanshu Shukla and Wing Commander Rakesh Sharma; borderless Earth viewed from the ISS orbiting at 28,000 km/h), The Blue Planet (liquid oceans covering 71% of surface and scattering blue light vs 29% landmasses), Boundless Nature (fluid circulation of atmosphere, rainclouds, seeds, and ocean currents without passports), Travelling Birds (the epic 5,000 km transcontinental winter migration of rosy starlings from Russia and Mongolia to India, consuming agricultural crop locusts), Yoga\\\'s Gift (ancient Indian 3,000-year science of holistic wellness, asanas, pranayama, and the United Nations June 21 International Day of Yoga across 177 nations), Chilli\\\'s Journey (South American native Capsicum brought to Goa by Portuguese traders 500 years ago, replacing black pepper), Sweet Sugar (ancient Indian mastery of boiling sugarcane juice into gur jaggery and crystalline Sarkara, spreading worldwide), Mexican Marigold (Aztec sacred Cempasúchil flower travelling to India to become festive Genda Phool and root bio-defense against nematodes), Cows in Brazil (hardy Indian Gir, Kankrej, and Ongole cattle adapting to Brazil\\\'s tropical heat, now forming over three-fourths of its national herd), Web of Life (interconnected food and energy networks binding sunlight, plants, pollinators, animals, and decomposers), World Family (ancient Sanskrit philosophy of Vasudhaiva Kutumbakam embracing all humans, animals, trees, rivers, and atmosphere as one household), Nature Protects (MoEFCC motto Prakriti Rakshati Rakshita: Nature Protects if She is Protected, guarding our sole cosmic oasis), Global Travelers (mapping the geographic roots of everyday foods in our lunchbox), Earth Guardians (daily student eco-actions saving water, conserving electricity, refusing plastics, and planting native trees), Seasons Across Borders (how axial tilt creates opposite seasons in Northern and Southern Hemispheres), and Our Living Earth (four planetary spheres: Atmosphere, Hydrosphere, Biosphere, and Geosphere working in eternal harmony), plus 32 in-slide checkpoints and 4 dedicated mastery quiz challenge slides with 40 questions and step-by-step solution modals.',
                    'topics' => [
                        'One Shared Home: Borderless Planetary View from ISS Orbit (Shukla & Sharma)',
                        'The Blue Planet: 71% Liquid Oceans, Continental Landforms & Blue Light Scattering',
                        'Boundless Nature: Global Atmospheric Circulation of Air, Clouds, Water & Seeds',
                        'Travelling Birds: Rosy Starling 5,000 km Winter Odyssey & Locust Pest Control',
                        'Yoga\\\'s Gift: 3,000-Year Ancient Indian Wellness, Harmony & June 21 UN Yoga Day',
                        'Chilli\\\'s Journey: South American Origin, Portuguese Galleons & Black Pepper Swap',
                        'Sweet Sugar: Ancient Indian Sugarcane Mastery, Jaggery (Gur) & Sarkara Crystals',
                        'Mexican Marigold: Aztec Cempasúchil, Festive Indian Garlands & Soil Bio-Defense',
                        'Cows in Brazil: Indian Zebu (Gir, Ongole) Dominating >75% of Brazilian Dairy',
                        'Web of Life: Interconnected Planetary Food Webs, Nutrient Cycles & Energy Flows',
                        'World Family: Vasudhaiva Kutumbakam (The Entire Earth is One Single Family)',
                        'Nature Protects: MoEFCC Motto (Prakriti Rakshati Rakshita) & Planetary Stewardship',
                        'Global Travelers: Tracing Origins of Everyday Foods (Potatoes, Tomatoes, Rice, Tea)',
                        'Earth Guardians: Daily Student Actions Conserving Water, Energy & Nurturing Trees',
                        'Seasons Across Borders: Axial Tilt, Opposite Hemispheres & Global Nature Journals',
                        'Our Living Earth: Four Planetary Spheres (Atmosphere, Hydro, Bio, Geo) in Harmony',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 6'''

target_ch9_end = '''                        'The Eternal Cycle: Six-Season Cosmic Wheel & Nature\\\'s Continuous Interconnection',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 6'''

if target_ch9_end not in ctrl_content:
    print("ERROR: Target for Chapter 9 end not found in MultimediaController.php")
    sys.exit(1)

replacement_ctrl = f'''                        'The Eternal Cycle: Six-Season Cosmic Wheel & Nature\\\'s Continuous Interconnection',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
{ch10_entry}'''

ctrl_content = ctrl_content.replace(target_ch9_end, replacement_ctrl, 1)

with open(controller_path, 'w', encoding='utf-8') as f:
    f.write(ctrl_content)
print("Updated MultimediaController.php with Chapter 10!")

# 2. Update layouts/app.blade.php
blade_path = 'resources/views/components/layouts/app.blade.php'
with open(blade_path, 'r', encoding='utf-8') as f:
    blade_content = f.read()

target_blade = '''                } else if (type === 'class5-science-rhythms-of-nature' || type === 'chapter9-science-class5' || type === 'class5-science-chapter9' || type === 'class5-rhythms-of-nature' || type === 'rhythms-of-nature-class5' || type === 'class5-science-rhythms' || type === 'class5-science-seasons-lab' || type === 'class5-seasons') {
                    fileUrl = "{{ asset('animations/class5-science-rhythms-of-nature.html') }}";
                    titleText = "NCERT Class 5 Science — Chapter 9: Rhythms of Nature Master Lab";
                    badgeText = "Class 5 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";'''

replacement_blade = target_blade + '''
                } else if (type === 'class5-science-earth-our-shared-home' || type === 'chapter10-science-class5' || type === 'class5-science-chapter10' || type === 'class5-earth-our-shared-home' || type === 'earth-our-shared-home-class5' || type === 'class5-science-shared-home' || type === 'class5-science-earth-lab' || type === 'class5-shared-home') {
                    fileUrl = "{{ asset('animations/class5-science-earth-our-shared-home.html') }}";
                    titleText = "NCERT Class 5 Science — Chapter 10: Earth - Our Shared Home Master Lab";
                    badgeText = "Class 5 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-sky-500/20 text-sky-300 border border-sky-500/30 shrink-0";'''

if target_blade not in blade_content:
    print("ERROR: Target for Chapter 9 not found in layouts/app.blade.php")
    sys.exit(1)

blade_content = blade_content.replace(target_blade, replacement_blade, 1)

with open(blade_path, 'w', encoding='utf-8') as f:
    f.write(blade_content)
print("Updated layouts/app.blade.php with Chapter 10!")

# 3. Update tests/Unit/MultimediaCurriculumTreeUnitTest.php
test_path = 'tests/Unit/MultimediaCurriculumTreeUnitTest.php'
with open(test_path, 'r', encoding='utf-8') as f:
    test_content = f.read()

# Update total count 890 -> 898
assert '$this->assertCount(890, $files);' in test_content, "Expected 890 count in test"
test_content = test_content.replace('$this->assertCount(890, $files);', '$this->assertCount(898, $files);', 1)

ch10_test = '''    public function test_ncert_class_5_has_earth_our_shared_home_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Earth - Our Shared Home', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class5-science-earth-our-shared-home', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-earth-our-shared-home.html'));
        $this->assertFileExists(public_path('animations/chapter10-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter10.html'));
        $this->assertFileExists(public_path('animations/class5-earth-our-shared-home.html'));
        $this->assertFileExists(public_path('animations/earth-our-shared-home-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-shared-home.html'));
        $this->assertFileExists(public_path('animations/class5-science-earth-lab.html'));
        $this->assertFileExists(public_path('animations/class5-shared-home.html'));
    }

'''

target_test_anchor = '    public function test_ncert_class_6_has_wonderful_world_of_science_multimedia(): void'
if target_test_anchor not in test_content:
    print("ERROR: Target anchor for test not found in test file")
    sys.exit(1)

test_content = test_content.replace(target_test_anchor, ch10_test + target_test_anchor, 1)

with open(test_path, 'w', encoding='utf-8') as f:
    f.write(test_content)
print("Updated MultimediaCurriculumTreeUnitTest.php with Chapter 10 test and count 898!")

