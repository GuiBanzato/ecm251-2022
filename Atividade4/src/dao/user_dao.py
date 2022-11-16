from models.user_model import User
import sqlite3
import streamlit as st

class UserDAO:
  
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = UserDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./Banco_de_dados/sqliteBanza.db')
           
    def get_all(self):
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                SELECT * FROM User;
            """)
            resultados = []
            for resultado in self.cursor.fetchall():
                resultados.append(User(name=resultado[1], email=resultado[2],password=resultado[3]))
            self.cursor.close()
            return resultados
    
    def insert_user(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute("""
                INSERT INTO User (name, email, password)
                VALUES(?,?,?);
            """, (user.name,user.email,user.password))
            self.conn.commit()
            self.cursor.close()
        except:
            print("Erro inserir_usuario user_dao")
            
    def delete_user(self, email):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM User 
                WHERE email = '{email}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def update_user(self, user):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE User 
                SET name = ?,
                    email = ?,
                    password = ?
                WHERE 
                    email = ?;
            """,(user.name,user.email,user.password,user.email))
            self.conn.commit()
            self.cursor.close()
        except:
            print('Erro DAO atualizar usuario')
        return True
    
    def get_user(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE id = '{id}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = User(id=resultado[0], name=resultado[1], email=resultado[2], password=resultado[3])
        self.cursor.close()
        return item
    
    def search_all_for_email(self,email):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM User
            WHERE email LIKE '{email}%';
        """)
        result = []
        for result in self.cursor.fetchall():
            result.append(User(name=result[1], email=result[2], password=result[3]))
        self.cursor.close()
        return result