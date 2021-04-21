from datetime import *
dd=int(input("enter number day: "))
nn=int(datetime.now().strftime("%w"))+1
# print(dd)
# print(nn)
print((datetime.now().date())+(timedelta(days=dd-nn)))
