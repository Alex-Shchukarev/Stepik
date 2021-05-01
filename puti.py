import os.path

spisok=[]
for current_dir, dirs, files in os.walk('\main'):
    for elem in files:
        if elem.find('.py') > 0:
            spisok.append(current_dir[1:])
            break

content = '\n'.join(sorted(spisok))
with open('C:\stepik\dataset_3333_otv.txt', 'w') as wile:
    wile.write(content)

# Well Done