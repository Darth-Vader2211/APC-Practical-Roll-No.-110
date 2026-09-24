class FoodOrder:
    def __init__(self, order_id, customer_name, food_item, quantity, price):
        self.order_id = order_id
        self.customer_name = customer_name
        self.food_item = food_item
        self.quantity = quantity
        self.price = price

    def total_bill(self):
        total = self.quantity * self.price
        tax = total * 0.05
        final_bill = total + tax

        print("Order ID:", self.order_id)
        print("Customer:", self.customer_name)
        print("Food Item:", self.food_item)
        print("Quantity:", self.quantity)
        print("Food Cost: ₹", total)
        print("Tax: ₹", tax)
        print("Total Bill: ₹", final_bill)

    def __del__(self):
        print("Order completed.")


order = FoodOrder(101, "Yash", "Pizza", 2, 300)

order.total_bill()