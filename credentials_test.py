import unittest #unittest module imported
from credentials import Credentials #Importing User class

class TestCredentials(unittest.TestCase):
    '''
    Test class that defines test cases for the credentials class behaviours.
    '''

    def setUp(self):
        '''
        Set up method to run before each test cases.
        '''
        self.new_credential = Credentials("evelyne","evelyne@22")

    def test_init(self):
          '''
          test_init test case to test if the object is initialized properly
          '''
          self.assertEqual(self.new_credential.account_name, "evelyne")
          self.assertEqual(self.new_credential.account_password, "evelyne@22")
          

if __name__ == '__main__':
    unittest.main()
 
