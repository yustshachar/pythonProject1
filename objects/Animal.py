

class Animal:
    def __init__(self,name,hungry=5.0,energy=5.0):
        self.name=name
        self.hungry=hungry
        self.energy=energy

    def toString(self):
        print(self.name,"\nhungry:",self.hungry,"\nenergy:",self.energy)

    def eat(self, food):
        self.hungry-=(food/50)
        if self.hungry<0:
            spear=self.hungry*-1
            self.hungry=0
            print("החיה שבעה ולא סיימה לאכול")
            self.energy-=(food-spear)/100
        else:
            self.energy-=(food/100)
            if self.energy<0:
                self.energy=0

    def play(self,time):
        self.energy-=(time/5)
        spear=0
        if self.energy<0:
            spear=(self.energy*-1)*5
            self.energy=0
            print("המשחק הסתיים כי החיה עייפה")
            self.hungry+=((time-spear)/5)
        else:
            self.hungry += (time / 5)
        if self.hungry>10:
            self.hungry=10

    def rest(self,time):
        self.energy+=(time/20)
        spear=0
        if self.energy>10:
            spear=(self.energy-10)*20
            self.energy=10
            print("החיה סיימה לנוח ורוצה לשחק")
            self.hungry+=((time-spear)/30)
        else:
            self.hungry+=(time/30)
        if self.hungry>10:
            spear=(self.hungry-10)*30
            self.hungry=10
            print("החיה סיימה לנוח ורוצה לאכול")
            self.energy-=((time-spear)/20)


animal1=Animal("riki")
animal1.toString()
while True:
    num=int(input("1-eat, 2-play, 3-sleep, 0-stop "))
    if num==1:
        animal1.eat(int(input("enter gram: ")))
        animal1.toString()
        continue
    if num==2:
        animal1.play(int(input("enter time: ")))
        animal1.toString()
        continue
    if num==3:
        animal1.rest(int(input("enter time: ")))
        animal1.toString()
        continue
    if num==0:
        break




