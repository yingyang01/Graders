lists = [int(e) for e in input().split()]
lists.sort()
prev = -1
distinct = []
cnt = 0
for e in lists:
    if(e != prev):
        cnt += 1
        distinct.append(e)
        prev = e
print("{}\n{}".format(cnt, distinct[:10]))