class Card:
    def __init__(self, value, suit):
        self.value = value
        self.suit = suit

    def __str__(self):
        return '('+self.value+' '+self.suit+')'
    
    def next1(self):
        dicts = {"club":0, "diamond":1, "heart":2, "spade":3}
        rev_dicts = {value:key for key, value in dicts.items()}
        order = {str(i):i for i in range(3, 11)}
        order['J'] = 11; order['Q'] = 12; order['K'] = 13; order['A'] = 14; order['2'] = 15
        rev_order = {value:key for key, value in order.items()}
        val = order[self.value]; sui = dicts[self.suit]
        sui += 1
        if(sui > 3):
            val += 1
            sui -= 4
            if(val > 15):
                val = 3
        return Card(rev_order[val], rev_dicts[sui])
    
    def next2(self):
        dicts = {"club":0, "diamond":1, "heart":2, "spade":3}
        rev_dicts = {value:key for key, value in dicts.items()}
        order = {str(i):i for i in range(3, 11)}
        order['J'] = 11; order['Q'] = 12; order['K'] = 13; order['A'] = 14; order['2'] = 15
        rev_order = {value:key for key, value in order.items()}
        self.value = order[self.value]; self.suit = dicts[self.suit]
        self.suit += 1
        if(self.suit > 3):
            self.value += 1
            self.suit -= 4
            if(self.value > 15):
                self.value = 3        
        self.value = rev_order[self.value]
        self.suit = rev_dicts[self.suit]

n = int(input())
cards = []
for i in range(n):
    value, suit = input().split()
    cards.append(Card(value, suit))
for i in range(n):
    print(cards[i].next1())
print("----------")
for i in range(n):
    print(cards[i])
print("----------")
for i in range(n):
    cards[i].next2()
    cards[i].next2()
    print(cards[i])
