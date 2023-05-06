from sqlalchemy.orm import Session

from src.database.models import Contact
from src.schemas import ContactModel


async def get_contacts(db: Session):
    return db.query(Contact).all()


async def get_contact_by_id(contact_id: int, db: Session):
    return db.query(Contact).filter_by(id = contact_id).first()


async def get_contact_by_email(email, db: Session):
    return db.query(Contact).filter_by(email=email).first()


async def create_contact(body: ContactModel, db: Session):
    contact = Contact(**body.dict())
    db.add(contact)
    db.commit()
    return contact


async def update_contact(body: ContactModel, contact_id, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        contact.name = body.name
        contact.surname = body.surname
        contact.email = body.email
        contact.birthday = body.birthday
        contact.phone = body.phone
        contact.description = body.description
        db.commit()
    return contact


async def remove_contact(contact_id, db: Session):
    contact = await get_contact_by_id(contact_id, db)
    if contact:
        db.delete(contact)
        db.commit()
    return contact
