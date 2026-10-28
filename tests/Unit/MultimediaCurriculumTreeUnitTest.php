<?php

namespace Tests\Unit;

use App\Http\Controllers\MultimediaController;
use Illuminate\Http\Request;
use Tests\TestCase;

class MultimediaCurriculumTreeUnitTest extends TestCase
{
    public function test_default_syllabus_is_ncert_and_has_all_14_multimedia_chapters_in_class_10(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia', 'GET');

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertArrayHasKey('ncert', $data['syllabuses']);
        $this->assertArrayHasKey('cbse', $data['syllabuses']);
        $this->assertArrayHasKey('scert-kerala', $data['syllabuses']);

        // Check 14 chapters in Class 10
        $this->assertCount(14, $data['activeChapters']);
        $this->assertTrue($data['hasAnyMultimedia']);

        $chapterNames = collect($data['activeChapters'])->pluck('name')->toArray();
        $this->assertContains('Real Numbers', $chapterNames);
        $this->assertContains('Polynomials', $chapterNames);
        $this->assertContains('Statistics', $chapterNames);
        $this->assertContains('Probability', $chapterNames);

        // Verify every chapter has multimedia
        foreach ($data['activeChapters'] as $ch) {
            $this->assertTrue($ch['has_multimedia'], "Chapter {$ch['chapter_num']} must have multimedia");
            $this->assertNotEmpty($ch['media_url']);
        }
    }

