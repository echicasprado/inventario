from sqlalchemy.orm import Session
from app.core.database_config import LocalSession
from app.interfaces.i_supplier_repository import ISupplierRepository
from app.models.supplier_model import SupplierModel
from app.entities.supplier import Supplier

class SupplierService(ISupplierRepository):
    
    def __init__(self):
        self.db: Session = LocalSession()

    def add_supplier(self, supplier):
        db_supplier = SupplierModel(name=supplier.name, address=supplier.address, contact_info= supplier.contact_info)
        self.db.add(db_supplier)
        self.db.commit()

    def get_supplier_by_id(self, supplier_id) -> Supplier:
        db_supplier = self.db.query(SupplierModel).filter(SupplierModel.id==supplier_id).first()
        if db_supplier:
            return Supplier(id=db_supplier.id, name=db_supplier.name, address=db_supplier.address, contact_info=db_supplier.contact_info)
        return None