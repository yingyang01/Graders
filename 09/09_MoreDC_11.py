n = int(input())
for i in range(0, n, 1):
    strg = input()
    if(len(strg) == 0):
        print("\n", end = '')
        continue
    if(strg[0] == '.'):
        i = 0
        while(i < len(strg) and strg[i] == '.'):
            i += 1
        print(strg[i//2:])
    else:
        print(strg)