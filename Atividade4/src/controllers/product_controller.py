from src.models.product_model import Product
from src.dao.product_dao import ProductDAO

class ProductController:
    def __init__(self) -> None:
        pass

    def get_product(self, id) -> Product:
        product = ProductDAO.get_instance().get_product(id)
        return product

    def insert_product(self, product) -> bool:
        try:
            ProductDAO.get_instance().insert_product(product)
        except:
            return False
        return True

    def get_all_products(self) -> list[Product]:
        products = ProductDAO.get_instance().get_all()
        return products
    
    def update_product(self, product) -> bool:
        return ProductDAO.get_instance().update_product(product)

    def delete_product(self, id) -> bool:
        return ProductDAO.get_instance().delete_product(id)

    def search_all_products_name(self, name) -> list[Product]:
        products = ProductDAO.get_instance().search_all_for_name(name)
        return products