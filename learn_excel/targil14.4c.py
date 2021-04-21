from openpyxl import *

xl=load_workbook("Login.xlsx")
ss=xl.active

for i in ss.iter_rows(min_row=1, max_row=3,min_col=1,max_col=2, values_only=True):
    for c in i:
        print(c)