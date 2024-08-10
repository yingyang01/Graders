strg = input()
dig = int(input())
if(len(strg) >= dig):
    print(strg)
else:
    zeros = dig-len(strg)
    for i in range(zeros):
        strg = '0'+strg
    print(strg)