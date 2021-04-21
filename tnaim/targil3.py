age=int(input("enter age: "))

if 0<=age<=18:
    print("child")
else:
    if 19<=age<=60:
        print("adult")
    else:
        if 61<=age<=120:
            print("senior")
