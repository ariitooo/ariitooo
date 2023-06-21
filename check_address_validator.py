import re
def address():
    adres = input("please enter the address :")
    match = bool(re.match("[\w+][\s\-\,]?", adres))
    if match:
        return True
    return False


print(address())

