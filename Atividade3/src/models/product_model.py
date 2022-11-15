class Product():
    def __init__(self,name, cost, link):
        self.name = name
        self.cost = cost
        self.link = link
    def __str__(self) -> str:
        return f'Product(name:{self.name}, cost:{self.price}, link:{self.url})'
    def __eq__(self, __o: object) -> bool:
        if type(__o) != Product:
            return False
        return self.name == __o.name