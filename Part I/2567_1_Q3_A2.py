dist = int(input())
fact = float(input())
end = float(input())
pit_st = float(input())
pit_ed = float(input())
cur = 0
cnt = 0
end = dist-end
while(cur < end):
    cur += (dist-cur)*fact
    if(cur >= pit_st and cur <= pit_ed):
        cur = pit_ed
    cnt += 1
print(cnt)