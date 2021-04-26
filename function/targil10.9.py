def sum_zugi(list1):
    sum=0
    for i in list1:
        if i%2==0:
            sum+=i
    return sum



print(sum_zugi([2,3,4,5,6,7,8,9]))