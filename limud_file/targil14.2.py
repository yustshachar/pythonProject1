# a
# tzair=open("story.txt", "r+")
# count=0
# for i in tzair:
#     if i[0]!="T":
#         count+=1
# tzair.close()
# print(count)


# b
# vatik=open("story.txt", "r+")
# count=0
# for i in vatik:
#     if " the " in i:
#         count+=1
#     if "The " in i:
#         count+=1
# vatik.close()
# print(count)


# d
free=open("story.txt", "r+")
count=0
for i in free:
    words=i.split()
    for c in words:
        count+=1
free.close()
print(count)


