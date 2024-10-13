def knows(R, x, y):
    if(y in R[x]):
        return True
    else:
        return False
    
def is_celeb(R, x):
    all = len(R)-1
    cnt = 0
    for key in R:
        if(key == x):
            continue
        elif(x in R[key]):
            cnt += 1
    if((len(R[x]) == 0 or (len(R[x]) == 1 and R[x] == set([x]))) and cnt == all):
        return True
    else:
        return False
    
def find_celeb(R):
    for key in R:
        if(is_celeb(R, key)):
            return key
    return

def read_relations():
    dicts = {}
    while(1):
        x = input().split()
        if(len(x) == 1):
            break
        if(dicts.get(x[0]) == None):
            dicts[x[0]] = set([x[1]])
        else:
            dicts[x[0]].add(x[1])
        if(dicts.get(x[1]) == None):
            dicts[x[1]] = set()
    return dicts

def main():
    R = read_relations()
    c = find_celeb(R)
    if(c == None):
        print('Not Found')
    else:
        print(c)

exec(input().strip())
# R = read_relations()
# print(R)