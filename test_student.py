from student import Student
import unittest

class TestStudent(unittest.TestCase):
    
    @classmethod
    def setUpClass(cls):
        print("setUpClass")
    
    @classmethod    
    def TearDownClass(cls):
        print("TearDownClass")
    
    def setUp(self):
        print("setUp")
        self.student = Student("John", "Doe")
        
    def tearDown(self):
        print("tearDown")

    def test_full_name(self):
        print("test_full_name")
        self.assertEqual(self.student.full_name, "John Doe")
      
    def test_email(self):
        print("test_email")
        self.assertEqual(self.student.email, "john.doe@email.com")
        
    def test_alert_santa(self):
        print("test_alert_santa")
        self.student.alert_santa()
        self.assertTrue(self.student.naughty_list)
        


if __name__ == '__main__':
    unittest.main()