def cmp(lists):
    return lists[1]
def read_answers():
    N = int(input())
    answers = []
    for k in range(N):
        sid, ans = input().split()
        answers.append([sid, ans])
    return answers

def marking(answer, solution):
    score = 0
    d = len(answer)
    for i in range(d):
        if(answer[i] == solution[i]):
            score += 1
    return score

def grading(score):
    g = [[80, 'A'], [70, 'B'], [60, 'C'], [50, 'D']]
    for a, b in g:
        if score >= a:
            return b
    return 'F'

def scoring(answers, solution):
    scores = []
    for sid, ans in answers:
        score = marking(ans, solution)/len(solution)*100
        grade = grading(score)
        scores.append([sid, score, grade])
    return scores

def report(scores):
    for sid, sc, grade in scores:
        print(sid, sc, grade)
    return

def sort(scores):
    scores.sort(reverse = 1, key = lambda x : (x[1] , x[0]))
    '''x = []
    for sid, score, grade in scores:
        x.append([score, sid, grade])
    x.sort(reverse = 1)
    sz = len(x)
    for i in range(sz):
        scores[i] = [x[i][1], x[i][0], x[i][2]]'''
    return

solution = input()
students = scoring(read_answers(), solution)
sort(students)
report(students)
