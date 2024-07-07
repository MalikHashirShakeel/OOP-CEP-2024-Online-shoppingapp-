# from datetime import datetime
# from .Product import Product
# from .History import History

# class Order:
#     def __init__(self, items, username) -> None:
#         self.items = items
#         self.order_date = datetime.now()
#         self.payment_details = {}
#         self.username = username

#     def calculate_total_price(self) -> float:
#         total = 0
#         for product, quantity in self.items:
#             total += product.get_price_with_discount() * quantity
#         return total
    
#     @staticmethod
#     def get_address() -> str:
#         while True:
#             address = input("Enter your address: ").strip()
#             if not address:
#                 print("Address cannot be empty. Please try again.")
#                 continue
#             if len(address) > 100:
#                 print("Address is too long. Please enter a shorter address (max 100 characters).")
#                 continue
#             return address
        
#     def get_payment_details(self, payment_method: str) -> None:
#         if payment_method.lower() == 'credit card':
#             self.payment_details['Payment Method'] = 'Credit Card'
#             while True:
#                 card_number = input("Enter your credit card number: ").strip()
#                 if card_number:
#                     self.payment_details['Card Number'] = card_number
#                     break
#                 else:
#                     print("Card number cannot be empty. Please enter your credit card number.")
            
#             while True:
#                 expiration_date = input("Enter the expiration date (MM/YY): ").strip()
#                 if expiration_date:
#                     self.payment_details['Expiration Date'] = expiration_date
#                     break
#                 else:
#                     print("Expiration date cannot be empty. Please enter the expiration date (MM/YY).")
            
#             while True:
#                 cvv = input("Enter the CVV: ").strip()
#                 if cvv:
#                     self.payment_details['CVV'] = cvv
#                     break
#                 else:
#                     print("CVV cannot be empty. Please enter the CVV.")
        
#         elif payment_method.lower() == 'paypal':
#             self.payment_details['Payment Method'] = 'PayPal'
#             while True:
#                 paypal_email = input("Enter your PayPal email: ").strip()
#                 if paypal_email:
#                     self.payment_details['PayPal Email'] = paypal_email
#                     break
#                 else:
#                     print("PayPal email cannot be empty. Please enter your PayPal email.")
        
#         elif payment_method.lower() == 'bank transfer':
#             self.payment_details['Payment Method'] = 'Bank Transfer'
#             while True:
#                 bank_name = input("Enter your bank name: ").strip()
#                 if bank_name:
#                     self.payment_details['Bank Name'] = bank_name
#                     break
#                 else:
#                     print("Bank name cannot be empty. Please enter your bank name.")
            
#             while True:
#                 account_number = input("Enter your account number: ").strip()
#                 if account_number:
#                     self.payment_details['Account Number'] = account_number
#                     break
#                 else:
#                     print("Account number cannot be empty. Please enter your account number.")
            
#             while True:
#                 routing_number = input("Enter your routing number: ").strip()
#                 if routing_number:
#                     self.payment_details['Routing Number'] = routing_number
#                     break
#                 else:
#                     print("Routing number cannot be empty. Please enter your routing number.")
        
#         else:
#             print("Invalid payment method. Please choose 'Credit Card', 'PayPal', or 'Bank Transfer'.")

#     def payment_method(self):
#         while True:
#             choice = input("Enter a payment method\n(a) Credit Card\n(b) Paypal\n(c) Bank Transfer\n: ").strip().lower()
#             if choice == "a":
#                 return 'credit card'
#             elif choice == "b":
#                 return 'paypal'
#             elif choice == "c":
#                 return 'bank transfer'
#             else:
#                 print("Invalid input entered!")

#     def confirm_order(self):
#         try:
#             with open(f"{self.username}_history.txt", 'a') as history_file:
#                 for product, quantity in self.items:
#                     history_entry = History(product.product_name, quantity, product.get_price_with_discount(), 
#                                             self.order_date.strftime('%Y-%m-%d'), self.order_date.strftime('%H:%M:%S'))
#                     history_file.write(history_entry.format_for_file() + "\n")
#             print("Order confirmed and added to history.")
#         except Exception as e:
#             print(f"Error saving order history: {e}")

#     def run(self):
#         print("Welcome to the Order Processing System!")
#         print("-" * 40)
        
