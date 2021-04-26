

def len1(list1):
    count=0
    for i in list1:
        count+=1
    return count

def count1(list1,num):
    count=0
    for i in list1:
        if i == num:
            count+=1
    return count

def find1(list1,num,start=0):
    for i in range(start,len1(list1)+1):
        if list1[i]==num:
            return i

def max1(list1):
    max=list1[0]
    for i in list1:
        if i>max:
            max=i
    return max

def list1(k):
    list1=[]
    for i in k:
        list1.append(i)
    return list1

def remove1(list1,num):
    for i in list1:
        if i == num:
            del list1[list1.index(num)]




ll=[10,20,30,40,50,60]
print(ll)
remove1(ll,20)
print(ll)
