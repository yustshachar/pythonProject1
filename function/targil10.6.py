def f2(str1):
    count = 0
    countb = 0
    for i in str1:
        if i.isupper():
            count += 1
        else:
            countb += 1
    print("count of upperletter", count)
    print("count of lowerletter", countb)



f2("Banana Sababa")