    public function test_ncert_class_9_has_number_system_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Number System', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
    }

    public function test_ncert_class_9_has_polynomials_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Polynomials', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class9-polynomials', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class9-polynomials.html'));
        $this->assertFileExists(public_path('animations/chapter2-maths-class9.html'));
        $this->assertFileExists(public_path('animations/algebra-linear-polynomials.html'));
    }

    public function test_ncert_class_9_has_sequences_and_progressions_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Sequences and Progressions', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class9-sequences-progressions', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class9-sequences-progressions.html'));
        $this->assertFileExists(public_path('animations/chapter3-maths-class9.html'));
        $this->assertFileExists(public_path('animations/sequences-and-progressions.html'));
    }

    public function test_ncert_class_9_has_algebraic_identities_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Exploring Algebraic Identities', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class9-algebraic-identities', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class9-algebraic-identities.html'));
        $this->assertFileExists(public_path('animations/chapter4-maths-class9.html'));
        $this->assertFileExists(public_path('animations/algebraic-identities.html'));
    }

    public function test_ncert_class_9_has_linear_equations_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Linear Equations in Two Variables', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class9-linear-equations', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class9-linear-equations.html'));
        $this->assertFileExists(public_path('animations/chapter5-maths-class9.html'));
        $this->assertFileExists(public_path('animations/linear-equations-in-two-variables.html'));
    }

    public function test_ncert_class_9_has_coordinate_geometry_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Coordinate Geometry', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class9-coordinate-geometry', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class9-coordinate-geometry.html'));
        $this->assertFileExists(public_path('animations/chapter6-maths-class9.html'));
        $this->assertFileExists(public_path('animations/class9-coord-geom.html'));
    }

    public function test_ncert_class_9_has_euclids_geometry_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Introduction to Euclid’s Geometry', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class9-euclids-geometry', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class9-euclids-geometry.html'));
        $this->assertFileExists(public_path('animations/chapter7-maths-class9.html'));
        $this->assertFileExists(public_path('animations/euclids-geometry.html'));
    }

    public function test_ncert_class_9_has_lines_and_angles_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Lines and Angles', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class9-lines-and-angles', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class9-lines-and-angles.html'));
        $this->assertFileExists(public_path('animations/chapter8-maths-class9.html'));
        $this->assertFileExists(public_path('animations/lines-and-angles.html'));
    }

    public function test_ncert_class_9_has_triangles_congruence_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Triangles: Congruence Theorems', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class9-triangles-congruence', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class9-triangles-congruence.html'));
        $this->assertFileExists(public_path('animations/chapter9-maths-class9.html'));
        $this->assertFileExists(public_path('animations/triangles-congruence.html'));
    }

    public function test_ncert_class_9_has_quadrilaterals_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('4-gons (Quadrilaterals)', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class9-quadrilaterals', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class9-quadrilaterals.html'));
        $this->assertFileExists(public_path('animations/chapter10-maths-class9.html'));
        $this->assertFileExists(public_path('animations/quadrilaterals-4gons.html'));
    }

    public function test_ncert_class_9_has_circles_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Circles', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class9-circles', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class9-circles.html'));
        $this->assertFileExists(public_path('animations/chapter11-maths-class9.html'));
        $this->assertFileExists(public_path('animations/circles-geometry.html'));
    }

    public function test_ncert_class_9_has_mensuration_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Mensuration: Area and Perimeter', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class9-mensuration', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class9-mensuration.html'));
        $this->assertFileExists(public_path('animations/chapter12-maths-class9.html'));
        $this->assertFileExists(public_path('animations/mensuration-area-perimeter.html'));
    }

    public function test_ncert_class_9_has_surface_areas_volumes_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Mensuration: Surface Area and Volume', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertEquals('class9-surface-areas-volumes', $data['activeChapters'][12]['media_key']);
        $this->assertFileExists(public_path('animations/class9-surface-areas-volumes.html'));
        $this->assertFileExists(public_path('animations/chapter13-maths-class9.html'));
        $this->assertFileExists(public_path('animations/surface-areas-volumes-3d.html'));
    }

    public function test_ncert_class_9_has_statistics_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Statistics', $data['activeChapters'][13]['name']);
        $this->assertTrue($data['activeChapters'][13]['has_multimedia']);
        $this->assertEquals('class9-statistics', $data['activeChapters'][13]['media_key']);
        $this->assertFileExists(public_path('animations/class9-statistics.html'));
        $this->assertFileExists(public_path('animations/chapter14-maths-class9.html'));
        $this->assertFileExists(public_path('animations/statistics-data-analysis.html'));
    }

    public function test_ncert_class_9_has_probability_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Introduction to Probability', $data['activeChapters'][14]['name']);
        $this->assertTrue($data['activeChapters'][14]['has_multimedia']);
        $this->assertEquals('class9-probability', $data['activeChapters'][14]['media_key']);
        $this->assertFileExists(public_path('animations/class9-probability.html'));
        $this->assertFileExists(public_path('animations/chapter15-maths-class9.html'));
        $this->assertFileExists(public_path('animations/probability-intro.html'));
    }

    public function test_ncert_class_9_has_cell_fundamental_unit_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Fundamental Unit of Life', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class9-cell-fundamental-unit', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class9-cell-fundamental-unit.html'));
        $this->assertFileExists(public_path('animations/chapter1-science-class9.html'));
        $this->assertFileExists(public_path('animations/the-fundamental-unit-of-life.html'));
        $this->assertFileExists(public_path('animations/cell-structure-and-function.html'));
    }

    public function test_ncert_class_9_has_tissues_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Tissues', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class9-tissues', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class9-tissues.html'));
        $this->assertFileExists(public_path('animations/chapter2-science-class9.html'));
        $this->assertFileExists(public_path('animations/tissues.html'));
        $this->assertFileExists(public_path('animations/plant-and-animal-tissues.html'));
    }

    public function test_ncert_class_9_has_reproduction_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Reproduction', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class9-reproduction', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class9-reproduction.html'));
        $this->assertFileExists(public_path('animations/chapter3-science-class9.html'));
        $this->assertFileExists(public_path('animations/class9-sexual-asexual-reproduction.html'));
        $this->assertFileExists(public_path('animations/reproduction-modes-and-health.html'));
    }

    public function test_ncert_class_9_has_diversity_in_living_organisms_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Diversity in Living Organisms', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class9-diversity-in-living-organisms', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class9-diversity-in-living-organisms.html'));
        $this->assertFileExists(public_path('animations/chapter4-science-class9.html'));
        $this->assertFileExists(public_path('animations/diversity-in-living-organisms.html'));
        $this->assertFileExists(public_path('animations/biological-diversity-and-classification.html'));
    }

    public function test_ncert_class_9_has_exploring_mixtures_and_separation_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Exploring Mixtures and their Separation', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class9-exploring-mixtures-and-separation', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class9-exploring-mixtures-and-separation.html'));
        $this->assertFileExists(public_path('animations/chapter5-science-class9.html'));
        $this->assertFileExists(public_path('animations/exploring-mixtures-and-their-separation.html'));
        $this->assertFileExists(public_path('animations/mixtures-and-separation-techniques.html'));
    }

    public function test_ncert_class_9_has_structure_of_atom_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Structure of an Atom', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class9-structure-of-atom', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class9-structure-of-atom.html'));
        $this->assertFileExists(public_path('animations/chapter6-science-class9.html'));
        $this->assertFileExists(public_path('animations/structure-of-an-atom.html'));
        $this->assertFileExists(public_path('animations/atomic-structure-and-models.html'));
    }

    public function test_ncert_class_9_has_atoms_and_molecules_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Atoms and Molecules', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class9-atoms-and-molecules', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class9-atoms-and-molecules.html'));
        $this->assertFileExists(public_path('animations/chapter7-science-class9.html'));
        $this->assertFileExists(public_path('animations/atoms-and-molecules.html'));
        $this->assertFileExists(public_path('animations/chemical-formulae-and-molecular-mass.html'));
    }

    public function test_ncert_class_9_has_earth_as_a_system_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Earth as a System: Energy, Matter & Life', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class9-earth-as-a-system', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class9-earth-as-a-system.html'));
        $this->assertFileExists(public_path('animations/chapter8-science-class9.html'));
        $this->assertFileExists(public_path('animations/earth-as-a-system.html'));
        $this->assertFileExists(public_path('animations/energy-matter-and-life.html'));
    }

    public function test_ncert_class_9_has_motion_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Motion', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class9-motion', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class9-motion.html'));
        $this->assertFileExists(public_path('animations/chapter9-science-class9.html'));
        $this->assertFileExists(public_path('animations/motion.html'));
        $this->assertFileExists(public_path('animations/kinematics-and-motion.html'));
    }

    public function test_ncert_class_9_has_force_and_laws_of_motion_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Force and Laws of Motion', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class9-force-and-laws-of-motion', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class9-force-and-laws-of-motion.html'));
        $this->assertFileExists(public_path('animations/chapter10-science-class9.html'));
        $this->assertFileExists(public_path('animations/force-and-laws-of-motion.html'));
        $this->assertFileExists(public_path('animations/laws-of-motion.html'));
    }

    public function test_ncert_class_9_has_work_energy_simple_machines_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Work, Energy and Simple Machines', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class9-work-energy-simple-machines', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class9-work-energy-simple-machines.html'));
        $this->assertFileExists(public_path('animations/chapter11-science-class9.html'));
        $this->assertFileExists(public_path('animations/work-energy-and-simple-machines.html'));
        $this->assertFileExists(public_path('animations/work-and-energy.html'));
    }

    public function test_ncert_class_9_has_sound_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Sound', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class9-sound', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class9-sound.html'));
        $this->assertFileExists(public_path('animations/chapter12-science-class9.html'));
        $this->assertFileExists(public_path('animations/sound.html'));
        $this->assertFileExists(public_path('animations/sound-waves-and-acoustics.html'));
    }

    public function test_ncert_class_9_has_english_writing_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=english&class=class9', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'english',
            'class' => 'class9',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('english', $data['selectedSubject']);
        $this->assertEquals('class9', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Effective Communication and Writing in Diverse Forms', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class9-english-communication-writing', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class9-english-communication-writing.html'));
        $this->assertFileExists(public_path('animations/chapter1-english-class9.html'));
        $this->assertFileExists(public_path('animations/class9-english-writing.html'));
        $this->assertFileExists(public_path('animations/effective-communication-writing.html'));
    }

    public function test_ncert_class_8_has_squares_cubes_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Exploring Squares and Cubes', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class8-math-square-and-cube', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-square-and-cube.html'));
        $this->assertFileExists(public_path('animations/chapter1-math-class8.html'));
        $this->assertFileExists(public_path('animations/a-square-and-a-cube.html'));
        $this->assertFileExists(public_path('animations/square-and-a-cube.html'));
    }

    public function test_ncert_class_8_has_linear_polynomials_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Fundamentals of Linear Polynomials', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class8-math-linear-polynomials', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-linear-polynomials.html'));
        $this->assertFileExists(public_path('animations/chapter2-math-class8.html'));
        $this->assertFileExists(public_path('animations/introduction-to-linear-polynomials.html'));
        $this->assertFileExists(public_path('animations/linear-polynomials-class8.html'));
    }

    public function test_ncert_class_8_has_story_of_numbers_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Evolution of Number Systems', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class8-math-story-of-numbers', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-story-of-numbers.html'));
        $this->assertFileExists(public_path('animations/chapter3-math-class8.html'));
        $this->assertFileExists(public_path('animations/a-story-of-numbers.html'));
        $this->assertFileExists(public_path('animations/story-of-numbers-class8.html'));
    }

    public function test_ncert_class_8_has_quadrilaterals_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Properties and Types of Quadrilaterals', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class8-math-quadrilaterals', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-quadrilaterals.html'));
        $this->assertFileExists(public_path('animations/chapter4-math-class8.html'));
        $this->assertFileExists(public_path('animations/quadrilaterals-class8.html'));
        $this->assertFileExists(public_path('animations/class8-quadrilaterals.html'));
    }

    public function test_ncert_class_8_has_number_play_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Investigating Numbers & Divisibility', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class8-math-number-play', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-number-play.html'));
        $this->assertFileExists(public_path('animations/chapter5-math-class8.html'));
        $this->assertFileExists(public_path('animations/number-play-class8.html'));
        $this->assertFileExists(public_path('animations/class8-number-play.html'));
    }

    public function test_ncert_class_8_has_distributive_property_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Distributive Property & Algebraic Multiplication', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class8-math-distributive-property', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-distributive-property.html'));
        $this->assertFileExists(public_path('animations/chapter6-math-class8.html'));
        $this->assertFileExists(public_path('animations/distributive-property-class8.html'));
        $this->assertFileExists(public_path('animations/class8-distributive-property.html'));
    }

    public function test_ncert_class_8_has_proportional_reasoning_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Comparing Quantities: Proportional Reasoning', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class8-math-proportional-reasoning', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-proportional-reasoning.html'));
        $this->assertFileExists(public_path('animations/chapter7-math-class8.html'));
        $this->assertFileExists(public_path('animations/proportional-reasoning-class8.html'));
        $this->assertFileExists(public_path('animations/class8-proportional-reasoning.html'));
    }

    public function test_ncert_class_8_has_percentages_applications_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Comparing Quantities: Percentages & Applications', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class8-math-percentages-applications', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-percentages-applications.html'));
        $this->assertFileExists(public_path('animations/chapter8-math-class8.html'));
        $this->assertFileExists(public_path('animations/percentages-applications-class8.html'));
        $this->assertFileExists(public_path('animations/class8-percentages-applications.html'));
    }

    public function test_ncert_class_8_has_baudhayana_pythagoras_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Baudhāyana-Pythagoras Theorem', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class8-math-baudhayana-pythagoras', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-baudhayana-pythagoras.html'));
        $this->assertFileExists(public_path('animations/chapter9-math-class8.html'));
        $this->assertFileExists(public_path('animations/baudhayana-pythagoras-class8.html'));
        $this->assertFileExists(public_path('animations/class8-baudhayana-pythagoras.html'));
        $this->assertFileExists(public_path('animations/the-baudhayana-pythagoras-theorem.html'));
    }

    public function test_ncert_class_8_has_proportional_reasoning_2_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Proportional Reasoning: Advanced Ratios & Inverse Variation', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class8-math-proportional-reasoning-2', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-proportional-reasoning-2.html'));
        $this->assertFileExists(public_path('animations/chapter10-math-class8.html'));
        $this->assertFileExists(public_path('animations/proportional-reasoning-2-class8.html'));
        $this->assertFileExists(public_path('animations/class8-proportional-reasoning-2.html'));
        $this->assertFileExists(public_path('animations/class8-math-inverse-proportions.html'));
        $this->assertFileExists(public_path('animations/inverse-proportions-class8.html'));
        $this->assertFileExists(public_path('animations/class8-inverse-proportions.html'));
    }

    public function test_ncert_class_8_has_geometric_themes_solids_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Exploring Geometric Themes: Fractals & Visualising Solids', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class8-math-geometric-themes-solids', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-geometric-themes-solids.html'));
        $this->assertFileExists(public_path('animations/chapter11-math-class8.html'));
        $this->assertFileExists(public_path('animations/geometric-themes-solids-class8.html'));
        $this->assertFileExists(public_path('animations/class8-geometric-themes-solids.html'));
        $this->assertFileExists(public_path('animations/class8-math-visualising-solids.html'));
        $this->assertFileExists(public_path('animations/visualising-solids-class8.html'));
        $this->assertFileExists(public_path('animations/class8-visualising-solids.html'));
        $this->assertFileExists(public_path('animations/geometric-themes-class8.html'));
    }

    public function test_ncert_class_8_has_data_handling_dots_lines_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Data Handling: Tales by Dots and Lines', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class8-math-data-handling-dots-lines', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-data-handling-dots-lines.html'));
        $this->assertFileExists(public_path('animations/chapter12-math-class8.html'));
        $this->assertFileExists(public_path('animations/data-handling-dots-lines-class8.html'));
        $this->assertFileExists(public_path('animations/class8-data-handling-dots-lines.html'));
        $this->assertFileExists(public_path('animations/class8-math-data-handling.html'));
        $this->assertFileExists(public_path('animations/data-handling-class8.html'));
        $this->assertFileExists(public_path('animations/class8-data-handling.html'));
        $this->assertFileExists(public_path('animations/tales-by-dots-and-lines.html'));
    }

    public function test_ncert_class_8_has_algebra_play_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Algebra Play', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertEquals('class8-math-algebra-play', $data['activeChapters'][12]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-algebra-play.html'));
        $this->assertFileExists(public_path('animations/chapter13-math-class8.html'));
        $this->assertFileExists(public_path('animations/algebra-play-class8.html'));
        $this->assertFileExists(public_path('animations/class8-algebra-play.html'));
        $this->assertFileExists(public_path('animations/class8-math-algebra.html'));
        $this->assertFileExists(public_path('animations/algebra-play.html'));
    }

    public function test_ncert_class_8_has_area_polygons_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Area', $data['activeChapters'][13]['name']);
        $this->assertTrue($data['activeChapters'][13]['has_multimedia']);
        $this->assertEquals('class8-math-area-polygons', $data['activeChapters'][13]['media_key']);
        $this->assertFileExists(public_path('animations/class8-math-area-polygons.html'));
        $this->assertFileExists(public_path('animations/chapter14-math-class8.html'));
        $this->assertFileExists(public_path('animations/area-polygons-class8.html'));
        $this->assertFileExists(public_path('animations/class8-area-polygons.html'));
        $this->assertFileExists(public_path('animations/class8-math-area.html'));
        $this->assertFileExists(public_path('animations/area-class8.html'));
    }

    public function test_ncert_class_8_has_microbes_health_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Microbes and Health', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class8-science-microbes-health', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-microbes-health.html'));
        $this->assertFileExists(public_path('animations/chapter1-science-class8.html'));
        $this->assertFileExists(public_path('animations/microbes-and-health-class8.html'));
        $this->assertFileExists(public_path('animations/class8-microbes-and-health.html'));
        $this->assertFileExists(public_path('animations/class8-science-microbes.html'));
        $this->assertFileExists(public_path('animations/microbes-and-health.html'));
    }

    public function test_ncert_class_8_has_cells_microbes_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Cell Structure and Functions', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class8-science-cells-microbes', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-cells-microbes.html'));
        $this->assertFileExists(public_path('animations/chapter2-science-class8.html'));
        $this->assertFileExists(public_path('animations/cell-structure-and-functions-class8.html'));
        $this->assertFileExists(public_path('animations/class8-cell-structure.html'));
        $this->assertFileExists(public_path('animations/cell-structure-and-functions.html'));
        $this->assertFileExists(public_path('animations/cells-and-microorganisms-class8.html'));
        $this->assertFileExists(public_path('animations/class8-cells-microbes.html'));
    }

    public function test_ncert_class_8_has_health_disease_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Health, Diseases and Prevention', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class8-science-health-disease', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-health-disease.html'));
        $this->assertFileExists(public_path('animations/chapter3-science-class8.html'));
        $this->assertFileExists(public_path('animations/health-and-disease-class8.html'));
        $this->assertFileExists(public_path('animations/class8-health-disease.html'));
        $this->assertFileExists(public_path('animations/class8-science-health.html'));
        $this->assertFileExists(public_path('animations/health-and-disease.html'));
        $this->assertFileExists(public_path('animations/health-disease-prevention-class8.html'));
    }

    public function test_ncert_class_8_has_electric_current_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Electric Current and Its Effects', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class8-science-electric-current', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-electric-current.html'));
        $this->assertFileExists(public_path('animations/chapter4-science-class8.html'));
        $this->assertFileExists(public_path('animations/electric-current-and-effects-class8.html'));
        $this->assertFileExists(public_path('animations/class8-electric-current.html'));
        $this->assertFileExists(public_path('animations/class8-science-electricity.html'));
        $this->assertFileExists(public_path('animations/electric-current-class8.html'));
        $this->assertFileExists(public_path('animations/electric-current-and-its-effects.html'));
    }

    public function test_ncert_class_8_has_force_buoyancy_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Force and Its Effects', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class8-science-force-buoyancy', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-force-buoyancy.html'));
        $this->assertFileExists(public_path('animations/chapter5-science-class8.html'));
        $this->assertFileExists(public_path('animations/force-and-buoyancy-class8.html'));
        $this->assertFileExists(public_path('animations/class8-force-buoyancy.html'));
        $this->assertFileExists(public_path('animations/class8-science-force.html'));
        $this->assertFileExists(public_path('animations/forces-and-pressure-class8.html'));
        $this->assertFileExists(public_path('animations/force-and-its-effects.html'));
    }

    public function test_ncert_class_8_has_pressure_winds_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Pressure, Winds, Storms and Cyclones', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class8-science-pressure-winds', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-pressure-winds.html'));
        $this->assertFileExists(public_path('animations/chapter6-science-class8.html'));
        $this->assertFileExists(public_path('animations/pressure-and-winds-class8.html'));
        $this->assertFileExists(public_path('animations/class8-pressure-winds.html'));
        $this->assertFileExists(public_path('animations/class8-science-pressure.html'));
        $this->assertFileExists(public_path('animations/winds-storms-cyclones-class8.html'));
        $this->assertFileExists(public_path('animations/pressure-winds-and-cyclones.html'));
    }

    public function test_ncert_class_8_has_particles_matter_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Particles and Matter', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class8-science-particles-matter', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-particles-matter.html'));
        $this->assertFileExists(public_path('animations/chapter7-science-class8.html'));
        $this->assertFileExists(public_path('animations/particles-and-matter-class8.html'));
        $this->assertFileExists(public_path('animations/class8-particles-matter.html'));
        $this->assertFileExists(public_path('animations/class8-science-particles.html'));
        $this->assertFileExists(public_path('animations/particulate-nature-matter-class8.html'));
        $this->assertFileExists(public_path('animations/particles-matter-class8.html'));
    }

    public function test_ncert_class_8_has_elements_compounds_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Elements, Compounds, and Mixtures', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class8-science-elements-compounds', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-elements-compounds.html'));
        $this->assertFileExists(public_path('animations/chapter8-science-class8.html'));
        $this->assertFileExists(public_path('animations/elements-compounds-and-mixtures.html'));
        $this->assertFileExists(public_path('animations/class8-elements-compounds.html'));
        $this->assertFileExists(public_path('animations/class8-science-elements.html'));
        $this->assertFileExists(public_path('animations/pure-substances-and-mixtures.html'));
        $this->assertFileExists(public_path('animations/elements-compounds-mixtures-class8.html'));
    }

    public function test_ncert_class_8_has_solutions_density_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Solutions, Solubility, and Density', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class8-science-solutions-density', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-solutions-density.html'));
        $this->assertFileExists(public_path('animations/chapter9-science-class8.html'));
        $this->assertFileExists(public_path('animations/solutions-solubility-and-density.html'));
        $this->assertFileExists(public_path('animations/class8-solutions-density.html'));
        $this->assertFileExists(public_path('animations/class8-science-solutions.html'));
        $this->assertFileExists(public_path('animations/nature-of-solutions-and-density.html'));
        $this->assertFileExists(public_path('animations/solutions-and-density-class8.html'));
    }

    public function test_ncert_class_8_has_light_optics_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Light and Optics', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class8-science-light-optics', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-light-optics.html'));
        $this->assertFileExists(public_path('animations/chapter10-science-class8.html'));
        $this->assertFileExists(public_path('animations/light-and-optics-class8.html'));
        $this->assertFileExists(public_path('animations/class8-light-optics.html'));
        $this->assertFileExists(public_path('animations/class8-science-light.html'));
        $this->assertFileExists(public_path('animations/reflection-and-refraction-class8.html'));
        $this->assertFileExists(public_path('animations/spherical-mirrors-and-lenses.html'));
    }

    public function test_ncert_class_8_has_astronomy_calendars_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Astronomy and Calendars', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class8-science-astronomy-calendars', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-astronomy-calendars.html'));
        $this->assertFileExists(public_path('animations/chapter11-science-class8.html'));
        $this->assertFileExists(public_path('animations/astronomy-and-calendars-class8.html'));
        $this->assertFileExists(public_path('animations/class8-astronomy-calendars.html'));
        $this->assertFileExists(public_path('animations/class8-science-astronomy.html'));
        $this->assertFileExists(public_path('animations/phases-of-the-moon-and-calendars.html'));
        $this->assertFileExists(public_path('animations/moon-phases-and-satellites.html'));
    }

    public function test_ncert_class_8_has_nature_harmony_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('How Nature Works in Harmony', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class8-science-nature-harmony', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-nature-harmony.html'));
        $this->assertFileExists(public_path('animations/chapter12-science-class8.html'));
        $this->assertFileExists(public_path('animations/how-nature-works-in-harmony.html'));
        $this->assertFileExists(public_path('animations/class8-nature-harmony.html'));
        $this->assertFileExists(public_path('animations/class8-science-ecosystems.html'));
        $this->assertFileExists(public_path('animations/nature-works-in-harmony-class8.html'));
        $this->assertFileExists(public_path('animations/ecosystems-and-communities.html'));
    }

    public function test_ncert_class_8_has_earth_life_planet_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class8', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class8',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class8', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Our Home: Earth, a Unique Life Sustaining Planet', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertEquals('class8-science-earth-life-planet', $data['activeChapters'][12]['media_key']);
        $this->assertFileExists(public_path('animations/class8-science-earth-life-planet.html'));
        $this->assertFileExists(public_path('animations/chapter13-science-class8.html'));
        $this->assertFileExists(public_path('animations/earth-unique-life-sustaining-planet.html'));
        $this->assertFileExists(public_path('animations/class8-earth-life-planet.html'));
        $this->assertFileExists(public_path('animations/class8-science-earth-planet.html'));
        $this->assertFileExists(public_path('animations/our-home-earth-unique-planet.html'));
        $this->assertFileExists(public_path('animations/earth-life-sustaining-planet.html'));
    }

    public function test_ncert_class_7_has_large_numbers_multimedia(): void
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
        $this->assertEquals('Large Numbers Around Us', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class7-math-large-numbers', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-large-numbers.html'));
        $this->assertFileExists(public_path('animations/chapter1-math-class7.html'));
        $this->assertFileExists(public_path('animations/large-numbers-around-us.html'));
        $this->assertFileExists(public_path('animations/class7-large-numbers.html'));
        $this->assertFileExists(public_path('animations/class7-math-large-numbers-around-us.html'));
        $this->assertFileExists(public_path('animations/numbers-around-us-class7.html'));
        $this->assertFileExists(public_path('animations/large-numbers-class7.html'));
    }

    public function test_ncert_class_7_has_arithmetic_expressions_multimedia(): void
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
        $this->assertEquals('Arithmetic Expressions', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class7-math-arithmetic-expressions', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-arithmetic-expressions.html'));
        $this->assertFileExists(public_path('animations/chapter2-math-class7.html'));
        $this->assertFileExists(public_path('animations/arithmetic-expressions.html'));
        $this->assertFileExists(public_path('animations/class7-arithmetic-expressions.html'));
        $this->assertFileExists(public_path('animations/class7-math-expressions.html'));
        $this->assertFileExists(public_path('animations/expressions-class7.html'));
        $this->assertFileExists(public_path('animations/arithmetic-expressions-class7.html'));
    }

    public function test_ncert_class_7_has_decimals_multimedia(): void
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
        $this->assertEquals('A Peek Beyond the Point (Decimals)', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class7-math-decimals', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-decimals.html'));
        $this->assertFileExists(public_path('animations/chapter3-math-class7.html'));
        $this->assertFileExists(public_path('animations/a-peek-beyond-the-point.html'));
        $this->assertFileExists(public_path('animations/class7-a-peek-beyond-the-point.html'));
        $this->assertFileExists(public_path('animations/class7-math-peek-beyond-the-point.html'));
        $this->assertFileExists(public_path('animations/decimals-class7.html'));
        $this->assertFileExists(public_path('animations/class7-decimals.html'));
    }

    public function test_ncert_class_7_has_expressions_letter_numbers_multimedia(): void
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
        $this->assertEquals('Expressions Using Letter-Numbers', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class7-math-expressions-letter-numbers', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-expressions-letter-numbers.html'));
        $this->assertFileExists(public_path('animations/chapter4-math-class7.html'));
        $this->assertFileExists(public_path('animations/expressions-using-letter-numbers.html'));
        $this->assertFileExists(public_path('animations/class7-expressions-letter-numbers.html'));
        $this->assertFileExists(public_path('animations/letter-numbers-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-algebraic-expressions.html'));
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
    }

    public function test_ncert_class_7_has_number_play_multimedia(): void
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
        $this->assertEquals('Number Play', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class7-math-number-play', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-number-play.html'));
        $this->assertFileExists(public_path('animations/chapter6-math-class7.html'));
        $this->assertFileExists(public_path('animations/number-play.html'));
        $this->assertFileExists(public_path('animations/class7-number-play.html'));
        $this->assertFileExists(public_path('animations/number-play-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-playing-with-numbers.html'));
        $this->assertFileExists(public_path('animations/playing-with-numbers-class7.html'));
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

    public function test_ncert_class_7_has_working_with_fractions_multimedia(): void
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
        $this->assertEquals('Working with Fractions', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class7-math-working-with-fractions', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-working-with-fractions.html'));
        $this->assertFileExists(public_path('animations/chapter8-math-class7.html'));
        $this->assertFileExists(public_path('animations/working-with-fractions.html'));
        $this->assertFileExists(public_path('animations/class7-working-with-fractions.html'));
        $this->assertFileExists(public_path('animations/working-with-fractions-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-fractions.html'));
        $this->assertFileExists(public_path('animations/fractions-class7.html'));
        $this->assertFileExists(public_path('animations/class7-fractions.html'));
    }

    public function test_ncert_class_7_has_geometric_twins_multimedia(): void
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
        $this->assertEquals('Geometric Twins (Congruence)', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class7-math-geometric-twins', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-geometric-twins.html'));
        $this->assertFileExists(public_path('animations/chapter9-math-class7.html'));
        $this->assertFileExists(public_path('animations/geometric-twins.html'));
        $this->assertFileExists(public_path('animations/class7-geometric-twins.html'));
        $this->assertFileExists(public_path('animations/geometric-twins-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-congruence.html'));
        $this->assertFileExists(public_path('animations/congruence-class7.html'));
        $this->assertFileExists(public_path('animations/class7-congruence.html'));
    }

    public function test_ncert_class_7_has_operations_with_integers_multimedia(): void
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
        $this->assertEquals('Operations with Integers', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class7-math-operations-with-integers', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-operations-with-integers.html'));
        $this->assertFileExists(public_path('animations/chapter10-math-class7.html'));
        $this->assertFileExists(public_path('animations/operations-with-integers.html'));
        $this->assertFileExists(public_path('animations/class7-operations-with-integers.html'));
        $this->assertFileExists(public_path('animations/operations-with-integers-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-integers.html'));
        $this->assertFileExists(public_path('animations/integers-class7.html'));
        $this->assertFileExists(public_path('animations/class7-integers.html'));
    }

    public function test_ncert_class_7_has_finding_common_ground_multimedia(): void
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
        $this->assertEquals('Finding Common Ground (HCF & LCM)', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class7-math-finding-common-ground', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-finding-common-ground.html'));
        $this->assertFileExists(public_path('animations/chapter11-math-class7.html'));
        $this->assertFileExists(public_path('animations/finding-common-ground.html'));
        $this->assertFileExists(public_path('animations/class7-finding-common-ground.html'));
        $this->assertFileExists(public_path('animations/finding-common-ground-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-hcf-lcm.html'));
        $this->assertFileExists(public_path('animations/hcf-lcm-class7.html'));
        $this->assertFileExists(public_path('animations/class7-hcf-lcm.html'));
    }

    public function test_cbse_syllabus_has_no_contents(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=cbse&subject=mathematics&class=class10', 'GET', [
            'syllabus' => 'cbse',
            'subject' => 'mathematics',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('cbse', $data['selectedSyllabus']);
        $this->assertEmpty($data['activeChapters']);
        $this->assertFalse($data['hasAnyMultimedia']);
    }

    public function test_scert_kerala_syllabus_has_no_contents(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=scert-kerala&subject=mathematics&class=class10', 'GET', [
            'syllabus' => 'scert-kerala',
            'subject' => 'mathematics',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('scert-kerala', $data['selectedSyllabus']);
        $this->assertEmpty($data['activeChapters']);
        $this->assertFalse($data['hasAnyMultimedia']);
    }

    public function test_ncert_class_12_has_all_multimedia_chapters(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class12', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class12',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('class12', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertCount(13, $data['activeChapters']);

        $this->assertEquals('Relations and Functions', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertStringContainsString('relations-and-functions.html', $data['activeChapters'][0]['media_url']);

        $this->assertEquals('Inverse Trigonometric Functions', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertStringContainsString('inverse-trigonometric-functions.html', $data['activeChapters'][1]['media_url']);

        $this->assertEquals('Matrices', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertStringContainsString('matrices.html', $data['activeChapters'][2]['media_url']);

        $this->assertEquals('Determinants', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertStringContainsString('determinants.html', $data['activeChapters'][3]['media_url']);

        $this->assertEquals('Continuity and Differentiability', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertStringContainsString('continuity-and-differentiability.html', $data['activeChapters'][4]['media_url']);

        $this->assertEquals('Application of Derivatives', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertStringContainsString('application-of-derivatives.html', $data['activeChapters'][5]['media_url']);

        $this->assertEquals('Integrals', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertStringContainsString('integrals.html', $data['activeChapters'][6]['media_url']);
        $this->assertEquals('Part - 2', $data['activeChapters'][6]['part']);

        $this->assertEquals('Application of Integrals', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertStringContainsString('application-of-integrals.html', $data['activeChapters'][7]['media_url']);
        $this->assertEquals('Part - 2', $data['activeChapters'][7]['part']);

        $this->assertEquals('Differential Equations', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertStringContainsString('differential-equations.html', $data['activeChapters'][8]['media_url']);
        $this->assertEquals('Part - 2', $data['activeChapters'][8]['part']);

        $this->assertEquals('Vector Algebra', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertStringContainsString('vector-algebra.html', $data['activeChapters'][9]['media_url']);
        $this->assertEquals('Part - 2', $data['activeChapters'][9]['part']);

        $this->assertEquals('Three Dimensional Geometry', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertStringContainsString('three-dimensional-geometry.html', $data['activeChapters'][10]['media_url']);
        $this->assertEquals('Part - 2', $data['activeChapters'][10]['part']);

        $this->assertEquals('Linear Programming', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertStringContainsString('linear-programming.html', $data['activeChapters'][11]['media_url']);
        $this->assertEquals('Part - 2', $data['activeChapters'][11]['part']);

        $this->assertEquals('Probability', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertStringContainsString('probability-class12.html', $data['activeChapters'][12]['media_url']);
        $this->assertEquals('Part - 2', $data['activeChapters'][12]['part']);
    }

    public function test_ncert_class_10_science_has_chemical_reactions_and_equations_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Chemical Reactions and Equations', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertStringContainsString('chemical-reactions-and-equations.html', $data['activeChapters'][0]['media_url']);
    }

    public function test_ncert_class_10_science_has_acids_bases_and_salts_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Acids, Bases and Salts', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertStringContainsString('acids-bases-and-salts.html', $data['activeChapters'][1]['media_url']);
    }

    public function test_ncert_class_10_science_has_metals_and_non_metals_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Metals and Non-metals', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertStringContainsString('metals-and-non-metals.html', $data['activeChapters'][2]['media_url']);
    }

    public function test_ncert_class_10_science_has_life_processes_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Life Processes', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertStringContainsString('life-processes.html', $data['activeChapters'][4]['media_url']);
    }

    public function test_ncert_class_10_science_has_control_and_coordination_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Control and Coordination', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertStringContainsString('control-and-coordination.html', $data['activeChapters'][5]['media_url']);
    }

    public function test_ncert_class_10_science_has_how_do_organisms_reproduce_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('How do Organisms Reproduce?', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertStringContainsString('how-do-organisms-reproduce.html', $data['activeChapters'][6]['media_url']);
    }

    public function test_ncert_class_10_science_has_light_reflection_and_refraction_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Light - Reflection and Refraction', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertStringContainsString('light-reflection-and-refraction.html', $data['activeChapters'][8]['media_url']);
    }

    public function test_ncert_class_10_science_has_the_human_eye_and_the_colourful_world_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Human Eye and the Colourful World', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertStringContainsString('the-human-eye-and-the-colourful-world.html', $data['activeChapters'][9]['media_url']);
    }

    public function test_ncert_class_10_science_has_electricity_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Electricity', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertStringContainsString('electricity.html', $data['activeChapters'][10]['media_url']);
    }

    public function test_ncert_class_10_science_has_magnetic_effects_of_electric_current_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Magnetic Effects of Electric Current', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertStringContainsString('magnetic-effects-of-electric-current.html', $data['activeChapters'][11]['media_url']);
    }

    public function test_ncert_class_10_science_has_our_environment_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Our Environment', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertStringContainsString('our-environment.html', $data['activeChapters'][12]['media_url']);
    }

    public function test_ncert_class_10_hindi_has_surdas_ke_pad_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=hindi&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'hindi',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('hindi', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('सूरदास के पद', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertStringContainsString('surdas-ke-pad.html', $data['activeChapters'][0]['media_url']);
    }

    public function test_ncert_class_10_hindi_has_ram_lakshman_parashuram_samvad_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=hindi&class=class10', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'hindi',
            'class' => 'class10',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('hindi', $data['selectedSubject']);
        $this->assertEquals('class10', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('राम-लक्ष्मण-परशुराम संवाद', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertStringContainsString('ram-lakshman-parashuram-samvad.html', $data['activeChapters'][1]['media_url']);
    }

    public function test_all_multimedia_files_have_last_slide_message_and_no_next_option(): void
    {
        $files = glob(public_path('animations/*.html'));
        $this->assertCount(399, $files);

        foreach ($files as $file) {
            $content = file_get_contents($file);
            $filename = basename($file);

            $this->assertStringContainsString('id="lastSlideNotice"', $content, "File {$filename} must have lastSlideNotice container");
            $this->assertStringContainsString('You have reached the last slide of this chapter', $content, "File {$filename} must show the exact last slide message");
            $this->assertTrue(
                str_contains($content, 'nextBtn.style.display = "none"') || str_contains($content, "nextBtn.style.display = 'none'"),
                "File {$filename} must hide nextBtn on last slide"
            );
        }
    }

    public function test_class12_multimedia_slides_have_part_1_subheading(): void
    {
        $class12Files = [
            'relations-and-functions.html',
            'inverse-trigonometric-functions.html',
            'matrices.html',
            'determinants.html',
            'continuity-and-differentiability.html',
            'application-of-derivatives.html',
        ];

        foreach ($class12Files as $filename) {
            $path = public_path("animations/{$filename}");
            $this->assertFileExists($path);
            $content = file_get_contents($path);

            $this->assertStringContainsString('Part - 1', $content, "File {$filename} must contain 'Part - 1' subheading/badge");
        }
    }

    public function test_class12_part_2_multimedia_slides_have_part_2_subheading(): void
    {
        $part2Files = [
            'integrals.html',
            'application-of-integrals.html',
            'differential-equations.html',
            'vector-algebra.html',
            'three-dimensional-geometry.html',
            'linear-programming.html',
            'probability-class12.html',
        ];

        foreach ($part2Files as $filename) {
            $path = public_path("animations/{$filename}");
            $this->assertFileExists($path);
            $content = file_get_contents($path);

            $this->assertStringContainsString('Part - 2', $content, "File {$filename} must contain 'Part - 2' subheading/badge");
        }
    }
}
