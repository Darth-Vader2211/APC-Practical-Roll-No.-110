from abc import ABC, abstractmethod

class FoodOrder(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def delivery_charge(self):
        pass


class RestaurantOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price

    def delivery_charge(self):
        return 0


class HomeDeliveryOrder(FoodOrder):
    def __init__(self, food_price):
        self.food_price = food_price

    def calculate_bill(self):
        return self.food_price + self.delivery_charge()

    def delivery_charge(self):
        return 50


r = RestaurantOrder(500)
h = HomeDeliveryOrder(500)

print("Restaurant Bill:", r.calculate_bill())
print("Restaurant Delivery Charge:", r.delivery_charge())

print("Home Delivery Bill:", h.calculate_bill())
print("Home Delivery Charge:", h.delivery_charge())