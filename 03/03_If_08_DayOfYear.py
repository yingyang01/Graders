def leap_year(year):
    if(year%400 == 0):
        return 1
    elif(year%100 == 0):
        return 0
    elif(year%4 == 0):
        return 1
    else:
        return 0
d = int(input())
m = int(input())
y = int(input())
y -= 543
number_of_days = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
ans = d
for i in range(m-1):
    ans += number_of_days[i]
if(m > 2 and leap_year(y)):
    ans += 1
elif(m == 2 and d == 29):
    ans += 1
print(ans)