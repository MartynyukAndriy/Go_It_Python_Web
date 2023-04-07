from mongoengine import *

connect(host="mongodb://localhost:27017/hw8_mongo")


class Author(Document):
    fullname = StringField(max_length=80, required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()


class Quotes(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    quotes = StringField()
    meta = {'allow_inheritance': True}
