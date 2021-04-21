min=0
for i in range(5):
    num = int(input("please enter number: "))
    is_prime = False
    if num<2:
        continue
    else:
        for i in range(2,num):
            if num%i==0:
                break
        else:
            is_prime = True
    if is_prime:
        if min==0:
            min = num
        if num<min:
            min=num
if min == 0:
    print("there wasnt a prime number")
else:
    print(min)