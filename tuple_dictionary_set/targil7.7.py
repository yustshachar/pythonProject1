dic1={"moshe":60, "dani":80, "maya":60, "shay":95}
dic_new={}

for i in dic1:
    if dic1[i] not in dic_new.values():
        dic_new[i]=dic1[i]
print(dic_new)
