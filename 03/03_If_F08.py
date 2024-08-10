def leap_year(y):
    if(y%4):
        return 0
    elif(y%100):
        return 1
    elif(y%400 == 0):
        return 1
    else:
        return 0
    
def day_of_year(d, m, y):
    number_of_day = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
    ans = d
    for i in range(m-1):
        ans += number_of_day[i]
    if(leap_year(y-543) and m > 2):
        ans += 1
    return ans

exec(input())