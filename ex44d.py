class Parent(object):

    def override(self):
        print("PARENT override()")

    def implicit(self):
        print("PARENT implicit")

    def altered(self):
        print("PARENT altered()")

class Child(Parent):

    def override(self):
        print("CHILD override")

    def altered(self):
        print("CHILD, BEFORE PARENT altered")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered()")

dad = Parent()
son = Child()

dad.implicit() #Not override, base class
son.implicit() #Not override

dad.override() #Not override, base class
son.override() #Override

dad.altered() #Not override, base class
son.altered() ##Not override, then override
