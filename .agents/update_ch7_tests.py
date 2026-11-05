# -*- coding: utf-8 -*-
with open('tests/Unit/MultimediaCurriculumTreeUnitTest.php', 'r', encoding='utf-8') as f:
    content = f.read()

sub = 'public function test_ncert_class_5_has_we_the_travellers_1_multimedia'
idx = content.find(sub)
assert idx != -1, "Sub not found in test file"

new_test = '''public function test_ncert_class_4_has_the_cleanest_village_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Cleanest Village', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class4-maths-the-cleanest-village', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-the-cleanest-village.html'));
        $this->assertFileExists(public_path('animations/chapter7-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter7.html'));
        $this->assertFileExists(public_path('animations/class4-the-cleanest-village.html'));
        $this->assertFileExists(public_path('animations/the-cleanest-village-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-the-cleanest-village-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-the-cleanest-village.html'));
        $this->assertFileExists(public_path('animations/class4-cleanest-village-lab.html'));
    }

    '''

content = content[:idx] + new_test + content[idx:]

target2 = '        $this->assertCount(1066, $files);'
assert target2 in content, "Target2 not found in test file"
content = content.replace(target2, '        $this->assertCount(1074, $files);', 1)

with open('tests/Unit/MultimediaCurriculumTreeUnitTest.php', 'w', encoding='utf-8') as f:
    f.write(content)

print('Successfully inserted Chapter 7 test and updated total count to 1074!')
