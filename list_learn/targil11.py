list1=[1,1]
a=0
b=1
while b<10:
    list1+=[list1[a]+list1[b]]
    a+=1
    b+=1
print(list1)