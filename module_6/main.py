'''
Завдання: Сортування файлів у папці.
Копіювати файли із зазначеної папки та покласти в нову папку з розширенням цього файлу.
'''

import argparse  # дозволяє писати консольні програми
from pathlib import Path
from shutil import copyfile

# Вважаємо що ми будемо запускати програму:
# python main.py -s picture -o dist
# -s => source (це короткий запис)
# -o output (це короткий запис)

parser = argparse.ArgumentParser(
    description='Sorting folder')  # парсер командної строки, description - просто опис.
parser.add_argument('--source', '-s', required=True, help='Source folder')  # --source ім'я змінної, довгий запис
parser.add_argument('--output', '-o', default='dist', help='Output folder')
args = vars(parser.parse_args())  # parser.parse_args() - парсер, vars - повертає словник
source = args.get('source')  # із словника отримаємо значення по ключу
output = args.get('output')  # із словника отримаємо значення по ключу
print(source, output)


def read_folder(path: Path) -> None:
    for el in path.iterdir():
        if el.is_dir():
            read_folder(el)
        else:
            ext = el.suffix
            new_path = output_folder / ext
            new_path.mkdir(exist_ok=True, parents=True)
            copyfile(el, new_path / el.name)


output_folder = Path(output)  # dist
read_folder(Path(source))
