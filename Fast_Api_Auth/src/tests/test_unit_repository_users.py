import unittest
from unittest.mock import MagicMock
from datetime import date, datetime

from pydantic import EmailStr
from sqlalchemy.orm import Session

from src.database.models import Contact, User
from src.schemas import ContactModel, UserModel
from src.repository.users import (
    get_user_by_email,
    create_user,
    update_avatar
)


class TestNotes(unittest.IsolatedAsyncioTestCase):

    def setUp(self):
        self.session = MagicMock(spec=Session)
        self.user = User(id=1)

    async def test_get_user_by_email(self):
        user = User()
        self.session.query().filter().first.return_value = user
        result = await get_user_by_email(email=f'aaa@gmail.com', db=self.session)
        self.assertEqual(result, user)

    async def test_create_user(self):
        body = UserModel(username='Andriy',
                         email=EmailStr('andriy@gmail.com'),
                         password='qwerty')
        result = await create_user(body=body, db=self.session)
        self.assertEqual(result.username, body.username)
        self.assertEqual(result.email, body.email)
        self.assertEqual(result.password, body.password)

    async def test_update_avatar(self):
        user = User(email='Andriy@gmail.com')
        self.session.query().filter().first.return_value = user
        result = await update_avatar(email='Andriy@gmail.com', url='http', db=self.session)
        self.assertEqual(result, user)


if __name__ == '__main__':
    unittest.main()
