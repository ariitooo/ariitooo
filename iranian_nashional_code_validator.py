import re

def national_code():
    code = input("please enter the national code :")
    if len(code) == 10 or len(code) == 12:
        match = bool(re.match("^\d{3}\-?\d{6}\-?\d{1}$", code))
        if match:
            return True
        return False
    else:
        print("wrong !")


print(national_code())


