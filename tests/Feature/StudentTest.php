<?php

namespace Tests\Feature;

use App\Models\Standard;
use App\Models\Student;
use App\Models\Syllabus;
use Illuminate\Foundation\Testing\DatabaseTransactions;
use Illuminate\Support\Facades\Schema;
use Tests\TestCase;

class StudentTest extends TestCase
{
    use DatabaseTransactions;

    public function test_students_table_has_expected_columns(): void
    {
        $this->assertTrue(Schema::hasTable('students'));
        $this->assertTrue(Schema::hasColumns('students', [
            'id',
            'name',
            'standard_id',
            'created_at',
            'updated_at',
        ]));
    }

    public function test_can_create_student_and_access_standard_relation(): void
    {
        $syllabus = Syllabus::firstOrCreate(['name' => 'General Syllabus']);
        $standard = Standard::firstOrCreate(['name' => '10th Standard', 'syllabus_id' => $syllabus->id]);

        $student = Student::create([
            'name' => 'John Doe',
            'standard_id' => $standard->id,
        ]);

        $this->assertDatabaseHas('students', [
            'id' => $student->id,
            'name' => 'John Doe',
            'standard_id' => $standard->id,
        ]);

        $this->assertEquals($standard->id, $student->standard->id);
    }
}
