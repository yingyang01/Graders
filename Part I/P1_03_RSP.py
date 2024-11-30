m = int(input())
idx = 0
score_1 = 0; score_2 = 0
while(True):
    if(idx == 3*m):
        print("%d %d\n%s" %(score_1, score_2, "Tie"))
        break
    x = input().split()
    if(x[0] == 'R'):
        if(x[1] == 'S'):
            score_1 += 1
        elif(x[1] == 'P'):
            score_2 += 1
    elif(x[0] == 'P'):
        if(x[1] == 'R'):
            score_1 += 1
        elif(x[1] == 'S'):
            score_2 += 1
    else:
        if(x[1] == 'P'):
            score_1 += 1
        elif(x[1] == 'R'):
            score_2 += 1
    if(score_1 == m):
        print("%d %d\n%s" %(score_1, score_2, "Player 1 wins"))
        break
    elif(score_2 == m):
        print("%d %d\n%s" %(score_1, score_2, "Player 2 wins"))
        break
    idx += 1
