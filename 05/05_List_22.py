op = input()
score = []
grade = ['A', "B+", 'B', "C+", 'C', "D+", 'D', 'F']
while(op != 'q'):
    score.append(op.split())
    op = input()
for e in input().split():
    for s in score:
        if(e == s[0]):
            if(s[1] != 'A'):
                s[1] = grade[grade.index(s[1])-1]
            break
score.sort()
for s in score:
    print(s[0], s[1])