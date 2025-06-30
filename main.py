from inventory import InventoryManager
from product import Product
from invoice_item import InvoiceItem
from invoice import Invoice

def main():
    manager = InventoryManager()

    while True:
        print("\n1. Add Product\n2. View Products\n3. Create Invoice\n4. Exit")
        choice = input("Choose: ")

        if choice == '1':
            id = input("ID: ")
            name = input("Name: ")
            price = float(input("Price: "))
            stock = int(input("Stock: "))
            manager.add_product(Product(id, name, price, stock))

        elif choice == '2':
            manager.view_products()

        elif choice == '3':
            customer = input("Customer Name: ")
            invoice = Invoice(customer)
            while True:
                manager.view_products()
                pid = input("Enter Product ID (or 'done'): ")
                if pid == 'done': break
                qty = int(input("Quantity: "))
                if pid in manager.products and qty <= manager.products[pid].stock:
                    product = manager.products[pid]
                    invoice.add_item(InvoiceItem(product, qty))
                    product.update_stock(-qty)
                else:
                    print("Invalid or insufficient stock.")
            invoice.print_invoice()
            invoice.save_invoice()
            manager.save_products()

        elif choice == '4':
            break

if __name__ == "__main__":
    main()
