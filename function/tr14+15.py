def grades(count):
    grade=[]
    for i in range(count):
        grade.append(int(input("enter geade: ")))
    return grade

def memutza(list1):
    return sum(list1)/len(list1)


num1=int(input("enter count students: "))
ggg=grades(num1)
print(ggg)
print("ממוצע:", memutza(ggg))