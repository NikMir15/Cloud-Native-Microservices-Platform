import os
from fastapi import FastAPI, HTTPException, Header
from pydantic import BaseModel
import requests
from jose import jwt, JWTError

app = FastAPI(title="Order Service")

# Product URL (local default, docker overrides via env var)
PRODUCT_SERVICE_URL = os.getenv("PRODUCT_SERVICE_URL", "http://127.0.0.1:8002")

# JWT config (must match auth-service)
SECRET_KEY = os.getenv("SECRET_KEY", "dev-secret-change-me")
ALGORITHM = os.getenv("ALGORITHM", "HS256")

class OrderRequest(BaseModel):
    product_id: int
    quantity: int

def require_jwt(authorization: str | None):
    if not authorization or not authorization.startswith("Bearer "):
        raise HTTPException(status_code=401, detail="Missing or invalid Authorization header")

    token = authorization.split(" ", 1)[1].strip()
    try:
        payload = jwt.decode(token, SECRET_KEY, algorithms=[ALGORITHM])
        email = payload.get("sub")
        if not email:
            raise HTTPException(status_code=401, detail="Invalid token payload")
        return email
    except JWTError:
        raise HTTPException(status_code=401, detail="Invalid or expired token")

@app.get("/health")
def health():
    return {"status": "ok", "service": "order-service"}

@app.post("/orders")
def create_order(order: OrderRequest, authorization: str | None = Header(default=None)):
    user_email = require_jwt(authorization)

    try:
        r = requests.get(f"{PRODUCT_SERVICE_URL}/products", timeout=5)
    except requests.exceptions.RequestException:
        raise HTTPException(status_code=503, detail="Unable to connect to Product Service")

    if r.status_code != 200:
        raise HTTPException(status_code=503, detail="Product Service unavailable")

    products = r.json()
    product = next((p for p in products if p["id"] == order.product_id), None)

    if not product:
        raise HTTPException(status_code=404, detail="Product not found")

    total = product["price"] * order.quantity

    return {
        "message": "Order created",
        "user": user_email,
        "product": product,
        "quantity": order.quantity,
        "total": total
    }