#         print("Your Order:")
#         print("-" * 40)
#         for product, quantity in self.items:
#             print(f"Product: {product.product_name}")
#             print(f"Quantity: {quantity}")
#             print(f"Price: ${product.get_price_with_discount() * quantity:.2f}")
#             print("-" * 40)
        
#         print(f"Total Price: ${self.calculate_total_price():.2f}")
#         print("-" * 40)
        
#         address = self.get_address()
#         print(f"Delivery Address: {address}")
#         print("-" * 40)
        
#         payment_method = self.payment_method()
#         self.get_payment_details(payment_method)
        
#         print("Payment Details:")
#         for key, value in self.payment_details.items():
#             print(f"{key}: {value}")
#         print("-" * 40)
        
#         confirmation = input("Confirm your order (yes/no): ").strip().lower()
#         if confirmation == 'yes':
#             self.confirm_order()
#         else:
#             print("Order canceled.")
#             return

#         print("-" * 40)
#         print("Thank you for your order!")
#         print("-" * 40)

#         # Print the final receipt
#         print(self)

#     def __str__(self):
#         receipt_lines = []
#         receipt_lines.append(f"Order Date: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}")
#         receipt_lines.append("")
#         receipt_lines.append(f"{'Product Name':<20} {'Quantity':<10} {'Price':<10}")
#         receipt_lines.append("-" * 40)

#         grand_total = 0
#         for product, quantity in self.items:
#             total_price = product.get_price_with_discount() * quantity
#             grand_total += total_price
#             receipt_lines.append(f"{product.product_name:<20} {quantity:<10} ${total_price:<10.2f}")

#         receipt_lines.append("-" * 40)
#         receipt_lines.append(f"{'Grand Total':<20} {'':<10} ${grand_total:<10.2f}")
#         receipt_lines.append("")
#         receipt_lines.append("Payment Details:")
#         for key, value in self.payment_details.items():
#             receipt_lines.append(f"{key}: {value}")

#         return "\n".join(receipt_lines)

# # Example usage
# if __name__ == "__main__":
#     product1 = Product(1, "Laptop", "High-end gaming laptop", 1500.0, 10, "Electronics", "http://example.com/laptop.jpg", 4.5, 10)
#     product2 = Product(2, "Mouse", "Wireless mouse", 50.0, 50, "Electronics", "http://example.com/mouse.jpg", 4.0, 5)

#     # Create an order with a list of (Product, quantity) tuples
#     order_items = [(product1, 2), (product2, 3)]
#     username = ""  # Replace with actual username
#     order = Order(order_items, username)
    
#     # Run the order process
#     order.run()
# from datetime import datetime

# class Order:
#     def __init__(self, items, username) -> None:
#         """
#         Initialize an Order object.

#         Args:
#             items (dict): A dictionary where keys are product objects and values are their quantities.
#             username (str): The username of the person placing the order.
#         """
#         self.cart = items  # Dictionary {Product: quantity}
#         self.order_date = datetime.now()
#         self.payment_details = {}
#         self.username = username

#     def calculate_total_price(self) -> float:
#         """
#         Calculate the total price of the order including discounts.

#         Returns:
#             float: The total price of all items in the order.
#         """
#         total = 0
#         for product, quantity in self.cart.items():
#             total += product.get_price_with_discount() * quantity
#         return total

#     @staticmethod
#     def get_address() -> str:
#         """
#         Prompt the user to enter their address with validation.

#         Returns:
#             str: The validated address entered by the user.
#         """
#         while True:
#             address = input("Enter your address: ").strip()
#             if not address:
#                 print("Address cannot be empty. Please try again.")
#                 continue
#             if len(address) > 100:
#                 print("Address is too long. Please enter a shorter address (max 100 characters).")
#                 continue
#             return address

#     def get_payment_details(self, payment_method: str) -> None:
#         """
#         Collect payment details from the user based on the selected payment method.

#         Args:
#             payment_method (str): The chosen payment method ('credit card', 'paypal', 'bank transfer').
#         """
#         self.payment_details['Payment Method'] = payment_method.capitalize()

