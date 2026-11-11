<?php

namespace App\Support;

use App\Models\User;

class CurriculumCatalog
{
    /**
     * Canonical syllabus definitions for the textbook curriculum tree.
     *
     * @return array<string, array<string, string>>
     */
    public static function syllabuses(): array
    {
        return [
            'ncert' => [
                'id' => 'ncert',
                'name' => 'NCERT',
                'badge' => 'National Council of Educational Research and Training',
                'description' => 'National Curriculum Framework Textbook Animations',
            ],
            'cbse' => [
                'id' => 'cbse',
                'name' => 'CBSE',
                'badge' => 'Central Board of Secondary Education',
                'description' => 'CBSE Board Curriculum',
            ],
            'scert-kerala' => [
                'id' => 'scert-kerala',
                'name' => 'SCERT Kerala',
                'badge' => 'State Council of Educational Research and Training (Kerala)',
                'description' => 'Kerala State Syllabus Curriculum Framework',
            ],
        ];
    }

    /**
     * Canonical subject definitions including Mathematics, Science, Social Science, English, and Hindi.
     *
     * @return array<string, array<string, string>>
     */
    public static function subjects(): array
    {
        return [
            'mathematics' => [
                'id' => 'mathematics',
                'name' => 'Mathematics',
                'icon' => '📐',
                'color' => 'emerald',
            ],
            'science' => [
                'id' => 'science',
                'name' => 'Science',
                'icon' => '🔬',
                'color' => 'cyan',
            ],
            'social-science' => [
                'id' => 'social-science',
                'name' => 'Social Science',
                'icon' => '🌍',
                'color' => 'rose',
            ],
            'english' => [
                'id' => 'english',
                'name' => 'English',
                'icon' => '📖',
                'color' => 'indigo',
            ],
            'hindi' => [
                'id' => 'hindi',
                'name' => 'Hindi',
                'icon' => '📚',
                'color' => 'amber',
            ],
        ];
    }

    /**
     * Canonical class definitions from Class 1 to Class 12.
     *
     * @return array<string, array<string, string>>
     */
    public static function classes(): array
    {
        return [
            'class1' => ['id' => 'class1', 'name' => 'Class 1', 'level' => 'Primary'],
            'class2' => ['id' => 'class2', 'name' => 'Class 2', 'level' => 'Primary'],
            'class3' => ['id' => 'class3', 'name' => 'Class 3', 'level' => 'Primary'],
            'class4' => ['id' => 'class4', 'name' => 'Class 4', 'level' => 'Primary'],
            'class5' => ['id' => 'class5', 'name' => 'Class 5', 'level' => 'Primary'],
            'class6' => ['id' => 'class6', 'name' => 'Class 6', 'level' => 'Middle'],
            'class7' => ['id' => 'class7', 'name' => 'Class 7', 'level' => 'Middle'],
            'class8' => ['id' => 'class8', 'name' => 'Class 8', 'level' => 'Middle'],
            'class9' => ['id' => 'class9', 'name' => 'Class 9', 'level' => 'Secondary'],
            'class10' => ['id' => 'class10', 'name' => 'Class 10', 'level' => 'Secondary'],
            'class11' => ['id' => 'class11', 'name' => 'Class 11', 'level' => 'Higher Secondary'],
            'class12' => ['id' => 'class12', 'name' => 'Class 12', 'level' => 'Higher Secondary'],
        ];
    }

    /**
     * Validate a curriculum tuple against the canonical catalog.
     */
    public static function isValidTuple(string $syllabus, string $subject, string $classKey): bool
    {
        return array_key_exists($syllabus, self::syllabuses())
            && array_key_exists($subject, self::subjects())
            && array_key_exists($classKey, self::classes());
    }

    /**
     * Parse `"syllabus|subject|classKey"` tokens into unique validated tuple arrays.
     *
     * @param  array<int, string>  $tokens
     * @return array<int, array{syllabus: string, subject: string, class_key: string}>
     */
    public static function parseSelectionTokens(array $tokens): array
    {
        $unique = [];
        foreach ($tokens as $token) {
            if (! is_string($token)) {
                continue;
            }
            $parts = explode('|', trim($token));
            if (count($parts) !== 3) {
                continue;
            }
            [$syllabus, $subject, $classKey] = $parts;
            if (! self::isValidTuple($syllabus, $subject, $classKey)) {
                continue;
            }
            $unique["{$syllabus}|{$subject}|{$classKey}"] = [
                'syllabus' => $syllabus,
                'subject' => $subject,
                'class_key' => $classKey,
            ];
        }

        return array_values($unique);
    }

