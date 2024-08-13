strg = input().lower()
vowel = ['a', 'e', 'i', 'o', 'u']
if(strg[-1] == "s" or strg[-1] == "x" or strg[-2::1] == "ch"):
    print(strg+"es")
elif(strg[-1] == "y" and not(strg[-2] in vowel)):
    print(strg[:-1:1]+"ies")
else:
    print(strg+"s")