#         if payment_method.lower() == 'credit card':
#             while True:
#                 card_number = input("Enter your credit card number: ").strip()
#                 if card_number:
#                     self.payment_details['Card Number'] = card_number
#                     break
#                 else:
#                     print("Card number cannot be empty. Please enter your credit card number.")

#             while True:
#                 expiration_date = input("Enter the expiration date (MM/YY): ").strip()
#                 if expiration_date:
#                     self.payment_details['Expiration Date'] = expiration_date
#                     break
#                 else:
#                     print("Expiration date cannot be empty. Please enter the expiration date (MM/YY).")

#             while True:
#                 cvv = input("Enter the CVV: ").strip()
#                 if cvv:
#                     self.payment_details['CVV'] = cvv
#                     break
#                 else:
#                     print("CVV cannot be empty. Please enter the CVV.")

#         elif payment_method.lower() == 'paypal':
#             while True:
#                 paypal_email = input("Enter your PayPal email: ").strip()
#                 if paypal_email:
#                     self.payment_details['PayPal Email'] = paypal_email
#                     break
#                 else:
#                     print("PayPal email cannot be empty. Please enter your PayPal email.")

#         elif payment_method.lower() == 'bank transfer':
#             while True:
#                 bank_name = input("Enter your bank name: ").strip()
#                 if bank_name:
#                     self.payment_details['Bank Name'] = bank_name
#                     break
#                 else:
#                     print("Bank name cannot be empty. Please enter your bank name.")

#             while True:
#                 account_number = input("Enter your account number: ").strip()
#                 if account_number:
#                     self.payment_details['Account Number'] = account_number
#                     break
#                 else:
#                     print("Account number cannot be empty. Please enter your account number.")

#             while True:
#                 routing_number = input("Enter your routing number: ").strip()
#                 if routing_number:
#                     self.payment_details['Routing Number'] = routing_number
#                     break
#                 else:
#                     print("Routing number cannot be empty. Please enter your routing number.")

#         else:
#             print("Invalid payment method. Please choose 'Credit Card', 'PayPal', or 'Bank Transfer'.")

#     def payment_method(self) -> str:
#         """
#         Prompt the user to select a payment method.

#         Returns:
#             str: The selected payment method.
#         """
#         while True:
#             choice = input("Enter a payment method\n(a) Credit Card\n(b) PayPal\n(c) Bank Transfer\n: ").strip().lower()
#             if choice == "a":
#                 return 'credit card'
#             elif choice == "b":
#                 return 'paypal'
#             elif choice == "c":
#                 return 'bank transfer'
#             else:
#                 print("Invalid input entered!")

#     def confirm_order(self):
#         """
#         Save the order details to a file and confirm the order.
#         """
#         try:
#             # with open(f"{self.username}_history.txt", 'a') as history_file:
#             #     for product, quantity in self.items.items():
#             #         history_entry = History(product.product_name, quantity, product.get_price_with_discount(),
#             #                                 self.order_date.strftime('%Y-%m-%d'), self.order_date.strftime('%H:%M:%S'))
#             #         history_file.write(history_entry.format_for_file() + "\n")
#             print("Order confirmed and added to history.")
#         except Exception as e:
#             print(f"Error saving order history: {e}")

#     def run(self):
#         """
#         Run the order process including showing order details, getting address, payment, and confirmation.
#         """
#         print("Welcome to the Order Processing System!")
#         print("-" * 40)

#         print("Your Order:")
#         print("-" * 40)
#         for product, quantity in self.cart.items():
#             print(f"Product: {product.product_name}")
#             print(f"Quantity: {quantity}")
#             print(f"Price: ${product.get_price_with_discount() * quantity:.2f}")
#             print("-" * 40)

#         print(f"Total Price: ${self.calculate_total_price():.2f}")
#         print("-" * 40)

#         address = self.get_address()
#         print(f"Delivery Address: {address}")
#         print("-" * 40)

#         payment_method = self.payment_method()
#         self.get_payment_details(payment_method)

#         print("Payment Details:")
#         for key, value in self.payment_details.items():
#             print(f"{key}: {value}")
#         print("-" * 40)

#         confirmation = input("Confirm your order (yes/no): ").strip().lower()
#         if confirmation == 'yes':
#             self.confirm_order()
#         else:
#             print("Order canceled.")
#             return

