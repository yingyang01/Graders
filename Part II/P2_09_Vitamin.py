def show(fruits):
    for fruit in fruits:
        for e in fruit:
            print(e, end = " ")
        print()
    return

def get(fruits, want):
    for fruit in fruits:
        if(fruit[0] == want):
            for e in fruit:
                print(e, end = " ")
            return
    print("%s not found" %(want))
    return

def avg(fruits, number):
    sgm = 0
    for fruit in fruits:
        sgm += fruit[number]
    print(round(sgm/(len(fruits)), 4))
    
def mx(fruits, number):
    ans = ""
    mxx = -1
    for fruit in fruits:
        if(fruit[number] > mxx):
            mxx = fruit[number]
            ans = fruit[0]
        elif(fruit[number] == mxx and fruit[0] < ans):
            ans = fruit[0]
    print(ans, mxx)
            
def sorts(fruits, number):
    lists = []
    for fruit in fruits:
        lists.append([fruit[number], fruit[0]])
    lists.sort()
    for k, name in lists:
        print(name, end = " ")

n = int(input())
info = []
for i in range(0, n, 1):
    x = input().strip().split()
    info.append(x[0:1:1]+[float(e) for e in x[1::1]])
op = input().strip().split()
if(op[0] == "show"):
    show(info)
elif(op[0] == "get"):
    get(info, op[1])
elif(op[0] == "avg"):
    avg(info, int(op[1]))
elif(op[0] == "max"):
    mx(info, int(op[1]))
else:
    sorts(info, int(op[1]))
