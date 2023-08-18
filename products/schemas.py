from pydantic import BaseModel, EmailStr, constr


class Category(BaseModel):
    name: constr(
        min_length=2,
        max_length=255
    )


class ProductBase(BaseModel):
    id: int
    quantity: int
    description: str
    price: float

    class Config:
        orm_mode = True


class Product(ProductBase):
    category_id : int
