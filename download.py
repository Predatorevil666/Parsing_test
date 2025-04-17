import requests_cache
import re
from bs4 import BeautifulSoup
from urllib.parse import urljoin
# Добавьте к списку импортов импорт класса Path из модуля pathlib.
from pathlib import Path
from tqdm import tqdm

# Добавьте константу, где будет храниться путь до директории с текущим файлом.
BASE_DIR = Path(__file__).parent

DOWNLOADS_URL = 'https://docs.python.org/3/download.html'

if __name__ == '__main__':
    session = requests_cache.CachedSession()
    response = session.get(DOWNLOADS_URL)
    response.encoding = 'utf-8'
    soup = BeautifulSoup(response.text, 'lxml')
    table_tag = soup.find('table', attrs={'class': 'docutils'})
    pdf_a4_tag = table_tag.find('a', {'href': re.compile(r'.+pdf-a4\.zip$')})
    # Сохраните в переменную содержимое атрибута href.
    pdf_a4_link = pdf_a4_tag['href']

    # Получите полную ссылку с помощью функции urljoin.
    archive_url = urljoin(DOWNLOADS_URL, pdf_a4_link)
    filename = archive_url.split('/')[-1]
    # Сформируйте путь до директории downloads.
    downloads_dir = BASE_DIR / 'downloads'
    # Создайте директорию.
    downloads_dir.mkdir(exist_ok=True)
    # Получите путь до архива, объединив имя файла с директорией.
    archive_path = downloads_dir / filename

    # # Загрузка архива по ссылке.
    # response = session.get(archive_url)
    #
    # # В бинарном режиме открывается файл на запись по указанному пути.
    # with open(archive_path, 'wb') as file:
    #     # Полученный ответ записывается в файл.
    #     file.write(response.content)

    # Загрузка с tqdm (упрощенный вариант)
    response = session.get(archive_url, stream=True)
    total_size = int(response.headers.get('content-length', 0))

    with open(archive_path, 'wb') as file:
        # Просто оборачиваем response.iter_content() в tqdm
        for chunk in tqdm(
                response.iter_content(chunk_size=1024),
                total=total_size // 1024 + 1,  # Округляем до количества чанков
                unit='KB',  # Кибибайты вместо байтов
                desc=filename,
                leave=True  # Оставляет прогресс-бар после завершения
        ):
            if chunk:
                file.write(chunk)