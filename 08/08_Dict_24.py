maps = {"abc" : '2', "def" : '3', "ghi" : '4', "jkl" : '5', "mno" : '6', "pqrs" : '7', "tuv" : '8', "wxyz" : '9', ' ' : '0'}
maps_reversed = {}
for key in maps:
    maps_reversed[maps[key]] = key

def text2keys(text):
    keys = ""
    for c in text:
        c = c.lower()
        if('a' <= c <= 'z' or c == ' '):
            this = ""
            for key in maps:
                if(c in key):
                    this = key
            sz_this = this.index(c)+1
            for i in range(0, sz_this):
                keys += maps[this]
            keys += ' '
    return keys

def keys2text(keys):
    keys = keys.split()
    text = ""
    for k in keys:
        sz = len(k)
        value = maps_reversed.get(k[0])
        text += value[sz-1]
    return text

exec(input().strip())
