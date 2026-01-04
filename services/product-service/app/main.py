from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI(title="Product Service")

class Product(BaseModel):
    id: int
    name: str
    price: float

# Demo product list
products = [
    Product(id=1, name="T-Shirt", price=19.99),
    Product(id=2, name="Jeans", price=49.99),
    Product(id=3, name="Shoes", price=89.99),
]

@app.get("/health")
def health():
    return {"status": "ok", "service": "product-service"}

@app.get("/products", response_model=List[Product])
def get_products():
    return products
