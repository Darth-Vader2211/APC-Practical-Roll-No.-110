class ShoppingCart:
    def __init__(self, customer_name, cart_id):
        self.customer_name = customer_name
        self.cart_id = cart_id
        self.products = []

    def add_product(self, name, price):
        self.products.append((name, price))
        print(name, "added to cart.")

    def remove_product(self, name):
        for product in self.products:
            if product[0] == name:
                self.products.remove(product)
                print(name, "removed from cart.")
                return

        print("Product not found.")

    def total_bill(self):
        total = 0

        for product in self.products:
            total += product[1]

        print("Total Bill: ₹", total)

    def __del__(self):
        print("Shopping cart destroyed.")


cart = ShoppingCart("Yash", 101)

cart.add_product("Keyboard", 1500)
cart.add_product("Mouse", 800)
cart.add_product("Headphones", 2000)

cart.remove_product("Mouse")
cart.total_bill()