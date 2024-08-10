strg = input()
prev = ""
consec = 0
pairs = []
for c in strg:
    if(c == prev):
        consec += 1
    else:
        if(consec):
            pairs.append([prev, consec])
        prev = c
        consec = 1
if(consec):
    pairs.append([prev, consec])
sz_pairs = len(pairs)
for pair in pairs:
    print(pair[0], pair[1], end = ' ')