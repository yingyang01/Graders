special_characters = ['!', '@', '#', '$', '%', '^', '&', '*', '(', ')', '-', '+', '"', '\'', '/', '\\', '.']
number_seq = "890123456789012"
letter_seq = "xyzabcdefghijklmnopqrstuvwxyzabc"
consec = ["!@#$%^&*()-+", "qwertyuiop", "asdfghjkl", "zxcvbnm"]
def less_than_8_characters(password, lists):
    if(len(password) < 8):
        lists.append("Less than 8 characters")
    return

def no(password, lists):
    ok_lower = 0
    ok_upper = 0
    ok_number = 0
    ok_symbol = 0
    for e in password:
        if('a' <= e <= 'z'):
            ok_lower = 1
        elif('A' <= e <= 'Z'):
            ok_upper = 1
        elif('0' <= e <= '9'):
            ok_number = 1
        elif(e in special_characters):
            ok_symbol = 1
    if(not(ok_lower)):
        lists.append("No lowercase letters")
    if(not(ok_upper)):
        lists.append("No uppercase letters")
    if(not(ok_number)):
        lists.append("No numbers")
    if(not(ok_symbol)):
        lists.append("No symbols")
    return

def repetition(password, lists):
    cnt = 0
    prev = "-1"
    ok = 1
    for e in password:
        if(e == prev):
            cnt += 1
            if(cnt >= 4):
                ok = 0
                break
        else:
            cnt = 1
            prev = e
    if(not(ok)):
        lists.append("Character repetition")
    return

def number_sequence(password, lists):
    sz_password = len(password)
    ok = 1
    for i in range(0, sz_password-3):
        temp = ""
        for j in range(i, i+4):
            temp += password[j]
        if(temp in number_seq or temp[::-1] in number_seq):
            ok = 0
            break
    if(not(ok)):
        lists.append("Number sequence")
    return

def letter_sequence(password, lists):
    sz_password = len(password)
    ok = 1
    for i in range(0, sz_password-3):
        temp = ""
        for j in range(i, i+4):
            temp += password[j].lower()
        if(temp in letter_seq or temp[::-1] in letter_seq):
            ok = 0
            break
    if(not(ok)):
        lists.append("Letter sequence")
    return

def keyboard_pattern(password, lists):
    sz_password = len(password)
    ok = 1
    for i in range(0, sz_password-3):
        temp = ""
        for j in range(i, i+4):
            temp += password[j].lower()
        for list in consec:
            if(temp in list or temp[::-1] in list):
                ok = 0
                break
        if(not(ok)):
            break
    if(not(ok)):
        lists.append("Keyboard pattern")
    return

lists = []
password = input()
less_than_8_characters(password, lists)
no(password, lists)
repetition(password, lists)
number_sequence(password, lists)
letter_sequence(password, lists)
keyboard_pattern(password, lists)
if(len(lists)):
    for e in lists:
        print(e)
else:
    print("OK")
