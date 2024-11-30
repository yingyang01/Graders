class roman:
    def __init__(self, r):
        self.r = r

    def __lt__(self, rhs):
        return int(self) < int(rhs)
    
    def __str__(self):
        return self.r
    
    def __int__(self):
        sgm = 0
        order = {"I":1, "V":5, "X":10, "L":50, "C":100, "D":500, "M":1000}
        for i in range(0, len(self.r), 1):
            if(i == len(self.r)-1):
                sgm += order[self.r[i]]
            elif(order[self.r[i]] >= order[self.r[i+1]]):
                sgm += order[self.r[i]]
            else:
                sgm -= order[self.r[i]]
        return sgm

    def __add__(self, rhs):
        now = int(self)+int(rhs)
        strg = ""
        while(now >= 1000):
            now -= 1000
            strg += 'M'
        if(now >= 900):
            now -= 900
            strg += "CM"
        while(now >= 500):
            now -= 500
            strg += 'D'
        if(now >= 400):
            now -= 400
            strg += 'CD'
        while(now >= 100):
            now -= 100
            strg += 'C'
        if(now >= 90):
            now -= 90
            strg += 'XC'
        while(now >= 50):
            now -= 50
            strg += 'L'
        if(now >= 40):
            now -= 40
            strg += 'XL'
        while(now >= 10):
            now -= 10
            strg += 'X'
        if(now == 9):
            now -= 9
            strg += 'IX'
        while(now >= 5):
            now -= 5
            strg += 'V'
        if(now == 4):
            now -= 4
            strg += 'IV'
        while(now >= 1):
            now -= 1
            strg += "I"
        return roman(strg)
    
t, r1, r2 = input().split()
a = roman(r1); b = roman(r2)
if t == '1' : print(a < b)
elif t == '2' : print(int(a),int(b))
elif t == '3' : print(str(a),str(b))
elif t == '4' : print(int(a + b))
else : print(str(a + b))
