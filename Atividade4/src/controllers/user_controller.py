from models.user_model import User
from src.dao.user_dao import UserDAO


class UserController():

    def __init__(self) -> None:
        pass
    
    def insert_user(self, user) -> bool:
        try:
            UserDAO.get_instance().insert_user(user)
        except:
            return False 
        return True
    
    def get_all_users(self) -> list[UserDAO]:
        users = UserDAO.get_instance().get_all()
        return users
            
    def delete_user(self, email) -> bool:
        return UserDAO.get_instance().delete_user(email)
    
    def update_user(self,user):
        return UserDAO.get_instance().update_user(user)
    
    def search_all_users_email(self, email) -> list[User]:
        user = UserDAO.get_instance().search_all_for_email(email)
        return user

    def check_login(self, email, password):
        user_teste = User(name=None, password=password, email=email)
        for user in UserDAO.get_instance().get_all():
            if user.email == user_teste.email and user.password == user_teste.password:
                return True            
        return False
    
    def getName(self, name):
        for user in self.users:
            if user.name == name:
                return user.name
        return None