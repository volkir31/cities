import requests
from bs4 import BeautifulSoup

URL = 'http://otzyvoteli.ru/goroda'
HEADERS = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36\
     (KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.105',
    'Accept': '*/*'
}


def get_html(url, params=None):
    r = requests.get(url, headers=HEADERS, params=params)
    return r


def get_content(html):
    soup = BeautifulSoup(html, 'html.parser')
    items = soup.find_all('tr')
    cities = []
    for item in items:
        cities.append({
            'city': item.find('td').get_text()
        })
    return cities


def save_file(item, path):
    with open(path, 'a', encoding='utf-8') as file:
        file.write(item)


def parse():
    html = get_html(URL)
    if html.status_code == 200:
        cities = get_content(html.text)
        for i in range(0, len(cities)):
            save_file(str(cities[i].values())+'\n', 'cities1.txt')
    else:
        print('Error')


parse()
