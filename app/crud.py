from sqlalchemy.orm import Session
from app import models


def get_contacts(
    db: Session,
    first_name: str | None = None,
    last_name: str | None = None,
    email: str | None = None,
):
    query = db.query(models.Contact)

    if first_name:
        query = query.filter(models.Contact.first_name.ilike(f"%{first_name}%"))

    if last_name:
        query = query.filter(models.Contact.last_name.ilike(f"%{last_name}%"))

    if email:
        query = query.filter(models.Contact.email.ilike(f"%{email}%"))

    return query.all()
from datetime import date, timedelta


def get_upcoming_birthdays(db: Session):
    today = date.today()
    end_date = today + timedelta(days=7)

    contacts = db.query(models.Contact).all()
    result = []

    for contact in contacts:
        if not contact.birthday:
            continue

        birthday_this_year = contact.birthday.replace(year=today.year)

        if today <= birthday_this_year <= end_date:
            result.append(contact)

    return result
