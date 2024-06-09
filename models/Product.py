class Product:
    def __init__(self,p_id,p_name,p_desc,p_price,p_qty,p_cat=None,p_img=None,p_rating=None,p_discount=None) -> None:
        self.product_id = p_id
        self.poduct_desription = p_desc
        self.product_price = p_price
        self.product_quantity = p_qty
        self.product_name = p_name
        self.product_category = p_cat
        self.product_image = p_img
        self.product_rating = p_rating
        self.product_discount = p_discount
        self.num_ratings = 0
        
    def update_stock(self, quantity):
        if quantity >= 0:
            self.product_quantity = quantity
        else:
            raise ValueError("Stock quantity cannot be negative")
        
    def is_in_stock(self):
        return self.product_quantity > 0
    
    def rate_product(self, new_rating):
        if 0 <= new_rating <= 5:
            total_rating = self.product_rating * self.num_ratings
            self.num_ratings += 1
            self.product_rating = (total_rating + new_rating) / self.num_ratings
        else:
            raise ValueError("Rating must be between 0 and 5")
        
    def get_price_with_discount(self):
        if self.product_discount > 0:
            return self.product_price * (1 - self.product_discount / 100)
        return self.product_price
    
    def apply_discount(self, discount_percentage):
        if 0 <= discount_percentage <= 100:
            self.product_discount = discount_percentage
        else:
            raise ValueError("Discount percentage must be between 0 and 100")
        
    def __repr__(self):
        return f"<Product {self.product_name} (ID: {self.product_id}) - Price: ${self.product_price:.2f}>"

if __name__ == "__main__":
    product = Product(1, "Laptop", "High-end gaming laptop", 1500.0, 10, "Electronics", "http://example.com/laptop.jpg", 4.5)
    print(product)
    print(product.is_in_stock())
    product.apply_discount(75)
    print(product.get_price_with_discount())
    print(product.product_quantity)
    product.update_stock(50)
    print(product.product_quantity)