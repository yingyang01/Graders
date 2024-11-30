a = input()
b = input()
cpy_a = a
cpy_b = b
a = a.lower()
b = b.lower()
A = [0]*26
B = [0]*26
alphabet = "abcdefghijklmnopqrstuvwxyz"
for char in a:
    if('a' <= char <= 'z'):
        A[alphabet.index(char)] += 1
for char in b:
    if('a' <= char <= 'z'):
        B[alphabet.index(char)] += 1
ok = 0
print(cpy_a)
for i in range(0, 26, 1):
    if(A[i]-B[i] > 1):
        print(" - remove {} {}'s".format(A[i]-B[i], alphabet[i]))
        ok = 1
    elif(A[i]-B[i] == 1):
        print(" - remove {} {}".format(A[i]-B[i], alphabet[i]))
        ok = 1
if(not(ok)):
    print(" - None")
ok = 0
print(cpy_b)
for i in range(0, 26, 1):
    if(B[i]-A[i] > 1):
        print(" - remove {} {}'s".format(B[i]-A[i], alphabet[i]))
        ok = 1
    elif(B[i]-A[i] == 1):
        print(" - remove {} {}".format(B[i]-A[i], alphabet[i]))
        ok = 1
if(not(ok)):
    print(" - None")
