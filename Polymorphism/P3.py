class Vehicle:
    def start(self):
        pass

class Car(Vehicle):
    def start(self):
        print("Car starts with a key.")

class Bike(Vehicle):
    def start(self):
        print("Bike starts with a self-start button.")

class Bus(Vehicle):
    def start(self):
        print("Bus starts with a heavy engine.")

vehicles = [Car(), Bike(), Bus()]

for vehicle in vehicles:
    vehicle.start()