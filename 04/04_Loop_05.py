want = input()
strg = input()
sz_want = len(want)
sz_strg = len(strg)
cnt = 0
for i in range(sz_strg):
    if(strg[i] == want[0] and i+sz_want-1 < sz_strg and strg[i:i+sz_want] == want ):
        if(i == 0 and i+sz_want == sz_strg):
            cnt += 1
        elif(i == 0 and (strg[i+sz_want] >= 'a' and strg[i+sz_want] <= 'z') == 0 and (strg[i+sz_want] >= 'A' and strg[i+sz_want] <= 'Z') == 0):
            cnt += 1
        elif(i+sz_want == sz_strg and (strg[i-1] >= 'a' and strg[i-1] <= 'z') == 0 and (strg[i-1] >= 'A' and strg[i-1] <= 'Z') == 0):
            cnt += 1
        elif((strg[i+sz_want] >= 'a' and strg[i+sz_want] <= 'z') == 0 and (strg[i+sz_want] >= 'A' and strg[i+sz_want] <= 'Z') == 0 and (strg[i-1] >= 'a' and strg[i-1] <= 'z') == 0 and (strg[i-1] >= 'A' and strg[i-1] <= 'Z') == 0):
            cnt += 1
print(cnt)