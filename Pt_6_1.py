from bs4 import BeautifulSoup
import requests

url = input("Введите ссылку: ")
try:
    page = requests.get(url)
    if page.status_code == 200:
        soup = BeautifulSoup(page.text, "html.parser")
        Top10 = soup.findAll("a", class_="d-track__title deco-link "
                                         "deco-link_stronger")[0:10]
        if Top10 is not None:
            print("Топ песен: ")
            for data in Top10:
                print(data.text)
        else:
            print("Неверная ссылка")
    elif page.status_code == 404:
        print("Нет такой страницы")
    else:
        print("ЧтО?")
except requests.exceptions.MissingSchema:
    print("Непрввильная ссылка на яндекс музыку в разделе Треки")

# https://music.yandex.ru/artist/257461/tracks
# https://music.yandex.ru/artist/165131/tracks
