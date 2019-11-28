import re

emailRegex = '^\w+([\.-]?\w+)*@\w+([\.-]?\w+)*(\.\w{2,3})+$'

def checkEmail(email):
    if re.search(emailRegex,email):
        return True
    return False
        