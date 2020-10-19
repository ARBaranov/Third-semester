class Animal:
    def __init__(self, name, age, vid):
        self.name = name
        self.age = age
        self.vid = vid
class Zebra(Animal):
    def Description(self):
        a = (self.name, self.age, self.vid)
        return a
class Dolphin(Animal):
    def Description(self):
        b = (self.name, self.age, self.vid)
        return b

a = Zebra(str(input()), int(input()), str(input()))
b = Dolphin(str(input()), int(input()), str(input()))

print(a.Description(), b.Description())

