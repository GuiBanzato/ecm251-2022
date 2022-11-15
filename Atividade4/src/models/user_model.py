class User():
    def __init__(self, user, email, password):
        self._email = email
        self._user = user
        self._password = password

    def get_user(self):
        return self._user

    def get_email(self):
        return self._email

    def get_password(self):
        return self._password

    def __str__(self) -> str:
        return f'User(user:{self.get_user()}, email:{self.get_email()}, password:{self.get_password()})'