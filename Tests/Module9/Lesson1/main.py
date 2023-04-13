import re
import requests
from bs4 import BeautifulSoup

from datetime import datetime


base_url = "https://index.minfin.com.ua/ua/russian-invading/casualties"


def get_urls():
    response = requests.get(base_url)
    soup = BeautifulSoup(response.text, 'html.parser')
    content = soup.select('div[class=ajaxmonth] h4[class=normal] a')
    urls = ['/']
    prefix = '/month.php?month='
    for a in content:
        url = prefix + re.search(r'\d{4}-\d{2}', a['href']).group()
        urls.append(url)
    return urls


def spider(urls):
    data = []
    for url in urls:
        response = requests.get(base_url + url)
        soup = BeautifulSoup(response.text, 'html.parser')
        content = soup.select('ul[class=see-also] li[class=gold]')
        for el in content:
            result = {}
            date = el.find('span', attrs={'class': 'black'}).text
            try:
                date = datetime.strptime(date, "%d.%m.%Y").isoformat()
            except ValueError as err:
                print(f'Error for date: {date}')
                continue
            result.update({'date': date})
            data.append(result)
    return data


if __name__ == "__main__":
    url_for_scraping = get_urls()
    r = spider(url_for_scraping)
    print(r)
