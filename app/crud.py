from sqlalchemy.orm import Session
from app import models
from app.auth import hash_password


# ---------- USERS ----------
def get_user_by_email(db: Session, email: str):
    return db.query(models.User).filter(models.User.email == email).first()


def create_user(db: Session, email: str, password: str):
    user = models.User(
        email=email,
        hashed_password=hash_password(password)
    )
    db.add(user)
    db.commit()
    db.refresh(user)
    return user


# ---------- CONTACTS ----------
def create_contact(db: Session, contact, user_id: int):
    db_contact = models.Contact(**contact.dict(), owner_id=user_id)
    db.add(db_contact)
    db.commit()
    db.refresh(db_contact)
    return db_contact


def get_contacts(db: Session, user_id: int):
    return db.query(models.Contact).filter(models.Contact.owner_id == user_id).all()
