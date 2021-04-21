list1=[1,2,3,4,5,6,7,8,9,10]

list2=list1.copy()
for i in list2:
    if i%3==0:
        list1.remove(i)
print(list1)


# for i in range(len(list1)):
#     if list1[1]%3==0:
#         list1.remove(i)
# print(list1)