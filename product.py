class Product:
    def __init__(self, id, name, price, stock):
        self.id = id
        self.name = name
        self.price = price
        self.stock = stock

    def update_stock(self, quantity):
        self.stock += quantity

    def to_dict(self):
        return vars(self)

    @staticmethod
    def from_dict(data):
        return Product(**data)
