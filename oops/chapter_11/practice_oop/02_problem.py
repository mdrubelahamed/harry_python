"""Class Product

Attributes: name, price, quantity_in_stock

Methods:

__str__() → returns the product’s name, price, and quantity."""


class Product:
    def __init__(self, name, price, quantity_in_stock):
        self.name = name
        self.price = price
        self.quantity_in_stock = quantity_in_stock

    def __str__(self):
        return f"Product: {self.name}, Price: ${self.price}, Quantity in stock: {self.quantity_in_stock}"

    def __repr__(self):
        return f"Product('{self.name}', {self.price}, {self.quantity_in_stock})"


class Store:
    def __init__(self):
        self.inventory = []  # a list of objects

    def add_product(self, product):
        self.inventory.append(product)

    # sell_product(name, quantity) → reduces the quantity_in_stock by the given amount
    def sell_product(self, name, quantity):
        for product in self.inventory:
            if product.name.lower() == name.lower() and product.quantity_in_stock >= quantity:
                product.quantity_in_stock -= quantity
                print(f"{product.name} has been sold in quantity {quantity}.")
                return

        print("Product is either not exists or 0 quantity.")

    # restock_product(name, quantity) → increases the quantity_in_stock by the given amount
    def restock_product(self, name, quantity):
        for product in self.inventory:
            if product.name.lower() == name.lower():
                product.quantity_in_stock += quantity
                print(f"{product.name} has been refilled of quantity {quantity}")
                return
        print(f"Product doesn't exists.")

    def list_inventory(self):
        for product in self.inventory:
            print(product)

    # # Approach 1: Manual loop
    # def total_inventory_value(self):
    #     total_value = 0
    #     for product in self.inventory:
    #         price = product.price
    #         quantity = product.quantity_in_stock
    #         total_value += price * quantity
    #     return total_value

    # Approach 2: Pythonic one-liner
    def total_inventory_value(self):
        return sum(p.price * p.quantity_in_stock for p in self.inventory)


# Create products
laptop = Product("Laptop", 1000, 10)
phone = Product("Phone", 500, 20)
tablet = Product("Tablet", 300, 15)

# Create store and add products
store = Store()
store.add_product(laptop)
store.add_product(phone)
store.add_product(tablet)

# Sell a product
# store.sell_product("Phone", 5)
# store.list_inventory()

# Restock a product
# store.restock_product("Tablet", 10)
# store.list_inventory()

# # List inventory
store.list_inventory()

# # Get total inventory value
print(store.total_inventory_value())
