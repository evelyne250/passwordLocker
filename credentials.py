class Credentials:
    '''
    Class that generates new instances of credentials for their user's accounts.
    '''

    credentials_list = []

    def __init__(self, account_name, account_password):
        self.account_name = account_name
        self.account_password = account_password

    def save_credentials(self):
        '''
        save credentials method that stores new credentials into our list
        '''
        Credentials.credentials_list.append(self)


    def delete_credential(self):

        '''
        delete_credential method deletes a saved credential from our list
        '''

        Credentials.credentials_list.remove(self)

    @classmethod
    def find_by_name(cls,account_name):
        '''
        Method that takes in a name and returns credentials that matches that name.

        Args:
            name: name of the social media to search for
        Returns :
            Credential of person that matches the name.
        '''

        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return credentials


    @classmethod
    def credential_exist(cls, account_name):
        '''
        Method that checks if a credentials exists from the list_of_creds.
        Args:
            name: acc_name to search if it exists
        Returns :
            Boolean: True or false depending if the credentials exists
        '''
        for credentials in cls.credentials_list:
            if credentials.account_name == account_name:
                return True
        return False
