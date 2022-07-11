"""
Методи: strip, removeprefix, replace, format
------
Провести валідацію списку телефонів
Телефон: +380501234567 Де: +380 код країни телефон 501234567
Вважаємо, що код валідний з кодом і без коду
"""
phone_storage = ["380669640547", "0637306465 ", " 380961935171", "632643973", "050832520 ", "000000000",
                 "48730283918", "986223575", "375297947963", "+38(050)123-32-34", "38(050)123 32 34",
                 "38(050)123 32 3b"]

codes_operators = {"067", "068", "096", "097", "098", "050", "066", "095", "099", "063", "073", "093"}


def isvalid_phone(phone: str) -> bool:
    def is_valid_operator(phone):
        if phone[:3] in codes_operators:
            return True
        return False

    if phone.isdigit():
        if len(phone) == 12:
            if phone[:2] == "38":
                return is_valid_operator(phone[2:])
        if len(phone) == 10:
            return is_valid_operator(phone)
    return False


def sanitize_phone(phone):
    new_phone = (phone.strip()
                 # .lstrip()
                 .removeprefix("+")
                 .replace("(", "")
                 .replace(")", "")
                 .replace("-", "")
                 .replace(" ", ""))
    return new_phone


if __name__ == "__main__":
    for phone in phone_storage:
        phone = sanitize_phone(phone)
        is_valid = isvalid_phone(phone)
        if is_valid:
            print("Phone:{:H<20} is valid".format(phone))
        else:
            print("Phone:{:$<20} is invalid".format(phone))
