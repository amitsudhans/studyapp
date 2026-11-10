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

    public function test_ncert_class_6_has_patterns_in_mathematics_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Patterns', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class6-math-patterns-in-mathematics', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-patterns-in-mathematics.html'));
        $this->assertFileExists(public_path('animations/chapter1-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter1.html'));
        $this->assertFileExists(public_path('animations/class6-patterns-in-mathematics.html'));
        $this->assertFileExists(public_path('animations/class6-math-patterns.html'));
        $this->assertFileExists(public_path('animations/patterns-in-mathematics-class6.html'));
        $this->assertFileExists(public_path('animations/patterns-in-mathematics.html'));
        $this->assertFileExists(public_path('animations/patterns-math-class6.html'));
        $this->assertFileExists(public_path('animations/patterns-class6.html'));
        $this->assertFileExists(public_path('animations/patterns.html'));
        $this->assertFileExists(public_path('animations/class6-patterns.html'));
    }

    public function test_ncert_class_6_has_lines_and_angles_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Lines and Angles', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class6-math-lines-and-angles', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-lines-and-angles.html'));
        $this->assertFileExists(public_path('animations/chapter2-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter2.html'));
        $this->assertFileExists(public_path('animations/class6-lines-and-angles.html'));
        $this->assertFileExists(public_path('animations/class6-math-lines-angles.html'));
        $this->assertFileExists(public_path('animations/lines-and-angles-class6.html'));
        $this->assertFileExists(public_path('animations/lines-angles-class6.html'));
        $this->assertFileExists(public_path('animations/lines-angles.html'));
        $this->assertFileExists(public_path('animations/lines-class6.html'));
        $this->assertFileExists(public_path('animations/angles-class6.html'));
        $this->assertFileExists(public_path('animations/class6-lines.html'));
    }

    public function test_ncert_class_6_has_number_play_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Numbers', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class6-math-number-play', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-number-play.html'));
        $this->assertFileExists(public_path('animations/chapter3-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter3.html'));
        $this->assertFileExists(public_path('animations/class6-number-play.html'));
        $this->assertFileExists(public_path('animations/number-play-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-numbers.html'));
        $this->assertFileExists(public_path('animations/numbers-play-class6.html'));
        $this->assertFileExists(public_path('animations/playing-with-numbers-class6.html'));
        $this->assertFileExists(public_path('animations/class6-playing-with-numbers.html'));
        $this->assertFileExists(public_path('animations/numberplay-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-play.html'));
    }

    public function test_ncert_class_6_has_data_handling_and_presentation_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Data', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class6-math-data-handling-and-presentation', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-data-handling-and-presentation.html'));
        $this->assertFileExists(public_path('animations/chapter4-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter4.html'));
        $this->assertFileExists(public_path('animations/class6-data-handling-and-presentation.html'));
        $this->assertFileExists(public_path('animations/class6-math-data-handling.html'));
        $this->assertFileExists(public_path('animations/data-handling-and-presentation-class6.html'));
        $this->assertFileExists(public_path('animations/data-handling-and-presentation.html'));
        $this->assertFileExists(public_path('animations/data-handling-class6.html'));
        $this->assertFileExists(public_path('animations/data-presentation-class6.html'));
        $this->assertFileExists(public_path('animations/class6-data-handling.html'));
        $this->assertFileExists(public_path('animations/class6-data.html'));
    }

    public function test_ncert_class_6_has_prime_time_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Primes', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class6-math-prime-time', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-prime-time.html'));
        $this->assertFileExists(public_path('animations/chapter5-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter5.html'));
        $this->assertFileExists(public_path('animations/class6-prime-time.html'));
        $this->assertFileExists(public_path('animations/class6-math-primes.html'));
        $this->assertFileExists(public_path('animations/prime-time-class6.html'));
        $this->assertFileExists(public_path('animations/prime-time.html'));
        $this->assertFileExists(public_path('animations/primes-class6.html'));
        $this->assertFileExists(public_path('animations/class6-primes.html'));
        $this->assertFileExists(public_path('animations/factors-multiples-class6.html'));
        $this->assertFileExists(public_path('animations/class6-factors-multiples.html'));
    }

    public function test_ncert_class_6_has_perimeter_and_area_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Perimeter and Area', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class6-math-perimeter-and-area', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-perimeter-and-area.html'));
        $this->assertFileExists(public_path('animations/chapter6-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter6.html'));
        $this->assertFileExists(public_path('animations/class6-perimeter-and-area.html'));
        $this->assertFileExists(public_path('animations/class6-math-perimeter-area.html'));
        $this->assertFileExists(public_path('animations/perimeter-and-area-class6.html'));
        $this->assertFileExists(public_path('animations/perimeter-and-area.html'));
        $this->assertFileExists(public_path('animations/perimeter-area-class6.html'));
        $this->assertFileExists(public_path('animations/perimeter-class6.html'));
        $this->assertFileExists(public_path('animations/area-class6.html'));
        $this->assertFileExists(public_path('animations/class6-perimeter.html'));
    }

    public function test_ncert_class_6_has_fractions_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Fractions', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class6-math-fractions', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-fractions.html'));
        $this->assertFileExists(public_path('animations/chapter7-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter7.html'));
        $this->assertFileExists(public_path('animations/class6-fractions.html'));
        $this->assertFileExists(public_path('animations/fractions-class6.html'));
        $this->assertFileExists(public_path('animations/fractions.html'));
        $this->assertFileExists(public_path('animations/class6-math-fractions-lab.html'));
        $this->assertFileExists(public_path('animations/fraction-units-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-fraction.html'));
        $this->assertFileExists(public_path('animations/fractions-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-fraction.html'));
    }

    public function test_ncert_class_6_has_constructions_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Constructions', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class6-math-constructions', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-constructions.html'));
        $this->assertFileExists(public_path('animations/chapter8-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter8.html'));
        $this->assertFileExists(public_path('animations/class6-constructions.html'));
        $this->assertFileExists(public_path('animations/constructions-class6.html'));
        $this->assertFileExists(public_path('animations/constructions.html'));
        $this->assertFileExists(public_path('animations/class6-math-playing-with-constructions.html'));
        $this->assertFileExists(public_path('animations/playing-with-constructions-class6.html'));
        $this->assertFileExists(public_path('animations/geometric-constructions-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-geometric-constructions.html'));
        $this->assertFileExists(public_path('animations/class6-construction.html'));
    }

    public function test_ncert_class_6_has_symmetry_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Symmetry', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class6-math-symmetry', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-symmetry.html'));
        $this->assertFileExists(public_path('animations/chapter9-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter9.html'));
        $this->assertFileExists(public_path('animations/class6-symmetry.html'));
        $this->assertFileExists(public_path('animations/symmetry-class6.html'));
        $this->assertFileExists(public_path('animations/symmetry.html'));
        $this->assertFileExists(public_path('animations/class6-math-symmetry-lab.html'));
        $this->assertFileExists(public_path('animations/reflection-symmetry-class6.html'));
        $this->assertFileExists(public_path('animations/rotational-symmetry-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-lines-of-symmetry.html'));
        $this->assertFileExists(public_path('animations/class6-symmetry-lab.html'));
    }

    public function test_ncert_class_6_has_integers_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class6',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Other Side of Zero', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class6-math-integers', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class6-math-integers.html'));
        $this->assertFileExists(public_path('animations/chapter10-math-class6.html'));
        $this->assertFileExists(public_path('animations/class6-math-chapter10.html'));
        $this->assertFileExists(public_path('animations/class6-integers.html'));
        $this->assertFileExists(public_path('animations/integers-class6.html'));
        $this->assertFileExists(public_path('animations/integers.html'));
        $this->assertFileExists(public_path('animations/class6-math-integers-lab.html'));
        $this->assertFileExists(public_path('animations/the-other-side-of-zero-class6.html'));
        $this->assertFileExists(public_path('animations/class6-the-other-side-of-zero.html'));
        $this->assertFileExists(public_path('animations/class6-math-the-other-side-of-zero.html'));
        $this->assertFileExists(public_path('animations/class6-integers-lab.html'));
    }

    public function test_ncert_class_3_has_whats_in_a_name_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals("What's in a Name?", $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class3-maths-whats-in-a-name', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-whats-in-a-name.html'));
        $this->assertFileExists(public_path('animations/chapter1-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter1.html'));
        $this->assertFileExists(public_path('animations/class3-whats-in-a-name.html'));
        $this->assertFileExists(public_path('animations/whats-in-a-name-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-whats-in-a-name-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-whats-in-a-name.html'));
        $this->assertFileExists(public_path('animations/class3-whats-in-a-name-lab.html'));
    }

    public function test_ncert_class_3_has_toy_joy_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Toy Joy', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class3-maths-toy-joy', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-toy-joy.html'));
        $this->assertFileExists(public_path('animations/chapter2-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter2.html'));
        $this->assertFileExists(public_path('animations/class3-toy-joy.html'));
        $this->assertFileExists(public_path('animations/toy-joy-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-toy-joy-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-toy-joy.html'));
        $this->assertFileExists(public_path('animations/class3-toy-joy-lab.html'));
    }

    public function test_ncert_class_3_has_double_century_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Double Century', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class3-maths-double-century', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-double-century.html'));
        $this->assertFileExists(public_path('animations/chapter3-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter3.html'));
        $this->assertFileExists(public_path('animations/class3-double-century.html'));
        $this->assertFileExists(public_path('animations/double-century-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-double-century-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-double-century.html'));
        $this->assertFileExists(public_path('animations/class3-double-century-lab.html'));
    }

    public function test_ncert_class_3_has_vacation_with_my_nani_maa_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Vacation with My Nani Maa', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class3-maths-vacation-with-my-nani-maa', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-vacation-with-my-nani-maa.html'));
        $this->assertFileExists(public_path('animations/chapter4-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter4.html'));
        $this->assertFileExists(public_path('animations/class3-vacation-with-my-nani-maa.html'));
        $this->assertFileExists(public_path('animations/vacation-with-my-nani-maa-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-vacation-with-my-nani-maa-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-vacation-with-my-nani-maa.html'));
        $this->assertFileExists(public_path('animations/class3-vacation-with-my-nani-maa-lab.html'));
    }

    public function test_ncert_class_3_has_fun_with_shapes_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Fun with Shapes', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class3-maths-fun-with-shapes', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-fun-with-shapes.html'));
        $this->assertFileExists(public_path('animations/chapter5-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter5.html'));
        $this->assertFileExists(public_path('animations/class3-fun-with-shapes.html'));
        $this->assertFileExists(public_path('animations/fun-with-shapes-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-fun-with-shapes-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-fun-with-shapes.html'));
        $this->assertFileExists(public_path('animations/class3-fun-with-shapes-lab.html'));
    }

    public function test_ncert_class_3_has_house_of_hundreds_1_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('House of Hundreds - 1', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class3-maths-house-of-hundreds-1', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-house-of-hundreds-1.html'));
        $this->assertFileExists(public_path('animations/chapter6-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter6.html'));
        $this->assertFileExists(public_path('animations/class3-house-of-hundreds-1.html'));
        $this->assertFileExists(public_path('animations/house-of-hundreds-1-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-house-of-hundreds-1-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-house-of-hundreds-1.html'));
        $this->assertFileExists(public_path('animations/class3-house-of-hundreds-1-lab.html'));
    }

    public function test_ncert_class_3_has_raksha_bandhan_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Raksha Bandhan', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class3-maths-raksha-bandhan', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-raksha-bandhan.html'));
        $this->assertFileExists(public_path('animations/chapter7-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter7.html'));
        $this->assertFileExists(public_path('animations/class3-raksha-bandhan.html'));
        $this->assertFileExists(public_path('animations/raksha-bandhan-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-raksha-bandhan-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-raksha-bandhan.html'));
        $this->assertFileExists(public_path('animations/class3-raksha-bandhan-lab.html'));
    }

    public function test_ncert_class_3_has_fair_share_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Fair Share', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class3-maths-fair-share', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-fair-share.html'));
        $this->assertFileExists(public_path('animations/chapter8-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter8.html'));
        $this->assertFileExists(public_path('animations/class3-fair-share.html'));
        $this->assertFileExists(public_path('animations/fair-share-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-fair-share-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-fair-share.html'));
        $this->assertFileExists(public_path('animations/class3-fair-share-lab.html'));
    }

    public function test_ncert_class_3_has_house_of_hundreds_2_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('House of Hundreds - II', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class3-maths-house-of-hundreds-2', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-house-of-hundreds-2.html'));
        $this->assertFileExists(public_path('animations/chapter9-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter9.html'));
        $this->assertFileExists(public_path('animations/class3-house-of-hundreds-2.html'));
        $this->assertFileExists(public_path('animations/house-of-hundreds-2-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-house-of-hundreds-2-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-house-of-hundreds-2.html'));
        $this->assertFileExists(public_path('animations/class3-house-of-hundreds-2-lab.html'));
    }

    public function test_ncert_class_3_has_fun_at_class_party_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Fun at Class Party!', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class3-maths-fun-at-class-party', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-fun-at-class-party.html'));
        $this->assertFileExists(public_path('animations/chapter10-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter10.html'));
        $this->assertFileExists(public_path('animations/class3-fun-at-class-party.html'));
        $this->assertFileExists(public_path('animations/fun-at-class-party-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-fun-at-class-party-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-fun-at-class-party.html'));
        $this->assertFileExists(public_path('animations/class3-fun-at-class-party-lab.html'));
    }

    public function test_ncert_class_3_has_filling_and_lifting_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Filling and Lifting', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class3-maths-filling-and-lifting', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-filling-and-lifting.html'));
        $this->assertFileExists(public_path('animations/chapter11-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter11.html'));
        $this->assertFileExists(public_path('animations/class3-filling-and-lifting.html'));
        $this->assertFileExists(public_path('animations/filling-and-lifting-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-filling-and-lifting-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-filling-and-lifting.html'));
        $this->assertFileExists(public_path('animations/class3-filling-and-lifting-lab.html'));
    }

    public function test_ncert_class_3_has_give_and_take_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Give and Take', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class3-maths-give-and-take', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-give-and-take.html'));
        $this->assertFileExists(public_path('animations/chapter12-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter12.html'));
        $this->assertFileExists(public_path('animations/class3-give-and-take.html'));
        $this->assertFileExists(public_path('animations/give-and-take-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-give-and-take-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-give-and-take.html'));
        $this->assertFileExists(public_path('animations/class3-give-and-take-lab.html'));
    }

    public function test_ncert_class_3_has_time_goes_on_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Time Goes On', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertEquals('class3-maths-time-goes-on', $data['activeChapters'][12]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-time-goes-on.html'));
        $this->assertFileExists(public_path('animations/chapter13-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter13.html'));
        $this->assertFileExists(public_path('animations/class3-time-goes-on.html'));
        $this->assertFileExists(public_path('animations/time-goes-on-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-time-goes-on-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-time-goes-on.html'));
        $this->assertFileExists(public_path('animations/class3-time-goes-on-lab.html'));
    }

    public function test_ncert_class_3_has_the_surajkund_fair_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Surajkund Fair', $data['activeChapters'][13]['name']);
        $this->assertTrue($data['activeChapters'][13]['has_multimedia']);
        $this->assertEquals('class3-maths-the-surajkund-fair', $data['activeChapters'][13]['media_key']);
        $this->assertFileExists(public_path('animations/class3-maths-the-surajkund-fair.html'));
        $this->assertFileExists(public_path('animations/chapter14-maths-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-chapter14.html'));
        $this->assertFileExists(public_path('animations/class3-the-surajkund-fair.html'));
        $this->assertFileExists(public_path('animations/the-surajkund-fair-class3.html'));
        $this->assertFileExists(public_path('animations/class3-maths-the-surajkund-fair-lab.html'));
        $this->assertFileExists(public_path('animations/class3-math-the-surajkund-fair.html'));
        $this->assertFileExists(public_path('animations/class3-the-surajkund-fair-lab.html'));
    }

    public function test_ncert_class_4_has_shapes_around_us_multimedia(): void
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
        $this->assertEquals('Shapes Around Us', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class4-maths-shapes-around-us', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-shapes-around-us.html'));
        $this->assertFileExists(public_path('animations/chapter1-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter1.html'));
        $this->assertFileExists(public_path('animations/class4-shapes-around-us.html'));
        $this->assertFileExists(public_path('animations/shapes-around-us-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-shapes-around-us-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-shapes-around-us.html'));
        $this->assertFileExists(public_path('animations/class4-shapes-lab.html'));
    }

    public function test_ncert_class_4_has_hide_and_seek_multimedia(): void
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
        $this->assertEquals('Hide and Seek', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class4-maths-hide-and-seek', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-hide-and-seek.html'));
        $this->assertFileExists(public_path('animations/chapter2-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter2.html'));
        $this->assertFileExists(public_path('animations/class4-hide-and-seek.html'));
        $this->assertFileExists(public_path('animations/hide-and-seek-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-hide-and-seek-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-hide-and-seek.html'));
        $this->assertFileExists(public_path('animations/class4-hide-seek-lab.html'));
    }

    public function test_ncert_class_4_has_patterns_around_us_multimedia(): void
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
        $this->assertEquals('Patterns Around Us', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class4-maths-patterns-around-us', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-patterns-around-us.html'));
        $this->assertFileExists(public_path('animations/chapter3-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter3.html'));
        $this->assertFileExists(public_path('animations/class4-patterns-around-us.html'));
        $this->assertFileExists(public_path('animations/patterns-around-us-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-patterns-around-us-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-patterns-around-us.html'));
        $this->assertFileExists(public_path('animations/class4-patterns-lab.html'));
    }

    public function test_ncert_class_4_has_thousands_around_us_multimedia(): void
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
        $this->assertEquals('Thousands Around Us', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class4-maths-thousands-around-us', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-thousands-around-us.html'));
        $this->assertFileExists(public_path('animations/chapter4-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter4.html'));
        $this->assertFileExists(public_path('animations/class4-thousands-around-us.html'));
        $this->assertFileExists(public_path('animations/thousands-around-us-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-thousands-around-us-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-thousands-around-us.html'));
        $this->assertFileExists(public_path('animations/class4-thousands-lab.html'));
    }

    public function test_ncert_class_4_has_sharing_and_measuring_multimedia(): void
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
        $this->assertEquals('Sharing and Measuring', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class4-maths-sharing-and-measuring', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-sharing-and-measuring.html'));
        $this->assertFileExists(public_path('animations/chapter5-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter5.html'));
        $this->assertFileExists(public_path('animations/class4-sharing-and-measuring.html'));
        $this->assertFileExists(public_path('animations/sharing-and-measuring-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-sharing-and-measuring-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-sharing-and-measuring.html'));
        $this->assertFileExists(public_path('animations/class4-sharing-measuring-lab.html'));
    }

    public function test_ncert_class_4_has_measuring_length_multimedia(): void
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
        $this->assertEquals('Measuring Length', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class4-maths-measuring-length', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-measuring-length.html'));
        $this->assertFileExists(public_path('animations/chapter6-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter6.html'));
        $this->assertFileExists(public_path('animations/class4-measuring-length.html'));
        $this->assertFileExists(public_path('animations/measuring-length-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-measuring-length-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-measuring-length.html'));
        $this->assertFileExists(public_path('animations/class4-measuring-length-lab.html'));
    }

    public function test_ncert_class_4_has_the_cleanest_village_multimedia(): void
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

    public function test_ncert_class_4_has_weigh_it_pour_it_multimedia(): void
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
        $this->assertEquals('Weigh It, Pour It', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class4-maths-weigh-it-pour-it', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-weigh-it-pour-it.html'));
        $this->assertFileExists(public_path('animations/chapter8-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter8.html'));
        $this->assertFileExists(public_path('animations/class4-weigh-it-pour-it.html'));
        $this->assertFileExists(public_path('animations/weigh-it-pour-it-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-weigh-it-pour-it-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-weigh-it-pour-it.html'));
        $this->assertFileExists(public_path('animations/class4-weigh-pour-lab.html'));
    }

    public function test_ncert_class_4_has_equal_groups_multimedia(): void
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
        $this->assertEquals('Equal Groups', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class4-maths-equal-groups', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-equal-groups.html'));
        $this->assertFileExists(public_path('animations/chapter9-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter9.html'));
        $this->assertFileExists(public_path('animations/class4-equal-groups.html'));
        $this->assertFileExists(public_path('animations/equal-groups-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-equal-groups-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-equal-groups.html'));
        $this->assertFileExists(public_path('animations/class4-equal-groups-lab.html'));
    }

    public function test_ncert_class_4_has_elephants_tigers_leopards_multimedia(): void
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
        $this->assertEquals('Elephants, Tigers, and Leopards', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class4-maths-elephants-tigers-leopards', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-elephants-tigers-leopards.html'));
        $this->assertFileExists(public_path('animations/chapter10-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter10.html'));
        $this->assertFileExists(public_path('animations/class4-elephants-tigers-leopards.html'));
        $this->assertFileExists(public_path('animations/elephants-tigers-leopards-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-elephants-tigers-leopards-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-elephants-tigers-leopards.html'));
        $this->assertFileExists(public_path('animations/class4-wildlife-census-lab.html'));
    }

    public function test_ncert_class_4_has_fun_with_symmetry_multimedia(): void
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
        $this->assertEquals('Fun with Symmetry', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class4-maths-fun-with-symmetry', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-fun-with-symmetry.html'));
        $this->assertFileExists(public_path('animations/chapter11-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter11.html'));
        $this->assertFileExists(public_path('animations/class4-fun-with-symmetry.html'));
        $this->assertFileExists(public_path('animations/fun-with-symmetry-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-fun-with-symmetry-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-fun-with-symmetry.html'));
        $this->assertFileExists(public_path('animations/class4-symmetry-lab.html'));
    }

    public function test_ncert_class_4_has_ticking_clocks_turning_calendar_multimedia(): void
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
        $this->assertEquals('Ticking Clocks and Turning Calendar', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class4-maths-ticking-clocks-turning-calendar', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-ticking-clocks-turning-calendar.html'));
        $this->assertFileExists(public_path('animations/chapter12-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter12.html'));
        $this->assertFileExists(public_path('animations/class4-ticking-clocks-turning-calendar.html'));
        $this->assertFileExists(public_path('animations/ticking-clocks-turning-calendar-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-ticking-clocks-turning-calendar-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-ticking-clocks-turning-calendar.html'));
        $this->assertFileExists(public_path('animations/class4-clocks-calendar-lab.html'));
    }

    public function test_ncert_class_4_has_the_transport_museum_multimedia(): void
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
        $this->assertEquals('The Transport Museum', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertEquals('class4-maths-the-transport-museum', $data['activeChapters'][12]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-the-transport-museum.html'));
        $this->assertFileExists(public_path('animations/chapter13-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter13.html'));
        $this->assertFileExists(public_path('animations/class4-the-transport-museum.html'));
        $this->assertFileExists(public_path('animations/the-transport-museum-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-the-transport-museum-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-the-transport-museum.html'));
        $this->assertFileExists(public_path('animations/class4-transport-museum-lab.html'));
    }

    public function test_ncert_class_4_has_data_handling_multimedia(): void
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
        $this->assertEquals('Data Handling', $data['activeChapters'][13]['name']);
        $this->assertTrue($data['activeChapters'][13]['has_multimedia']);
        $this->assertEquals('class4-maths-data-handling', $data['activeChapters'][13]['media_key']);
        $this->assertFileExists(public_path('animations/class4-maths-data-handling.html'));
        $this->assertFileExists(public_path('animations/chapter14-maths-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-chapter14.html'));
        $this->assertFileExists(public_path('animations/class4-data-handling.html'));
        $this->assertFileExists(public_path('animations/data-handling-class4.html'));
        $this->assertFileExists(public_path('animations/class4-maths-data-handling-lab.html'));
        $this->assertFileExists(public_path('animations/class4-math-data-handling.html'));
        $this->assertFileExists(public_path('animations/class4-data-handling-lab.html'));
    }

    public function test_ncert_class_5_has_we_the_travellers_1_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('We the Travellers - I', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class5-maths-we-the-travellers-1', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-we-the-travellers-1.html'));
        $this->assertFileExists(public_path('animations/chapter1-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter1.html'));
        $this->assertFileExists(public_path('animations/class5-we-the-travellers-1.html'));
        $this->assertFileExists(public_path('animations/we-the-travellers-1-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-travellers.html'));
        $this->assertFileExists(public_path('animations/class5-maths-travellers-lab.html'));
        $this->assertFileExists(public_path('animations/class5-travellers.html'));
    }

    public function test_ncert_class_5_has_fractions_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Fractions', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class5-maths-fractions', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-fractions.html'));
        $this->assertFileExists(public_path('animations/chapter2-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter2.html'));
        $this->assertFileExists(public_path('animations/class5-fractions.html'));
        $this->assertFileExists(public_path('animations/fractions-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-fractions-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-fractions.html'));
        $this->assertFileExists(public_path('animations/class5-fractions-lab.html'));
    }

    public function test_ncert_class_5_has_angles_as_turns_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Angles as Turns', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class5-maths-angles-as-turns', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-angles-as-turns.html'));
        $this->assertFileExists(public_path('animations/chapter3-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter3.html'));
        $this->assertFileExists(public_path('animations/class5-angles-as-turns.html'));
        $this->assertFileExists(public_path('animations/angles-as-turns-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-angles-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-angles.html'));
        $this->assertFileExists(public_path('animations/class5-angles-lab.html'));
    }

    public function test_ncert_class_5_has_we_the_travellers_2_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('We the Travellers - II', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class5-maths-we-the-travellers-2', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-we-the-travellers-2.html'));
        $this->assertFileExists(public_path('animations/chapter4-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter4.html'));
        $this->assertFileExists(public_path('animations/class5-we-the-travellers-2.html'));
        $this->assertFileExists(public_path('animations/we-the-travellers-2-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-travellers-2-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-travellers-2.html'));
        $this->assertFileExists(public_path('animations/class5-travellers-2-lab.html'));
    }

    public function test_ncert_class_5_has_far_and_near_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Far and Near', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class5-maths-far-and-near', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-far-and-near.html'));
        $this->assertFileExists(public_path('animations/chapter5-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter5.html'));
        $this->assertFileExists(public_path('animations/class5-far-and-near.html'));
        $this->assertFileExists(public_path('animations/far-and-near-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-far-and-near-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-far-and-near.html'));
        $this->assertFileExists(public_path('animations/class5-far-and-near-lab.html'));
    }

    public function test_ncert_class_5_has_the_dairy_farm_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Dairy Farm', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class5-maths-the-dairy-farm', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-the-dairy-farm.html'));
        $this->assertFileExists(public_path('animations/chapter6-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter6.html'));
        $this->assertFileExists(public_path('animations/class5-the-dairy-farm.html'));
        $this->assertFileExists(public_path('animations/the-dairy-farm-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-dairy-farm-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-dairy-farm.html'));
        $this->assertFileExists(public_path('animations/class5-dairy-farm-lab.html'));
    }

    public function test_ncert_class_5_has_shapes_and_patterns_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Shapes and Patterns', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class5-maths-shapes-and-patterns', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-shapes-and-patterns.html'));
        $this->assertFileExists(public_path('animations/chapter7-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter7.html'));
        $this->assertFileExists(public_path('animations/class5-shapes-and-patterns.html'));
        $this->assertFileExists(public_path('animations/shapes-and-patterns-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-shapes-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-shapes-and-patterns.html'));
        $this->assertFileExists(public_path('animations/class5-shapes-lab.html'));
    }

    public function test_ncert_class_5_has_weight_and_capacity_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Weight and Capacity', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class5-maths-weight-and-capacity', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-weight-and-capacity.html'));
        $this->assertFileExists(public_path('animations/chapter8-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter8.html'));
        $this->assertFileExists(public_path('animations/class5-weight-and-capacity.html'));
        $this->assertFileExists(public_path('animations/weight-and-capacity-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-weight-capacity-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-weight-and-capacity.html'));
        $this->assertFileExists(public_path('animations/class5-weight-capacity-lab.html'));
    }

    public function test_ncert_class_5_has_coconut_farm_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Coconut Farm', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class5-maths-coconut-farm', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-coconut-farm.html'));
        $this->assertFileExists(public_path('animations/chapter9-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter9.html'));
        $this->assertFileExists(public_path('animations/class5-coconut-farm.html'));
        $this->assertFileExists(public_path('animations/coconut-farm-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-coconut-farm-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-coconut-farm.html'));
        $this->assertFileExists(public_path('animations/class5-coconut-lab.html'));
    }

    public function test_ncert_class_5_has_symmetrical_designs_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Symmetrical Designs', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class5-maths-symmetrical-designs', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-symmetrical-designs.html'));
        $this->assertFileExists(public_path('animations/chapter10-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter10.html'));
        $this->assertFileExists(public_path('animations/class5-symmetrical-designs.html'));
        $this->assertFileExists(public_path('animations/symmetrical-designs-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-symmetrical-designs-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-symmetrical-designs.html'));
        $this->assertFileExists(public_path('animations/class5-symmetry-lab.html'));
    }

    public function test_ncert_class_5_has_grandmothers_quilt_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals("Grandmother's Quilt", $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class5-maths-grandmothers-quilt', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-grandmothers-quilt.html'));
        $this->assertFileExists(public_path('animations/chapter11-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter11.html'));
        $this->assertFileExists(public_path('animations/class5-grandmothers-quilt.html'));
        $this->assertFileExists(public_path('animations/grandmothers-quilt-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-grandmothers-quilt-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-grandmothers-quilt.html'));
        $this->assertFileExists(public_path('animations/class5-quilt-lab.html'));
    }

    public function test_ncert_class_5_has_racing_seconds_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Racing Seconds', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class5-maths-racing-seconds', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-racing-seconds.html'));
        $this->assertFileExists(public_path('animations/chapter12-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter12.html'));
        $this->assertFileExists(public_path('animations/class5-racing-seconds.html'));
        $this->assertFileExists(public_path('animations/racing-seconds-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-racing-seconds-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-racing-seconds.html'));
        $this->assertFileExists(public_path('animations/class5-seconds-lab.html'));
    }

    public function test_ncert_class_5_has_animal_jumps_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Animal Jumps', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertEquals('class5-maths-animal-jumps', $data['activeChapters'][12]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-animal-jumps.html'));
        $this->assertFileExists(public_path('animations/chapter13-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter13.html'));
        $this->assertFileExists(public_path('animations/class5-animal-jumps.html'));
        $this->assertFileExists(public_path('animations/animal-jumps-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-animal-jumps-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-animal-jumps.html'));
        $this->assertFileExists(public_path('animations/class5-jumps-lab.html'));
    }

    public function test_ncert_class_5_has_maps_and_locations_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Maps and Locations', $data['activeChapters'][13]['name']);
        $this->assertTrue($data['activeChapters'][13]['has_multimedia']);
        $this->assertEquals('class5-maths-maps-and-locations', $data['activeChapters'][13]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-maps-and-locations.html'));
        $this->assertFileExists(public_path('animations/chapter14-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter14.html'));
        $this->assertFileExists(public_path('animations/class5-maps-and-locations.html'));
        $this->assertFileExists(public_path('animations/maps-and-locations-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-maps-and-locations-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-maps-and-locations.html'));
        $this->assertFileExists(public_path('animations/class5-maps-lab.html'));
    }

    public function test_ncert_class_5_has_data_through_pictures_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class5', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'mathematics',
            'class' => 'class5',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('mathematics', $data['selectedSubject']);
        $this->assertEquals('class5', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Data Through Pictures', $data['activeChapters'][14]['name']);
        $this->assertTrue($data['activeChapters'][14]['has_multimedia']);
        $this->assertEquals('class5-maths-data-through-pictures', $data['activeChapters'][14]['media_key']);
        $this->assertFileExists(public_path('animations/class5-maths-data-through-pictures.html'));
        $this->assertFileExists(public_path('animations/chapter15-maths-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-chapter15.html'));
        $this->assertFileExists(public_path('animations/class5-data-through-pictures.html'));
        $this->assertFileExists(public_path('animations/data-through-pictures-class5.html'));
        $this->assertFileExists(public_path('animations/class5-maths-data-through-pictures-lab.html'));
        $this->assertFileExists(public_path('animations/class5-math-data-through-pictures.html'));
        $this->assertFileExists(public_path('animations/class5-data-lab.html'));
    }

    public function test_ncert_class_3_has_family_and_friends_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Family and Friends', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class3-science-family-and-friends', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class3-science-family-and-friends.html'));
        $this->assertFileExists(public_path('animations/chapter1-science-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-chapter1.html'));
        $this->assertFileExists(public_path('animations/class3-family-and-friends.html'));
        $this->assertFileExists(public_path('animations/family-and-friends-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-family-and-friends-lab.html'));
        $this->assertFileExists(public_path('animations/class3-sci-family-and-friends.html'));
        $this->assertFileExists(public_path('animations/class3-family-and-friends-lab.html'));
    }

    public function test_ncert_class_3_has_going_to_the_mela_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Going to the Mela', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class3-science-going-to-the-mela', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class3-science-going-to-the-mela.html'));
        $this->assertFileExists(public_path('animations/chapter2-science-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-chapter2.html'));
        $this->assertFileExists(public_path('animations/class3-going-to-the-mela.html'));
        $this->assertFileExists(public_path('animations/going-to-the-mela-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-going-to-the-mela-lab.html'));
        $this->assertFileExists(public_path('animations/class3-sci-going-to-the-mela.html'));
        $this->assertFileExists(public_path('animations/class3-going-to-the-mela-lab.html'));
    }

    public function test_ncert_class_3_has_celebrating_festivals_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Celebrating Festivals', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class3-science-celebrating-festivals', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class3-science-celebrating-festivals.html'));
        $this->assertFileExists(public_path('animations/chapter3-science-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-chapter3.html'));
        $this->assertFileExists(public_path('animations/class3-celebrating-festivals.html'));
        $this->assertFileExists(public_path('animations/celebrating-festivals-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-celebrating-festivals-lab.html'));
        $this->assertFileExists(public_path('animations/class3-sci-celebrating-festivals.html'));
        $this->assertFileExists(public_path('animations/class3-celebrating-festivals-lab.html'));
    }

    public function test_ncert_class_3_has_getting_to_know_plants_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Getting to Know Plants', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class3-science-getting-to-know-plants', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class3-science-getting-to-know-plants.html'));
        $this->assertFileExists(public_path('animations/chapter4-science-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-chapter4.html'));
        $this->assertFileExists(public_path('animations/class3-getting-to-know-plants.html'));
        $this->assertFileExists(public_path('animations/getting-to-know-plants-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-getting-to-know-plants-lab.html'));
        $this->assertFileExists(public_path('animations/class3-sci-getting-to-know-plants.html'));
        $this->assertFileExists(public_path('animations/class3-getting-to-know-plants-lab.html'));
    }

    public function test_ncert_class_3_has_plants_and_animals_live_together_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Plants and Animals Live Together', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class3-science-plants-and-animals-live-together', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class3-science-plants-and-animals-live-together.html'));
        $this->assertFileExists(public_path('animations/chapter5-science-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-chapter5.html'));
        $this->assertFileExists(public_path('animations/class3-plants-and-animals-live-together.html'));
        $this->assertFileExists(public_path('animations/plants-and-animals-live-together-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-plants-and-animals-live-together-lab.html'));
        $this->assertFileExists(public_path('animations/class3-sci-plants-and-animals-live-together.html'));
        $this->assertFileExists(public_path('animations/class3-plants-and-animals-live-together-lab.html'));
    }

    public function test_ncert_class_3_has_living_in_harmony_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Living in Harmony', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class3-science-living-in-harmony', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class3-science-living-in-harmony.html'));
        $this->assertFileExists(public_path('animations/chapter6-science-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-chapter6.html'));
        $this->assertFileExists(public_path('animations/class3-living-in-harmony.html'));
        $this->assertFileExists(public_path('animations/living-in-harmony-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-living-in-harmony-lab.html'));
        $this->assertFileExists(public_path('animations/class3-sci-living-in-harmony.html'));
        $this->assertFileExists(public_path('animations/class3-living-in-harmony-lab.html'));
    }

    public function test_ncert_class_3_has_water_a_precious_gift_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Water - A Precious Gift', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class3-science-water-a-precious-gift', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class3-science-water-a-precious-gift.html'));
        $this->assertFileExists(public_path('animations/chapter7-science-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-chapter7.html'));
        $this->assertFileExists(public_path('animations/class3-water-a-precious-gift.html'));
        $this->assertFileExists(public_path('animations/water-a-precious-gift-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-water-a-precious-gift-lab.html'));
        $this->assertFileExists(public_path('animations/class3-sci-water-a-precious-gift.html'));
        $this->assertFileExists(public_path('animations/class3-water-a-precious-gift-lab.html'));
    }

    public function test_ncert_class_3_has_food_we_eat_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class3', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class3',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class3', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Food We Eat', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class3-science-food-we-eat', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class3-science-food-we-eat.html'));
        $this->assertFileExists(public_path('animations/chapter8-science-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-chapter8.html'));
        $this->assertFileExists(public_path('animations/class3-food-we-eat.html'));
        $this->assertFileExists(public_path('animations/food-we-eat-class3.html'));
        $this->assertFileExists(public_path('animations/class3-science-food-we-eat-lab.html'));
        $this->assertFileExists(public_path('animations/class3-sci-food-we-eat.html'));
        $this->assertFileExists(public_path('animations/class3-food-we-eat-lab.html'));
    }

    public function test_ncert_class_4_has_living_together_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Living Together', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class4-science-living-together', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-living-together.html'));
        $this->assertFileExists(public_path('animations/chapter1-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter1.html'));
        $this->assertFileExists(public_path('animations/class4-living-together.html'));
        $this->assertFileExists(public_path('animations/living-together-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-living-together-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-living-together.html'));
        $this->assertFileExists(public_path('animations/class4-living-together-lab.html'));
    }

    public function test_ncert_class_4_has_exploring_our_neighbourhood_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Exploring Our Neighbourhood', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class4-science-exploring-our-neighbourhood', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-exploring-our-neighbourhood.html'));
        $this->assertFileExists(public_path('animations/chapter2-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter2.html'));
        $this->assertFileExists(public_path('animations/class4-exploring-our-neighbourhood.html'));
        $this->assertFileExists(public_path('animations/exploring-our-neighbourhood-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-exploring-our-neighbourhood-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-exploring-our-neighbourhood.html'));
        $this->assertFileExists(public_path('animations/class4-exploring-neighbourhood-lab.html'));
    }

    public function test_ncert_class_4_has_nature_trail_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Nature Trail', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class4-science-nature-trail', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-nature-trail.html'));
        $this->assertFileExists(public_path('animations/chapter3-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter3.html'));
        $this->assertFileExists(public_path('animations/class4-nature-trail.html'));
        $this->assertFileExists(public_path('animations/nature-trail-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-nature-trail-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-nature-trail.html'));
        $this->assertFileExists(public_path('animations/class4-nature-trail-lab.html'));
    }

    public function test_ncert_class_4_has_growing_up_with_nature_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Growing up with Nature', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class4-science-growing-up-with-nature', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-growing-up-with-nature.html'));
        $this->assertFileExists(public_path('animations/chapter4-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter4.html'));
        $this->assertFileExists(public_path('animations/class4-growing-up-with-nature.html'));
        $this->assertFileExists(public_path('animations/growing-up-with-nature-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-growing-up-with-nature-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-growing-up-with-nature.html'));
        $this->assertFileExists(public_path('animations/class4-growing-nature-lab.html'));
    }

    public function test_ncert_class_4_has_food_for_health_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Food for Health', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class4-science-food-for-health', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-food-for-health.html'));
        $this->assertFileExists(public_path('animations/chapter5-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter5.html'));
        $this->assertFileExists(public_path('animations/class4-food-for-health.html'));
        $this->assertFileExists(public_path('animations/food-for-health-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-food-for-health-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-food-for-health.html'));
        $this->assertFileExists(public_path('animations/class4-food-health-lab.html'));
    }

    public function test_ncert_class_4_has_happy_and_healthy_living_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Happy and Healthy Living', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class4-science-happy-and-healthy-living', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-happy-and-healthy-living.html'));
        $this->assertFileExists(public_path('animations/chapter6-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter6.html'));
        $this->assertFileExists(public_path('animations/class4-happy-and-healthy-living.html'));
        $this->assertFileExists(public_path('animations/happy-and-healthy-living-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-happy-and-healthy-living-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-happy-and-healthy-living.html'));
        $this->assertFileExists(public_path('animations/class4-happy-healthy-living-lab.html'));
    }

    public function test_ncert_class_4_has_how_things_work_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('How Things Work', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class4-science-how-things-work', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-how-things-work.html'));
        $this->assertFileExists(public_path('animations/chapter7-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter7.html'));
        $this->assertFileExists(public_path('animations/class4-how-things-work.html'));
        $this->assertFileExists(public_path('animations/how-things-work-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-how-things-work-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-how-things-work.html'));
        $this->assertFileExists(public_path('animations/class4-how-things-work-lab.html'));
    }

    public function test_ncert_class_4_has_how_things_are_made_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('How Things are Made', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class4-science-how-things-are-made', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-how-things-are-made.html'));
        $this->assertFileExists(public_path('animations/chapter8-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter8.html'));
        $this->assertFileExists(public_path('animations/class4-how-things-are-made.html'));
        $this->assertFileExists(public_path('animations/how-things-are-made-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-how-things-are-made-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-how-things-are-made.html'));
        $this->assertFileExists(public_path('animations/class4-how-things-made-lab.html'));
    }

    public function test_ncert_class_4_has_different_lands_different_lives_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Different Lands, Different Lives', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class4-science-different-lands-different-lives', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-different-lands-different-lives.html'));
        $this->assertFileExists(public_path('animations/chapter9-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter9.html'));
        $this->assertFileExists(public_path('animations/class4-different-lands-different-lives.html'));
        $this->assertFileExists(public_path('animations/different-lands-different-lives-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-different-lands-different-lives-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-different-lands-different-lives.html'));
        $this->assertFileExists(public_path('animations/class4-different-lands-lives-lab.html'));
    }

    public function test_ncert_class_4_has_our_sky_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class4', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class4',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class4', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Our Sky', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class4-science-our-sky', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class4-science-our-sky.html'));
        $this->assertFileExists(public_path('animations/chapter10-science-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-chapter10.html'));
        $this->assertFileExists(public_path('animations/class4-our-sky.html'));
        $this->assertFileExists(public_path('animations/our-sky-class4.html'));
        $this->assertFileExists(public_path('animations/class4-science-our-sky-lab.html'));
        $this->assertFileExists(public_path('animations/class4-sc-our-sky.html'));
        $this->assertFileExists(public_path('animations/class4-our-sky-lab.html'));
    }

    public function test_ncert_class_5_has_water_essence_of_life_multimedia(): void
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
        $this->assertEquals('Water - The Essence of Life', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class5-science-water-essence-of-life', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-water-essence-of-life.html'));
        $this->assertFileExists(public_path('animations/chapter1-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter1.html'));
        $this->assertFileExists(public_path('animations/class5-water-essence-of-life.html'));
        $this->assertFileExists(public_path('animations/water-essence-of-life-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-water-lab.html'));
        $this->assertFileExists(public_path('animations/class5-science-water-cycle.html'));
        $this->assertFileExists(public_path('animations/class5-water-cycle.html'));
    }

    public function test_ncert_class_5_has_journey_of_a_river_multimedia(): void
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
        $this->assertEquals('Journey of a River', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class5-science-journey-of-a-river', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-journey-of-a-river.html'));
        $this->assertFileExists(public_path('animations/chapter2-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter2.html'));
        $this->assertFileExists(public_path('animations/class5-journey-of-a-river.html'));
        $this->assertFileExists(public_path('animations/journey-of-a-river-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-river-lab.html'));
        $this->assertFileExists(public_path('animations/class5-science-godavari-river.html'));
        $this->assertFileExists(public_path('animations/class5-godavari-river.html'));
    }

    public function test_ncert_class_5_has_mystery_of_food_multimedia(): void
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
        $this->assertEquals('The Mystery of Food', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class5-science-mystery-of-food', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-mystery-of-food.html'));
        $this->assertFileExists(public_path('animations/chapter3-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter3.html'));
        $this->assertFileExists(public_path('animations/class5-mystery-of-food.html'));
        $this->assertFileExists(public_path('animations/mystery-of-food-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-food-lab.html'));
        $this->assertFileExists(public_path('animations/class5-science-food-spoilage.html'));
        $this->assertFileExists(public_path('animations/class5-food-spoilage.html'));
    }

    public function test_ncert_class_5_has_our_school_happy_place_multimedia(): void
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
        $this->assertEquals('Our School - A Happy Place', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class5-science-our-school-happy-place', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-our-school-happy-place.html'));
        $this->assertFileExists(public_path('animations/chapter4-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter4.html'));
        $this->assertFileExists(public_path('animations/class5-our-school-happy-place.html'));
        $this->assertFileExists(public_path('animations/our-school-happy-place-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-school-lab.html'));
        $this->assertFileExists(public_path('animations/class5-science-green-school.html'));
        $this->assertFileExists(public_path('animations/class5-green-school.html'));
    }

    public function test_ncert_class_5_has_our_vibrant_country_multimedia(): void
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
        $this->assertEquals('Our Vibrant Country', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class5-science-our-vibrant-country', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-our-vibrant-country.html'));
        $this->assertFileExists(public_path('animations/chapter5-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter5.html'));
        $this->assertFileExists(public_path('animations/class5-our-vibrant-country.html'));
        $this->assertFileExists(public_path('animations/our-vibrant-country-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-vibrant-country.html'));
        $this->assertFileExists(public_path('animations/class5-science-india-lab.html'));
        $this->assertFileExists(public_path('animations/class5-vibrant-country.html'));
    }

    public function test_ncert_class_5_has_some_unique_places_multimedia(): void
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
        $this->assertEquals('Some Unique Places', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class5-science-some-unique-places', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-some-unique-places.html'));
        $this->assertFileExists(public_path('animations/chapter6-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter6.html'));
        $this->assertFileExists(public_path('animations/class5-some-unique-places.html'));
        $this->assertFileExists(public_path('animations/some-unique-places-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-unique-places.html'));
        $this->assertFileExists(public_path('animations/class5-science-places-lab.html'));
        $this->assertFileExists(public_path('animations/class5-unique-places.html'));
    }

    public function test_ncert_class_5_has_energy_how_things_work_multimedia(): void
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
        $this->assertEquals('Energy - How Things Work', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class5-science-energy-how-things-work', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-energy-how-things-work.html'));
        $this->assertFileExists(public_path('animations/chapter7-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter7.html'));
        $this->assertFileExists(public_path('animations/class5-energy-how-things-work.html'));
        $this->assertFileExists(public_path('animations/energy-how-things-work-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-energy.html'));
        $this->assertFileExists(public_path('animations/class5-science-energy-lab.html'));
        $this->assertFileExists(public_path('animations/class5-energy.html'));
    }

    public function test_ncert_class_5_has_clothes_how_things_are_made_multimedia(): void
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
        $this->assertEquals('Clothes - How Things are Made', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class5-science-clothes-how-things-are-made', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class5-science-clothes-how-things-are-made.html'));
        $this->assertFileExists(public_path('animations/chapter8-science-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-chapter8.html'));
        $this->assertFileExists(public_path('animations/class5-clothes-how-things-are-made.html'));
        $this->assertFileExists(public_path('animations/clothes-how-things-are-made-class5.html'));
        $this->assertFileExists(public_path('animations/class5-science-clothes.html'));
        $this->assertFileExists(public_path('animations/class5-science-clothes-lab.html'));
        $this->assertFileExists(public_path('animations/class5-clothes.html'));
    }

    public function test_ncert_class_5_has_rhythms_of_nature_multimedia(): void
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

    public function test_ncert_class_5_has_earth_our_shared_home_multimedia(): void
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

    public function test_ncert_class_6_has_wonderful_world_of_science_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('The Wonderful World of Science', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class6-science-wonderful-world', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-wonderful-world.html'));
        $this->assertFileExists(public_path('animations/chapter1-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter1.html'));
        $this->assertFileExists(public_path('animations/class6-science-wonderful-world-of-science.html'));
        $this->assertFileExists(public_path('animations/wonderful-world-of-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-world-of-science.html'));
        $this->assertFileExists(public_path('animations/class6-science-intro.html'));
        $this->assertFileExists(public_path('animations/science-class6-chapter1.html'));
        $this->assertFileExists(public_path('animations/class6-science-nature-of-science.html'));
        $this->assertFileExists(public_path('animations/scientific-method-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-lab.html'));
    }

    public function test_ncert_class_6_has_diversity_in_living_world_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Diversity in the Living World', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class6-science-diversity-living-world', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-diversity-living-world.html'));
        $this->assertFileExists(public_path('animations/chapter2-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter2.html'));
        $this->assertFileExists(public_path('animations/class6-diversity-in-the-living-world.html'));
        $this->assertFileExists(public_path('animations/diversity-in-the-living-world-class6.html'));
        $this->assertFileExists(public_path('animations/diversity-living-world-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-diversity.html'));
        $this->assertFileExists(public_path('animations/class6-living-world.html'));
        $this->assertFileExists(public_path('animations/living-world-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-living-diversity.html'));
        $this->assertFileExists(public_path('animations/class6-science-diversity-lab.html'));
    }

    public function test_ncert_class_6_has_mindful_eating_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Mindful Eating: A Path to a Healthy Body', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class6-science-mindful-eating', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-mindful-eating.html'));
        $this->assertFileExists(public_path('animations/chapter3-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter3.html'));
        $this->assertFileExists(public_path('animations/class6-mindful-eating.html'));
        $this->assertFileExists(public_path('animations/mindful-eating-class6.html'));
        $this->assertFileExists(public_path('animations/mindful-eating-healthy-body-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-mindful-eating-lab.html'));
        $this->assertFileExists(public_path('animations/class6-science-food-nutrition.html'));
        $this->assertFileExists(public_path('animations/class6-science-components-of-food.html'));
        $this->assertFileExists(public_path('animations/class6-components-of-food.html'));
        $this->assertFileExists(public_path('animations/components-of-food-class6.html'));
    }

    public function test_ncert_class_6_has_exploring_magnets_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Exploring Magnets', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class6-science-exploring-magnets', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-exploring-magnets.html'));
        $this->assertFileExists(public_path('animations/chapter4-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter4.html'));
        $this->assertFileExists(public_path('animations/class6-exploring-magnets.html'));
        $this->assertFileExists(public_path('animations/exploring-magnets-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-magnets.html'));
        $this->assertFileExists(public_path('animations/magnets-class6.html'));
        $this->assertFileExists(public_path('animations/class6-magnets.html'));
        $this->assertFileExists(public_path('animations/class6-science-magnetism.html'));
        $this->assertFileExists(public_path('animations/class6-science-exploring-magnets-lab.html'));
        $this->assertFileExists(public_path('animations/class6-science-fun-with-magnets.html'));
    }

    public function test_ncert_class_6_has_length_and_motion_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $response = $controller->index($request);
        $data = $response->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Measurement of Length and Motion', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class6-science-length-and-motion', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-length-and-motion.html'));
        $this->assertFileExists(public_path('animations/chapter5-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter5.html'));
        $this->assertFileExists(public_path('animations/class6-measurement-of-length-and-motion.html'));
        $this->assertFileExists(public_path('animations/measurement-of-length-and-motion-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-measurement.html'));
        $this->assertFileExists(public_path('animations/measurement-class6.html'));
        $this->assertFileExists(public_path('animations/class6-measurement.html'));
        $this->assertFileExists(public_path('animations/class6-science-motion.html'));
        $this->assertFileExists(public_path('animations/class6-science-length-and-motion-lab.html'));
        $this->assertFileExists(public_path('animations/class6-science-motion-and-measurement.html'));
    }

    public function test_ncert_class_6_has_materials_around_us_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Materials Around Us', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class6-science-materials-around-us', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-materials-around-us.html'));
        $this->assertFileExists(public_path('animations/chapter6-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter6.html'));
        $this->assertFileExists(public_path('animations/class6-materials-around-us.html'));
        $this->assertFileExists(public_path('animations/materials-around-us-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-materials.html'));
        $this->assertFileExists(public_path('animations/materials-class6.html'));
        $this->assertFileExists(public_path('animations/class6-materials.html'));
        $this->assertFileExists(public_path('animations/class6-science-materials-around-us-lab.html'));
        $this->assertFileExists(public_path('animations/class6-science-sorting-materials.html'));
        $this->assertFileExists(public_path('animations/sorting-materials-into-groups-class6.html'));
    }

    public function test_ncert_class_6_has_temperature_measurement_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Temperature and its Measurement', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class6-science-temperature-measurement', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-temperature-measurement.html'));
        $this->assertFileExists(public_path('animations/chapter7-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter7.html'));
        $this->assertFileExists(public_path('animations/class6-temperature-and-its-measurement.html'));
        $this->assertFileExists(public_path('animations/temperature-and-its-measurement-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-temperature.html'));
        $this->assertFileExists(public_path('animations/temperature-class6.html'));
        $this->assertFileExists(public_path('animations/temperature-measurement-class6.html'));
        $this->assertFileExists(public_path('animations/class6-temperature.html'));
        $this->assertFileExists(public_path('animations/class6-science-temperature-measurement-lab.html'));
        $this->assertFileExists(public_path('animations/class6-science-temperature-and-measurement.html'));
        $this->assertFileExists(public_path('animations/class6-science-heat-and-temperature.html'));
        $this->assertFileExists(public_path('animations/heat-and-temperature-class6.html'));
    }

    public function test_ncert_class_6_has_states_of_water_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('A Journey through States of Water', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class6-science-states-of-water', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-states-of-water.html'));
        $this->assertFileExists(public_path('animations/chapter8-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter8.html'));
        $this->assertFileExists(public_path('animations/class6-science-journey-through-states-of-water.html'));
        $this->assertFileExists(public_path('animations/class6-science-states-of-water-lab.html'));
        $this->assertFileExists(public_path('animations/class6-science-water-cycle.html'));
        $this->assertFileExists(public_path('animations/class6-science-water-states.html'));
        $this->assertFileExists(public_path('animations/class6-science-water-states-lab.html'));
        $this->assertFileExists(public_path('animations/class6-states-of-water.html'));
        $this->assertFileExists(public_path('animations/class6-water-states.html'));
        $this->assertFileExists(public_path('animations/states-of-water-class6.html'));
        $this->assertFileExists(public_path('animations/water-states-class6.html'));
    }

    public function test_ncert_class_6_has_methods_of_separation_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Methods of Separation in Everyday Life', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class6-science-methods-of-separation', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-methods-of-separation.html'));
        $this->assertFileExists(public_path('animations/chapter9-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter9.html'));
        $this->assertFileExists(public_path('animations/class6-methods-of-separation.html'));
        $this->assertFileExists(public_path('animations/methods-of-separation-class6.html'));
        $this->assertFileExists(public_path('animations/class6-separation-methods.html'));
        $this->assertFileExists(public_path('animations/separation-methods-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-separation-methods.html'));
        $this->assertFileExists(public_path('animations/class6-science-separation.html'));
        $this->assertFileExists(public_path('animations/class6-science-separation-techniques.html'));
        $this->assertFileExists(public_path('animations/class6-science-methods-of-separation-lab.html'));
    }

    public function test_ncert_class_6_has_living_creatures_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Living Creatures: Exploring their Characteristics', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class6-science-living-creatures', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-living-creatures.html'));
        $this->assertFileExists(public_path('animations/chapter10-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter10.html'));
        $this->assertFileExists(public_path('animations/class6-living-creatures.html'));
        $this->assertFileExists(public_path('animations/living-creatures-class6.html'));
        $this->assertFileExists(public_path('animations/class6-living-creatures-characteristics.html'));
        $this->assertFileExists(public_path('animations/class6-science-living-creatures-characteristics.html'));
        $this->assertFileExists(public_path('animations/class6-science-living-creatures-lab.html'));
    }

    public function test_ncert_class_6_has_natures_treasures_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Nature\'s Treasures', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class6-science-natures-treasures', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-natures-treasures.html'));
        $this->assertFileExists(public_path('animations/chapter11-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter11.html'));
        $this->assertFileExists(public_path('animations/class6-natures-treasures.html'));
        $this->assertFileExists(public_path('animations/natures-treasures-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-natures-treasures-lab.html'));
        $this->assertFileExists(public_path('animations/class6-science-natural-resources.html'));
        $this->assertFileExists(public_path('animations/class6-natural-resources.html'));
    }

    public function test_ncert_class_6_has_beyond_earth_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class6', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class6',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class6', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Beyond Earth', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class6-science-beyond-earth', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class6-science-beyond-earth.html'));
        $this->assertFileExists(public_path('animations/chapter12-science-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-chapter12.html'));
        $this->assertFileExists(public_path('animations/class6-beyond-earth.html'));
        $this->assertFileExists(public_path('animations/beyond-earth-class6.html'));
        $this->assertFileExists(public_path('animations/class6-science-beyond-earth-lab.html'));
        $this->assertFileExists(public_path('animations/class6-science-solar-system.html'));
        $this->assertFileExists(public_path('animations/class6-solar-system.html'));
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

    public function test_ncert_class_7_has_another_peek_beyond_the_point_multimedia(): void
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
        $this->assertEquals('Decimal Operations', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class7-math-another-peek-beyond-the-point', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-another-peek-beyond-the-point.html'));
        $this->assertFileExists(public_path('animations/chapter12-math-class7.html'));
        $this->assertFileExists(public_path('animations/another-peek-beyond-the-point.html'));
        $this->assertFileExists(public_path('animations/class7-another-peek-beyond-the-point.html'));
        $this->assertFileExists(public_path('animations/another-peek-beyond-the-point-class7.html'));
        $this->assertFileExists(public_path('animations/class7-math-decimal-operations.html'));
        $this->assertFileExists(public_path('animations/decimal-operations-class7.html'));
        $this->assertFileExists(public_path('animations/class7-decimal-operations.html'));
    }

    public function test_ncert_class_7_has_connecting_the_dots_multimedia(): void
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
        $this->assertEquals('Connecting the Dots... (Data Handling)', $data['activeChapters'][12]['name']);
        $this->assertTrue($data['activeChapters'][12]['has_multimedia']);
        $this->assertEquals('class7-math-connecting-the-dots', $data['activeChapters'][12]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-connecting-the-dots.html'));
        $this->assertFileExists(public_path('animations/chapter5-connecting-the-dots.html'));
        $this->assertFileExists(public_path('animations/chapter13-math-class7.html'));
        $this->assertFileExists(public_path('animations/connecting-the-dots.html'));
        $this->assertFileExists(public_path('animations/connecting-the-dots-class7.html'));
        $this->assertFileExists(public_path('animations/class7-connecting-the-dots.html'));
        $this->assertFileExists(public_path('animations/class7-math-data-handling.html'));
        $this->assertFileExists(public_path('animations/data-handling-class7.html'));
        $this->assertFileExists(public_path('animations/class7-data-handling.html'));
    }

    public function test_ncert_class_7_has_constructions_and_tilings_multimedia(): void
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
        $this->assertEquals('Constructions and Tilings', $data['activeChapters'][13]['name']);
        $this->assertTrue($data['activeChapters'][13]['has_multimedia']);
        $this->assertEquals('class7-math-constructions-and-tilings', $data['activeChapters'][13]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-constructions-and-tilings.html'));
        $this->assertFileExists(public_path('animations/chapter6-constructions-and-tilings.html'));
        $this->assertFileExists(public_path('animations/chapter14-math-class7.html'));
        $this->assertFileExists(public_path('animations/constructions-and-tilings.html'));
        $this->assertFileExists(public_path('animations/constructions-and-tilings-class7.html'));
        $this->assertFileExists(public_path('animations/class7-constructions-and-tilings.html'));
        $this->assertFileExists(public_path('animations/class7-math-constructions.html'));
        $this->assertFileExists(public_path('animations/constructions-class7.html'));
        $this->assertFileExists(public_path('animations/tilings-class7.html'));
    }

    public function test_ncert_class_7_has_finding_the_unknown_multimedia(): void
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
        $this->assertEquals('Finding the Unknown', $data['activeChapters'][14]['name']);
        $this->assertTrue($data['activeChapters'][14]['has_multimedia']);
        $this->assertEquals('class7-math-finding-the-unknown', $data['activeChapters'][14]['media_key']);
        $this->assertFileExists(public_path('animations/class7-math-finding-the-unknown.html'));
        $this->assertFileExists(public_path('animations/chapter7-finding-the-unknown.html'));
        $this->assertFileExists(public_path('animations/chapter15-math-class7.html'));
        $this->assertFileExists(public_path('animations/finding-the-unknown.html'));
        $this->assertFileExists(public_path('animations/finding-the-unknown-class7.html'));
        $this->assertFileExists(public_path('animations/class7-finding-the-unknown.html'));
        $this->assertFileExists(public_path('animations/class7-math-equations.html'));
        $this->assertFileExists(public_path('animations/simple-equations-class7.html'));
        $this->assertFileExists(public_path('animations/class7-simple-equations.html'));
    }

    public function test_ncert_class_7_has_the_ever_evolving_world_of_science_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Exploring the World of Science', $data['activeChapters'][0]['name']);
        $this->assertTrue($data['activeChapters'][0]['has_multimedia']);
        $this->assertEquals('class7-science-ever-evolving-world', $data['activeChapters'][0]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-ever-evolving-world.html'));
        $this->assertFileExists(public_path('animations/chapter1-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter1.html'));
        $this->assertFileExists(public_path('animations/the-ever-evolving-world-of-science.html'));
        $this->assertFileExists(public_path('animations/ever-evolving-world-of-science.html'));
        $this->assertFileExists(public_path('animations/class7-ever-evolving-world-of-science.html'));
        $this->assertFileExists(public_path('animations/class7-science-intro.html'));
        $this->assertFileExists(public_path('animations/exploring-the-world-of-science.html'));
        $this->assertFileExists(public_path('animations/class7-exploring-the-world-of-science.html'));
        $this->assertFileExists(public_path('animations/class7-science-exploring-world.html'));
        $this->assertFileExists(public_path('animations/exploring-world-of-science.html'));
        $this->assertFileExists(public_path('animations/exploring-the-world-of-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-exploring-the-world-of-science.html'));
    }

    public function test_ncert_class_7_has_exploring_substances_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Acids, Bases, and Salts', $data['activeChapters'][1]['name']);
        $this->assertTrue($data['activeChapters'][1]['has_multimedia']);
        $this->assertEquals('class7-science-exploring-substances', $data['activeChapters'][1]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-exploring-substances.html'));
        $this->assertFileExists(public_path('animations/chapter2-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter2.html'));
        $this->assertFileExists(public_path('animations/exploring-substances-acidic-basic-and-neutral.html'));
        $this->assertFileExists(public_path('animations/exploring-substances.html'));
        $this->assertFileExists(public_path('animations/class7-exploring-substances.html'));
        $this->assertFileExists(public_path('animations/class7-science-substances.html'));
        $this->assertFileExists(public_path('animations/acids-bases-and-salts-class7.html'));
        $this->assertFileExists(public_path('animations/class7-acids-bases-and-salts.html'));
    }

    public function test_ncert_class_7_has_electricity_circuits_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Electricity: Circuits and their Components', $data['activeChapters'][2]['name']);
        $this->assertTrue($data['activeChapters'][2]['has_multimedia']);
        $this->assertEquals('class7-science-circuits', $data['activeChapters'][2]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-circuits.html'));
        $this->assertFileExists(public_path('animations/chapter3-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter3.html'));
        $this->assertFileExists(public_path('animations/electricity-circuits-and-their-components.html'));
        $this->assertFileExists(public_path('animations/electricity-circuits.html'));
        $this->assertFileExists(public_path('animations/class7-electricity-circuits.html'));
        $this->assertFileExists(public_path('animations/electricity-and-circuits-class7.html'));
        $this->assertFileExists(public_path('animations/class7-electricity-and-circuits.html'));
        $this->assertFileExists(public_path('animations/electricity-circuits-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-electricity-circuits.html'));
    }

    public function test_ncert_class_7_has_metals_and_nonmetals_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Metals and Non-metals', $data['activeChapters'][3]['name']);
        $this->assertTrue($data['activeChapters'][3]['has_multimedia']);
        $this->assertEquals('class7-science-metals-and-nonmetals', $data['activeChapters'][3]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-metals-and-nonmetals.html'));
        $this->assertFileExists(public_path('animations/chapter4-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter4.html'));
        $this->assertFileExists(public_path('animations/class7-metals-and-non-metals.html'));
        $this->assertFileExists(public_path('animations/class7-metals-and-nonmetals.html'));
        $this->assertFileExists(public_path('animations/class7-science-metals-nonmetals.html'));
        $this->assertFileExists(public_path('animations/metals-and-non-metals-class7.html'));
        $this->assertFileExists(public_path('animations/metals-and-nonmetals-class7.html'));
        $this->assertFileExists(public_path('animations/the-world-of-metals-and-non-metals.html'));
        $this->assertFileExists(public_path('animations/the-world-of-metals-and-nonmetals.html'));
        $this->assertFileExists(public_path('animations/world-of-metals-and-non-metals.html'));
    }

    public function test_ncert_class_7_has_changes_around_us_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Physical and Chemical Changes', $data['activeChapters'][4]['name']);
        $this->assertTrue($data['activeChapters'][4]['has_multimedia']);
        $this->assertEquals('class7-science-physical-chemical-changes', $data['activeChapters'][4]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-physical-chemical-changes.html'));
        $this->assertFileExists(public_path('animations/chapter5-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter5.html'));
        $this->assertFileExists(public_path('animations/changes-around-us-physical-and-chemical.html'));
        $this->assertFileExists(public_path('animations/class7-changes-around-us.html'));
        $this->assertFileExists(public_path('animations/class7-physical-and-chemical-changes.html'));
        $this->assertFileExists(public_path('animations/physical-and-chemical-changes-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-changes-around-us.html'));
        $this->assertFileExists(public_path('animations/changes-around-us-class7.html'));
        $this->assertFileExists(public_path('animations/physical-and-chemical-changes.html'));
    }

    public function test_ncert_class_7_has_adolescence_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Adolescence', $data['activeChapters'][5]['name']);
        $this->assertTrue($data['activeChapters'][5]['has_multimedia']);
        $this->assertEquals('class7-science-adolescence-growth', $data['activeChapters'][5]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-adolescence-growth.html'));
        $this->assertFileExists(public_path('animations/chapter6-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter6.html'));
        $this->assertFileExists(public_path('animations/adolescence.html'));
        $this->assertFileExists(public_path('animations/adolescence-a-stage-of-growth-and-change.html'));
        $this->assertFileExists(public_path('animations/class7-adolescence-growth.html'));
        $this->assertFileExists(public_path('animations/class7-adolescence-stage-of-growth.html'));
        $this->assertFileExists(public_path('animations/adolescence-growth-and-change-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-adolescence.html'));
        $this->assertFileExists(public_path('animations/adolescence-class7.html'));
        $this->assertFileExists(public_path('animations/adolescence-a-stage-of-growth.html'));
    }

    public function test_ncert_class_7_has_heat_transfer_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Heat and Its Effects in Nature', $data['activeChapters'][6]['name']);
        $this->assertTrue($data['activeChapters'][6]['has_multimedia']);
        $this->assertEquals('class7-science-heat-nature', $data['activeChapters'][6]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-heat-nature.html'));
        $this->assertFileExists(public_path('animations/chapter7-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter7.html'));
        $this->assertFileExists(public_path('animations/heat-and-its-effects-in-nature.html'));
        $this->assertFileExists(public_path('animations/heat-and-its-effects-in-nature-class7.html'));
        $this->assertFileExists(public_path('animations/class7-heat-and-its-effects-in-nature.html'));
        $this->assertFileExists(public_path('animations/heat-transfer-in-nature.html'));
        $this->assertFileExists(public_path('animations/heat-transfer-in-nature-class7.html'));
        $this->assertFileExists(public_path('animations/class7-heat-transfer-in-nature.html'));
        $this->assertFileExists(public_path('animations/class7-science-heat-transfer.html'));
        $this->assertFileExists(public_path('animations/class7-heat-transfer.html'));
        $this->assertFileExists(public_path('animations/heat-transfer-class7.html'));
        $this->assertFileExists(public_path('animations/heat-transfer.html'));
    }

    public function test_ncert_class_7_has_time_motion_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Time and Motion', $data['activeChapters'][7]['name']);
        $this->assertTrue($data['activeChapters'][7]['has_multimedia']);
        $this->assertEquals('class7-science-time-motion', $data['activeChapters'][7]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-time-motion.html'));
        $this->assertFileExists(public_path('animations/chapter8-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter8.html'));
        $this->assertFileExists(public_path('animations/measurement-of-time-and-motion.html'));
        $this->assertFileExists(public_path('animations/measurement-of-time-and-motion-class7.html'));
        $this->assertFileExists(public_path('animations/class7-measurement-of-time-and-motion.html'));
        $this->assertFileExists(public_path('animations/class7-time-and-motion.html'));
        $this->assertFileExists(public_path('animations/class7-time-motion.html'));
        $this->assertFileExists(public_path('animations/time-and-motion-class7.html'));
        $this->assertFileExists(public_path('animations/time-and-motion.html'));
        $this->assertFileExists(public_path('animations/measurement-of-time.html'));
    }

    public function test_ncert_class_7_has_life_processes_in_animals_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Animal Life', $data['activeChapters'][8]['name']);
        $this->assertTrue($data['activeChapters'][8]['has_multimedia']);
        $this->assertEquals('class7-science-life-processes-animals', $data['activeChapters'][8]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-life-processes-animals.html'));
        $this->assertFileExists(public_path('animations/chapter9-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter9.html'));
        $this->assertFileExists(public_path('animations/class7-life-processes-in-animals.html'));
        $this->assertFileExists(public_path('animations/class7-life-processes-animals.html'));
        $this->assertFileExists(public_path('animations/class7-science-life-processes.html'));
        $this->assertFileExists(public_path('animations/life-processes-in-animals-class7.html'));
        $this->assertFileExists(public_path('animations/life-processes-animals-class7.html'));
        $this->assertFileExists(public_path('animations/life-processes-in-animals.html'));
        $this->assertFileExists(public_path('animations/life-processes-animals.html'));
        $this->assertFileExists(public_path('animations/nutrition-and-respiration-in-animals-class7.html'));
        $this->assertFileExists(public_path('animations/animal-life.html'));
        $this->assertFileExists(public_path('animations/animal-life-class7.html'));
        $this->assertFileExists(public_path('animations/class7-animal-life.html'));
        $this->assertFileExists(public_path('animations/class7-science-animal-life.html'));
    }

    public function test_ncert_class_7_has_life_processes_in_plants_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Plant Life', $data['activeChapters'][9]['name']);
        $this->assertTrue($data['activeChapters'][9]['has_multimedia']);
        $this->assertEquals('class7-science-life-processes-plants', $data['activeChapters'][9]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-life-processes-plants.html'));
        $this->assertFileExists(public_path('animations/chapter10-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter10.html'));
        $this->assertFileExists(public_path('animations/class7-life-processes-in-plants.html'));
        $this->assertFileExists(public_path('animations/class7-life-processes-plants.html'));
        $this->assertFileExists(public_path('animations/life-processes-in-plants-class7.html'));
        $this->assertFileExists(public_path('animations/life-processes-plants-class7.html'));
        $this->assertFileExists(public_path('animations/life-processes-in-plants.html'));
        $this->assertFileExists(public_path('animations/life-processes-plants.html'));
        $this->assertFileExists(public_path('animations/nutrition-and-transport-in-plants-class7.html'));
        $this->assertFileExists(public_path('animations/plant-life.html'));
        $this->assertFileExists(public_path('animations/plant-life-class7.html'));
        $this->assertFileExists(public_path('animations/class7-plant-life.html'));
        $this->assertFileExists(public_path('animations/class7-science-plant-life.html'));
    }

    public function test_ncert_class_7_has_light_shadows_and_reflections_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Light', $data['activeChapters'][10]['name']);
        $this->assertTrue($data['activeChapters'][10]['has_multimedia']);
        $this->assertEquals('class7-science-light-shadows-reflections', $data['activeChapters'][10]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-light-shadows-reflections.html'));
        $this->assertFileExists(public_path('animations/chapter11-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter11.html'));
        $this->assertFileExists(public_path('animations/class7-light-shadows-and-reflections.html'));
        $this->assertFileExists(public_path('animations/class7-light-shadows-reflections.html'));
        $this->assertFileExists(public_path('animations/class7-science-light.html'));
        $this->assertFileExists(public_path('animations/light-shadows-and-reflections-class7.html'));
        $this->assertFileExists(public_path('animations/light-shadows-reflections-class7.html'));
        $this->assertFileExists(public_path('animations/light-shadows-and-reflections.html'));
        $this->assertFileExists(public_path('animations/light-shadows-reflections.html'));
        $this->assertFileExists(public_path('animations/light-shadows.html'));
        $this->assertFileExists(public_path('animations/class7-light.html'));
        $this->assertFileExists(public_path('animations/light-class7.html'));
        $this->assertFileExists(public_path('animations/light.html'));
    }

    public function test_ncert_class_7_has_earth_moon_and_the_sun_multimedia(): void
    {
        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=science&class=class7', 'GET', [
            'syllabus' => 'ncert',
            'subject' => 'science',
            'class' => 'class7',
        ]);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertEquals('ncert', $data['selectedSyllabus']);
        $this->assertEquals('science', $data['selectedSubject']);
        $this->assertEquals('class7', $data['selectedClass']);
        $this->assertTrue($data['hasAnyMultimedia']);
        $this->assertEquals('Earth, Moon, and the Sun', $data['activeChapters'][11]['name']);
        $this->assertTrue($data['activeChapters'][11]['has_multimedia']);
        $this->assertEquals('class7-science-earth-moon-sun', $data['activeChapters'][11]['media_key']);
        $this->assertFileExists(public_path('animations/class7-science-earth-moon-sun.html'));
        $this->assertFileExists(public_path('animations/chapter12-science-class7.html'));
        $this->assertFileExists(public_path('animations/class7-science-chapter12.html'));
        $this->assertFileExists(public_path('animations/class7-earth-moon-and-the-sun.html'));
        $this->assertFileExists(public_path('animations/class7-earth-moon-sun.html'));
        $this->assertFileExists(public_path('animations/earth-moon-and-the-sun-class7.html'));
        $this->assertFileExists(public_path('animations/earth-moon-sun-class7.html'));
        $this->assertFileExists(public_path('animations/earth-moon-and-the-sun.html'));
        $this->assertFileExists(public_path('animations/earth-moon-sun.html'));
        $this->assertFileExists(public_path('animations/earth-moon-and-sun.html'));
        $this->assertFileExists(public_path('animations/earth-sun-moon.html'));
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
        $this->assertCount(1386, $files);

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
