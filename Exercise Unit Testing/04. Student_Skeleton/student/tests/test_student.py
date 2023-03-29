from unittest import TestCase, main

from project.student import Student


class TestStudent(TestCase):
    def setUp(self) -> None:
        self.student = Student('amy', {'math': ['first']})

    def test_init(self):
        self.assertEqual(self.student.name, 'amy')
        self.assertEqual(self.student.courses, {'math': ['first']})

    def test_init_if_courses_None(self):
        self.my_student = Student('amy')
        self.assertEqual(self.my_student.name, 'amy')
        self.assertEqual(self.my_student.courses, {})

    def test_if_coure_name_in_courses(self):
        result = self.student.enroll('math', ['second'])
        self.assertEqual(self.student.courses['math'][1], 'second')
        self.assertEqual(result, "Course already added. Notes have been updated.")

    def test_if_course_name_is_not_in_courses_with_notes_yes(self):
        result = self.student.enroll('english', 'first', 'Y')
        self.assertEqual(self.student.courses['english'], 'first')
        self.assertEqual(result, "Course and course notes have been added.")

    def test_if_course_name_is_not_in_courses_with_notes_empty_string(self):
        result = self.student.enroll('english', 'first')
        self.assertEqual(self.student.courses['english'], 'first')
        self.assertEqual(result, "Course and course notes have been added.")

    def test_if_course_name_not_in_courses(self):
        result = self.student.enroll('english', 'first', 'No')
        self.assertEqual(self.student.courses['english'], [])
        self.assertEqual(result, "Course has been added.")

    def test_notes_if_course_name_in_courses(self):
        result = self.student.add_notes('math','again')
        self.assertEqual(self.student.courses['math'][1],'again')
        self.assertEqual(result,"Notes have been updated")

    def test_notes_if_course_name_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.add_notes('english','yes')
        self.assertEqual("Cannot add notes. Course not found.",str(ex.exception))

    def test_leave_course_if_course_in_courses(self):
        result = self.student.leave_course('math')
        self.assertEqual(self.student.courses,{})
        self.assertEqual(result,"Course has been removed")

    def test_leave_course_if_course_not_in_courses(self):
        with self.assertRaises(Exception) as ex:
            self.student.leave_course('english')
        self.assertEqual("Cannot remove course. Course not found.",str(ex.exception))


if __name__ == "__main__":
    main()
