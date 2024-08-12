def peaks(data):
    sz = len(data)
    peak = []
    if(sz == 1):
        return data
    else:
        for i in range(sz):
            if(i and i != sz-1 and data[i] > data[i-1] and data[i] > data[i+1]):
                peak.append(i)
        return peak

exec(input())