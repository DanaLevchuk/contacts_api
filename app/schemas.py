from pydantic import BaseModel, EmailStr

class UserCreate(BaseModel):
    email: EmailStr
    password: str


class Token(BaseModel):
    access_token: str
    token_type: str


class ContactCreate(BaseModel):
    name: str
    email: EmailStr | None = None
    phone: str | None = None


class Contact(BaseModel):
    id: int
    name: str
    email: str | None
    phone: str | None

    class Config:
        from_attributes = True
