class piggybank:
    def __init__(self):
        self.coins = {}

    def add(self, v, n):
        total = 0
        for key in self.coins:
            total += self.coins[key]
        if(n+total > 100):
            return False
        if(float(v) not in self.coins):
            self.coins[float(v)] = n
        else:
            self.coins[float(v)] += n
        return True
    
    def __float__(self):
        sgm = 0.0
        for key in self.coins:
            sgm += key*self.coins[key]
        return sgm
    
    def __str__(self):
        strg = "{"
        ok = 0
        lists = []
        for key in self.coins:
            ok = 1
            lists.append((key, self.coins[key]))
        if(not(ok)):
            return "{}"
        lists.sort()
        for key, value in lists:
            strg += str(key)+':'+str(value)+", "
        return strg[:-2:1]+'}'
    
cmd1 = input().split(';')
cmd2 = input().split(';')
p1 = piggybank(); p2 = piggybank()
for c in cmd1: eval(c)
for c in cmd2: eval(c)
