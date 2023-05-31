import logging

from libgravatar import Gravatar
from sqlalchemy.orm import Session

from src.database.models import User
from src.schemas import UserModel


async def get_user_by_email(email: str, db: Session) -> User | None:
    """
    The get_user_by_email function takes in an email and a database session,
    and returns the user associated with that email. If no such user exists, it returns None.

    :param email: str: Specify the type of the parameter
    :param db: Session: Pass the database session to the function
    :return: A user object or none if no user is found
    :doc-author: Andriy
    """
    return db.query(User).filter(User.email == email).first()


async def create_user(body: UserModel, db: Session) -> User:
    """
    The create_user function creates a new user in the database.

    :param body: UserModel: Get the user data from the request body
    :param db: Session: Access the database
    :return: A user object
    :doc-author: Andriy
    """
    avatar = None
    try:
        g = Gravatar(body.email)
        avatar = g.get_image()
    except Exception as e:
        logging.error(e)

    new_user = User(**body.dict(), avatar=avatar)
    db.add(new_user)
    db.commit()
    db.refresh(new_user)
    return new_user


async def update_token(user: User, token: str | None, db: Session) -> None:
    """
    The update_token function updates the refresh token for a user.

    :param user: User: Identify the user that is being updated
    :param token: str | None: Pass the token to the function
    :param db: Session: Pass the database session to the function
    :return: None
    :doc-author: Andriy
    """
    user.refresh_token = token
    db.commit()


async def confirmed_email(email: str, db: Session) -> None:
    """
    The confirmed_email function takes in an email and a database session,
    and sets the confirmed field of the user with that email to True.


    :param email: str: Get the email of the user who is trying to confirm their account
    :param db: Session: Pass the database session to the function
    :return: None
    :doc-author: Andriy
    """
    user = await get_user_by_email(email, db)
    user.confirmed = True
    db.commit()


async def update_avatar(email, url: str, db: Session) -> User:
    """
    The update_avatar function updates the avatar of a user.

    :param email: Find the user in the database
    :param url: str: Specify the type of data that will be passed to the function
    :param db: Session: Pass the database session to the function
    :return: The updated user
    :doc-author: Andriy
    """
    user = await get_user_by_email(email, db)
    user.avatar = url
    db.commit()
    return user
