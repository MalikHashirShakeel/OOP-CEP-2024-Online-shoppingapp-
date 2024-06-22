from .Product import Product
from typing import Dict, List, Any

class Marketplace:
    def __init__(self):
        self.products = {}  # Store products with product_id as the key
    
    def add_product(self, product: Product) -> None:
        if product.product_id in self.products:
            raise ValueError("Product with this ID already exists.")
        self.products[product.product_id] = product

    def remove_product(self, product_id: int) -> None:
        if product_id in self.products:
            del self.products[product_id]
        else:
            raise ValueError("Product with this ID does not exist.")

    def get_product(self, product_id: int) -> Product:
        return self.products.get(product_id, None)

    def list_products(self) -> List[Product]:
        return list(self.products.values())

    def search_products(self, keyword: str) -> List[Product]:
        return [product for product in self.products.values() 
                if keyword.lower() in product.name.lower() or keyword.lower() in product.description.lower()]

    # Optional: List products by category
    def list_products_by_category(self, category: str) -> List[Product]:
        return [product for product in self.products.values() if product.category == category]

    # Optional: Update a product's details
    def update_product(self, product_id: int, **kwargs) -> None:
        product = self.get_product(product_id)
        if not product:
            raise ValueError("Product not found.")
        
        for key, value in kwargs.items():
            if hasattr(product, key):
                setattr(product, key, value)
            else:
                raise ValueError(f"Attribute {key} not found in Product class.")

    # Optional: Filter products based on criteria
    def filter_products(self, criteria: Dict[str, Any]) -> List[Product]:
        def matches_criteria(product: Product) -> bool:
            for key, value in criteria.items():
                if not hasattr(product, key) or getattr(product, key) != value:
                    return False
            return True

        return [product for product in self.products.values() if matches_criteria(product)]
