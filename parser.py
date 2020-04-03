import requests
from bs4 import BeautifulSoup

URL = 'http://www.1000mest.ru/cityA'
HEADERS = {
	'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 \
(KHTML, like Gecko) Chrome/80.0.3987.116 Safari/537.36 OPR/67.0.3575.105',
	'Accept': '*/*'
}


def get_html(url, params=None):
	r = requests.get(url, headers=HEADERS, params=params)
	return r


def parse():
	html = get_html(URL)
	print(html)


parse()
