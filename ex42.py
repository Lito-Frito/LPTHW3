## Animal is-a object
class Animal(object):
    pass

## Dog is-a animal
class Dog(Animal):

    def __init__(self, name):
        ## Dog has-a name
        self.name = name

## Cat is-a animal
class Cat(Animal):

    def __init__(self, name):
        ##Cat has-a name
        self.name = name

## Person is-a object
class Person(object):

    def __init__(self,name):
        ## Person has-a name
        self.name = name

        ## Person has-a pet of some kind
        self.pet = None

        ## something to practice with OOP
        self.song = f"{name} has a little "

## Employee is-a Person
class Employee(Person):

    def __init__(self, name, salary):
        ## Employee is-a child class that inherits from Person
        super(Employee, self).__init__(name) #run the __init__ function from Person() with name param
        ## Employee has-a salary
        self.salary = salary

## Fish is-a object
class Fish(object):
    pass

## Salmon is-a Fish
class Salmon(Fish):
    pass

## Halibut is-a Fish
class Halibut(Fish):
    pass


## rover is-a Dog
rover = Dog("Rover")

## satan is a Cat
satan = Cat("Satan")

## mary is-a Person
mary = Person("Mary")

## Mary is-a Person and has-a Pet named Satan
mary.pet = satan

## frank is-a employee and has-a 120,000
frank = Employee("Frank", "$120,000")

## Frank has-a pet named Rover
frank.pet = rover

## Flipper is-a Fish
flipper = Fish()

## crouse is-a Salmon? Idk what crouse means in this context
crouse = Salmon()

## harry is-a Halibut
harry = Halibut()
print(rover.name)
print(mary.name)
print(crouse)
print(mary.song + mary.pet.name) #This line does two things. 1) It cats the two things I want to print (name.song & pet's name).
                                 #2) It goes to Mary which is-a Person class, which means it has-a song parm and prints it
                                 #Then it Goes to Mary again which is-a Person class, which means it has-a Pet and sees it is
                                 #set to satan. And satan is-a Cat, meaning it has-a name, and it prints that name
print(frank.song + frank.pet.name)
print(frank.song + frank.salary)
