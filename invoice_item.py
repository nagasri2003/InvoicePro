class InvoiceItem:
    def __init__(self, product, quantity):
        self.product = product
        self.quantity = quantity
        self.total_price = product.price * quantity
