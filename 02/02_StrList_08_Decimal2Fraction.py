import math
def divs(strg, q):
    ans = ""
    divided = ""
    remainder = 0
    sz = len(strg)
    for i in range(sz):
        divided += strg[i]
        if(int(divided) >= q):
            ans += str(int(divided)//q)
            remainder = int(divided)%q
            divided = str(remainder)
        else:
            ans += '0'
    real_ans = ""
    ok = 0
    sz = len(ans)
    for i in range(sz):
        if(ans[i] != '0'):
            ok = 1
        if(ok):
            real_ans += ans[i]
    if(real_ans == ""):
        real_ans = '0'
    return real_ans
strg = input()
attr = ["", "", ""]
i = 0
sz = len(strg)
for j in range(3):
    while(i < sz and strg[i] != ','):
        attr[j] += strg[i]
        i += 1
    i += 1
sz_repeat = len(attr[2])
nine = ""
for i in range(sz_repeat):
    nine += '9'
nine = int(nine)
remainder = int(attr[1]+attr[2])-int('0'+attr[1])
frac = [int(attr[0])*(nine*(10**len(attr[1])))+remainder, nine*(10**len(attr[1]))]
Gcd = math.gcd(int(frac[0]), int(frac[1]))
frac = [divs(str(frac[0]), Gcd), divs(str(frac[1]), Gcd)]
print(frac[0]+" / "+frac[1])
'''frac[0] /= Gcd
frac[1] /= Gcd
print("{rem} / {deno}".format(rem = int(frac[0]), deno = int(frac[1])))'''
