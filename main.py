from fastapi import FastAPI, Header
from fastapi.params import Body
from typing import Optional
from pydantic import BaseModel

app = FastAPI()


@app.get("/")
def read_root():
    return {"message": "Welcome to the FastAPI application!"}


products = [
    {"id": 1, "name": "Laptop", "price": 10099},
    {"id": 2, "name": "mobile", "price": 12999},
    {"id": 3, "name": "Laptop", "price": 15999},
]


@app.get("/products")
def get_products():
    return {"products": products}


@app.post("/products")
def create_product(product: dict = Body(...)):
    products.append(product)
    return {"message": "Product created successfully!"}


categories = ["mobile", "laptop", "tablet", "desktop", "headphone", "Tv"]


@app.get("/categories")
def get_categories():
    return {"categories": categories}


@app.get("/categories/{category_name}")
def get_category(category_name: str):
    if category_name in categories:
        return {"category": category_name}
    else:
        return {"message": "Category not found."}


@app.get("/get_header")
async def get_header(accept: str = Header(None), content_type: str = Header(None), user_agent: Header(None), host: str = Header(None)):
    request_header = {}
    request_header["Accept"] = accept
    request_header["Content-Type"] = content_type
    request_header["User-Agent"] = user_agent
    request_header["Host"] = host

    return {"Request Header": request_header}
