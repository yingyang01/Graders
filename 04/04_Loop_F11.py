def RLE(t):
    prev = ""
    consec = 0
    pairs = []
    for c in t:
        if(c == prev):
            consec += 1
        else:
            if(consec):
                pairs.append([prev, consec])
            prev = c
            consec = 1
    if(consec):
        pairs.append([prev, consec])
    return pairs

exec(input())