def hezka(num1,kefel):
    num2=num1
    for i in range(kefel-1):
        num2*=num1
    return num2

num1=int(input("enter number: "))
num2=int(input("enter hezka: "))
print(hezka(num1,num2))