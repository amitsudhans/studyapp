"""
Patch script for Class 5 Science Chapter 9: Rhythms of Nature
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

ch9_entry = '''                [
                    'chapter_num' => 9,
                    'name' => 'Rhythms of Nature',
                    'has_multimedia' => true,
                    'media_key' => 'class5-science-rhythms-of-nature',
                    'media_title' => 'NCERT Class 5 Science • Chapter 9 • Rhythms of Nature Master Lab',
                    'media_url' => asset('animations/class5-science-rhythms-of-nature.html'),
                    'description' => 'Comprehensive 20-slide interactive multimedia animated laboratory for Grade 5 Science Chapter 9: Rhythms of Nature (Curiosity, NEP 2020) featuring comprehensive spoken classroom audio lectures in authentic Indian English narration, Web Speech API integration, and 16 bespoke SVG/HTML interactive simulators covering Nature\\\'s Clock (personal and ecological changes across seconds, hours, and years; Saba and Aparna\\\'s reunion), Day and Night (Activity 1 torch and globe demonstration proving Earth\\\'s axial rotation causes day and night while the Sun remains stationary), Earth\\\'s Spin (west-to-east axial rotation, sunrise in East, sunset in West, and changing solar shadow lengths), Seasons\\\' Journal (recording four three-month quarters across five themes: plant life, birds/animals, air, heat/light, and human habits), Yearly Rhythms (decoding cyclic weather and ecological patterns), Shad Ritu (Vasanta, Grishma, Varsha, Sharad, Hemant, and Shishir), Vasanta Spring (Chaitra–Vaishakha blooming flame of the forest Palash and Asian Koel song), Grishma Summer (Jyeshtha–Ashadha intense heat, Loo winds, and hydrating Aam Panna), Varsha Monsoon (Shravana–Bhadrapada sweet petrichor rain, overflowing ponds, and bullfrog chorus), Sharad Autumn (Ashvina–Kartika sapphire blue skies, white Kaash reeds, and nocturnal Shiuli blooms), Hemant Pre-Winter (Margashirsha–Pausha morning mist, dew drops on grass tips, golden paddy harvest, and Til-Gur), Shishir Winter (Magha–Phalguna cold Himalayan winds, bare deciduous trees, bonfires, and immunity pantry with Sarson Saag, Amla, and oranges), Regional Contrasts (sub-zero snowy winters in Kashmir with Kangri heaters under pherans vs warm tropical maritime climate in Kerala, Thar desert heat swings, and Meghalaya Mawsynram world-record rains), Seasonal Crops (agricultural cropping triad: Kharif monsoon rice/maize/cotton, Rabi winter wheat/mustard/gram, and Zaid summer melons/cucumbers), Harvest Festivals (pan-Indian harvest celebrations: Makar Sankranti, Pongal, Lohri, Magh Bihu, and Baisakhi), and Living in Rhythm (Ritucharya seasonal lifestyles, breathable cottons vs layered woollens, and the eternal cycle of seasons), plus 32 in-slide checkpoints and 4 dedicated mastery quiz challenge slides with 40 questions and step-by-step solution modals.',
                    'topics' => [
                        'Nature\\\'s Clock: Personal & Environmental Changes Across Seconds, Hours & Years',
                        'Day and Night: Stationary Sun, Axial Spin & Activity 1 Torch-Globe Demonstration',
                        'Earth\\\'s Spin: West-to-East 24-Hour Rotation, Solar Path & Changing Shadows',
                        'Seasons\\\' Journal: 4 Quarters & 5 Ecological Themes (Flora, Fauna, Air, Sun, Water)',
                        'Yearly Rhythms: Decoding Repeating Natural Cycles & Seasonal Biological Clocks',
                        'Vasanta Spring: Chaitra–Vaishakha, Flame of the Forest Palash & Asian Koel Song',
                        'Grishma Summer: Jyeshtha–Ashadha, Scorching Sun, Loo Winds & Hydrating Panna',
                        'Varsha Monsoon: Shravana–Bhadrapada, Petrichor Aroma, Bullfrogs & Kharif Sowing',
                        'Sharad Autumn: Ashvina–Kartika, Sapphire Blue Skies, Kaash Reeds & Shiuli Blooms',
                        'Hemant Pre-Winter: Margashirsha–Pausha, Morning Dewdrops, Golden Harvest & Til-Gur',
                        'Shishir Winter: Magha–Phalguna, Chilly Winds, Bonfires & Immunity Foods (Amla, Saag)',
                        'Regional Contrasts: Kashmir Pheran & Kangri vs Kerala Coastal Breeze & Thar Desert',
                        'Seasonal Crops: Agricultural Triad (Kharif Monsoon, Rabi Winter & Zaid Summer)',
                        'Harvest Festivals: Pan-Indian Celebrations (Makar Sankranti, Pongal, Lohri, Magh Bihu)',
                        'Living in Rhythm: Ritucharya Seasonal Clothing, Diet & Harmonious Adaptation',
                        'The Eternal Cycle: Six-Season Cosmic Wheel & Nature\\\'s Continuous Interconnection',
                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 6'''

target_ch8_end = '''                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
            ],

            // NCERT Science Class 6'''

if target_ch8_end not in ctrl_content:
    print("ERROR: Target for Chapter 8 end not found in MultimediaController.php")
    sys.exit(1)

replacement_ctrl = f'''                        '32 In-Slide Checkpoint Inquiries with Instant Visual Feedback',
                        '4 Dedicated Mastery Challenge Slides (40 Questions with Step-by-Step Pop-up Solutions)',
                    ],
                ],
{ch9_entry}'''

ctrl_content = ctrl_content.replace(target_ch8_end, replacement_ctrl, 1)

with open(controller_path, 'w', encoding='utf-8') as f:
    f.write(ctrl_content)
print("Updated MultimediaController.php with Chapter 9!")

# 2. Update layouts/app.blade.php
blade_path = 'resources/views/components/layouts/app.blade.php'
with open(blade_path, 'r', encoding='utf-8') as f:
    blade_content = f.read()

target_blade = '''                } else if (type === 'class5-science-clothes-how-things-are-made' || type === 'chapter8-science-class5' || type === 'class5-science-chapter8' || type === 'class5-clothes-how-things-are-made' || type === 'clothes-how-things-are-made-class5' || type === 'class5-science-clothes' || type === 'class5-science-clothes-lab' || type === 'class5-clothes') {
                    fileUrl = "{{ asset('animations/class5-science-clothes-how-things-are-made.html') }}";
                    titleText = "NCERT Class 5 Science — Chapter 8: Clothes - How Things are Made Master Lab";
                    badgeText = "Class 5 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-amber-500/20 text-amber-300 border border-amber-500/30 shrink-0";'''

replacement_blade = target_blade + '''
                } else if (type === 'class5-science-rhythms-of-nature' || type === 'chapter9-science-class5' || type === 'class5-science-chapter9' || type === 'class5-rhythms-of-nature' || type === 'rhythms-of-nature-class5' || type === 'class5-science-rhythms' || type === 'class5-science-seasons-lab' || type === 'class5-seasons') {
                    fileUrl = "{{ asset('animations/class5-science-rhythms-of-nature.html') }}";
                    titleText = "NCERT Class 5 Science — Chapter 9: Rhythms of Nature Master Lab";
                    badgeText = "Class 5 • NCERT Science";
                    badgeClass = "hidden sm:inline-block px-2 py-0.5 rounded text-[10px] font-bold bg-emerald-500/20 text-emerald-300 border border-emerald-500/30 shrink-0";'''

if target_blade not in blade_content:
    print("ERROR: Target for Chapter 8 not found in layouts/app.blade.php")
    sys.exit(1)

blade_content = blade_content.replace(target_blade, replacement_blade, 1)

with open(blade_path, 'w', encoding='utf-8') as f:
    f.write(blade_content)
print("Updated layouts/app.blade.php with Chapter 9!")

# 3. Update tests/Unit/MultimediaCurriculumTreeUnitTest.php
test_path = 'tests/Unit/MultimediaCurriculumTreeUnitTest.php'
with open(test_path, 'r', encoding='utf-8') as f:
    test_content = f.read()

# Update total count 882 -> 890
assert '$this->assertCount(882, $files);' in test_content, "Expected 882 count in test"
test_content = test_content.replace('$this->assertCount(882, $files);', '$this->assertCount(890, $files);', 1)

ch9_test = '''    public function test_ncert_class_5_has_rhythms_of_nature_multimedia(): void
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
        $this->assertEquals('Rhythms of Nature', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class5-science-rhythms-of-nature', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-rhythms-of-nature.html'));
        $this->assertFileExists(public_path('animations/chapter9-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter9.html'));
        $this->assertFileExists(public_path('animations/class5-rhythms-of-nature.html'));
        $this->assertFileExists(public_path('animations/rhythms-of-nature-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-rhythms.html'));
        $this->assertFileExists(public_path('animations/class5-science-seasons-lab.html'));
        $this->assertFileExists(public_path('animations/class5-seasons.html'));
    }

'''

target_test_anchor = '    public function test_ncert_class_6_has_wonderful_world_of_science_multimedia(): void'
if target_test_anchor not in test_content:
    print("ERROR: Target anchor for test not found in test file")
    sys.exit(1)

test_content = test_content.replace(target_test_anchor, ch9_test + target_test_anchor, 1)

with open(test_path, 'w', encoding='utf-8') as f:
    f.write(test_content)
print("Updated MultimediaCurriculumTreeUnitTest.php with Chapter 9 test and count 890!")

