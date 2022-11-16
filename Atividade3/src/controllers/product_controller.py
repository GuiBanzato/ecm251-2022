from src.models.product_model import Product

class ProductController:
    def __init__(self):
        self._produtos = [
            Product("Camiseta UA", Custo = "100.00", Link = "http://d3ugyf2ht6aenh.cloudfront.net/stores/001/053/900/products/boku-nh-bl-mockup-camiseta-2020-frente21-664344fafec466225215857648887919-640-0.jpg"),
            Product("Student ID", Custo = "5.00", Link = "https://cdn.shopify.com/s/files/1/0589/7568/2732/products/uraraka.jpg?v=1631147648"),
            Product("Deku Action Figure", Custo = "250.00", Link = "https://cf.shopee.com.br/file/d12cc589c1ecabb4f3128ad7732246cf"),
            Product("Mangá Volume 1", Custo = "20.00", Link = "https://m.media-amazon.com/images/I/71bELfIWTDL.jpg")
        ]

    def get_product(self,index):
        return self._products[index]