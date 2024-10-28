from app.entities.product import Product
from app.interfaces.i_product_repository import IProductRepository

class ProductManager:
    
    def __init__(self, repository: IProductRepository):
        self.repository = repository

    def add_new_product(self, name: str, quantity: int):
        product = Product(id=1, name = name, quantity = quantity)
        self.repository.add_product(product)
        return f"Product {name} added successfully."
    
    def get_product_info(self, product_id: int):
        product = self.repository.get_product_by_id(product_id)
        if product:
            return f"Product: {product.name}, Quantity: {product.quantity}"
        return "Product not found."