#         print("-" * 40)
#         print("Thank you for your order!")
#         print("-" * 40)

#         # Print the final receipt
#         print(self)

#     def __str__(self) -> str:
#         """
#         Generate a string representation of the order for a receipt.

#         Returns:
#             str: Formatted receipt of the order.
#         """
#         receipt_lines = []
#         receipt_lines.append(f"Order Date: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}")
#         receipt_lines.append("")
#         receipt_lines.append(f"{'Product Name':<20} {'Quantity':<10} {'Price':<10}")
#         receipt_lines.append("-" * 40)

#         grand_total = 0
#         for product, quantity in self.cart.items():
#             total_price = product.get_price_with_discount() * quantity
#             grand_total += total_price
#             receipt_lines.append(f"{product.product_name:<20} {quantity:<10} ${total_price:<10.2f}")

#         receipt_lines.append("-" * 40)
#         receipt_lines.append(f"{'Grand Total':<20} {'':<10} ${grand_total:<10.2f}")
#         receipt_lines.append("")
#         receipt_lines.append("Payment Details:")
#         for key, value in self.payment_details.items():
#             receipt_lines.append(f"{key}: {value}")

#         return "\n".join(receipt_lines)

# Example usage
# if __name__ == "__main__":
    # class Product:
    #     def __init__(self, product_id, product_name, description, price, stock, category, image_url, rating, discount):
    #         self.product_id = product_id
    #         self.product_name = product_name
    #         self.description = description
    #         self.price = price
    #         self.stock = stock
    #         self.category = category
    #         self.image_url = image_url
    #         self.rating = rating
    #         self.discount = discount
        
    #     def get_price_with_discount(self):
    #         return self.price * (1 - self.discount / 100)

    # class History:
    #     def __init__(self, product_name, quantity, price, date, time):
    #         self.product_name = product_name
    #         self.quantity = quantity
    #         self.price = price
    #         self.date = date
    #         self.time = time
        
    #     def format_for_file(self):
    #         return f"{self.date} {self.time} - {self.product_name}: {self.quantity} @ ${self.price:.2f}"

    # product1 = Product(1, "Laptop", "High-end gaming laptop", 1500.0, 10, "Electronics", "http://example.com/laptop.jpg", 4.5, 10)
    # product2 = Product(2, "Mouse", "Wireless mouse", 50.0, 50, "Electronics", "http://example.com/mouse.jpg", 4.0, 5)

    # # Create an order with a dictionary {Product: quantity}
    # order_items = {product1: 2, product2: 3}
    # username = "john_doe"  # Replace with actual username
    # order = Order(order_items, username)
    
    # # Run the order process
    # order.run()



# from datetime import datetime

# class Order:
#     def __init__(self, cart, username) -> None:
#         """
#         Initialize an Order object.

#         Args:
#             cart (Cart): An instance of the Cart class.
#             username (str): The username of the person placing the order.
#         """
#         # Convert the cart to the desired format: {Product: quantity}
#         self.items = cart.get_cart()
#         self.order_date = datetime.now()
#         self.payment_details = {}
#         self.username = username

#     def calculate_total_price(self) -> float:
#         total = 0
#         for product, quantity in self.items.items():
#             total += product.get_price_with_discount() * quantity
#         return total

#     @staticmethod
#     def get_address() -> str:
#         while True:
#             address = input("Enter your address: ").strip()
#             if not address:
#                 print("Address cannot be empty. Please try again.")
#                 continue
#             if len(address) > 100:
#                 print("Address is too long. Please enter a shorter address (max 100 characters).")
#                 continue
#             return address
        
#     def get_payment_details(self, payment_method: str) -> None:
#         if payment_method.lower() == 'credit card':
#             self.payment_details['Payment Method'] = 'Credit Card'
#             while True:
#                 card_number = input("Enter your credit card number: ").strip()
#                 if card_number:
#                     self.payment_details['Card Number'] = card_number
#                     break
#                 else:
#                     print("Card number cannot be empty. Please enter your credit card number.")
            
#             while True:
#                 expiration_date = input("Enter the expiration date (MM/YY): ").strip()
#                 if expiration_date:
#                     self.payment_details['Expiration Date'] = expiration_date
#                     break
#                 else:
#                     print("Expiration date cannot be empty. Please enter the expiration date (MM/YY).")
            
