class CatalogService:
    def __init__(self):
        self.products = [
            {"name": "Book", "price": 120, "category": "books"},
            {"name": "Phone", "price": 500, "category": "electronics"},
        ]

    def get_products(self):
        return self.products

    def add_product(self, product: dict):
        self.products.append(product)
