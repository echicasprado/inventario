from abc import ABC, abstractmethod
from typing import Optional
from app.entities.product import Product

class IProductRepository(ABC):

    @abstractmethod
    def add_product(self, product: Product) -> None:
        pass
    
    @abstractmethod
    def get_product_by_id(self, product_id:int ) -> Optional[Product]:
        """Obtener un producto por ID"""
        pass