import datetime

print("Check if its Tuesday!")

today = datetime.datetime.today()
day_of_week = today.weekday()

if day_of_week == 1:
  print("its Tueday")
else:
  print("Its not Tuesday")

