class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '('+self.value+' '+self.suit+')'
    
    def getScore(self):
        if(self.value in "JQK"):
            return 10
        elif(self.value == 'A'):
            return 1
        return int(self.value) 
    
    def sum(self, other):
        return (self.getScore()+other.getScore())%10
    
    def __lt__(self, rhs):
        if(self.value != rhs.value):
            return self.getOrder() < rhs.getOrder()
        dicts = {"club":0, "diamond":1, "heart":2, "spade":3}
        return dicts[self.suit] < dicts[rhs.suit]
    
    def getOrder(self):
        if(self.value == 'A'):
            return 14
        elif(self.value == '2'):
            return 15
        elif(self.value == 'J'):
            return 11
        elif(self.value == 'Q'):
            return 12
        elif(self.value == 'K'):
            return 13
        return self.getScore()

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].getScore())
print("----------")
for i in range(n-1):
     print(Card.sum(cards[i], cards[i+1]))
print("----------")
cards.sort()
for i in range(n):
 print(cards[i])
