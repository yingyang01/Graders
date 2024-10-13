n = int(input())
score = {}
for i in range(0, n, 1):
    x = input().split()
    if(score.get(x[0]) == None):
        score[x[0]] = 0
    else:
        score[x[0]] = score[x[0]]|0
    score[x[1]] = 1
winner = []
for key, value in score.items():
    if(score[key] == 0):
        winner.append(key)
print(sorted(winner))