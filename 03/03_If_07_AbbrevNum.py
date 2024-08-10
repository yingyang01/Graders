n = input()
sz = len(n)
ans = ""
if(sz <= 3):
    print(n)
else:
    if(sz >= 13):
        sz -= 9
        for i in range(sz-1):
            ans += n[i]
        if(int(n[sz]) >= 5):
            ans += str(int(n[sz-1])+1)
        else:
            ans += str(int(n[sz-1]))
        sz += 9
    elif(sz%3 == 1):
        ans += n[0]+'.'
        if(int(n[2]) >= 5):
            ans += str(int(n[1])+1)
        else:
            ans += str(int(n[1]))
    elif(sz%3 == 2):
        ans += n[0]
        if(int(n[2]) >= 5):
            ans += str(int(n[1])+1)
        else:
            ans += str(int(n[1]))
    elif(sz%3 == 0):
        ans += n[0]+n[1]
        if(int(n[3]) >= 5):
            ans += str(int(n[2])+1)
        else:
            ans += str(int(n[2]))        
    if(sz <= 6):
        ans += 'K'
    elif(sz <= 9):
        ans += 'M'
    else:
        ans += 'B'
    print(ans)