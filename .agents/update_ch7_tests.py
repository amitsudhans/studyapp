with open('tests/Unit/MultimediaCurriculumTreeUnitTest.php', 'r', encoding='utf-8') as f:
    content = f.read()

# 1. Add unit test for Chapter 7
target_test = """        $this->assertFileExists(public_path('animations/playing-with-numbers-class7.html'));
    }

    public function test_cbse_syllabus_has_no_contents(): void"""

new_test = """        $this->assertFileExists(public_path('animations/playing-with-numbers-class7.html'));
    }

    public function test_ncert_class_7_has_tale_of_three_intersecting_lines_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('A Tale of Three Intersecting Lines', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class7-math-tale-of-three-intersecting-lines', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-tale-of-three-intersecting-lines.html'));
        $this->assertFileExists(public_path('animations/chapter7-math-class7.html'));
        $this->assertFileExists(public_path('animations/tale-of-three-intersecting-lines.html'));
        $this->assertFileExists(public_path('animations/class7-tale-of-three-intersecting-lines.html'));
        $this->assertFileExists(public_path('animations/tale-of-three-lines-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-triangles.html'));
        $this->assertFileExists(public_path('animations/triangles-class7.html'));
        $this->assertFileExists(public_path('animations/class7-triangles.html'));
    }

    public function test_cbse_syllabus_has_no_contents(): void"""

if target_test in content:
    content = content.replace(target_test, new_test, 1)
    print("Added test_ncert_class_7_has_tale_of_three_intersecting_lines_multimedia successfully!")
else:
    print("ERROR: target_test not found!")
    exit(1)

# 2. Update assertCount(359, $files) to assertCount(367, $files)
target_count = "$this->assertCount(359, $files);"
new_count = "$this->assertCount(367, $files);"

if target_count in content:
    content = content.replace(target_count, new_count, 1)
    print("Updated assertCount to 367 successfully!")
else:
    print("ERROR: target_count not found!")
    exit(1)

with open('tests/Unit/MultimediaCurriculumTreeUnitTest.php', 'w', encoding='utf-8') as f:
    f.write(content)

print("Updated tests/Unit/MultimediaCurriculumTreeUnitTest.php successfully!")
