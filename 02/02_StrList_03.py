months = ["January", "February", "March", "April", "May", "June", "July", "August", "September", "October", "November", "December"]
date = input().split('/')
print("{month} {day}, {year}".format(month = months[int(date[1])-1], day = date[0], year = date[2]))