from mongoengine import disconnect

from models import Author, Quotes


def search_tag(tag):
    result = []
    quotes = Quotes.objects()
    for quote in quotes:
        if tag in quote.tags:
            result.append(quote.quotes)
    return result


def search_tags(tags):
    result = []
    quotes = Quotes.objects()
    for quote in quotes:
        for tag in tags:
            if tag in quote.tags:
                result.append(quote.quotes)
                break
    return result


def search_name(name):
    result = []
    quotes = Quotes.objects()
    author = Author.objects(fullname=name)[0]
    for quote in quotes:
        if quote.author.id == author.id:
            result.append(quote.quotes)
    return result
