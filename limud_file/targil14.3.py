# a
# nahag_hadash=open("story.txt","r+")
# for i in nahag_hadash:
#     print(i,end="")
# nahag_hadash.close()



# b
nahag_hadash=open("story.txt","r+")
count=0
for i in nahag_hadash:
    count+=1
print("lines count:", count)