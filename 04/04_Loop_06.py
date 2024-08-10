h = int(input())
for i in range(h):
    for j in range(2*h-1):
        if(j == h-1+i or i == h-1 or i+j == h-1):
            print('*', end = '')
        elif(j < h-1+i):
            print('.', end = '')
    print('\n', end = '')
            