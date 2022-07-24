'''
Прочитати перші N рядків файлу.
Ім'я файлу для читання передаємо як аргумент командного рядка
'''

import sys

NUMBER_LINES = 4

if len(sys.argv) != 2:
    print("Потрібно передати лише ім'я файлу для читання!")
    quit()

try:
    file = open(sys.argv[1], 'r', encoding='utf-8')
    line = file.readline()
    count = 0
    while count < NUMBER_LINES and line != '':  # перевіряємо чи файл пустий
        line = line.strip()  # відкидаємо пробіли, табуляцію
        count += 1
        print(line)
        # line = file.readline()
    file.close()
except OSError as err:
    print(f'Помилка доступу до файлу: {err}')
