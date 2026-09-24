from abc import ABC, abstractmethod

class Transport(ABC):
    @abstractmethod
    def calculate_fare(self, distance):
        pass


class Bus(Transport):
    def calculate_fare(self, distance):
        return distance * 2


class Train(Transport):
    def calculate_fare(self, distance):
        return distance * 3


class Taxi(Transport):
    def calculate_fare(self, distance):
        return distance * 10


class Flight(Transport):
    def calculate_fare(self, distance):
        return distance * 15


distance = 100

print("Bus Fare:", Bus().calculate_fare(distance))
print("Train Fare:", Train().calculate_fare(distance))
print("Taxi Fare:", Taxi().calculate_fare(distance))
print("Flight Fare:", Flight().calculate_fare(distance))