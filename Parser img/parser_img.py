import requests
from lxml import html
import sys, os
from urllib import parse as urlparse

# Указываем адрес сайта, с которого скачиваются фото
response = requests.get('http://daler.ru/%D0%9C%D1%83%D0%B6%D1%87%D0%B8%D0%BD%D1%8B')

# Преобразуем тело документа в дерево элементов (DOM)
parsed_body = html.fromstring(response.text)
images = parsed_body.xpath('//img/@src')

# Если картинок не было
if not images:
    sys.exit("Картинок не было найдено")

images = [urlparse.urljoin(response.url, url) for url in images]
print('Найдено %s картинок' % len(images))

# Указываем папку. Если ее нет - создаем.
newpath = r'C:\Users\Василий\Desktop\Downloads'
if not os.path.exists(newpath):
    os.makedirs(newpath)

# Переходим в папку
os.chdir(newpath)

# Если необходимо скачать определенное кол-во картинок,
# то пишем for url in images[0:кол-во]:
for url in images:
    r = requests.get(url)
    f = open('%s' % url.split('/')[-1], 'wb+')
    f.write(r.content)
    f.close()

