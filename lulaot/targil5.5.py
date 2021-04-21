grade=int(input("enter grade: "))
num=1
count=0
ave=0
while 0<=grade<=100:
    if grade>60:
        count+=grade
        ave=count/num
        num += 1
    print(ave)
    grade = int(input("enter grade: "))
