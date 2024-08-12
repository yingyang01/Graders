card = input().split()
sz = len(card)
op = input()
for e in op:
    if(e == 'C'):
        card = card[sz//2:]+card[:sz//2]
    elif(e == 'S'):
        szz = sz//2
        temp = []
        for i in range(szz):
            temp.append(card[i])
            temp.append(card[i+szz])
        card = temp
for e in card:
    print(e, end = ' ')
