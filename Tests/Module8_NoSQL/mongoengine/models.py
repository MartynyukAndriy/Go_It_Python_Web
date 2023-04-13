from mongoengine import *

connect(host="mongodb://localhost:27017/web10")


class Author(Document):
    fullname = StringField(max_length=80, required=True)
    born_date = StringField(max_length=50)
    born_location = StringField(max_length=50)
    description = StringField()


class Quotes(Document):
    author = ReferenceField(Author, reverse_delete_rule=CASCADE)
    tags = ListField(StringField(max_length=30))
    Quotes = StringField(max_length=120)
    meta = {'allow_inheritance': True}
