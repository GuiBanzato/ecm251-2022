import sqlite3
from src.models.product_model import Product
import streamlit as st

class ProductDAO:
    
    _instance = None

    def __init__(self) -> None:
        self._connect()

    @classmethod
    def get_instance(cls):
        if cls._instance == None:
            cls._instance = ProductDAO()
        return cls._instance

    def _connect(self):
        self.conn = sqlite3.connect('./Banco_de_dados/sqliteBanza.db')

    def get_all(self):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            SELECT * FROM Products;
        """)
        resultados = []
        for result in self.cursor.fetchall():
            result.append(Product(id=result[0], name=result[1], cost=result[2], link=result[3]))
        self.cursor.close()
        return result
    
    def insert_product(self, product):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Products (id, name, cost, link)
            VALUES(?,?,?,?);
        """, (product.id, product.name, product.cost, product.link))
        self.conn.commit()
        self.cursor.close()
        
    def get_product(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE id = '{id}';
        """)
        product = None
        result = self.cursor.fetchone()
        if result != None:
            product = Product(id=result[0], name=result[1], cost=result[2], link=result[3])
        self.cursor.close()
        return product
    
    def update_product(self, product):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                UPDATE Products SET
                Nome = '{product.name}',
                Custo = {product.cost}, 
                Link = '{product.link}'
                WHERE id = '{product.id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True
    
    def delete_product(self, id):
        try:
            self.cursor = self.conn.cursor()
            self.cursor.execute(f"""
                DELETE FROM Itens 
                WHERE id = '{id}'
            """)
            self.conn.commit()
            self.cursor.close()
        except:
            return False
        return True

    def search_all_for_name(self,name):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE nome LIKE '{name}%';
        """)
        result = []
        for result in self.cursor.fetchall():
            result.append(Product(id=result[0], name=result[1], cost=result[2], link=result[3]))
        self.cursor.close()
        return result