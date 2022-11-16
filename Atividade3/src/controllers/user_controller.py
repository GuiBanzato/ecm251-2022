from models.user_model import User


class UserController():
    def __init__(self) -> None:
       
        self.user = [
            User( Nome = "Deku", Senha = "Midoriya", Email = "Deku.Midoriya@myheroacademia.com"),
            User( Nome = "AllMight", Senha = "Toshinori", Email = "All.Might@myheroacademia.com"),
            User( Nome = "Todoroki", Senha = "Shoto", Email = "Todoroki.Shoto@myheroacademia.com"),
            User( Nome = "Bakugou", Senha = "Boom", Email = "Bakugou.Katsuki@myheroacademia.com"),
        ]
    def checkUser(self,user):
        return user in self.user

    def checkLogin(self, name, password):
        user_test = User(name=name, password=password, email=None)
        for user in self.user:
            if user.name == user_test.name and user.password == user_test.password:
                
                return True            
        return False
    
    def getName(self, name):
        for user in self.user:
            if user.name == name:
                return user.name
        return None