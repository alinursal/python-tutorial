class Product:
    def __init__(self, name, price, quantity):
        self.name = name
        self.price = price
        self.quantity = quantity

    def display_info(self):
        print(f"Product Name: {self.name}")
        print(f"Price: ${self.price:.2f}")
        print(f"Available Quantity: {self.quantity}")

    def update_quantity(self, amount):
        """Update the quantity of the product. Use a positive amount to restock and negative to sell."""
        if self.quantity + amount < 0:
            print(f"Cannot sell {abs(amount)} units of '{self.name}'. Not enough stock.")
        else:
            self.quantity += amount
            action = "restocked" if amount > 0 else "sold"
            print(f"Successfully {action} {abs(amount)} units of '{self.name}'. New quantity: {self.quantity}")

    def total_value(self):
        """Calculate the total value of the product based on price and quantity."""
        return self.price * self.quantity


class Inventory:
    def __init__(self):
        self.products = []

    def add_product(self, name, price, quantity):
        new_product = Product(name, price, quantity)
        self.products.append(new_product)
        print(f"Added product '{name}' to the inventory.")

    def display_inventory(self):
        print("\nCurrent Inventory:")
        for product in self.products:
            product.display_info()
            print("-" * 30)

    def calculate_total_value(self):
        total_value = sum(product.total_value() for product in self.products)
        print(f"Total value of inventory: ${total_value:.2f}")


def main():
    # Creating the inventory
    inventory = Inventory()

    # Adding products to the inventory
    inventory.add_product("Laptop", 1500.99, 10)
    inventory.add_product("Smartphone", 999.99, 20)
    inventory.add_product("Headphones", 150.99, 50)

    # Displaying the current inventory
    inventory.display_inventory()

    # Updating product quantities
    print("Updating product quantities:")
    inventory.products[0].update_quantity(-3)  # Sell 3 Laptops
    inventory.products[1].update_quantity(5)   # Restock 5 Smartphones

    # Displaying updated inventory
    inventory.display_inventory()

    # Calculating total value of inventory
    inventory.calculate_total_value()

main()