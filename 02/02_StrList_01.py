a = input()
check_dig = 11
dels = 0
for i in range(12):
    dels += (13-i)*int(a[i])
dels %= 11
check_dig = (11-dels)%10
print(a[0], a[1:5], a[5:10], a[10:12], check_dig)