import json
import re
from datetime import datetime

import requests
from bs4 import BeautifulSoup

base_url = "http://quotes.toscrape.com"
URLS = ["http://quotes.toscrape.com/"]


def get_urls(start_url):
    response = requests.get(start_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select(
        'div[class=row] div[class=col-md-8] nav ul[class=pager] li[class=next] a')
    prefix = '/page/'
    if content:
        url = prefix + re.search(r'\d+', content[0]['href']).group()
        new_url = base_url + url
        URLS.append(new_url)
        get_urls(new_url)


def spider_quotes(urls):
    data = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('div[class=row]  div[class=quote]')
        for el in content:
            result = {}
            author = el.find('small', attrs={"class": "author"}).text
            quote = el.find('span', attrs={"class": "text"}).text
            tags = [tag.text for tag in el.find_all(
                'a', attrs={'class': 'tag'})]
            result.update({'quote': quote, "author": author, "tags": tags})
            data.append(result)
    return data


def spider_authors(urls):
    data = []
    for url in urls:
        response = requests.get(url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select(
            'div[class=row]  div[class=quote] span a')
        for el in content:
            author = el['href']
            authors_responce = requests.get(base_url + author)
            authors_soup = BeautifulSoup(authors_responce.text, 'html.parser')
            authors_content = authors_soup.select(
                'div[class=container] div[class=author-details]')
            author_name = author.replace("-", " ").replace("/author/", "")
            author_born = authors_content[0].find(
                'span', attrs={'class': 'author-born-date'}).text
            author_location = "Born " + authors_content[0].find(
                'span', attrs={'class': 'author-born-location'}).text
            bio = authors_content[0].find(
                'div', attrs={'class': 'author-description'}).text.strip()
            if data:
                if not author_name in [value['name'] for value in data]:
                    data.append({'name': author_name, 'born': author_born,
                                 'location': author_location, 'bio': bio})
            else:
                data.append({'name': author_name, 'born': author_born,
                             'location': author_location, 'bio': bio})
    return data


if __name__ == '__main__':
    get_urls(base_url)
    r = spider_quotes(URLS)
    with open('quotes.json', 'w', encoding='utf-8') as fd:
        json.dump(r, fd, ensure_ascii=False)
    a = spider_authors(URLS)
    with open('authors.json', 'w', encoding='utf-8') as fd:
        json.dump(a, fd, ensure_ascii=False)
