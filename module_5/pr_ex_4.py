'''
Метод: split
Напишемо універсальну функцію get_parameters, яка повертатиме словник з даними.
Оскільки в першому рядку розділити символ ; а на другий &, тому тут вдало підійде
випадок (a|b - відповідає a або b)
'''

import re

url_query = "20850=ot-25-mp-do-47-mp;23777=6-6-5;38435=8-gb;41404=16gb"  # ;
url_search = "q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"  # &
url_searc = "q=Cat+and+dog%ie=utf-8%oe=utf-8%aq=t"  # &

def get_parameters(data: list) -> dict:
    obj_query = {}
    for el in data:
        key, value = el.split("=")
        obj_query.update({key: value.replace("+", " ")})
    return obj_query


pattern = r";|&|\*"
data_url_query = re.split(pattern, url_query, url_search)
print(get_parameters(data_url_query))
print(data_url_query)
#
# data_url_search = re.split(pattern, url_search)
# print(data_url_search)
# data_url_url_searc = re.split(pattern, url_searc)
# print(data_url_url_searc)