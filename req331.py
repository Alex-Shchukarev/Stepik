# Обзорно об интернете: http-запросы, html-страницы и requests
#
# Рассмотрим два HTML-документа A и B.
# Из A можно перейти в B за один переход, если в A есть ссылка на B, т. е. внутри A есть тег <a href="B">, возможно с дополнительными параметрами внутри тега.
# Из A можно перейти в B за два перехода если существует такой документ C, что из A в C можно перейти за один переход и из C в B можно перейти за один переход.
#
# Вашей программе на вход подаются две строки, содержащие url двух документов A и B.
# Выведите Yes, если из A в B можно перейти за два перехода, иначе выведите No.
#
# Обратите внимание на то, что не все ссылки внутри HTML документа могут вести на существующие HTML документы.

import requests
import re

A = input()
B = input()


res1 = requests.get(A)
pat_rn = r'<a href="(.*)">'
spisok1_urls = re.findall(pat_rn, res1.text)
spisok2_urls = []
for elem in spisok1_urls:
    res2 = requests.get(elem)
    spisok2_urls += re.findall(pat_rn, res2.text)
if B in spisok2_urls:
    print('Yes')
else:
    print('No')
