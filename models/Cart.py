from models.Product import Product 
from models.MarketPlace import Marketplace


class Cart:
    def __init__(self,marketplace) -> None:
        self.cart = {}
        self.marketplace = marketplace
        
    def add_product(self, product, quantity=1):
        while True:
            if quantity < 0:
                print("Quantity can't be negative")
                continue
            else:
                if product.product_id in self.cart:
                    self.cart[product.product_id] += quantity
                else:
                    self.cart[product.product_id] = quantity
                break
                
    def remove_product(self, product):
            if product.product_id in self.cart:
                del self.cart[product.product_id]
    
    def update_quantity(self, product, quantity):
        while True:
            if quantity < 0 :
                print('Quantity cant be negative')
                continue
            else:
                self.cart[product.product_id] = quantity
                break
            
    def clear_cart(self):
        self.cart.clear()
    
    def is_empty(self):
        return len(self.cart) == 0
    
    def get_total_price(self):
        total = 0
        for product_id, quantity in self.cart.items():
            product = self.get_product_by_id(product_id)
            total += product.product_price * quantity
        return total
    
    def get_cart(self):
        # Returns a dictionary with product instances as keys and their quantities as values
        return {self.marketplace.get_product(product_id): quantity for product_id, quantity in self.cart.items() if self.marketplace.get_product(product_id)}
    
    def get_product_by_id(self, product_id):
        return self.marketplace.get_product(product_id)