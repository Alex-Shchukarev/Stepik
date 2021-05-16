# 3.4 Распространённые форматы текстовых файлов: CSV, JSON
# Вам дана частичная выборка из датасета зафиксированных преступлений, совершенных в городе Чикаго с 2001 года по настоящее время.
# Одним из атрибутов преступления является его тип – Primary Type.
# Вам необходимо узнать тип преступления, которое было зафиксировано максимальное число раз в 2015 году.
import csv
import re

crimes_2015 = {}
pat_rn = re.compile(r"\d\d\/\d\d\/2015")
with open('C:\stepik\Crimes.csv', 'r') as f:
    file = csv.DictReader(f)
    for row in file:
        if pat_rn.search(row['Date']):
            if row['Primary Type'] not in crimes_2015:
                crimes_2015[row['Primary Type']] = 1
            else:
                crimes_2015[row['Primary Type']] += 1
max_crime_count = max(crimes_2015.values())
most_crime = [k for k, v in crimes_2015.items() if v == max_crime_count]
print(*most_crime)



