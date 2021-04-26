dic1={1: 1, 2: 4, 3: 9, 4: 16, 5: 25}
value1=list(dic1.values())
key1=list(dic1.keys())
sum=0

for i in range(len(dic1)):
    sum+=value1[i]+key1[i]

print(sum)
