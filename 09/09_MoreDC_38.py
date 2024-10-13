dicts = {}
destiny = set()
a = ""
while(1):
    n = input().split()
    if(len(n) == 1):
        a = n[0]
        break
    else:
        if(n[0] in dicts):
            dicts[n[0]].append(n[1])
        else:
            dicts[n[0]] = [n[1]]
        if(n[1] in dicts):
            dicts[n[1]].append(n[0])
        else:
            dicts[n[1]] = [n[0]]
destiny.add(a)
if(dicts.get(a) != None):
    for city1 in dicts[a]:
        destiny.add(city1)
        if(dicts.get(city1) == None):
            continue
        for city2 in dicts[city1]:
            destiny.add(city2)
destiny = list(destiny)
destiny.sort()
for city in destiny:
    print(city)