# 3.5 API
# В этой задаче вам необходимо воспользоваться API сайта artsy.net
# API проекта Artsy предоставляет информацию о некоторых деятелях искусства, их работах, выставках.
# В рамках данной задачи вам понадобятся сведения о деятелях искусства (назовем их, условно, художники).
# Вам даны идентификаторы художников в базе Artsy.
# Для каждого идентификатора получите информацию о имени художника и годе рождения.
# Выведите имена художников в порядке неубывания года рождения. В случае если у художников одинаковый год рождения,
# выведите их имена в лексикографическом порядке.
# Работа с API Artsy
# Полностью открытое и свободное API предоставляют совсем немногие проекты. В большинстве случаев, для получения доступа
# к API необходимо зарегистрироваться в проекте, создать свое приложение, и получить уникальный ключ (или токен), и в
# дальнейшем все запросы к API осуществляются при помощи этого ключа.
# Чтобы начать работу с API проекта Artsy, вам необходимо пройти на стартовую страницу документации к API
# https://developers.artsy.net/start и выполнить необходимые шаги, а именно зарегистрироваться, создать приложение, и
# получить пару идентификаторов Client Id и Client Secret. Не публикуйте эти идентификаторы.
# После этого необходимо получить токен доступа к API. На стартовой странице документации есть примеры того, как можно
# выполнить запрос и как выглядит ответ сервера. Мы приведем пример запроса на Python.
# Теперь все готово для получения информации о художниках. На стартовой странице документации есть пример того, как
# осуществляется запрос и как выглядит ответ сервера. Пример запроса на Python.

import requests
import json

client_id = 'e392e2131b65ab386d6c'
client_secret = '3a699cc2ab7f370c6fc34da46bb3d9e2'

# инициируем запрос на получение токена
r = requests.post("https://api.artsy.net/api/tokens/xapp_token",
                  data={
                      "client_id": client_id,
                      "client_secret": client_secret
                  })

# разбираем ответ сервера
for_token = json.loads(r.text)

# достаем токен
token = for_token["token"]

# создаем заголовок, содержащий наш токен
headers = {"X-Xapp-Token" : token}
# инициируем запрос с заголовком
with open(r"C:\stepik\dataset_24476_4.txt", encoding='UTF-8') as file:
    name_artists = [line.strip() for line in file]

spisok_artists = [[] for i in range(len(name_artists))]
i = 0
for name_id in name_artists:
    r = requests.get(f"https://api.artsy.net/api/artists/{name_id}", headers=headers)
    result = json.loads(r.text)
    name = result['sortable_name']
    year = result['birthday']
    spisok_artists[i].append(year)
    spisok_artists[i].append(name)
    i += 1

sort_spisok = sorted(spisok_artists)
print(sort_spisok)

with open("C:\stepik\dataset_otvet_24476.txt", "w", encoding='UTF-8') as wfile:
    for sp in sort_spisok:
        name_artist = sp[1]
        wfile.write(name_artist + '\n')

