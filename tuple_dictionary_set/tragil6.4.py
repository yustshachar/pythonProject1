from random import randint

numbers=[]

for i in range(10):
    numbers+=[randint(1,100)]
print(numbers)

tup_num=tuple(numbers)
print(tup_num)

tup_num+=(int(input("enter number to add: ")),)
print(tup_num)

new_tup=(tup_num[:4])+(tup_num[-4:])
print(new_tup)

tup_del=new_tup[1:]
print(tup_del)



