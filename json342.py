# 3.4 Распространённые форматы текстовых файлов: CSV, JSON
# Вам дано описание наследования классов в формате JSON.
# Описание представляет из себя массив JSON-объектов, которые соответствуют классам. У каждого JSON-объекта есть поле
# name, которое содержит имя класса, и поле parents, которое содержит список имен прямых предков.
# Пример:
# [{"name": "A", "parents": []}, {"name": "B", "parents": ["A", "C"]}, {"name": "C", "parents": ["A"]}]
# Эквивалент на Python:
# class A:
#     pass
# class B(A, C):
#     pass
# class C(A):
#     pass
#
# Гарантируется, что никакой класс не наследуется от себя явно или косвенно, и что никакой класс не наследуется явно от
# одного класса более одного раза. Для каждого класса вычислите предком скольких классов он является и выведите эту
# информацию в следующем формате.
# <имя класса> : <количество потомков>
# Выводить классы следует в лексикографическом порядке.

import json

def count_parents(elem):
    buf_1, buf_2 = slovar_class[elem], []
    while buf_1 != []:
        for element in buf_1:
            if element not in count_slovar_class and set(slovar_class[element]) <= set(buf_1):
                count_slovar_class[element] = 1
            else:
                count_slovar_class[element] = count_slovar_class.get(element,0) + 1
                buf_2 += slovar_class[element]
        buf_1, buf_2 = buf_2, []

    return





count_slovar_class, slovar_class = dict(), dict()
json_slovar_class = input()
py_slovar_class = json.loads(json_slovar_class)

for slovar in py_slovar_class:
    key = slovar['name']
    value = slovar['parents']
    slovar_class[key] = value
with_children = {element['name']: [] for element in py_slovar_class}
print(slovar_class)
print(with_children)

# for k, v in slovar_class.items():
#     if k not in count_slovar_class:
#         count_slovar_class[k] = 1
#     else:
#         count_slovar_class[k] += 1
#     for elem in v:
#         if elem not in count_slovar_class:
#             count_slovar_class[elem] = 1
#         else:
#             count_slovar_class[elem] += 1
#             count_parents(elem)

# for k, v in slovar_class.items():
#     if k not in count_slovar_class:
#         count_slovar_class[k] = 1
#         count_parents(k)
#     else:
#         count_slovar_class[k] += 1
#         count_parents(k)
#
# for k,v in sorted(count_slovar_class.items()):
#     print(k, ':', v)