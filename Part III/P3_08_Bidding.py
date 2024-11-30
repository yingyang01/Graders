class Product:
    def __init__(self, productName):
        self.name = productName
        self.bidder = []

    def bid(self, bidderName, value, order):
        ok = 0
        for i in range(0, len(self.bidder)):
            if(self.bidder[i][2] == bidderName):
                ok = 1
                self.bidder[i][0] = -value
                self.bidder[i][1] = order
                break
        if(not(ok)):
            self.bidder.append([-value, order, bidderName])
        return
    
    def withdraw(self, bidderName):
        # print(bidderName)
        # print(self.bidder)
        for i in range(0, len(self.bidder)):
            if(self.bidder[i][2] == bidderName):
                self.bidder.pop(i)
                break
        # print(self.bidder)
        return

class Bidders:
    def __init__(self, bidderName):
        self.name = bidderName
        self.got = []
        self.total = 0

    def update(self, got, value):
        self.got.append(got)
        self.total += value

    def __lt__(self, rhs):
        return self.name < rhs.name

    def display(bidder):
        print("%s: " %(bidder.name), end = "")
        if(bidder.total == 0):
            print("$0", end = "")
        else:
            print("${} -> ".format(bidder.total), end = "")
            for product in sorted(bidder.got):
                print(product, end = ' ')
        print()

n = int(input())
mp = {}
winners = []
mp_w = {}
order = 0
for i in range(0, n, 1):
    # print("----> %d" %(i))
    ord = input().split()
    if(ord[0] == 'B'):
        ord[3] = int(ord[3])
        if(ord[2] not in mp):
            mp[ord[2]] = Product(ord[2])
        mp[ord[2]].bid(ord[1], ord[3], order)
        order += 1
        if(ord[1] not in mp_w):
            mp_w[ord[1]] = Bidders(ord[1])
            winners.append(mp_w[ord[1]])
    elif(ord[0] == 'W'):
        if(ord[2] in mp):
            mp[ord[2]].withdraw(ord[1])
for product in mp:
    if(len(mp[product].bidder)):
        winner = min(mp[product].bidder)
        mp_w[winner[2]].update(product, -winner[0])
winners.sort()
for winner in winners:
    winner.display()

