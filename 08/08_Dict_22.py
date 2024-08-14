n = int(input())
brand = {}
sales = {}
sgm = 0
for i in range(0, n):
    lists = input().split()
    brand[lists[0]] = float(lists[1])
m = int(input())
mx = -1
for i in range(0, m):
    lists = input().split()
    if(brand.get(lists[0]) == None):
        continue
    else:
        if(sales.get(lists[0]) == None):
            sales[lists[0]] = brand[lists[0]]*int(lists[1])
        else:
            sales[lists[0]] += brand[lists[0]]*int(lists[1])
        sgm += brand[lists[0]]*int(lists[1])
        mx = max(mx, sales[lists[0]])
if(abs(sgm) < 1e-10):
    print("No ice cream sales")
else:
    print("Total ice cream sales:", sgm, "\nTop sales: ", end = '')
    lists = []
    for sale in sales:
        if(abs(sales[sale]-mx) < 1e-10):
            lists.append(sale)
    sz_lists = len(lists)
    lists.sort()
    for i in range(0, sz_lists):
        if(i != sz_lists-1):
            print("{}, ".format(lists[i]), end = '')
        else:
            print(lists[i])
    