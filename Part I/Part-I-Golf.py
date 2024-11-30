from math import floor as fl
sgm_par = 0; sgm_stk = 0; sgm_imp_stk = 0
for i in range(0, 9, 1):
    x = [int(e) for e in input().split()]
    sgm_par += x[0]
    sgm_stk += x[1]
    if(x[2]):
        sgm_imp_stk += min(x[0]+2, x[1])
helping_score = fl(0.8*(1.5*sgm_imp_stk-sgm_par))
print("{}\n{}\n{}".format(sgm_stk, helping_score, sgm_stk-helping_score))
