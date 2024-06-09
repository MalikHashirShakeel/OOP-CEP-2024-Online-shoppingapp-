import sys
import os

# Add the parent directory to sys.path
sys.path.insert(0, os.path.abspath(os.path.join(os.path.dirname(__file__), '..')))

from Product import Product 
#<--------------------JUST TO CHECK FOR ERRORS , REMOVE AFTER PASS------------------------------------->|
class Cart:
    def __init__(self) -> None:
        self.cart = {}
        
    def add_product(self, product, quantity=1):
        if quantity < 0:
            raise ValueError("Quantity can't be nagative")
        else:
            if product.product_id in self.cart:
                self.cart[product.product_id] += quantity
            else:
                self.cart[product.product_id] = quantity
                
    def remove_product(self, product):
            if product.product_id in self.items:
                del self.items[product.product_id]
    
    def update_quantity(self, product, quantity):
        if quantity < 0:
            raise ValueError("Quantity can't be nagative")
        else:
            self.cart[product.product_id] = quantity
            
    def clear_cart(self):
        self.cart.clear()
    
    def is_empty(self):
        return len(self.cart) == 0
    
    def get_total_price(self):
        total = 0
        for product_id, quantity in self.cart.items():
            product = get_product_by_id(product_id)
            total += product.product_price * quantity
        return total
    
    def get_items(self):
        # Returns a dictionary with product instances as keys and their quantities as values
        return {get_product_by_id(product_id): quantity for product_id, quantity in self.items.items()}
    
def get_product_by_id(product_id):
    return Product(product_id, "Mock Product", "Description", 10.0, 100)