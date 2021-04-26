dic1={"moshe":40, "dani":80, "maya":60, "shay":95}


dic2={}
# a=list(dic1.items())
# for i in a:
#     # dic2.update({i[1]:i[0]})
#     dic2[i[1]]=i[0]
# print(dic2)

# ============================
for key in dic1:
    dic2[dic1[key]]=key
print(dic2)