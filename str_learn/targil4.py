word1=input("enter word 1: ")
word2=input("enter word 2: ")
count=0
str1=""

for i in word1:
    if i in word2:
        if i not in str1:
            str1+=i
print(len(str1))
