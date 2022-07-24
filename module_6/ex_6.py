'''
Основні можливості pathlib
'''

from pathlib import Path

current_path = Path('.')   # показує поточну папку, як він це бачить, це те саме що і Path()
# print(current_path)
# print(current_path.cwd())  # показує абсолютний шлях, звідки ми запускаємо

# Шлях
file = current_path / 'bin' / 'utils' / 'paint.drawio.svg'
print(file)
# print(current_path.joinpath('bin', 'utils', 'paint.drawio.svg'))

# Частини файла
print(file.parts)

# Ім'я файла
print(file.name)
print(file.name.split('.')[0])

# Батьківська папка
print(file.parent)

# Суфікс
print(file.suffix)
print(file.suffixes)