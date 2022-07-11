"""
Методи: split, replace
----
Парсимо query запит для гугла. Тут класичний роздільник & і перетворюємо на словник із даними
"""

# replace(old, new, num)
phone = "+1-234-567-89-10"
url_search = "https://www.google.com/search?q=Cat+and+dog&ie=utf-8&oe=utf-8&aq=t"

# edited_phone = phone.replace("-", " ", 2)
# print(edited_phone)

_, query = url_search.split("?")
print(query)

obj_query = {}
for el in query.split("&"):  # ["q=Cat+and+dog", "ie=utf-8", "oe=utf-8", "aq=t"]
    key, value = el.split("=")  # "q=Cat+and+dog" => key: 'q' value: 'Cat+and+dog'

    obj_query.update(
        {
            key: value.replace("-", " ").replace("+", " ")  # key: 'q' value: 'Cat and dog'
        }
    )

print(obj_query)


