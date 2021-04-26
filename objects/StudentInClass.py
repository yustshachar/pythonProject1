# id, name, address, grade

class StudentInClass:
    def over(self):
        if self.grade>=70:
            return True
        else:
            return False

    def updateGrade(self, ahuz=0):
        self.grade+=(self.grade*(ahuz/100))
        if self.grade>100:
            self.grade=100

    def print(self):
        print(f"id: {self.id}, name: {self.name}, address: {self.address}, grade: {self.grade}")


talmid1=StudentInClass()

talmid1.id=123456789
talmid1.name="dani"
talmid1.address="Yafo 15"
talmid1.grade=64

if talmid1.over():
    print("התלמיד עבר בהצלחה")
else:
    print("התלמיד נכשל")


num=int(input("enter ahuz: "))
talmid1.updateGrade(num)

talmid1.print()