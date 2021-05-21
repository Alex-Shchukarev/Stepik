# 3.6 XML, библиотека ElementTree, библиотека lxml
# Вам дано описание пирамиды из кубиков в формате XML.
# Кубики могут быть трех цветов: красный (red), зеленый (green) и синий (blue).
# Для каждого кубика известны его цвет, и известны кубики, расположенные прямо под ним.
# Введем понятие ценности для кубиков. Самый верхний кубик, соответствующий корню XML документа имеет ценность 1.
# Кубики, расположенные прямо под ним, имеют ценность 2. Кубики, расположенные прямо под нижележащими кубиками, имеют
# ценность 3. И т. д.
# Ценность цвета равна сумме ценностей всех кубиков этого цвета.
# Выведите через пробел три числа: ценности красного, зеленого и синего цветов.

from xml.etree import ElementTree

def count_color(vetka_tree, worth):
    worth += 1
    color_count[vetka_tree.get('color')] += worth
    for elem in vetka_tree:
        count_color(elem, worth)


color_count = {'red': 0,
               'green': 0,
               'blue': 0
               }

worth = 0
root = ElementTree.fromstring(input())

count_color(root, worth)

print(color_count['red'], color_count['green'], color_count['blue'])

