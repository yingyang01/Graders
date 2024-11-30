months = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
results = []
while(1):
    x = input()
    if(x == "END"):
        break
    x = x.split()
    x = [int(x[0]), x[1], int(x[2]), int(x[3]), int(x[4])]
    leap_year = 0
    if(x[3] == 2 and ((x[4]-543)%400 == 0 or ((x[4]-543)%4 == 0 and (x[4]-543)%100 != 0))):
        leap_year = 1
    if(x[4] < 2558):
        print("Error: ", end = "")
        for e in x:
            print(e, end = " ")
        print("--> Invalid year")
        continue
    elif(x[3] < 1 or x[3] > 12):
        print("Error: ", end = "")
        for e in x:
            print(e, end = " ")
        print("--> Invalid month")
        continue
    elif(x[2] < 1 or x[2] > months[x[3]]+leap_year):
        print("Error: ", end = "")
        for e in x:
            print(e, end = " ")
        print("--> Invalid date")
        continue
    elif(x[1] not in "EQNF"):
        print("Error: ", end = "")
        for e in x:
            print(e, end = " ")
        print("--> Invalid delivery type")
        continue
    x = [x[4], x[3], x[2], x[0], x[1]]
    det = 0
    if(x[4] == 'E'): det = 1
    elif(x[4] == 'Q'): det = 3
    elif(x[4] == 'N'): det = 7
    else: det = 14
    x[2] += det
    if(x[2] > months[x[1]]+leap_year):
        x[2] -= months[x[1]]+leap_year
        x[1] += 1
        if(x[1] > 12):
            x[1] -= 12
            x[0] += 1
    results.append(x)
if(len(results)):
    results.sort()
    for result in results:
        print("%d: delivered on %d/%d/%d" %(result[3], result[2], result[1], result[0]))
    
