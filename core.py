from fastapi import FastAPI
from users.router import router as user_router
from products.router import router as product_router
app = FastAPI(title="FastKommerce", version="0.0.1")

app.include_router(user_router)
app.include_router(product_router)
