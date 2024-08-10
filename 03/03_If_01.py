s = input()
ok = 0
for c in s:
    if(c < '0' or c > '9'):
        ok = 1
        break;
if(ok or len(s) != 2):
    print("Error")
else:
    s = int(s)
    if((s >= 1 and s <= 2) or (s >= 20 and s <= 40) or s == 51 or s == 53 or s == 55 or s == 58):
        print("OK")
    else:
        print("Error")
