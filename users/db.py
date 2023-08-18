from typing import List, Any, Union, Optional
from fastapi import HTTPException, status
from sqlalchemy import update
from .models import User


async def create(user, database) -> HTTPException | User:
    # check if user exists in the database
    email_exists = database.query(User).filter(User.email == user.email).first()

    if email_exists:
        raise HTTPException(
            status_code=status.HTTP_400_BAD_REQUEST,
            detail="User with this email exists"
        )

    new_user = User(
        first_name=user.first_name,
        last_name=user.last_name,
        email=user.email,
        password=user.password
    )

    database.add(new_user)
    database.commit()
    database.refresh(new_user)
    return new_user


def check_user_exists(user_id, database) -> User:
    user = database.query(User).filter(User.id == user_id).first()
    if not user:
        raise HTTPException(
            status_code=status.HTTP_404_NOT_FOUND,
            detail=f"User with id {user_id} not found"
        )
    return user


async def get(database, user_id=None) -> Union[User, List[User]]:
    if user_id:
        user = check_user_exists(user_id, database)
        return user
    users = database.query(User).all()
    return users


async def put(user_id, data, database) -> User:
    update_user = check_user_exists(user_id, database)

    for field, value in data.items():
        setattr(update_user, field, value)
    database.commit()
    database.refresh(update_user)
    return update_user


async def delete(user_id, database):
    check_user_exists(user_id, database)

    database.query(User).filter(User.id == user_id).delete()
    database.commit()
