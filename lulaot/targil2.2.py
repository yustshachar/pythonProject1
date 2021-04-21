sum=0
count=0

for i in range(6):
    num=int(input("enter number: "))
    if num%2==0:
        sum+=num
        count+=1

if count!=0:
    print(f"sum={sum}")
    print(f"evarage={sum/count}")