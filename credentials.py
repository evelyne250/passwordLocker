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