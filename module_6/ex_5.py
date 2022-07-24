'''
Читаємо файл за допомогою бібліотеки pathlib
'''

from pathlib import Path

folder = Path('./Temp')  # ./ відносно того де ми знаходимось має бути папка

filename = folder / 'temp.txt'

try:
    with open(filename, 'r', encoding='utf-8') as file:
        for line in file:
            print(line, end='')
except OSError as err:
    print(f'Error: {err}')
finally:
    print('\nFile operation completed')
