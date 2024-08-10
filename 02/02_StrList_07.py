s = input()
a = s[3]+s[10]+s[17]+s[24]+s[31]
b = s[7]+s[12]+s[17]+s[22]+s[27]
s = str(int(a)+int(b)+10000)
sz = len(s)
s = s[sz-4]+s[sz-3]+s[sz-2]
cpys = s
s = int(s[0])+int(s[1])+int(s[2])
s = s%10+1
alphabets = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J']
print(str(cpys)+alphabets[s-1])

