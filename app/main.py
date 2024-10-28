from app.services.product_services import ProductServices
from app.source.product_repository import ProductManager

def main():
    repository = ProductServices()
    manager = ProductManager(repository)

    print(manager.add_new_product(name="surface", quantity=100))
    print(manager.get_product_info(product_id=1))

if __name__ == "__main__":
    main()