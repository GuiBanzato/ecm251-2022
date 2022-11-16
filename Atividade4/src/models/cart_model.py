from controllers.product_controller import ProductController
import streamlit as st
class Cart():
    def __init__(self, id, name, cost, link):
        self.id = id
        self.name = name
        self.cost = cost
        self.link = link
    
    def __str__(self):
        return f'Cart(Id: {self.id}, Name: {self.name}, Cost: {self.cost}, Link: {self.link})'
    