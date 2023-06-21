import re


def phone_number():
    mobile = input("please enter the phone number :")
    match = bool(re.match("^(0|\+98)\s?\d{3}\s?\d{3}\s?\d{2}\s?\d{2}$", mobile))
    if match:
        return True
    return False


print(phone_number())
