from models.Product import Product 
from models.MarketPlace import Marketplace


class Cart:
    def __init__(self,marketplace) -> None:
        self.cart = {}
        self.marketplace = marketplace
        
    def add_product(self, product, quantity):
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
    
    def remove_product(self, product, qty=0):
        product_id = product if isinstance(product, int) else product.product_id
        if product_id in self.cart:
            if qty == 0:
                del self.cart[product_id]
            else:
                self.cart[product_id] -= qty
                if self.cart[product_id] <= 0:
                    del self.cart[product_id]
    
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
    
    def __iadd__(self, product_qty):
        """Override the in-place addition operator (+=) to add product quantity to the cart"""
        product, quantity = product_qty
        self.add_product(product, quantity)
        return self
    
    def __isub__(self, item):
        product, quantity = item
        self.remove_product(product, quantity)
        return self