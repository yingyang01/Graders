elec = {}
n = int(input())
for i in range(0, n, 1):
    state, electoralVotes = input().split(',')
    elec[state] = int(electoralVotes)

m = int(input())
cState = {}
score = {}
for i in range(0, m, 1):
    county, state = input().split(',')
    if(state not in cState):
        cState[state] = [county]
        score[state] = {county:[0, 0]}
    else:
        cState[state].append(county)
        score[state][county] = [0, 0]
    
o = int(input())
for i in range(0, o, 1):
    county, state, rep, dem = input().split(',')
    if(state in cState and county in cState[state]):
        score[state][county][0] += int(rep)
        score[state][county][1] += int(dem)

republican = 0; democrat = 0

for state in elec:
    rep = 0; dem = 0
    for county in cState[state]:
        rep += score[state][county][0]
        dem += score[state][county][1]
    if(rep > dem):
        republican += elec[state]
    else:
        democrat += elec[state]

print(str(republican)+':'+str(democrat))
if(republican > democrat):
    print("Republican wins")
elif(republican < democrat):
    print("Democrat wins")
else:
    print("Undecided")