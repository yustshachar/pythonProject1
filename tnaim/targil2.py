num=int(input("enter number: "))

if 100<=num<=999:
    print((num//100)+(num//10%10)+(num%10))
else:
    print("error")
