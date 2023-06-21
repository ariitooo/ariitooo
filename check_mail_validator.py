import re
def email():
    E_mail = input("please enter the E-mail :")
    return bool(re.match("[\w\.]+@[\w\.]+\.com", E_mail, re.I))


print(email())
