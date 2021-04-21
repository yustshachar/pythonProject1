num=int(input("enter number: "))
if num > 0:
    low = num
num = int(input("enter number: "))

while num!=0:
    if num<low and num>0:
        low=num
    num=int(input("enter number: "))
else:
    print(low)
