strg = input()
op = input()
dict = {'A' : 'T', 'T' : 'A', 'G' : 'C', 'C' : 'G'}
temp = ""
ok = 0
for c in strg:
    c = c.upper()
    if(not(c == 'A' or c == 'T' or c == 'G' or c == 'C')):
        ok = 1
if(ok):
    print("Invalid DNA")
else:
    if(op == 'R'):
        for c in strg:
            temp += dict[c.upper()]
        print(temp[::-1])
    elif(op == 'F'):
        cnt = [0]*4
        for c in strg:
            c = c.upper()
            if(c == 'A'):
                cnt[0] += 1
            elif(c == 'T'):
                cnt[1] += 1
            elif(c == 'G'):
                cnt[2] += 1
            else:
                cnt[3] += 1
        print("A={}, T={}, G={}, C={}".format(cnt[0], cnt[1], cnt[2], cnt[3]))
    else:
        com = input()
        sz = len(strg)
        cnt = 0
        for i in range(sz-1):
            if(strg[i:i+2].upper() == com.upper()):
                cnt += 1
        print(cnt)