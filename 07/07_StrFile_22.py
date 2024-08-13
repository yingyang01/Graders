cnt = [0]*26
strg = input()
strg2 = input()
alpha = "abcdefghijklmnopqrstuvwxyz"
for c in strg:
    if('a' <= c.lower() <= 'z'):
        cnt[alpha.index(c.lower())] += 1
for c in strg2:
    if('a' <= c.lower() <= 'z'):
        cnt[alpha.index(c.lower())] -= 1
ok = 1
for e in cnt:
    if(e):
        ok = 0
if(ok):
    print("YES")
else:
    print("NO")