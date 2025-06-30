import json

class InventoryManager:
    def __init__(self, file_path='products.json'):
        self.file_path = file_path
        self.products = self.load_products()

    def load_products(self):
        try:
            with open(self.file_path, 'r') as f:
                data = json.load(f)
                return {p['id']: Product.from_dict(p) for p in data}
        except FileNotFoundError:
            return {}

    def save_products(self):
        with open(self.file_path, 'w') as f:
            json.dump([p.to_dict() for p in self.products.values()], f, indent=2)

    def add_product(self, product):
        self.products[product.id] = product
        self.save_products()

    def update_product(self, product_id, quantity):
        if product_id in self.products:
            self.products[product_id].update_stock(quantity)
            self.save_products()

    def view_products(self):
        for p in self.products.values():
            print(f"{p.id}: {p.name} - ₹{p.price:.2f} (Stock: {p.stock})")
