def over(grade):
    if 70<=grade<=100:
        return True
    else:
        return False



for i in range(5):
    if over(int(input("enter grade: "))):
        print("yes")
    else:
        print("no")
