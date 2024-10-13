def func(student):
    return student[1]
n = int(input())
mp = {}
for i in range(0, n, 1):
    x = input().split()
    mp[x[0]] = int(x[1])
m = int(input())
students = []
results = []
for i in range(0, m, 1):
    x = input().split()
    x[1] = float(x[1])
    students.append(x)
students.sort(reverse = True, key = func)
for i in range(0, m, 1):
    for j in range(2, 6, 1):
        if(mp[students[i][j]]):
            mp[students[i][j]] -= 1
            results.append([students[i][0], students[i][j]])
            break
results.sort()
for i in range(0, m, 1):
    print(results[i][0], results[i][1])