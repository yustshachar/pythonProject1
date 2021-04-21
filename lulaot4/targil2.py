num=int(input("enter number: "))
low=1
high=10
count=1
for i in range(num):
    if low<=num<high:
        print(count)
        break
    else:
        low *= 10
        high *= 10
        count += 1