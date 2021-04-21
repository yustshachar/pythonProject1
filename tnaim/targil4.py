num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))

if num1<0:
    num1*=(-1)
if num2<0:
    num2*=(-1)

if num1>=num2:
    print(num1-num2)
else:
    print(num2-num1)