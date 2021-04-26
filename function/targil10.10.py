def rev(str1):
    str2=""
    if " " in str1:
        str1=str1.replace(" ","")
    for i in range(len(str1)-1,-1,-1):
        str2+=str1[i]
    if str1==str2:
        return True
    else:
        return False

    # if str1==str1[::-1]: pass


print(rev("banab"))
