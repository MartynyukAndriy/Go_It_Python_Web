from datetime import datetime

from pydantic import BaseModel, EmailStr, Field


class ContactModel(BaseModel):
    name: str = Field(min_length=1, max_length=20)
    surname: str = Field(min_length=1, max_length=20)
    email: EmailStr
    phone: str
    birthday: str
    description: str


class ContactResponse(BaseModel):
    id: int
    name: str = 'Name'
    surname: str = 'Surname'
    email: EmailStr
    phone: str = '0993334567'
    birthday: str
    description: str

    class Config:
        orm_mode = True