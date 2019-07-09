import re

def phone_number(string):
    return re.findall(r'\d{3}-\d{3}-\d{4}', string)

print(phone_number('333-222-1111'))