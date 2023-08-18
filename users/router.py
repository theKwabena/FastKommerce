from typing import List, Optional
from fastapi import APIRouter, Depends, status, HTTPException, Response
from sqlalchemy.orm import Session
from config.settings import get_db

from .schema import UserCreate, UserResponse, UserUpdate
from .validator import check_email
from . import db

router = APIRouter(tags=["Users"], prefix='/user')


@router.get("/", status_code=status.HTTP_200_OK, response_model=List[UserResponse])
async def all_users(database: Session = Depends(get_db)):
    return await db.get(database)


@router.get("/{user_id}", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def get_user_by_id(user_id: int, database: Session = Depends(get_db)):
    user = await db.get(user_id=user_id, database=database)
    return user


@router.post("/", status_code=status.HTTP_201_CREATED, response_model=UserResponse)
async def create_user(user: UserCreate, database: Session = Depends(get_db)):
    new_user = await db.create(user, database)
    return new_user


@router.put("/{user_id}", status_code=status.HTTP_200_OK)
async def update_user(user_id: int, user: UserUpdate, database: Session = Depends(get_db)):
    user_data = user.model_dump(exclude_unset=True)
    return await db.put(user_id, user_data, database)


@router.delete("/{user_id}", status_code=status.HTTP_204_NO_CONTENT, response_class=Response)
async def delete_user(user_id: int, database: Session = Depends(get_db)):
    return await db.delete(user_id, database)
