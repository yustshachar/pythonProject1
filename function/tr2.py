def num_3(num1):
    if 99<num1<1000:
        return "חוקי"
    else:
        return "לא חוקי"


print(num_3(int(input("enter number: "))))