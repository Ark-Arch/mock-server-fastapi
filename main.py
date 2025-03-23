from fastapi import FastAPI
from pydantic import BaseModel
from typing import List

app = FastAPI()

# Sample Data
products = [
    {
        "id": 1,
        "category": "shoes",
        "image": "shoe1.jpg",
        "name": "Hiker",
        "price": 94.95,
        "skus": [{"sku": "17", "size": 7}, {"sku": "18", "size": 8}],
        "description": "This rugged boot will get you up the mountain safely."
    },
    {
        "id": 2,
        "category": "shoes",
        "image": "shoe2.jpg",
        "name": "Climber",
        "price": 78.99,
        "skus": [{"sku": "28", "size": 8}, {"sku": "29", "size": 9}],
        "description": "Sure-footed traction in slippery conditions."
    },
    {
        "id": 3,
        "category": "shoes",
        "image": "shoe3.jpg",
        "name": "Explorer",
        "price": 145.95,
        "skus": [{"sku": "37", "size": 7}, {"sku": "38", "size": 8}, {"sku": "39", "size": 9}],
        "description": "Look stylish while stomping in the mud."
    }
]

shipping_addresses = [{"id": 1, "city": "", "country": ""}]

# Routes
@app.get("/products")
def get_products():
    return {"products": products}

@app.get("/products/{product_id}")
def get_product(product_id: int):
    product = next((p for p in products if p["id"] == product_id), None)
    return product or {"error": "Product not found"}

@app.get("/shipping")
def get_shipping_addresses():
    return {"shippingAddress": shipping_addresses}

# Run Server: uvicorn main:app --reload
