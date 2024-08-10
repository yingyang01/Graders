def grade_mcq(sol, ans):
    if(len(sol) != len(ans)):
        return -1
    else:
        sz_sol = len(sol)
        cnt = 0
        for i in range(sz_sol):
            if(sol[i] == ans[i]):
                cnt += 1
        return cnt

exec(input())