#             while True:
#                 cvv = input("Enter the CVV: ").strip()
#                 if cvv:
#                     self.payment_details['CVV'] = cvv
#                     break
#                 else:
#                     print("CVV cannot be empty. Please enter the CVV.")
        
#         elif payment_method.lower() == 'paypal':
#             self.payment_details['Payment Method'] = 'PayPal'
#             while True:
#                 paypal_email = input("Enter your PayPal email: ").strip()
#                 if paypal_email:
#                     self.payment_details['PayPal Email'] = paypal_email
#                     break
#                 else:
#                     print("PayPal email cannot be empty. Please enter your PayPal email.")
        
#         elif payment_method.lower() == 'bank transfer':
#             self.payment_details['Payment Method'] = 'Bank Transfer'
#             while True:
#                 bank_name = input("Enter your bank name: ").strip()
#                 if bank_name:
#                     self.payment_details['Bank Name'] = bank_name
#                     break
#                 else:
#                     print("Bank name cannot be empty. Please enter your bank name.")
            
#             while True:
#                 account_number = input("Enter your account number: ").strip()
#                 if account_number:
#                     self.payment_details['Account Number'] = account_number
#                     break
#                 else:
#                     print("Account number cannot be empty. Please enter your account number.")
            
#             while True:
#                 routing_number = input("Enter your routing number: ").strip()
#                 if routing_number:
#                     self.payment_details['Routing Number'] = routing_number
#                     break
#                 else:
#                     print("Routing number cannot be empty. Please enter your routing number.")
        
#         else:
#             print("Invalid payment method. Please choose 'Credit Card', 'PayPal', or 'Bank Transfer'.")

#     def payment_method(self):
#         while True:
#             choice = input("Enter a payment method\n(a) Credit Card\n(b) PayPal\n(c) Bank Transfer\n: ").strip().lower()
#             if choice == "a":
#                 return 'credit card'
#             elif choice == "b":
#                 return 'paypal'
#             elif choice == "c":
#                 return 'bank transfer'
#             else:
#                 print("Invalid input entered!")

#     def confirm_order(self):
#         try:
#             print("Order confirmed and added to history.")
#         except Exception as e:
#             print(f"Error saving order history: {e}")

#     def run(self):
#         print("Welcome to the Order Processing System!")
#         print("-" * 40)
        
#         print("Your Order:")
#         print("-" * 40)
#         for product, quantity in self.items.items():
#             print(f"Product: {product.product_name}")
#             print(f"Quantity: {quantity}")
#             print(f"Price: ${product.get_price_with_discount() * quantity:.2f}")
#             print("-" * 40)
        
#         print(f"Total Price: ${self.calculate_total_price():.2f}")
#         print("-" * 40)
        
#         address = self.get_address()
#         print(f"Delivery Address: {address}")
#         print("-" * 40)
        
#         payment_method = self.payment_method()
#         self.get_payment_details(payment_method)
        
#         print("Payment Details:")
#         for key, value in self.payment_details.items():
#             print(f"{key}: {value}")
#         print("-" * 40)
        
#         confirmation = input("Confirm your order (yes/no): ").strip().lower()
#         if confirmation == 'yes':
#             self.confirm_order()
#         else:
#             print("Order canceled.")
#             return

#         print("-" * 40)
#         print("Thank you for your order!")
#         print("-" * 40)

#         # Print the final receipt
#         print(self)

#     def __str__(self):
#         receipt_lines = []
#         receipt_lines.append(f"Order Date: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}")
#         receipt_lines.append("")
#         receipt_lines.append(f"{'Product Name':<20} {'Quantity':<10} {'Price':<10}")
#         receipt_lines.append("-" * 40)

#         grand_total = 0
#         for product, quantity in self.items.items():
#             total_price = product.get_price_with_discount() * quantity
#             grand_total += total_price
#             receipt_lines.append(f"{product.product_name:<20} {quantity:<10} ${total_price:<10.2f}")

#         receipt_lines.append("-" * 40)
#         receipt_lines.append(f"{'Grand Total':<20} {'':<10} ${grand_total:<10.2f}")
#         receipt_lines.append("")
#         receipt_lines.append("Payment Details:")
#         for key, value in self.payment_details.items():
#             receipt_lines.append(f"{key}: {value}")

