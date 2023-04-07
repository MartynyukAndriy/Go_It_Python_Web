from mongoengine import *

connect(host="mongodb://localhost:27017/hw8_RabbitMQ")


class Contacts(Document):
    fullname = StringField(max_length=80, required=True)
    email = StringField(max_length=50)
    send = BooleanField(default=False)
