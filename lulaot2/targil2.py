password=input("הכנס סיסמא לאימות: ")
count=0
sisma=input("הכנס סיסמא: ")
# while sisma!=password:
#     sisma = input("הכנס סיסמא: ")
#     count+=1
#     if count==4:
#         print("יותר מידי נסיונות")
#         break
# else:
#     print("סיסמא נכונה")
#

for i in range(4):
    if password==sisma:
        print("סיסמא נכונה")
        break
    else:
        sisma = input("הכנס סיסמא: ")
        count+=1
else:
    print("יותר מידי נסיונות")