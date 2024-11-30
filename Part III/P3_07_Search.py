class Document:
    def __init__(self, name, doc):
        self.name = name
        self.doc = doc.split()
        s = set()
        for each in self.doc:
            s.add(each)
        self.unique = 1/len(s)
    
    def calculateRelevant(self, want):
        rel = 0
        f = 0
        for each in self.doc:
            if(each == want):
                f += 1
        return f/len(self.doc)*self.unique

n = int(input())
lists = []
for i in range(0, n, 1):
    name = input()
    doc = input()
    lists.append(Document(name, doc))
while(1):
    x = input()
    if(x == "-1"):
        break
    mx = 0
    name = ""
    for obj in lists:
        if(obj.calculateRelevant(x) > mx):
            mx = obj.calculateRelevant(x)
            name = obj.name
    if(mx == 0):
        print("NOT FOUND")
    else:
        print(name)