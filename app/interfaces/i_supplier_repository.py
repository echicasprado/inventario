from abc import ABC, abstractmethod
from app.entities.supplier import Supplier

class ISupplierRepository(ABC):

    @abstractmethod
    def add_supplier(self, supplier: Supplier) -> None:
        """Agregar un nuevo proveedor"""
        pass

    @abstractmethod
    def get_supplier_by_id(self, supplier_id: int) -> Supplier:
        """Obtener informacion de proveedor por id"""
        pass