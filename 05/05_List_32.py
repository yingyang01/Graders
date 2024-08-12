n = int(input())
cur_ticket = 0; cur_time = 0
cur_id = 0; cur_t = 0
queue = []
sgm = 0; cnt = 0
while(n):
    op = input().split()
    if(op[0] == "reset"):
        cur_ticket = int(op[1])
    elif(op[0] == "new"):
        queue.append([cur_ticket, int(op[1])])
        print("ticket {}".format(cur_ticket))
        cur_ticket += 1
    elif(op[0] == "next"):
        print("call {}".format(queue[0][0]))
        cur_id = queue[0][0]; cur_t = queue[0][1]
        queue = queue[1:] 
    elif(op[0] == "order"):
        print("qtime {} {}".format(cur_id, int(op[1])-cur_t))
        cur_time = int(op[1])
        sgm += int(op[1])-cur_t
        cnt += 1
    else:
        print("avg_qtime {}".format(round(sgm/cnt, 4)))
    n -= 1
    queue.sort()