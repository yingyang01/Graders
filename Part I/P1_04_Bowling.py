def next_two(i, results):
    sgm = 0
    if(results[i+1] == 'X'):
        sgm += 10
        if(results[i+2] == 'X'):
            sgm += 10
        else:
            if('0' <= results[i+2] <= '9'):
                sgm += int(results[i+2])
    else:
        if(results[i+2] == '/'):
            sgm += 10
        else:
            sgm += int(results[i+1])+int(results[i+2])
    return sgm
        
results = input()
reg = [0]*10
cur_game = 0
score = 0
i = 0; sz_results = len(results)
while(cur_game < 10):
    if(results[i] == 'X'):
        reg[cur_game] += 10+next_two(i, results)
        i += 1
    else:
        if(results[i+1] == '/'):
            reg[cur_game] += 10
            if(results[i+2] == 'X'):
                reg[cur_game] += 10
            else:
                reg[cur_game] += int(results[i+2])
        else:
            reg[cur_game] += int(results[i])+int(results[i+1])
        i += 2
    score += reg[cur_game]
    cur_game += 1
want = int(input())
if(1 <= want <= 9):
    print(reg[want-1])
else:
    print(score)