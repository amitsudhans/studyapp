with open("tests/Unit/MultimediaCurriculumTreeUnitTest.php", "r", encoding="utf-8") as f:
    text = f.read()

assert "$this->assertCount(345, $files);" in text, "Count 345 not found"
text = text.replace("$this->assertCount(345, $files);", "$this->assertCount(352, $files);")

target = """        $this->assertFileExists(public_path('animations/class7-math-algebraic-expressions.html'));
        $this->assertFileExists(public_path('animations/using-letter-numbers-class7.html'));
    }"""

new_test = """        $this->assertFileExists(public_path('animations/class7-math-algebraic-expressions.html'));
        $this->assertFileExists(public_path('animations/using-letter-numbers-class7.html'));
    }

    public function test_ncert_class_7_has_parallel_intersecting_lines_multimedia(): void
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
        $this->assertEquals('Parallel and Intersecting Lines', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class7-math-parallel-intersecting-lines', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-parallel-intersecting-lines.html'));
        $this->assertFileExists(public_path('animations/chapter5-math-class7.html'));
        $this->assertFileExists(public_path('animations/parallel-and-intersecting-lines.html'));
        $this->assertFileExists(public_path('animations/class7-parallel-intersecting-lines.html'));
        $this->assertFileExists(public_path('animations/parallel-lines-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-lines-angles.html'));
        $this->assertFileExists(public_path('animations/intersecting-lines-class7.html'));
    }"""

assert target in text, "target not found"
text = text.replace(target, new_test, 1)

with open("tests/Unit/MultimediaCurriculumTreeUnitTest.php", "w", encoding="utf-8") as f:
    f.write(text)

print("Successfully updated tests/Unit/MultimediaCurriculumTreeUnitTest.php")
