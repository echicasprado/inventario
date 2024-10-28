from app.entities.supplier import Supplier
from app.interfaces.i_supplier_repository import ISupplierRepository

class SupplierManager():
    
    def __init__(self, repository: ISupplierRepository):
        self.repository = repository

    def add_supplier(self, name:str, address:str, contact_info:str):
        supplier = Supplier(id=1, name=name, address=address, contact_info=contact_info)
        self.repository.add_supplier(supplier)
        return f"Supplier {name} added successfully."
    
    def get_supplier_by_id(self, supplier_id:int):
        supplier = self.repository.get_supplier_by_id(supplier_id)
        if supplier:
            return f"Supplier: {supplier.name}, Address: {supplier.address}, Contact info: {supplier.contact_info}"
        return "Supplier not found."