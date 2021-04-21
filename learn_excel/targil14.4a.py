from openpyxl import *

xl=Workbook("Login.xlsx")
ss=xl.active
xl.save("Login.xlsx")

xl=load_workbook("Login.xlsx")
ss=xl.active

ss["A1"].value="UserName"
ss["B1"]="Password"
ss["A2"]="Tester1"
ss["A3"]="Tester2"
ss["B2"]="1234"
ss["B3"]="45678"

xl.save("Login.xlsx")
