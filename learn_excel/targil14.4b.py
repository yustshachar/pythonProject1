from openpyxl import *

xl=load_workbook("Login.xlsx")
ss=xl.active

print("name sheet:", ss.title)

for i in ss["A"]:
    print(i.value)
for i in ss["B"]:
    print(i.value)
