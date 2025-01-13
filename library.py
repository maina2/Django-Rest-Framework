import json
import uuid
from datetime import datetime

# File to store data
DATABASE_FILE = "ecommerce_store.json"

# Initialize the database
def initialize_database():
    try:
        with open(DATABASE_FILE, "r") as file:
            json.load(file)
    except (FileNotFoundError, json.JSONDecodeError):
        with open(DATABASE_FILE, "w") as file:
            json.dump({"products": [], "orders": []}, file)

# Product class
class Product:
    def __init__(self, name, price, stock):
        self.id = str(uuid.uuid4())
        self.name = name
        self.price = price
        self.stock = stock

    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "price": self.price,
            "stock": self.stock,
        }

    @staticmethod
    def add_product(name, price, stock):
        product = Product(name, price, stock)
        data = read_database()
        data["products"].append(product.to_dict())
        write_database(data)
        print(f"Product '{name}' added successfully!")

    @staticmethod
    def view_products():
        data = read_database()
        print("\nAvailable Products:")
        print("ID                                   | Name           | Price   | Stock")
        print("-" * 70)
        for product in data["products"]:
            print(f"{product['id']:<36} | {product['name']:<15} | ${product['price']:<7} | {product['stock']}")
        print()

# Order class
class Order:
    def __init__(self, product_id, quantity, customer_name):
        self.id = str(uuid.uuid4())
        self.product_id = product_id
        self.quantity = quantity
        self.customer_name = customer_name
        self.date = datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    def to_dict(self):
        return {
            "id": self.id,
            "product_id": self.product_id,
            "quantity": self.quantity,
            "customer_name": self.customer_name,
            "date": self.date,
        }

    @staticmethod
    def place_order():
        Product.view_products()
        product_id = input("Enter the product ID to order: ")
        quantity = int(input("Enter the quantity: "))
        customer_name = input("Enter your name: ")

        data = read_database()
        product = next((p for p in data["products"] if p["id"] == product_id), None)

        if not product:
            print("Invalid product ID!")
            return

        if product["stock"] < quantity:
            print(f"Insufficient stock! Only {product['stock']} left.")
            return

        order = Order(product_id, quantity, customer_name)
        data["orders"].append(order.to_dict())
        product["stock"] -= quantity
        write_database(data)

        print(f"Order placed successfully for {quantity} x '{product['name']}'!")

    @staticmethod
    def view_orders():
        data = read_database()
        print("\nCustomer Orders:")
        print("ID                                   | Customer       | Product          | Quantity | Date")
        print("-" * 90)
        for order in data["orders"]:
            product = next((p for p in data["products"] if p["id"] == order["product_id"]), None)
            print(
                f"{order['id']:<36} | {order['customer_name']:<13} | {product['name']:<15} | {order['quantity']:<8} | {order['date']}"
            )
        print()

# Utility functions for database handling
def read_database():
    with open(DATABASE_FILE, "r") as file:
        return json.load(file)

def write_database(data):
    with open(DATABASE_FILE, "w") as file:
        json.dump(data, file, indent=4)

# Main menu
def main_menu():
    while True:
        print("\nE-Commerce Store Management")
        print("1. Add Product")
        print("2. View Products")
        print("3. Place Order")
        print("4. View Orders")
        print("5. Exit")
        choice = input("Enter your choice: ")

        if choice == "1":
            name = input("Enter product name: ")
            price = float(input("Enter product price: "))
            stock = int(input("Enter product stock: "))
            Product.add_product(name, price, stock)
        elif choice == "2":
            Product.view_products()
        elif choice == "3":
            Order.place_order()
        elif choice == "4":
            Order.view_orders()
        elif choice == "5":
            print("Exiting... Have a great day!")
            break
        else:
            print("Invalid choice! Please try again.")

# Run the program
if __name__ == "__main__":
    initialize_database()
    main_menu()
