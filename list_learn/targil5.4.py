list1=[]
list2=[]

for i in range(5):
    list1+=[int(input("enter number for list 1: "))]

for i in range(5):
    list2+=[int(input("enter number for list 2: "))]

print(list1+list2)
print(len(list1+list2))