class Product():
    def __init__(self, id, name, cost, link) -> None:
        self.id = id
        self.name = name
        self.cost = cost
        self.link = link

    def __str__(self) -> str:
        return f'Product["Id":{self.id}, "Nome":{self.name}, "Custo":{self.cost}, "Link":{self.link}]'