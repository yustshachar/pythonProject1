
list1=[1,2,3,4,5,6,7,8,9,10]
list2=list1[-3:]
print(list2)

print(list1[-1::-1])

print(list1[2::2])

list3=list1[:5]
print(list3)

print(list1[1::2])

num=int(input("enter number: "))
# list1[7:]=[num]
# print(list1)
list1[-3:]=[num]
print(list1)