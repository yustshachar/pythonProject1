set1={1,2,3,4}
set2={3,4,5,6}

set3=set()
set3.update(set1)
set3.update(set2)
print(set3)

set3.discard(5)
print(set3)

print(max(set3))
print(min(set3))
print(len(set3))

set4=set()
set4.update(set3)
set4.update({5,7})
print(set4)


set1.clear()
set2.clear()
print(set1,set2)