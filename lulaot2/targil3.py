num=int(input("enter number: "))
# print((12345%10))
sum = (num % 10)
for i in range(num):
    num=num//10
    sum+=(num%10)
print(sum)