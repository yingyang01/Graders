strg = input()
temp = ""
for c in strg:
    if(c == '('):
        temp += '['
    elif(c == ')'):
        temp += ']'
    elif(c == '['):
        temp += '('
    elif(c == ']'):
        temp += ')'
    else:
        temp += c
print(temp)