class Animal:
    def __init__(self,name,sound="grrrr"):
        self.name = name
        self.sound = sound

    def make_noise(self):
        print("{} says, {}".format(self.name, self.sound))

class Dog(Animal):
    def __init__(self,name):
        super().__init__(name,sound="woofff!!!")

class Cat(Animal):
    def __init__(self,name,sound):
        super().__init__(name,sound)

d1 = Dog("jango")
c1 = Cat('billi','meow')

c1.make_noise()


d1.make_noise()