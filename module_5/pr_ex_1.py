'''
Метод: search
'''

import re

string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858-1911), "\
         "й Еллен Адлер (1860—1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом "\
         "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного "\
         "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826—1878) і Дженні Рафаел (1830—1902) "\
         "із британської єврейської банкірської династії Raphael Raphael & sons[en][7]."

pattern = r"[0-9]+"
result = re.search(pattern, string)
print(result.span())

# first_index, last_index = result.span()  # span return tuple of index
# print(string[first_index:last_index])

print(result.group())

