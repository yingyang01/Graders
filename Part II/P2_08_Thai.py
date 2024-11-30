def to_Thai(N):
    word = ""
    N = str(N)
    ptr = 0
    if(len(N) == 4):
        word += dicts[N[ptr]]+" pun "
        ptr += 1
    if(len(N) >= 3):
        if(N[ptr] != '0'):
            word += dicts[N[ptr]]+" roi "
        ptr += 1
    if(len(N) >= 2):
        if(N[ptr] != '0'):
            if(N[ptr] == '1'):
                word += " sip "
            elif(N[ptr] == '2'):
                word += "yi sip "
            else:
                word += dicts[N[ptr]]+" sip "
        ptr += 1
    if(len(N) >= 1):
        if(N[ptr] == '0'):
            if(len(N) == 1):
                word += dicts[N[ptr]]
        else:
            if(N[ptr] == '1'):
                if(len(N) == 1):
                    word += dicts[N[ptr]]
                else:
                    word += "et"
            else:
                word += dicts[N[ptr]]
    return word.strip()

dicts = {'0': 'soon', '1': 'neung', '2': 'song', '3': 'sam', '4': 'si', '5': 'ha', '6': 'hok', '7': 'chet', '8': 'paet', '9': 'kao'}
exec(input().strip())
