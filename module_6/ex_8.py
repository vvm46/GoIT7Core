'''
Створення директорій pathlib
'''
from pathlib import Path

new_dir = Path('ABC')
new_dir.mkdir(exist_ok=True)  # exist_ok=True якщо папка вже існує, то не буде помилки при спробі створити нову
new_dir.rmdir()  # удаляє папку

new_dir = Path('Test/Temp')
new_dir.mkdir(exist_ok=True, parents=True)