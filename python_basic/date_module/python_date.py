import datetime
 # print current year
now = datetime.datetime.now()

year = now.strftime("%Y")

print("year: ", year)