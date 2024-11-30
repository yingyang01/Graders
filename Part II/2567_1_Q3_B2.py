replaced, want = input().split('/')
strg = ""
sliced1 = ""
n = int(input())
for i in range(0, n, 1):
    x = input()
    strg += x.lower()
    sliced1 += x
    if(i != n-1):
        strg += ' '
        sliced1 += '\n'
idx = 0
while(idx < len(strg)):
    r = strg.find(replaced.lower(), idx)
    if(r == -1):
        print(sliced1[idx::1])
        break
    print(sliced1[idx:r:1]+want, end = "")
    idx = r+len(replaced)
    