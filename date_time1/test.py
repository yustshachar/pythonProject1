from datetime import *

d1=int(input("enter day 1: "))
m1=int(input("enter month 1: "))
y1=int(input("enter year 1: "))
print("******************")
d2=int(input("enter day 2: "))
m2=int(input("enter month 2: "))
y2=int(input("enter year 2: "))

day1=datetime(y1,m1,d1).date()
day2=datetime(y2,m2,d2).date()

while day2>day1:
    day1+=timedelta(days=1)
    print(day1)

# בדיקה לגיט
