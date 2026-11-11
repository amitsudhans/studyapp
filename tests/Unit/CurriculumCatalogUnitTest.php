<?php

namespace Tests\Unit;

use App\Http\Controllers\MultimediaController;
use App\Models\User;
use App\Models\UserCurriculum;
use App\Support\CurriculumCatalog;
use Illuminate\Http\Request;
use Illuminate\Support\Collection;
use Tests\TestCase;

class CurriculumCatalogUnitTest extends TestCase
{
    public function test_catalog_contains_ncert_cbse_maths_science_social_science_class1_to_12(): void
    {
        $syllabuses = CurriculumCatalog::syllabuses();
        $subjects = CurriculumCatalog::subjects();
        $classes = CurriculumCatalog::classes();

        $this->assertArrayHasKey('ncert', $syllabuses);
        $this->assertArrayHasKey('cbse', $syllabuses);
        $this->assertArrayHasKey('mathematics', $subjects);
        $this->assertArrayHasKey('science', $subjects);
        $this->assertArrayHasKey('social-science', $subjects);
        $this->assertCount(12, $classes);
        $this->assertArrayHasKey('class1', $classes);
        $this->assertArrayHasKey('class12', $classes);
    }

    public function test_parse_selection_tokens_filters_invalid_and_deduplicates_entries(): void
    {
        $parsed = CurriculumCatalog::parseSelectionTokens([
            'ncert|mathematics|class8',
            'ncert|mathematics|class8',
            'cbse|social-science|class10',
            'invalid|mathematics|class8',
            'ncert|unknown|class8',
            'ncert|science|class99',
        ]);

        $this->assertCount(2, $parsed);
        $this->assertSame([
            ['syllabus' => 'ncert', 'subject' => 'mathematics', 'class_key' => 'class8'],
            ['syllabus' => 'cbse', 'subject' => 'social-science', 'class_key' => 'class10'],
        ], $parsed);
    }

    public function test_restricted_user_only_sees_enabled_curriculum_in_multimedia_controller(): void
    {
        $user = new User(['name' => 'Student User', 'email' => 'student@example.com', 'curriculum_restricted' => true]);
        $user->setRelation('curricula', new Collection([
            new UserCurriculum([
                'syllabus' => 'ncert',
                'subject' => 'mathematics',
                'class_key' => 'class8',
                'is_enabled' => true,
            ]),
        ]));

        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=cbse&subject=science&class=class10', 'GET', [
            'syllabus' => 'cbse',
            'subject' => 'science',
            'class' => 'class10',
        ]);
        $request->setUserResolver(fn (): User => $user);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertTrue($data['hasCurriculumAccess']);
        $this->assertSame(['ncert'], array_keys($data['syllabuses']));
        $this->assertSame(['mathematics'], array_keys($data['subjects']));
        $this->assertSame(['class8'], array_keys($data['classes']));
        $this->assertSame('ncert', $data['selectedSyllabus']);
        $this->assertSame('mathematics', $data['selectedSubject']);
        $this->assertSame('class8', $data['selectedClass']);
        $this->assertCount(14, $data['activeChapters']);
        $this->assertSame(14, $data['totalChaptersCount']);
    }

    public function test_restricted_user_with_zero_enabled_curricula_has_no_curriculum_access(): void
    {
        $user = new User(['name' => 'Teacher User', 'email' => 'teacher@example.com', 'curriculum_restricted' => true]);
        $user->setRelation('curricula', new Collection);

        $controller = new MultimediaController;
        $request = Request::create('/multimedia?syllabus=ncert&subject=mathematics&class=class10', 'GET');
        $request->setUserResolver(fn (): User => $user);

        $view = $controller->index($request);
        $data = $view->getData();

        $this->assertFalse($data['hasCurriculumAccess']);
        $this->assertSame([], $data['syllabuses']);
        $this->assertSame([], $data['subjects']);
        $this->assertSame([], $data['classes']);
        $this->assertSame([], $data['activeChapters']);
        $this->assertSame(0, $data['totalChaptersCount']);
    }
}
