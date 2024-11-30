n = int(input())
actor = {}
for i in range(0, n, 1):
    x = input().strip().split(", ")
    if(x[1] not in actor):
        actor[x[1]] = [x[0]]
    else:
        actor[x[1]].append(x[0])
    if(x[2] not in actor):
        actor[x[2]] = [x[0]]
    else:
        actor[x[2]].append(x[0]) 
want = input().strip().split(", ")
for i in range(0, len(want), 1):
    print(want[i], "-> ", end = "")
    if(want[i] not in actor):
        print("Not found")
    else:
        for j in range(0, len(actor[want[i]]), 1):
            if(j != len(actor[want[i]])-1):
                print(actor[want[i]][j], end = ", ")
            else:
                print(actor[want[i]][j])