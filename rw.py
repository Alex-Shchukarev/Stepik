with open('C:\stepik\dataset_24465.txt', 'r') as file:
    spisok_strok = [line.strip() for line in file]

spst = '\n'.join(reversed(spisok_strok))

with open('C:\stepik\dataset_3333.txt', 'w') as wile:
    wile.write(spst)