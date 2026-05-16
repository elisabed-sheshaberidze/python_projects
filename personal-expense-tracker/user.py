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
        value = value.strip()
        if len(value) < 4 or len(value) > 20:
            raise ValueError("Username must be between 4 and 20 characters.")
        elif not all(c.isalnum() or c == '_' for c in value):
            raise ValueError("Username can only contain letters, numbers, and underscores.")
        elif value[0] in '_0123456789':
            raise ValueError("Username cannot start with underscore or number.")
        else:
            self._username = value.lower().strip()

    @property
    def password(self):
        return self._password
        
    @password.setter
    def password(self, value):
        value = value.strip()
        if len(value) < 8:
            raise ValueError("Password must be at least 8 characters long.")
        elif not re.search(r'[A-Z]', value):
            raise ValueError("Password must contain at least one uppercase letter.")
        elif not re.search(r'[a-z]', value):
            raise ValueError("Password must contain at least one lowercase letter.")
        elif not re.search(r'[0-9]', value):
            raise ValueError("Password must contain at least one digit.")
        else:
            self._password = value