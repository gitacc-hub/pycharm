#Abstraction in python
from abc import ABC ,abstractmethod
class Payment(ABC):
    @abstractmethod
    def make_payment(self,amount):
        pass
    @abstractmethod
    def refund(self,amount):
        pass
#Concrete Sub class
class CreditCardPayment(Payment):
    def __init__(self,card_number):
        self.card_number=card_number
    def make_payment(self,amount):
        print(f"Processing payment of ${amount} using card number {self.card_number[-4:]}")
        print("Payment is successful.")
    def refund(self,amount):
        print(f"Issuing a refund of ${amount} to credit card number {self.card_number[-4:]}")

class PayPalPayment(Payment):
    def __init__(self, email):
        self.email = email

    def make_payment(self, amount):
        print(f"Processing PayPal payment of ${amount} for {self.email}")
        # Simulate processing logic
        print("Payment successful!")

    def refund(self, amount):
        print(f"Refunding ${amount} to PayPal account {self.email}")

def process_order(payment_method: Payment, amount: float):
    print("\n--- Order Processing ---")
    payment_method.make_payment(amount)
    print("Generating receipt...")
    payment_method.refund(amount / 2)  # Example partial refund
    print("--- Transaction Complete ---")

if __name__ == "__main__":
    # Try both payment methods
    cc_payment = CreditCardPayment("1234-5678-9876-5432")
    paypal_payment = PayPalPayment("user@example.com")

    process_order(cc_payment, 120.0)
    process_order(paypal_payment, 85.0)