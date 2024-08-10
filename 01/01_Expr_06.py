hms1 = [0, 0, 0]
hms2 = [0, 0, 0]
for i in range(3):
    hms1[i] = int(input())
for i in range(3):
    hms2[i] = int(input())
second_1 = hms1[0]*3600+hms1[1]*60+hms1[2]
second_2 = hms2[0]*3600+hms2[1]*60+hms2[2]
diff = (second_2-second_1+86400)%86400
print("{hours}:{minutes}:{seconds}".format(hours = diff//3600, minutes = (diff-(diff//3600)*3600)//60, seconds = diff-diff//3600*3600-((diff-diff//3600*3600)//60)*60))