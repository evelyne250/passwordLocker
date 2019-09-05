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

    def test_save_credentials(self):
        '''
        test_save_credentials test case to test if the credentials object is saved into our list
        '''
        self.new_credential.save_credentials()  # saving the new credentials
        self.assertEqual(len(Credentials.credentials_list), 1)

    def test_save_multiple_credentials(self):
        '''
        test_save_multiple_credentials to check if we can save multiple credentials
        objects to our credentials_list
        '''
        self.new_credential.save_credentials()
        test_credentials = Credentials("instagram", "eve64@78")  # new credential
        test_credentials.save_credentials()
        self.assertEqual(len(Credentials.credentials_list), 2)

    def tearDown(self):
        '''
        tearDown method that does clean up after each test case has run.
        '''
        Credentials.credentials_list = []

    def test_delete_credential(self):
            '''
            test_delete_credential test if we can remove a credential from our list of credentials
            '''
            self.new_credential.save_credentials()
            test_credentials = Credentials("instagram", "eve64@78")  # new credential
            test_credentials.save_credentials()

            self.new_credential.delete_credential()  # Deleting a credential's object
            self.assertEqual(len(Credentials.credentials_list), 1)



if __name__ == '__main__':
    unittest.main()
 