#         return "\n".join(receipt_lines)

from datetime import datetime
from abc import ABC, abstractmethod

class Order(ABC):
    def __init__(self, cart, username) -> None:
        """
        Initialize an Order object.

        Args:
            cart (Cart): An instance of the Cart class.
            username (str): The username of the person placing the order.
        """
        # Convert the cart to the desired format: {Product: quantity}
        self.items = cart.get_cart()
        self.order_date = datetime.now()
        self.payment_details = {}
        self.username = username

    @abstractmethod
    def calculate_total_price(self) -> float:
        """
        Calculate the total price of the order.
        """
        total = 0
        for product, quantity in self.items.items():
            total += product.get_price_with_discount() * quantity
        return total

    @abstractmethod
    def confirm_order(self) -> None:
        """
        Confirm the order and save it to the history.
        """
        try:
            print("Order confirmed and added to history.")
        except Exception as e:
            print(f"Error saving order history: {e}")

    @abstractmethod
    def get_address(self) -> str:
        """
        Get the delivery address from the user.
        """
        while True:
            address = input("Enter your address: ").strip()
            if not address:
                print("Address cannot be empty. Please try again.")
                continue
            if len(address) > 100:
                print("Address is too long. Please enter a shorter address (max 100 characters).")
                continue
            return address

    @abstractmethod
    def get_payment_details(self, payment_method: str) -> None:
        """
        Get the payment details based on the selected payment method.
        """
        if payment_method.lower() == 'credit card':
            self.payment_details['Payment Method'] = 'Credit Card'
            while True:
                card_number = input("Enter your credit card number: ").strip()
                if card_number:
                    self.payment_details['Card Number'] = card_number
                    break
                else:
                    print("\nCard number cannot be empty. Please enter your credit card number.")
            
            while True:
                expiration_date = input("Enter the expiration date (MM/YY): ").strip()
                if expiration_date:
                    self.payment_details['Expiration Date'] = expiration_date
                    break
                else:
                    print("\nExpiration date cannot be empty. Please enter the expiration date (MM/YY).")
            
            while True:
                cvv = input("Enter the CVV: ").strip()
                if cvv:
                    self.payment_details['CVV'] = cvv
                    break
                else:
                    print("\nCVV cannot be empty. Please enter the CVV.")
        
        elif payment_method.lower() == 'paypal':
            self.payment_details['Payment Method'] = 'PayPal'
            while True:
                paypal_email = input("Enter your PayPal email: ").strip()
                if paypal_email:
                    self.payment_details['PayPal Email'] = paypal_email
                    break
                else:
                    print("\nPayPal email cannot be empty. Please enter your PayPal email.")
        
        elif payment_method.lower() == 'bank transfer':
            self.payment_details['Payment Method'] = 'Bank Transfer'
            while True:
                bank_name = input("Enter your bank name: ").strip()
                if bank_name:
                    self.payment_details['Bank Name'] = bank_name
                    break
                else:
                    print("Bank name cannot be empty. Please enter your bank name.")
            
            while True:
                account_number = input("Enter your account number: ").strip()
                if account_number:
                    self.payment_details['Account Number'] = account_number
                   
