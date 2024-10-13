n = int(input())
dicts = dict()
for i in range(0, n, 1):
    x = input()
    j = 0
    id = ''
    while(x[j] != ':'):
        id += x[j]
        j += 1
    for e in x[j+1:].strip().split(", "):
        if(id in dicts):
            dicts[id].append(e)
        else:
            dicts[id] = [e]
want = input()
results = []
for key in dicts:
    if(key == want):
        continue
    for k in dicts[want]:
        if(k in dicts[key]):
            results.append(key)
            break
for i in results:
    print(i)
if(len(results) == 0):
    print("Not Found")