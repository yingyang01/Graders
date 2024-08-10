def is_mobile_number(number):
    if(len(number) != 10):
        return False
    strg = number[:2]
    if(strg == "06" or strg == "08" or strg == "09"):
        return True
    else:
        return False

exec(input())