from student import Student
import unittest

class TestStudent(unittest.TestCase):

    def test_full_name(self):
        student = Student("John", "Doe")
        self.assertEqual(student.full_name, "John Doe")

if __name__ == '__main__':
    unittest.main()