from fastapi import FastAPI
from app.service import CatalogService
from app.parser import parse_query
from app.logger import logger

app = FastAPI()
service = CatalogService()


@app.get("/products")
def get_products(q: str | None = None):
    try:
        products = service.get_products()

        if q:
            pred = parse_query(q)
            products = list(filter(pred, products))

        return products

    except Exception as e:
        logger.error(f"Error in /products: {e}")
        return {"error": str(e)}


@app.post("/products")
def add_product(item: dict):
    service.add_product(item)
    return {"status": "ok"}
