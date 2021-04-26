from random import randint

def rand(list1):
    for i in range(20):
        list1.append(randint(1,100))

def count_num_in_list(num,list1):
    return list1.count(num)


def where_max(list1):
    return list1.index(max(list1))


list1=[]
rand(list1)
print(list1)

num1=int(input("enter number: "))
print(count_num_in_list(num1,list1))

print(where_max(list1))