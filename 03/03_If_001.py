lists = []
for i in range(5):
    lists.append(int(input()))
if(lists[0] > lists[1]):
    lists[0], lists[1] = lists[1], lists[0]
if(lists[2] > lists[3]):
    lists[2], lists[3] = lists[3], lists[2]
if(lists[0] > lists[2]):
    lists[1], lists[3] = lists[3], lists[1]
    lists[2] = lists[0]
a = lists[4]
if(lists[0] > lists[1]):
    lists[0], lists[1] = lists[1], lists[0]
if(lists[2] > lists[0]):
    lists[1], lists[3] = lists[3], lists[1]
    lists[0] = lists[2]
if(lists[0] > lists[3]):
    print(lists[3])
else:
    print(lists[0])
