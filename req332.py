# 3.3 Обзорно об интернете: http-запросы, html-страницы и requests
# Вашей программе на вход подается ссылка на HTML файл.
# Вам необходимо скачать этот файл, затем найти в нем все ссылки вида <a ... href="..." ... > и вывести список сайтов, на которые есть ссылка.
#
# Сайтом в данной задаче будем называть имя домена вместе с именами поддоменов. То есть, это последовательность символов, которая следует сразу после символов протокола, если он есть, до символов порта или пути, если они есть, за исключением случаев с относительными ссылками вида
# <a href="../some_path/index.html">.
#
# Сайты следует выводить в алфавитном порядке.

import requests
import re

cur_url = input()

spisok_domain = []
res = requests.get(cur_url).text
pat_rn = re.compile(r"<a(.*?)href(.*?)=(.*?)(\"|')(((.*?):\/\/)|)(.*?)(\/|:|\"|')(.*?)")
spisok_urls = pat_rn.findall(res)
for elem in spisok_urls:
    if elem[7] not in spisok_domain and elem[7]!='..':
        spisok_domain.append(elem[7])

spisok_domain.sort()

for elem in spisok_domain:
    print(elem)