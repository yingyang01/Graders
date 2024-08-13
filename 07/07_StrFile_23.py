file, y = input().split()
f = open(file, "r")
mx = -1e10
mn = 1e10
sgm = 0
cnt = 0
while(1):
    s = f.readline()
    if(len(s) == 0):
        break
    id, score = s.split()
    score = float(score)
    if(y[-2::1] == id[:2]):
        mx = max(mx, score)
        mn = min(mn, score)
        sgm += score
        cnt += 1
if(cnt):
    print(mn, mx, sgm/cnt)
else:
    print("No data")