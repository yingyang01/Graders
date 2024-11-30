strg = input()
order = "A23456789TJQKCDHS"
for i in range(0, len(strg)-2, 2):
    if(strg[i] != strg[i+2]):
        diff = order.index(strg[i])-order.index(strg[i+2])
        if(diff <= 0):
            print(diff, end = "")
        else:
            print('+'+str(diff), end = "")
    else:
        diff = order.index(strg[i+1])-order.index(strg[i+3])
        if(diff <= 0):
            print(diff, end = "")
        else:
            print('+'+str(diff), end = "")
            
