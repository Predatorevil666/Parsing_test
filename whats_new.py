import requests_cache
from pprint import pprint
from bs4 import BeautifulSoup
# Импортируйте функцию из библиотеки.
from urllib.parse import urljoin
from tqdm import tqdm

WHATS_NEW_URL = 'https://docs.python.org/3/whatsnew/'

if __name__ == '__main__':
    # Загрузка веб-страницы с кешированием.
    session = requests_cache.CachedSession()
    response = session.get(WHATS_NEW_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    news = soup.find('div', class_='toctree-wrapper compound')
    news_link = news.find_all('li', class_='toctree-l1')
    # print(news_link[0].prettify())
    # for link in news_link:
    #     link_1 = link.find('a')
    #     href = link_1['href']
    #     version_link = urljoin(WHATS_NEW_URL, href)
    #     print(version_link)
    result = []
    for section in tqdm(news_link):
        version_a_tag = section.find('a')
        href = version_a_tag['href']
        version_link = urljoin(WHATS_NEW_URL, href)
        # Здесь начинается новый код!
        response = session.get(version_link)  # Загрузите все страницы со статьями. Используйте кеширующую сессию.
        response.encoding = 'utf-8'  # Укажите кодировку utf-8.
        soup = BeautifulSoup(response.text, 'lxml')  # Сварите "супчик".
        h1 = soup.find('h1')  # Найдите в "супе" тег h1.
        dl = soup.find('dl')  # Найдите в "супе" тег dl.
        dl_text = dl.text.replace('\n', ' ')
        # print(version_link, h1.text, dl_text)  # Добавьте в вывод на печать текст из тегов h1 и dl.
        result.append((version_link, h1.text, dl_text))
    for row in result:
        print(*row)