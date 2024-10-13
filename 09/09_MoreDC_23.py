def sec_to_min(x):
    return str(x//60)+':'+('0'+str(x-x//60*60))[-2:]

def min_to_sec(p):
    p = [int(e) for e in p.split(':')]
    return p[0]*60+p[1]

n = int(input())
genre = {}
for i in range(0, n, 1):
    x = input().split(", ")
    if(genre.get(x[2]) == None):
        genre[x[2]] = min_to_sec(x[3])
    else:
        genre[x[2]] =  genre[x[2]]+min_to_sec(x[3])
lists = []
for key, value in genre.items():
    lists.append((key, value))
lists.sort(reverse = True, key = (lambda x : x[1]))
i = 1
while(i <= min(len(lists), 3)):
    print("{} --> {}".format(lists[i-1][0], sec_to_min(lists[i-1][1])))
    i += 1