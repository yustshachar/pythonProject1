num = int(input("enter a number: "))
reversed = 0
while(num!= 0):
    r=int(num%10)
    reversed = reversed*10 + r
    num=num//10
print(reversed)
print(reversed*2)