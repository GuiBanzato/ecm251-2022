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
        for resultado in self.cursor.fetchall():
            resultados.append(Product(id=resultado[0], name=resultado[1], cost=resultado[2], link=resultado[3]))
        self.cursor.close()
        return resultados
    
    def inserir_item(self, item):
        self.cursor = self.conn.cursor()
        self.cursor.execute("""
            INSERT INTO Itens (id, name, cost, link)
            VALUES(?,?,?,?);
        """, (item.id, item.name, item.cost, item.link))
        self.conn.commit()
        self.cursor.close()
    def pegar_item(self, id):
        self.cursor = self.conn.cursor()
        self.cursor.execute(f"""
            SELECT * FROM Products
            WHERE id = '{id}';
        """)
        item = None
        resultado = self.cursor.fetchone()
        if resultado != None:
            item = Product(id=resultado[0], name=resultado[1], cost=resultado[2], link=resultado[3])
        self.cursor.close()
        return item
    
    def atualizar_item(self, product):
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
    
    def deletar_item(self, id):
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
        resultados = []
        for resultado in self.cursor.fetchall():
            resultados.append(Product(id=resultado[0], name=resultado[1], cost=resultado[2], link=resultado[3]))
        self.cursor.close()
        return resultados