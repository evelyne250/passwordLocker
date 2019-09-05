import unittest #unittest module imported
from user import User #Importing User class

class TestUser(unittest.TestCase):
    '''
    Test class that defines test cases for the user class behaviours.
    '''
    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_user = User("evelyne","umuhire", "evelyne250", "evelyne@22")

    def test_init(self):
          '''
          test_init test case to test if the object is initialized properly
          '''
          self.assertEqual(self.new_user.first_name, "evelyne")
          self.assertEqual(self.new_user.last_name, "umuhire")
          self.assertEqual(self.new_user.user_name, "evelyne250")
          self.assertEqual(self.new_user.password, "evelyne@22")

# if __name__ == '__main__':
#     unittest.main()