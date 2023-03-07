class Profile:
    def __init__(self, username, password):
        self.username = username
        self.password = password

    @property
    def username(self):
        return self.__username

    @username.setter
    def username(self, username):
        if 5 < len(username) <15:
            self.__username = username
        else:
            raise ValueError("The username must be between 5 and 15 characters.")

    @property
    def password(self):
        return self.__password

    @password.setter
    def password(self, password):
        if len(password) < 8:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if password.lower() == password:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        if not [l for l in password if l.isdigit()]:
            raise ValueError("The password must be 8 or more characters with at least 1 digit and 1 uppercase letter.")
        self.__password = password
    def __str__(self):
        return f'You have a profile with username: "{self.username}" and password: { "*" * len(self.password)}'

correct_profile = Profile("Username", "Passw0rd")
print(correct_profile)