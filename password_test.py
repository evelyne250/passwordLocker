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

