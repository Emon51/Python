class Animal: #Base class or supper class.
    def __init__(self, name):
        self.name = name

    def eat(self):
        print(self.name, " is eating.")
#========================================================================================================================#
class Dog(Animal): #Child class or subclass or drived class.
    def bark(self):
        print(self.name, "is barking.")

#========================================================================================================================#

a1 = Animal("Jack")
d1 = Dog("Rover")
d1.eat()
d1.bark()
a1.eat()
#a1.bark() #Error: Animal' object has no attribute 'bark'.

#isinstance(object, className)
#issubclass(class1, class2)

#print(isinstance(a1, Animal)) #True
#print(isinstance(a1, Dog)) #False

#print(issubclass(Dog, Animal)) #True
#print(issubclass(Animal, Dog)) #False


