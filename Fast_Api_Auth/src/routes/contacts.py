from fastapi import APIRouter, Depends, HTTPException, status, Path
from typing import List

from sqlalchemy.orm import Session

from src.database.db import get_db
from src.schemas import ContactResponse, ContactModel, ContactName
from src.repository import contacts as repository_contacts
from src.database.models import Role, User
from src.services.auth import auth_service
from src.services.roles import RolesAccess
from fastapi_limiter.depends import RateLimiter

router = APIRouter(prefix='/contacts', tags=['contacts'])

access_get = RolesAccess([Role.admin, Role.user])
access_create = RolesAccess([Role.admin])
access_update = RolesAccess([Role.admin])
access_delete = RolesAccess([Role.admin])


@router.get('/', response_model=List[ContactResponse],
            dependencies=[Depends(RateLimiter(times=5, seconds=2)), Depends(access_get)])
async def get_contacts(db: Session = Depends(get_db), _: User = Depends(auth_service.get_current_user)):
    """
    The get_contacts function returns a list of contacts.

    :param db: Session: Pass the database connection to the function
    :param _: User: Get the current user
    :return: A list of contacts
    :doc-author: Andriy
    """
    contacts = await repository_contacts.get_contacts(db)
    return contacts


@router.get('/birthdays', response_model=List[ContactResponse], dependencies=[Depends(access_get)])
async def get_contacts_by_birthdays(db: Session = Depends(get_db), _: User = Depends(auth_service.get_current_user)):
    """
    The get_contacts_by_birthdays function returns a list of contacts that have birthdays in the current month.
        The function is called by the get_contacts_by_birthdays endpoint, which requires authentication.

    :param db: Session: Pass the database session to the function
    :param _: User: Get the current user from the auth_service
    :return: A list of contacts that have a birthday in the next 30 days
    :doc-author: Andriy
    """
    contacts = await repository_contacts.get_contacts_by_birthdays(db)
    return contacts


@router.get('/{contact_id}', response_model=ContactResponse, dependencies=[Depends(access_get)])
async def get_contact_by_id(contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                            _: User = Depends(auth_service.get_current_user)):
    """
    The get_contact_by_id function returns a contact by its id.
        The function takes an integer as the contact_id parameter, which is required and must be greater than 1.
        It also takes a database session object (db) and the current user (_).
        If no such contact exists, it raises an HTTPException with status code 404 Not Found.

    :param contact_id: int: Get the contact by id
    :param db: Session: Pass the database session to the function
    :param _: User: Get the current user, and the db: session parameter is used to get a database session
    :return: A contact object
    :doc-author: Andriy
    """
    contact = await repository_contacts.get_contact_by_id(contact_id, db)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such contact")
    return contact


@router.get('/search_by_name/{contact_name}', response_model=List[ContactResponse], dependencies=[Depends(access_get)])
async def get_contact_by_name(contact_name: str, db: Session = Depends(get_db),
                              _: User = Depends(auth_service.get_current_user)):
    """
    The get_contact_by_name function is a GET request that returns the contact with the given name.
    If no such contact exists, it will return a 404 error.

    :param contact_name: str: Get the contact name from the url
    :param db: Session: Pass the database session to the function
    :param _: User: Pass the current user to the function
    :return: A contact object
    :doc-author: Andriy
    """
    contact = await repository_contacts.get_contact_by_name(contact_name, db)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such contact")
    return contact


@router.get('/search_by_surname/{contact_surname}', response_model=List[ContactResponse],
            dependencies=[Depends(access_get)])
async def get_contact_by_surname(contact_surname: str, db: Session = Depends(get_db),
                                 _: User = Depends(auth_service.get_current_user)):
    """
    The get_contact_by_surname function is a GET request that returns the contact with the given surname.
        If no such contact exists, it will return an HTTP 404 error.

    :param contact_surname: str: Pass the surname of the contact to be retrieved
    :param db: Session: Pass the database session to the function
    :param _: User: Get the current user from the auth_service
    :return: A contact with a given surname
    :doc-author: Andriy
    """
    contact = await repository_contacts.get_contact_by_surname(contact_surname, db)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such contact")
    return contact


@router.get('/search_by_email/{contact_email}', response_model=ContactResponse, dependencies=[Depends(access_get)])
async def get_contact_by_email(contact_email: str, db: Session = Depends(get_db),
                               _: User = Depends(auth_service.get_current_user)):
    """
    The get_contact_by_email function is used to get a contact by email.
        The function takes in the contact_email and db as parameters, and returns the contact.

    :param contact_email: str: Get the email of the contact
    :param db: Session: Get the database session
    :param _: User: Check if the user is authenticated
    :return: A contact object
    :doc-author: Andriy
    """
    contact = await repository_contacts.get_contact_by_email(contact_email, db)
    if not contact:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists')
    return contact


@router.post('/', response_model=ContactResponse, status_code=status.HTTP_201_CREATED,
             dependencies=[Depends(RateLimiter(times=2, seconds=5)), Depends(access_get)])
async def create_contact(body: ContactModel, db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    """
    The create_contact function creates a new contact in the database.

    :param body: ContactModel: Get the contact information from the request body
    :param db: Session: Pass the database session to the function
    :param _: User: Get the current user from the auth_service
    :return: A contactmodel object
    :doc-author: Andriy
    """
    contact = await repository_contacts.get_contact_by_email(body.email, db)
    if contact:
        raise HTTPException(status_code=status.HTTP_409_CONFLICT, detail='Email already exists')
    contact = await repository_contacts.create_contact(body, db)
    return contact


@router.put('/{contact_id}', response_model=ContactResponse, dependencies=[Depends(access_get)])
async def update_contact(body: ContactModel, contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    """
    The update_contact function updates a contact in the database.
        The function takes an id of the contact to be updated, and a body containing all fields that need updating.
        If no such contact exists, it returns 404 Not Found.

    :param body: ContactModel: Pass the contact model to the function
    :param contact_id: int: Get the id of the contact to be deleted
    :param db: Session: Pass the database session to the repository layer
    :param _: User: Ensure that the user is logged in
    :return: The updated contact
    :doc-author: Andriy
    """
    contact = await repository_contacts.update_contact(body, contact_id, db)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such contact")
    return contact


@router.delete('/{contact_id}', response_model=ContactResponse, dependencies=[Depends(access_get)])
async def remove_contact(contact_id: int = Path(ge=1), db: Session = Depends(get_db),
                         _: User = Depends(auth_service.get_current_user)):
    """
    The remove_contact function removes a contact from the database.

    :param contact_id: int: Specify the contact id that will be deleted
    :param db: Session: Get the database session
    :param _: User: Ensure that the user is logged in
    :return: A contact object
    :doc-author: Andriy
    """
    contact = await repository_contacts.remove_contact(contact_id, db)
    if not contact:
        raise HTTPException(status_code=status.HTTP_404_NOT_FOUND, detail="No such contact")
    return contact
