n = int(input())
names = [["Robert", "Dick"], ["William", "Bill"], ["James", "Jim"], ["John", "Jack"], ["Margaret", "Peggy"], ["Edward", "Ed"], ["Sarah", "Sally"], ["Andrew", "Andy"], ["Anthony", "Tony"], ["Deborah", "Debbie"]]
for i in range(n):
    name = input()
    ok = 0
    for name_nickname in names:
        if(name_nickname[0] == name):
            print(name_nickname[1])
            ok = 1
        elif(name_nickname[1] == name):
            print(name_nickname[0])
            ok = 1
        if(ok):
            break
    if(not(ok)):
        print("Not found")