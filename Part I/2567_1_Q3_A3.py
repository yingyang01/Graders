score = []
for i in range(0, 3, 1):
    score.append([int(e) for e in input().split()])
sgm = 0
for i in range(0, len(score[0])):
    sgm += max([score[0][i], score[1][i], score[2][i]])
for i in range(len(score[0]), len(score[1])):
    sgm += max([score[1][i], score[2][i]])
for i in range(len(score[1]), len(score[2])):
    sgm += score[2][i]
print(sgm)