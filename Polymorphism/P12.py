class Payment:
    def make_payment(self, amount):
        pass

class UPIPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using UPI.")

class CardPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Card.")

class WalletPayment(Payment):
    def make_payment(self, amount):
        print("Paid", amount, "using Wallet.")

def process_payment(payment, amount):
    payment.make_payment(amount)

process_payment(UPIPayment(), 1500)
process_payment(CardPayment(), 2500)
process_payment(WalletPayment(), 1000)