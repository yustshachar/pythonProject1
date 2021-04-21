grade=int(input("enter grade: "))
high=0
count=0
sum=0

while 0<=grade<=100:
    if grade>high:
        high=grade
        print(f"high grade: {high}")
        sum+=grade
        count+=1
        print(f"average grade: {sum/count}")
        print(f"The difference is: {high-(sum/count)}")
    else:
        print(f"high grade: {high}")
        sum+=grade
        count+=1
        print(f"average grade: {sum/count}")
        print(f"The difference is: {high-(sum/count)}")
    grade = int(input("enter grade: "))