class BasicOrder(Order):
    def calculate_total_price(self) -> float:
        total = 0
        for product, quantity in self.items.items():
            total += product.get_price_with_discount() * quantity
        return total

    def confirm_order(self) -> None:
        try:
            print("Order confirmed and added to history.")
        except Exception as e:
            print(f"Error saving order history: {e}")

    @staticmethod
    def get_address() -> str:
        while True:
            address = input("Enter your address: ").strip()
            if not address:
                print("Address cannot be empty. Please try again.")
                continue
            if len(address) > 100:
                print("Address is too long. Please enter a shorter address (max 100 characters).")
                continue
            return address

    def get_payment_details(self, payment_method: str) -> None:
        if payment_method.lower() == 'credit card':
            self.payment_details['Payment Method'] = 'Credit Card'
            while True:
                card_number = input("Enter your credit card number: ").strip()
                if card_number:
                    self.payment_details['Card Number'] = card_number
                    break
                else:
                    print("\nCard number cannot be empty. Please enter your credit card number.")
            
            while True:
                expiration_date = input("Enter the expiration date (MM/YY): ").strip()
                if expiration_date:
                    self.payment_details['Expiration Date'] = expiration_date
                    break
                else:
                    print("\nExpiration date cannot be empty. Please enter the expiration date (MM/YY).")
            
            while True:
                cvv = input("Enter the CVV: ").strip()
                if cvv:
                    self.payment_details['CVV'] = cvv
                    break
                else:
                    print("\nCVV cannot be empty. Please enter the CVV.")
        
        elif payment_method.lower() == 'paypal':
            self.payment_details['Payment Method'] = 'PayPal'
            while True:
                paypal_email = input("Enter your PayPal email: ").strip()
                if paypal_email:
                    self.payment_details['PayPal Email'] = paypal_email
                    break
                else:
                    print("\nPayPal email cannot be empty. Please enter your PayPal email.")
        
        elif payment_method.lower() == 'bank transfer':
            self.payment_details['Payment Method'] = 'Bank Transfer'
            while True:
                bank_name = input("\nEnter your bank name: ").strip()
                if bank_name:
                    self.payment_details['Bank Name'] = bank_name
                    break
                else:
                    print("Bank name cannot be empty. Please enter your bank name.")
            
            while True:
                account_number = input("Enter your account number: ").strip()
                if account_number:
                    self.payment_details['Account Number'] = account_number
                    break
                else:
                    print("Account number cannot be empty. Please enter your account number.")
            
            while True:
                routing_number = input("Enter your routing number: ").strip()
                if routing_number:
                    self.payment_details['Routing Number'] = routing_number
                    break
                else:
                    print("Routing number cannot be empty. Please enter your routing number.")
        
        else:
            print("Invalid payment method. Please choose 'Credit Card', 'PayPal', or 'Bank Transfer'.")

    def payment_method(self):
        while True:
            choice = input("Enter a payment method\n(a) Credit Card\n(b) PayPal\n(c) Bank Transfer\n: ").strip().lower()
            if choice == "a":
                return 'credit card'
            elif choice == "b":
                return 'paypal'
            elif choice == "c":
                return 'bank transfer'
            else:
                print("Invalid input entered!")

    def run(self):
        print("Welcome to the Order Processing System!")
        print("-" * 40)
        
        print("Your Order:")
        print("-" * 40)
        for product, quantity in self.items.items():
            print(f"Product: {product.product_name}")
            print(f"Quantity: {quantity}")
            print(f"Price: ${product.get_price_with_discount() * quantity:.2f}")
            print("-" * 40)
        
        print(f"Total Price: ${self.calculate_total_price():.2f}")
        print("-" * 40)
        
        address = self.get_address()
        print(f"Delivery Address: {address}")
        print("-" * 40)
        
        payment_method = self.payment_method()
        self.get_payment_details(payment_method)
        
        print("Payment Details:")
        for key, value in self.payment_details.items():
            print(f"{key}: {value}")
        print("-" * 40)
        
        confirmation = input("Confirm your order (yes/no): ").strip().lower()
        if confirmation == 'yes':
            self.confirm_order()
        else:
            print("Order canceled.")
            return

        print("-" * 40)
        print("Thank you for your order!")
        print("-" * 40)

        # Print the final receipt
        print(self)

    def __str__(self):
        receipt_lines = []
        receipt_lines.append(f"Order Date: {self.order_date.strftime('%Y-%m-%d %H:%M:%S')}")
        receipt_lines.append("")
        receipt_lines.append(f"{'Product Name':<20} {'Quantity':<10} {'Price':<10}")
        receipt_lines.append("-" * 40)

        grand_total = 0
        for product, quantity in self.items.items():
            total_price = product.get_price_with_discount() * quantity
            grand_total += total_price
            receipt_lines.append(f"{product.product_name:<20} {quantity:<10} ${total_price:<10.2f}")

        receipt_lines.append("-" * 40)
        receipt_lines.append(f"{'Grand Total':<20} {'':<10} ${grand_total:<10.2f}")
        receipt_lines.append("")
        receipt_lines.append("Payment Details:")
        for key, value in self.payment_details.items():
            receipt_lines.append(f"{key}: {value}")

        return "\n".join(receipt_lines)
