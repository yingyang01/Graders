p = [0, 0]
dicts = {"R":1, "Y":2, "G":3, "W":4, "B":5, "P":6, "K":7}
while(1):
    state = input().strip()
    player = int(state[0])-1
    one = state[1]
    if(one =='X'):
        continue
    p[player] += dicts[one]
    if(one != 'R'):
        if(one == "K"):
            break
        continue
    two = state[2]
    if(two != 'X'):
        p[player] += dicts[two]
print(p[0], p[1])
if(p[0] == p[1]):
    print("Tie")
elif(p[0] > p[1]):
    print("Player 1 wins")
else:
    print("Player 2 wins")
