file_name = input()
n = int(input())
file = open(file_name, "r")
strg = ""
while(1):
    x = file.readline().strip()
    if(len(x) == 0):
        break
    strg += x+'.'
strg = strg[0:-1:1]
top = ""
for i in range(0, n//10, 1):
    top += "-"*9+str(i+1)
top += "-"*(n%10)
print(top)
l = 0
while(l < len(strg)):
    select = strg[l:l+n:1]
    if(select[-1] == '.'):
        # print("a")
        print(select.strip('.'))
        l = l+n
        while(strg[l] == '.'):
            l += 1
    else:
        if('.' not in select):
            next = strg.find('.', l)
            if(next == -1):
                next = len(strg)
            # print("b")
            print(strg[l:next])
            l = next+1
        else:
            ll = l+n
            if(ll >= len(strg) or (ll < len(strg) and strg[ll] == '.')):
                # print("c")
                print(select)
                ll += 1
                while(ll < len(strg) and strg[ll] == '.'):
                    ll += 1
                l = ll
                continue
            while(strg[ll] != '.'):
                ll -= 1
            # print("d")
            print(strg[l:ll].strip('.'))
            l = ll+1

    