strg = input()
temp = ""
for c in strg:
    if('a' <= c.lower() <= 'z'  or '0' <= c.lower() <= '9'):
        temp += c
    else:
        temp += ' '
temp = (temp.strip()).split()
sz_temp = len(temp)
for i in range(sz_temp):
    if(i):
        print(temp[i][0].upper()+temp[i][1:].lower(), end = '')
    else:
        print(temp[i].lower(), end = '')
