class Vehicle:
    def __init__(self, vehicle_no, model, rental_rate):
        self.vehicle_no = vehicle_no
        self.model = model
        self.rental_rate = rental_rate
        self.available = True

    def rent(self):
        if self.available:
            self.available = False
            print("Vehicle rented successfully.")
        else:
            print("Vehicle is not available.")

    def return_vehicle(self, days):
        self.available = True
        charge = self.rental_rate * days
        print("Vehicle returned successfully.")
        print("Rental Charges: ₹", charge)


v = Vehicle("MH09AB1234", "Toyota", 1500)

v.rent()
v.return_vehicle(3)