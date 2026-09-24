from abc import ABC, abstractmethod

class Patient(ABC):
    @abstractmethod
    def calculate_bill(self):
        pass

    @abstractmethod
    def treatment(self):
        pass


class InPatient(Patient):
    def calculate_bill(self):
        return 5000

    def treatment(self):
        print("In-patient treatment with hospital stay")


class OutPatient(Patient):
    def calculate_bill(self):
        return 1500

    def treatment(self):
        print("Out-patient consultation")


class EmergencyPatient(Patient):
    def calculate_bill(self):
        return 8000

    def treatment(self):
        print("Emergency treatment")


patients = [InPatient(), OutPatient(), EmergencyPatient()]

for p in patients:
    p.treatment()
    print("Bill:", p.calculate_bill())
    print()