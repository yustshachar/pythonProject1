

class HardDisk:
    def __init__(self,busy=0,files=0):
        self.all=100
        self.busy=busy
        self.files=files
    def print(self):
        print(f"all: {self.all}, busy: {self.busy}, files: {self.files}")
    def freeSpace(self):
        return self.all - self.busy
    def addFile(self, size):
        if (self.busy+size)<=self.all:
            self.busy+=size
            self.files+=1
            return True
        else:
            return False
    def delFile(self, size):
        self.busy-=size
        self.files-=1
        if self.busy<0:
            self.busy=0


disk1=HardDisk()
disk1.print()
for i in range(5):
    disk1.addFile(int(input("enter size file to input: ")))
disk1.print()
disk1.delFile(int(input("enter size file to delete: ")))
disk1.print()