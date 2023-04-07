from mongoengine import disconnect
from json import loads

from models import Author, Quotes


def seed_authors(file):
    data_json = file.read()
    data = loads(data_json)
    for authors in data:
        author = Author(fullname=authors["fullname"],
                        born_date=authors["born_date"],
                        born_location=authors["born_location"],
                        description=authors["description"])
        author.save()


def seed_quotes(file):
    data_json = file.read()
    data = loads(data_json)
    for quotes in data:
        quote_author = Author.objects(fullname=quotes["author"])
        quote = Quotes(tags=quotes["tags"],
                       quotes=quotes["quote"],
                       author=quote_author[0])
        quote.save()


if __name__ == '__main__':
    with open("authors.json", "r") as file:
        seed_authors(file)
    with open("quotes.json", "r") as file:
        seed_quotes(file)

    disconnect()
