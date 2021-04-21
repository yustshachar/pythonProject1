grade=int(input("enter grade: "))
num=1
count=0
ave=0
numn=1
countn=0
aven=0
while 0<=grade<=100:
    if grade>60:
        count+=grade
        ave=count/num
        num += 1
    else:
        countn+=grade
        aven=countn/numn
        numn += 1
    print(f"yes: {ave}, no: {aven}")
    grade = int(input("enter grade: "))
