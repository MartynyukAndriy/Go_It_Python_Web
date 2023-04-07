from mongoengine import disconnect
from json import loads

from models import Contacts

from faker import Faker

fake = Faker()


def seed_contacts():
    contacts_list = []
    for _ in range(5):
        contact = Contacts(fullname=fake.name(),
                           email=fake.email())
        contacts_list.append(contact)
        contact.save()
    return contacts_list


if __name__ == '__main__':
    seed_contacts()

    disconnect()
