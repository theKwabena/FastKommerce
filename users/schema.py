from pydantic import BaseModel, constr, EmailStr


class UserBase(BaseModel):
    pass


class UserCreate(UserBase):
    first_name: constr(
        min_length=2, max_length=255
    )
    last_name: constr(
        min_length=2, max_length=255
    )
    email: EmailStr
    password: str


class UserResponse(UserBase):
    id: int
    first_name: str
    last_name: str
    email: str

    class Config:
        orm_mode = True


class UserUpdate(UserBase):
    first_name: constr(
        min_length=2, max_length=255
    ) | None = None
    last_name: constr(
        min_length=2, max_length=255
    ) | None = None
    email: EmailStr
