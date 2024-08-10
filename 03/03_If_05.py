n = int(input())
if(n > 0):
    print("positive")
elif(n < 0):
    print("negative")
else:
    print("zero")
if(n&1):
    print("odd")
elif(n%2 == 0):
    print("even")

