"""
Метод: isdigit
----
1. Знайти кількість цифр у рядку
2. Знайти кількість чисел у рядку
"""

string = "Нільс Бор народився в родині професора фізіології Копенгагенського університету Християна Бора (1858—1911), "\
         "й Еллен Адлер (1860—1930). Батьки Бора одружилися 1881 року. Батька Нільса Бора двічі висували кандидатом "\
         "на Нобелівську премію з фізіології або медицини[6]. Мати була донькою впливового та вельми заможного "\
         "єврейського банкіра і парламентаря-ліберала Давида Баруха Адлера[da] (1826—1878) і Дженні Рафаел (1830—1902) "\
         "із британської єврейської банкірської династії Raphael Raphael & sons[en][7]."

# Знайти кількість цифр у рядку
def count_digits(string):
    count = 0
    for element in string:
        if element.isdigit():
            count += 1
    return count

# print(count_digits(string))


def count_numbers(string):
    count = 0
    pos = 0
    numbers = []
    while pos < len(string):
        if string[pos].isdigit():
            num = ''
            while pos < len(string) and string[pos].isdigit():
                num = num + string[pos]  # 1 + 8 + 5 + 8
                pos = pos + 1
            numbers.append(num)
            count += 1
        else:
            pos = pos + 1
    return count, numbers

print(count_numbers(string))
