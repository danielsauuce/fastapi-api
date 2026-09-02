from fastapi import FastAPI

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
