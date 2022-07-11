"""
Метод: isdigit
----
Заданий список, кожним елементом якого є рядок символів, що складається з одних цифр.
Впорядкувати елементи масиву за зростанням їх числових значень і вивести на екран.
Від максимального елемента відняти значення мінімального та вивести різницю на екран.
Підрахувати середнє значення всіх елементів.
"""

numbers = ["123", "456", "321", "10", "75", "abc", "23c"]

def sanitize(data):
    result = []
    for el in data:
        if el.isdigit():
            result.append(int(el))
    return result


sanitize_numbers = sanitize(numbers)
print(sanitize_numbers)
print(sorted(sanitize_numbers))

print(max(sanitize_numbers) - min(sanitize_numbers))
print(sum(sanitize_numbers) / len(sanitize_numbers))
