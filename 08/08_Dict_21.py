strg = input()
cnt = {}
lists = []
for e in strg:
    e = e.lower()
    if('a' <= e <= 'z'):
        if(cnt.get(e) != None):
            cnt[e] += 1
        else:
            cnt[e] = 1
for key in cnt:
    lists += [[-cnt[key], key]]
lists.sort()
for e in lists:
    print("{} -> {}".format(e[1], -e[0]))
        