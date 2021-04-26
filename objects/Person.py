#name, age, children

class Person:

    def print(self):
        print(f"name: {self.name}, age: {self.age}, child: {self.children}")

    def hasChildren(self):
        if self.children>0:
            return True
        else:
            return False

    def ageGroup(self):
        if 0<=self.age<=18:
            return "Child"
        elif 19<=self.age<=60:
            return "Adult"
        elif 61<=self.age<=120:
            return "Senior"


adam1=Person()

adam1.name="yaniv"
adam1.age=43
adam1.children=2

adam1.print()

if adam1.hasChildren():
    print("has children")
else:
    print("has not children")

print(adam1.ageGroup())
