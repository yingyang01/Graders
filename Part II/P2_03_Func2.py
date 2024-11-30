def convex_polygon_area(p):
    sgm = 0
    for i in range(0, len(p), 1):
        sgm += (p[i][0]*p[(i+1)%len(p)][1]-p[i][1]*p[(i+1)%len(p)][0])
    return abs(sgm)/2

def is_heterogram(s):
    dicts = {}
    for e in s:
        if(e.lower() in dicts):
            return False
        else:
            if('a' <= e.lower() <= 'z'):
                dicts[e.lower()] = 1
    return True

def replace_ignorecase(s, a, b):
    pairs = []
    cpys = s.lower()
    cpya = a.lower()
    cur = 0
    while(1):
        cur = cpys.find(cpya, cur)
        if(cur == -1):
            break
        pairs.append((cur, cur+len(a)))
        cur += len(a)
    pairs.append((len(s), len(s)))
    replaced = ""
    idx = 0
    i = 0
    while(i < len(s)):
        if(i < pairs[idx][0]):
            replaced += s[i]
        else:
            replaced += b
            i = pairs[idx][1]-1
            idx += 1
        i += 1
    return replaced

def top3(votes):
    score = []
    for key, value in votes.items():
        score.append(value)
    score.sort(reverse = True)
    prev = score[0]
    top_score = [score[0]]
    for i in range(1, len(score), 1):
        if(prev != score[i]):
            top_score.append(score[i])
            if(len(top_score) == 3):
                break
            prev = score[i]
    top = []
    for key, value in votes.items():
        if(value >= score[2]):
            top.append([-value, key])
    top.sort()
    return [value for key, value in top[0:3:1]]

for k in range(2):
    exec(input().strip())


