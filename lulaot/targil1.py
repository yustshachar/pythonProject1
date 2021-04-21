num=int(input("enter nuber: "))

while 100<=num<=999:
    print(int(num/100)+(int(123%100/10))+(num%10))
    num = int(input("enter nuber: "))

print("error")
