dd=int(input("enter day: "))
mm=int(input("enter month: "))
yy=int(input("enter year: "))

while 1<=dd<=31 and 1<=mm<=12 and 1950<=yy<=2025:
    if dd<10:
        dd="0"+str(dd)
    if mm<10:
        mm="0"+str(mm)
    yy=yy%100
    if yy<10:
        yy="0"+str(yy)

    print(f"{dd}/{mm}/{yy}")

    dd = int(input("enter day: "))
    mm = int(input("enter month: "))
    yy = int(input("enter year: "))

if dd<1 or dd>31:
    print("day error")
if mm<1 or mm>12:
    print("month error")
if yy<1950 or yy>2025:
    print("year error")