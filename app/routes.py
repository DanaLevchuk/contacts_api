from fastapi import APIRouter, Depends, HTTPException, status
from fastapi.security import OAuth2PasswordBearer
from sqlalchemy.orm import Session

from app.database import get_db
from app.schemas import UserCreate, Token
from app import crud

router = APIRouter()

oauth2_scheme = OAuth2PasswordBearer(tokenUrl="/auth/login")


# ===================== AUTH =====================

@router.post("/auth/register", status_code=status.HTTP_201_CREATED)
def register(user: UserCreate, db: Session = Depends(get_db)):
    """
    Register a new user.
    """
    db_user = crud.get_user_by_email(db, user.email)
    if db_user:
        raise HTTPException(status_code=400, detail="Email already registered")

    return crud.create_user(db, user)


@router.post("/auth/login", response_model=Token)
def login(user: UserCreate, db: Session = Depends(get_db)):
    """
    Login user and return JWT token.
    """
    db_user = crud.authenticate_user(db, user.email, user.password)
    if not db_user:
        raise HTTPException(status_code=401, detail="Invalid credentials")

    access_token = crud.create_access_token({"sub": db_user.email})
    return {"access_token": access_token, "token_type": "bearer"}


# ===================== CONTACTS =====================

@router.get("/contacts/", status_code=status.HTTP_200_OK)
def get_contacts(
    token: str = Depends(oauth2_scheme),
):
    """
    Get contacts (authorized users only).
    """
    # якщо токена нема або він невалідний —
    # FastAPI автоматично поверне 401
    return []
