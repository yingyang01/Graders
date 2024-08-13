low = "abcdefghijklmnopqrstuvwxyz"
def rot13(encode):
    encoded = ""
    sz_encode = len(encode)
    is_upper = 0
    x = ""
    for i in range(0, sz_encode, 1):
        if('A' <= encode[i] <= 'Z'):
            is_upper = 1
        x = encode[i].lower()
        if('a' <= x <= 'z'):
            idx = 0
            for j in range(0, 26):
                if(low[j] == x):
                    idx = j
                    break
            if(is_upper):
                encoded += low[(j+13)%26].upper()
            else:
                encoded += low[(j+13)%26]
        else:
            encoded += encode[i]
        is_upper = 0
    return encoded

strg = input()
while(strg != "end"):
    print(rot13(strg))
    strg = input()