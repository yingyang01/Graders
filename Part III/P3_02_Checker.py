def isValidRow(char):
    if(len(char) > 1 or len(char) == 0):
        return False
    if(('a' <= char <= 'z') or ('A' <= char <= 'Z')):
        return True
    return False

def isValidColumn(char):
    if(len(char) == 0 or len(char) > 2):
        return False
    ok = ('0' <= char[0] <= '9') and ('0' <= char[-1] <= '9')
    if(ok):
       char = int(char)
       if(1 <= char <= 52):
           return True
       else:
           return False 
    return False

position = input().strip()
alpha = "abcdefghijklmnopqrstuvwxyz"
alpha += alpha.upper()
if(len(position) <= 3):
    if(not(isValidRow(position[0])) and not(isValidColumn(position[1::].strip()))):
        print("Invalid row and column")
    elif(not(isValidRow(position[0]))):
        print("Invalid row")
    elif(not(isValidColumn(position[1::].strip()))):
        print("Invalid column") 
    else:
        col = int(position[1::].strip())
        row = alpha.find(position[0])
        if((row+col)%2 == 1):
            print("White")
        else:
            print("Black")
else:
    pos1 = position.find("=")
    pos2 = position.find(",")
    f = position[pos1+1:pos2:1].strip()
    s = position[position.find("=", pos1+1)+1::].strip()
    if(position.find("row") > position.find("col")):
        f, s = s, f
    if(not(isValidRow(f)) and not(isValidColumn(s))):
        print("Invalid row and column")
    elif(not(isValidRow(f))):
        print("Invalid row")
    elif(not(isValidColumn(s))):
        print("Invalid column") 
    else:
        col = int(s)
        row = alpha.find(f)
        if((row+col)%2 == 1):
            print("White")
        else:
            print("Black")