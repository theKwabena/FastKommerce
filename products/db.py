from typing import List, Any, Union, Optional
from fastapi import HTTPException, status
from sqlalchemy import update
from .models import Category


async def create_category(category, database)-> Category:
    category_exists = database.query(Category).filter(Category.name == category.name).first()
    if category_exists:
        raise  HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="Category already exists"
        )
    new_category = Category(
        name = category.name
    )

    database.add(new_category)
    database.commit()
    database.refresh(new_category)

    return new_category


def check_category(category_id, database):
    category = database.query(Category).filter(Category.id == category_id).first()
    if not category:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"Category with id {id} not found"
        )
    return category


async def get_category(*, category_id : int | None = None, database) -> Union[Category, list[Category]]:
    if category_id:
        category = check_category(category_id, database)
        return category
    categories = database.query(Category).all()
    return categories


async def delete_category(category_id : int, database):
    category = check_category(category_id, database=database)

    database.query(Category).filter(Category.id == category_id).delete()
    database.commit()

