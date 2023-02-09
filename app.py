class Animal:
    def __init__(self,name,sound="grrrr"):
        self.name = name
        self.sound = sound

    def make_noise(self):
        print("{} says, {}".format(self.name, self.sound))

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,sound="woofff!!!")

d1 = Dog("jango")

d1.make_noise()