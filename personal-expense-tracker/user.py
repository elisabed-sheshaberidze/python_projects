import re
class User:
    def __init__(self, username, password):
        self.username = username
        self.password = password

        @property
        def username(self):
            return self._username
        

        @username.setter
        def username(self, value):
            if len(value.strip()) < 4 or len(value.strip()) > 20:
                raise ValueError("Username must be between 4 and 20 characters.")
            elif not all(char.isalnum() for char in value.strip()):
                raise ValueError('Username must contain only letters and numbers.')
        
        @property
        def password(self):
            return self._password
        
        @password.setter
        def password(self, value):
            pass

        


    
