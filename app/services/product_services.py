from app.interfaces.i_product_repository import IProductRepository
from app.models.product_model import ProductModel
from app.entities.product import Product
from app.core.database_config import LocalSession

class ProductServices(IProductRepository):

    def __init__(self):
        self.db = LocalSession()

    def add_product(self, product: Product) -> None:
        db_product = ProductModel(name = product.name, quantity = product.quantity)
        self.db.add(db_product)
        self.db.commit()

    def get_product_by_id(self, product_id: int) -> Product:
        db_product = self.db.query(ProductModel).filter(ProductModel.id == product_id).first()
        if db_product:
            return Product(id = db_product.id, name = db_product.name, quantity = db_product.quantity)
        return None