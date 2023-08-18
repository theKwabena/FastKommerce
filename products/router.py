from fastapi import APIRouter, Depends, status, Response, HTTPException
from sqlalchemy.orm import Session

from config.settings import get_db

from .schemas import Category, Product
from . import db

router = APIRouter(
    tags=['Products'],
    prefix="/products"
)


@router.post("/category", status_code=status.HTTP_200_OK, response_model=Category)
async def create_category(category: Category, database: Session = Depends(get_db)):
    new_category = await db.create_category(category, database)
    return new_category


@router.get("/category", status_code=status.HTTP_200_OK, response_model=list[Category])
async def get_all_categories(database : Session = Depends(get_db)):
    return await db.get_category(database=database)


@router.get("/category/{category_id}", status_code=status.HTTP_200_OK, response_model=Category)
async def get_category(category_id: int, database : Session = Depends(get_db)):
    return await db.get_category(category_id=category_id, database=database)


@router.delete("/category/{category_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_category(category_id : int, database : Session = Depends(get_db)):
    return await db.delete_category(category_id, database)