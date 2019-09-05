class User:
    """
    class that generates and create
    user instances
    """
    users_list = []

    def __init__(self, first_name, last_name, user_name, password):
        self.first_name = first_name
        self.last_name = last_name
        self.user_name = user_name
        self.password = password

    def save_user(self):
        '''
        save_user function saves User objects into users_list
        '''
        self.users_list.append(self)
