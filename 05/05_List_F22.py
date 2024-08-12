def index_of(grades, ID):
    sz = len(grades)
    for i in range(sz):
        if(grades[i][0] == ID):
            return i
    return -1

def upgrade(grades, IDs):
    grade = ['A', "B+", 'B', "C+", 'C', "D+", 'D', 'F']
    grades.sort()
    sz_grades = len(grades)
    for ID in IDs:
        for i in range(sz_grades):
            if(grades[i][0] == ID):
                grades[i][1] = grade[max(0, grade.index(grades[i][1])-1)]
    return

exec(input())
exec(input())
exec(input())