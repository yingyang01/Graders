strg = input()
sz = len(strg)
num = ""
i = 0
sgm = 0
while(i < sz):
    while(i < sz and strg[i] == ' '):
        i += 1
    while(i < sz and strg[i] >= '0' and strg[i] <= '9'):
        num += strg[i]
        i += 1
    if(len(num)):
        sgm += int(num)
    num = ""
print(sgm)