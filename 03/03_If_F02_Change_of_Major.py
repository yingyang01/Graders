def choose(stu1, stu2):
    ok_A = 0
    ok_B = 0
    ans = []
    if(stu1[2] == 'A' and stu1[3] <= 'C' and stu1[4] <= 'C'):
        ok_A = 1
    if(stu2[2] == 'A' and stu2[3] <= 'C' and stu2[4] <= 'C'):
        ok_B = 1
    if(ok_A and ok_B):
        if(stu1[1] > stu2[1]):
            ans.append(stu1[0])
        elif(stu1[1] < stu2[1]):
            ans.append(stu2[0])
        else:
            if(stu1[3] < stu2[3]):
                ans.append(stu1[0])
            elif(stu1[3] > stu2[3]):
                ans.append(stu2[0])
            else:
                if(stu1[4] < stu2[4]):
                    ans.append(stu1[0])
                elif(stu1[4] > stu2[4]):
                    ans.append(stu2[0])
                else:
                    ans.append(stu1[0])
                    ans.append(stu2[0])
    elif(ok_A):
        ans.append(stu1[0])
    elif(ok_B):
        ans.append(stu2[0])
    return ans
exec(input())   