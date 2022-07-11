'''
Метод: sub
'''

import re

string = "The Java best Java language is Java"
a = re.sub(r"Java", "Python", string)

print(a)