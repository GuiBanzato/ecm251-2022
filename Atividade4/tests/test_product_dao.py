from src.dao.product_dao import ProductDAO

products = ProductDAO.get_instance().get_all()

for product in products:
    print(product)

product = ProductDAO.get_instance().get_product()
product.name = "Camiseta UA"
product.cost = 100
print(ProductDAO.get_instance().update_product(product))
print(ProductDAO.get_instance().delete_product(product.id))