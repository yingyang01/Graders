mp = {}
while(1):
    x = input()
    if(x == 'q'):
        break
    x = x.split(", ")
    if(mp.get(x[1]) == None):
        mp[x[1]] = [x[0]]
    else:
        mp[x[1]].append(x[0])
for key in mp:
    print(key+': ', end = '')
    for i in range(0, len(mp[key]), 1):
        if(i != len(mp[key])-1):
            print(mp[key][i]+', ', end = '')
        else:
            print(mp[key][i])