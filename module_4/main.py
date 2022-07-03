# List Comprehensions
a = [i**2 for i in range(8)]

even_nums = [x for x in range(21) if x % 2 == 0]  # запис еквівалентний =>

even_nums = []
for x in range(21):
    if x % 2 == 0:
        even_nums.append(x)

names = ['Steve', 'Bill', 'Ram', 'Mohan', 'Abdul']
names2 = [s for s in names if 'a' in s]

nums = [x for x in range(21) if x % 2 == 0 if x % 5 == 0]

# if-elif-else condition
l = [1, 2, 3, 4, 5]
a = ['yes' if v == 1 else 'no' if v == 2 else 'idle' for v in l]  # запис еквівалентний =>
for v in l:
   if v == 1:
       print('yes')
   else:
       if v == 2:
           print('no')
       else:
           print('idle')


# Dictionary Comprehension
import random
customers = ["Alex","Bob","Carol","Dave","Flow","Katie","Nate"]
discount_dict = {customer:random.randint(1,100) for customer in customers}

nums = [0, 1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_squares = {n: n ** 2 for n in nums if n % 2 == 0}  # запис еквівалентний =>

numbers = range(10)
new_dict_for = {}
for n in numbers:
    if n % 2 == 0:
        new_dict_for[n] = n**2


# Set Comprehension

my_list = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
new_set = {element*3 for element in my_list}
new_set_1 = {element*3 for element in my_list if element % 2 ==0}

# Створюємо новий список в якому будуть числа які кратні 30 АБО 35
a = [i for i in range(30, 250) if i % 30 == 0 or i % 35 == 0]

# Пошук директорій і файлів за допомогою рекурсії
from pathlib import Path
import sys

p = Path(sys.argv[1])

def parse_folder_recursion(path):
   for element in path.iterdir():
       if element.is_dir():
           print(f"This is folder - {element.name}")
           parse_folder_recursion(element)
       else:
           print(f"This is file - {element.name}")


if __name__ == "__main__":
   parse_folder_recursion(p)

# Small calculator used only dict and lambda
def if_elif_vs_dict(operator, x, y):
   return {
       'add': lambda: x+y,
       'sub': lambda: x-y,
       'mul': lambda: x*y,
       'div': lambda: x/y,
   }.get(operator, lambda: 'Not a valid operation')()


# Morse
morze_dict = {'A':'.-', 'B':'-...', 'C':'-.-.', 'D':'-..', 'E':'.', 'F':'..-.',
             'G':'--.', 'H':'....', 'I':'..', 'J':'.---', 'K':'-.-', 'L':'.-..',
             'M':'--', 'N':'-.', 'O':'---', 'P':'.--.', 'Q':'--.-', 'R':'.-.',
             'S':'...', 'T':'-', 'U':'..-', 'V':'...-', 'W':'.--', 'X':'-..-',
             'Y':'-.--', 'Z':'--..', '0':'-----', '1':'.----', '2':'..---',
             '3':'...--', '4':'....-', '5':'.....', '6':'-....', '7':'--...',
             '8':'---..', '9':'----.'}

def convert_to_morze(text:str) -> str:
   result = []
   text = text.upper()
   for s in text:
       if s in morze_dict:
           result.append(morze_dict.get(s))
   return ' '.join(result)

if __name__ == "__main__":
   text = input('Please set the text: ')
   print(convert_to_morze(text))