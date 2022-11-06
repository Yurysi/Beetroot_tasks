"""
Method overloading.

Create a base class named Animal with a method called talk and then create two
subclasses: Dog and Cat, and make their own implementation of the method talk
be different. For instance, Dog’s can be to print ‘woof woof’, while Cat’s can
be to print ‘meow’.

Also, create a simple generic function, which takes as input instance of a Cat
or Dog classes and performs talk method on input parameter.
"""


class Animal:

    def talk(self):
        return "I don't know who says"

class Cat(Animal):

    def talk(self):
        return f'meow'


class Dog(Animal):
    def talk(self):
        return 'woof woof'


def makeSound(animal_type):
    return animal_type.talk()


pet = Cat()
pet2 = Dog()
print(makeSound(pet))
print(makeSound(pet2))
# makeSound(pet)
