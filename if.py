import datetime

print ("Check if it's Tuesday, Wednesday or other!")

today = datetime.datetime.today()
day_of_week = today.weekday()

if day_of_week == 1:
    print ("It's Tuesday")
elif day_of_week == 2:
    print ("It's Wednesday")
else:
    print ("It's not Tuesday or Wednesday")