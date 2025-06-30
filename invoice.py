from datetime import datetime

class Invoice:
    TAX_RATE = 0.12

    def __init__(self, customer_name):
        self.customer_name = customer_name
        self.items = []
        self.subtotal = 0
        self.tax = 0
        self.total = 0
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M")

    def add_item(self, item):
        self.items.append(item)
        self.calculate_total()

    def calculate_total(self):
        self.subtotal = sum(item.total_price for item in self.items)
        self.tax = round(self.subtotal * self.TAX_RATE, 2)
        self.total = round(self.subtotal + self.tax, 2)

    def print_invoice(self):
        print(f"\nINVOICE — {self.date}")
        print(f"Customer: {self.customer_name}")
        print("-" * 40)
        for item in self.items:
            print(f"{item.product.name:20} x{item.quantity}  ₹{item.total_price:.2f}")
        print("-" * 40)
        print(f"Subtotal: ₹{self.subtotal:.2f}")
        print(f"Tax:      ₹{self.tax:.2f}")
        print(f"Total:    ₹{self.total:.2f}")

    def save_invoice(self):
        filename = f"invoice_{self.customer_name}_{self.date.replace(' ', '_').replace(':', '-')}.txt"
        with open(filename, 'w') as f:
            f.write(f"INVOICE — {self.date}\nCustomer: {self.customer_name}\n")
            f.write("-" * 40 + "\n")
            for item in self.items:
                f.write(f"{item.product.name:20} x{item.quantity}  ₹{item.total_price:.2f}\n")
            f.write("-" * 40 + "\n")
            f.write(f"Subtotal: ₹{self.subtotal:.2f}\n")
            f.write(f"Tax:      ₹{self.tax:.2f}\n")
            f.write(f"Total:    ₹{self.total:.2f}\n")
