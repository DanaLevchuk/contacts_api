from pydantic import BaseModel, EmailStr
from datetime import date


# ---------- USERS ----------
class UserCreate(BaseModel):
    email: EmailStr
    password: str


class UserResponse(BaseModel):
    id: int
    email: EmailStr

    class Config:
        from_attributes = True


class Token(BaseModel):
    access_token: str
    refresh_token: str
    token_type: str = "bearer"


# ---------- CONTACTS ----------
class ContactCreate(BaseModel):
    first_name: str
    last_name: str
    email: EmailStr
    phone: str
    birthday: date
    extra_data: str | None = None


class ContactResponse(ContactCreate):
    id: int

    class Config:
        from_attributes = True
