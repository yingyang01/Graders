strg = input()
if(len(strg) != 10):
    print("Not a mobile number")
else:
    if(strg[:2] == "06" or strg[:2] == "08" or strg[:2] == "09"):
        print("Mobile number")
    else:
        print("Not a mobile number")