class Animal(object):
    def __init__(self, name):
        self.name = name

    def make_sound(self):
        print("General animal sound!")

class Dog(Animal):
    def __init__(self, name, color):
        super().__init__(name)
        self.color = color

    def make_sound(self):
        print("i am d0gg0 woof")

    def __str__(self):
        return "Hi my name is {} and I'm a {} dog!".format(self.name, self.color)


class Cat(Animal):
    def __init__(self, name, color, personality):
        super().__init__(name)
        self.color = color
        self.personality = personality

    def meow(self):
        print("gib me food h00man")


def main():
    a = Dog("Alfred", "Black")
    c = Cat("Mr. bojangles", "brown", "sneaky")
    a.make_sound()
    print(a)
    c.meow()

main()

