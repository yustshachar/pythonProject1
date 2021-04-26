def sum_num(num1):
    sum=0
    for i in range(1,num1+1):
        sum+=i
    print(sum)



number=int(input("enter number: "))
sum_num(number)