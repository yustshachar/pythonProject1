dd=int(input("enter day: "))
mm=int(input("enter month: "))
yy=int(input("enter year: "))

if 1<=dd<=31:
    if 1<=mm<=12:
        if 1950<=yy<=1999 or 2010<=yy<=2020:
            print(f"{dd}/{mm}/{yy%100}")
        if 2000<=yy<=2009:
            print(f"{dd}/{mm}/0{yy % 100}")
        if 1950>yy<2020:
            print("year error")
    else:
        print("month error")
else:
    print("day error")

# לא מצליח לעשות בשנה מעל 2000 שני ספרות