class Product():

    def __init__(self, name, cost, link):
        self._name = name
        self._price = cost
        self._link = link
        
    def get_name(self):
        return self._name
        
    def get_price(self):
        return self._price

    def get_url(self):
        return self._url
    

    def __str__(self) -> str:
        return f'Product(name:{self.get_name()}, price:{self.get_price()}, url:{self.get_url()})'