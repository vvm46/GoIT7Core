'''
Метод: sub
Дано рядок символів.
Виключити з цього рядка групи символів між дужками [, ].
Самі дужки теж мають бути виключені.
'''

import re
string = "Виключити із цієї [групи] символів, [розташовані між] дужками [, ]."

pattern = r"\[.+?\]"
print(re.sub(pattern, "", string))


pattern = r"\[|\]"
print(re.sub(pattern, "", string))

pattern = r"\[.+?\]"
print(re.sub(pattern, "[]", string))