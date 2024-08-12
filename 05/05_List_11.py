strg = input()
used = []
for i in range(10):
    used.append(0)
for c in strg:
    if('0' <= c <= '9'):
        used[int(c)] = 1
ok = 0
printed = []
for i in range(10):
    if(not(used[i])):
        printed.append(i)
        ok = 1
if(not(ok)):
    print("None")
else:
    sz = len(printed)
    for i in range(sz):
        if(i != sz-1):
            print("{},".format(printed[i]), end = '')
        else:
            print(printed[i], end = '')
