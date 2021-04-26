def seder_ole(num1,num2):
    for i in range(num1,num2+1):
        print(i,end=" ")

def big(num1,num2):
    if num1>=num2:
        return num1
    else:
        return num2

def small(num1,num2):
    if num1<=num2:
        return num1
    else:
        return num2

num1=int(input("enter number 1: "))
num2=int(input("enter number 2: "))
b=big(num1,num2)
s=small(num1,num2)
seder_ole(s,b)