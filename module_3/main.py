# test_1.py
def hello(text):
   print(f"Hello -> {text}")


def like(interest):
   if interest == 'yoga':
      return "I quite like " + interest + "."

   elif interest == "football":
      return "Yes, I play " + interest + "."

   elif interest == 'guitar':
      return "Yes, I play the " + interest + "."
   else:
      return "I'm interested in " + interest + "."

story = like('photography')
print(story)
story = like('yoga')
print(story)
story = like('football')
print(story)
story = like('guitar')
print(story)


def is_none(thing):
   if thing is None:
      print("It's None")
   elif thing:
      print("It's True")
   else:
      print("It's False")

is_none(None) # It's None
is_none(True) # It's True
is_none(False) # It's False
is_none(0) # It's False
is_none(0.0) # It's False
is_none(()) # It's False
is_none([]) # It's False
is_none({}) # It's False
is_none(set()) # It's False


def print_days(*args):
   print('Get ready:', args)
print_days('Wednesday', 'Thursday', 'Friday', 'Weekend...')


def print_character(**kwargs):
   print('Kwargs is :', kwargs)


add = lambda x, y: x + y
def add(x, y):
   return x + y


x = 50
def func(x):
   print('x is', x)
   x = 2
   print('Changed local x to', x)


x = 50
def func():
   global x
   print('x is', x)
   x = 2
   print('Changed global x to', x)


def outer():
   x = "локальна змінна"
   def inner():
      nonlocal x

      x = "нелокальна змінна x"
      print("внутрішня функція:", x)
      inner()
      print("зовнішня функція:", x)
outer()

# Рекурсивна функція - повертає суму чисел у вхідному наборі
def сalc_sum_numbers(a):
   if a == []:
      # якщо набір пустий, повернути 0
      return 0
   else:
      # Обчислити суму - додати перший елемент набору
      summ = сalc_sum_numbers(a[1:]) # рекурсивний виклик цієї ж функції
      # Додати до загальної суми перший елемент
      summ = summ + a[0]
   return summ

L = [ 2, 3, 8, 11, 4, 6 ]
summ = сalc_sum_numbers(L)
print("summ = ", summ)


def factorial(n):
   if n == 0:
      return 1
   else:
      return n * factorial(n - 1)


def iterative_fib(n):
   a, b = 0, 1
   for i in range(n):
      a, b = b, a + b
   return a

import random
for i in range(5):
   print(random.randint(1, 10))


# Функція приймає рядок, а повертає словник, де ключ це символ рядка, а значення код ASCII
def codes_of_string(string: str) -> dict:
   codes = {}
   for ch in string:
       if not ch in codes:
           codes[ch] = ord(ch)
   return codes

print(codes_of_string("Hello world!"))

def is_prime(n: int) -> bool:
   if n <= 1:
       return False
   for i in range(2, n):
       if n % i == 0:
           return False
   return True


def to_seconds(seconds=0, minutes=0, hours=0, days=0, weeks=0):
   number_seconds_in_minute = 60
   number_seconds_in_hour = 60 * number_seconds_in_minute
   number_seconds_in_day = 24 * number_seconds_in_hour
   number_seconds_in_week = 7 * number_seconds_in_day

   return seconds + minutes * number_seconds_in_minute + \
       hours * number_seconds_in_hour + \
       days * number_seconds_in_day + \
       weeks * number_seconds_in_week