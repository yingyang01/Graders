score = {}
cnt = {}
kami = {}
dicts = {}
while(1):
    x = input().strip().split()
    if(len(x) == 1):
        break
    x[2] = int(x[2])
    if(x[1] not in score):
        score[x[1]] = x[2]
    else:
        score[x[1]] += x[2]
    if(x[1] not in cnt):
        cnt[x[1]] = {x[0], }
    else:
        cnt[x[1]].add(x[0])
    if(x[0] not in kami):
        kami[x[0]] = [x[1], x[2]]
    elif(x[1] == kami[x[0]][0]):
        kami[x[0]][1] += x[2]
    elif(x[2] > kami[x[0]][1]):
        kami[x[0]][0] = x[1]; kami[x[0]][1] = x[2]
    elif(x[2] == kami[x[0]][1] and x[1] < kami[x[0]][0]):
        kami[x[0]][0] = x[1]
    dicts[x[1]] = 0
x = int(x[0])
if(x == 1):
    result = [[value, name] for name, value in score.items()]
    result.sort(key = (lambda y: (-y[0], y[1])))
    for i in range(0, 3):
        if(i == 2):
            print(result[i][1], end = "")
        else:
            print("%s, " %(result[i][1]), end = "")
elif(x == 2):
    result = [[value, name] for name, value in cnt.items()]
    result.sort(key = (lambda x: (-len(x[0]), x[1])))
    for i in range(0, 3):
        if(i == 2):
            print(result[i][1], end = "")
        else:
            print("%s, " %(result[i][1]), end = "")
else:
    result = dicts
    for key in kami:
        if(not(kami[key][0] in result)):
            result[kami[key][0]] = 1
        else:
            result[kami[key][0]] += 1
    result = [[result[key], key] for key in result]
    result.sort(key = lambda x: (-x[0], x[1]))
    for i in range(0, 3):
        if(i == 2):
            print(result[i][1], end = "")
        else:
            print("%s, " %(result[i][1]), end = "") 