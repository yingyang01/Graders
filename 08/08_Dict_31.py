def total(pocket):
    sgm = 0
    for e in pocket:
        sgm += e*pocket[e]
    return sgm

def take(pocket, money_in):
    cpy_pocket = {}
    for e in pocket:
        cpy_pocket[e] = pocket[e]
    for e in money_in:
        if(pocket.get(e) != None):
            pocket[e] += money_in[e]
        else:
            pocket[e] = money_in[e]
    return pocket

def pay(pocket, amt):
    cpy_pocket1 = {}
    cpy_pocket2 = {}
    for e in pocket:
        cpy_pocket2[e] = pocket[e]
    for e in cpy_pocket2:
        while(cpy_pocket2[e] and e <= amt):
            amt -= e
            if(cpy_pocket1.get(e) != None):
                cpy_pocket1[e] += 1
            else:
                cpy_pocket1[e] = 1
            cpy_pocket2[e] -= 1
    if(amt):
        return {}
    for e in cpy_pocket1:
        pocket[e] -= cpy_pocket1[e]
    return cpy_pocket1

exec(input().strip())