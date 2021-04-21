from datetime import *

name=input("what your name? ")
age=int(input("what your age? "))

now_year=datetime.now().strftime("%Y")
more=100-age
print(name,"whill be 100 in", int(now_year)+more)
