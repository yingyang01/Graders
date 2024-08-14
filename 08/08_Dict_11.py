def reverse(d):
    dd = {}
    for key in d:
        dd[d[key]] = key
    return dd

def keys(d, v):
    lists = []
    for key in d:
        if(d[key] == v):
            lists.append(key)
    return lists

exec(input().strip())