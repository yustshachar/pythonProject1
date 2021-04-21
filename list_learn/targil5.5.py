grade=input("enter grades: ")
list1=grade.split()
count_over=0
count_lo=0
for i in list1:
     if int(i)>=60:
         count_over+=1
     else:
         count_lo+=1
print("over:", count_over)
print("lo over:", count_lo)