from random import randint

list1=[]
for i in range(20):
    list1.append(randint(1,100))
print(list1)
num=input("enter number: ")
for i in range(len(list1)):
    if list1[i]==num:
        list1.remove(list1[i])