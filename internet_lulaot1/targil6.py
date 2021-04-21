num=int(input("enter number: "))
count=0
while num>=10:
    num=num//10
    count+=1
print(count+1)