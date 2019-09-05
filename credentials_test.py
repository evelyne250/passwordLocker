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
          
    #######

    def test_save_credentials(self):
        '''
        test_save_credential test case to test if the credential object is saved into
         the credentials list
        '''
        self.new_credential.test_save_credentials() # saving the new credential
        self.assertEqual(len(Credentials.credentials_list),1)
if __name__ == '__main__':
    unittest.main()
 