    /**
     * Build the enabled map `[syllabus][subject][classKey] => true`, or null when unrestricted.
     *
     * @return array<string, array<string, array<string, bool>>>|null
     */
    public static function enabledMapForUser(?User $user): ?array
    {
        if (! $user || ! $user->curriculum_restricted) {
            return null;
        }

        $entries = $user->relationLoaded('curricula')
            ? $user->curricula->where('is_enabled', true)
            : $user->curricula()->where('is_enabled', true)->get();

        $map = [];
        foreach ($entries as $entry) {
            $map[$entry->syllabus][$entry->subject][$entry->class_key] = true;
        }

        return $map;
    }

    /**
     * Check whether a single tuple is enabled for the given user.
     */
    public static function isEnabledForUser(?User $user, string $syllabus, string $subject, string $classKey): bool
    {
        $map = self::enabledMapForUser($user);
        if ($map === null) {
            return true;
        }

        return ! empty($map[$syllabus][$subject][$classKey]);
    }

    /**
     * Filter syllabuses, subjects, classes, and resolve active selections for a user.
     *
     * @param  array<string, array<string, string>>  $syllabuses
     * @param  array<string, array<string, string>>  $subjects
     * @param  array<string, array<string, string>>  $classes
     * @return array{
     *     syllabuses: array<string, array<string, string>>,
     *     subjects: array<string, array<string, string>>,
     *     classes: array<string, array<string, string>>,
     *     selectedSyllabus: string,
     *     selectedSubject: string,
     *     selectedClass: string,
     *     hasCurriculumAccess: bool,
     *     enabledMap: array<string, array<string, array<string, bool>>>|null
     * }
     */
    public static function resolveForUser(
        ?User $user,
        array $syllabuses,
        array $subjects,
        array $classes,
        string $requestedSyllabus,
        string $requestedSubject,
        string $requestedClass
    ): array {
        $enabledMap = self::enabledMapForUser($user);

        if ($enabledMap === null) {
            return [
                'syllabuses' => $syllabuses,
                'subjects' => $subjects,
                'classes' => $classes,
                'selectedSyllabus' => $requestedSyllabus,
                'selectedSubject' => $requestedSubject,
                'selectedClass' => $requestedClass,
                'hasCurriculumAccess' => true,
                'enabledMap' => null,
            ];
        }

        $visibleSyllabuses = array_filter(
            $syllabuses,
            fn (array $item, string $key): bool => ! empty($enabledMap[$key]),
            ARRAY_FILTER_USE_BOTH
        );

        if (empty($visibleSyllabuses)) {
            return [
                'syllabuses' => [],
                'subjects' => [],
                'classes' => [],
                'selectedSyllabus' => '',
                'selectedSubject' => '',
                'selectedClass' => '',
                'hasCurriculumAccess' => false,
                'enabledMap' => $enabledMap,
            ];
        }

        $selectedSyllabus = array_key_exists($requestedSyllabus, $visibleSyllabuses)
            ? $requestedSyllabus
            : (string) array_key_first($visibleSyllabuses);

        $visibleSubjects = array_filter(
            $subjects,
            fn (array $item, string $key): bool => ! empty($enabledMap[$selectedSyllabus][$key]),
            ARRAY_FILTER_USE_BOTH
        );

        if (empty($visibleSubjects)) {
            return [
                'syllabuses' => $visibleSyllabuses,
                'subjects' => [],
                'classes' => [],
                'selectedSyllabus' => $selectedSyllabus,
                'selectedSubject' => '',
                'selectedClass' => '',
                'hasCurriculumAccess' => false,
                'enabledMap' => $enabledMap,
            ];
        }

        $selectedSubject = array_key_exists($requestedSubject, $visibleSubjects)
            ? $requestedSubject
            : (string) array_key_first($visibleSubjects);

        $visibleClasses = array_filter(
            $classes,
            fn (array $item, string $key): bool => ! empty($enabledMap[$selectedSyllabus][$selectedSubject][$key]),
            ARRAY_FILTER_USE_BOTH
        );

        $selectedClass = array_key_exists($requestedClass, $visibleClasses)
            ? $requestedClass
            : (string) (array_key_first($visibleClasses) ?? '');

        return [
            'syllabuses' => $visibleSyllabuses,
            'subjects' => $visibleSubjects,
            'classes' => $visibleClasses,
            'selectedSyllabus' => $selectedSyllabus,
            'selectedSubject' => $selectedSubject,
            'selectedClass' => $selectedClass,
            'hasCurriculumAccess' => $selectedClass !== '',
            'enabledMap' => $enabledMap,
        ];
    }
}
