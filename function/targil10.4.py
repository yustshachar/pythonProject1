def reverse(str1):
    str2=""
    for i in range(len(str1)-1,-1,-1):
        str2+=str1[i]
    print(str2)



aaa="abcd1234"
reverse(aaa)