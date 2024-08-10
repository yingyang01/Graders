def check_digit(n):
    check_dig = 11
    dels = 0
    for i in range(12):
        dels += (13-i)*int(n[i])
    check_dig -= (dels%11)
    check_dig %= 10
    return check_dig;

exec(input())