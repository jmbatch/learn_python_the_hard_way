

class Parent(object):

    def implicit(self):
        print("\nPARENT implicit()\n")

    def override(self):
        print("\nPARENT override()\n")

    def altered(self):
        print("\nPARENT altered()\n")

class Child(Parent):
    pass

    def override(self):
        print("\nCHILD override()\n")

    def altered(self):
        print("CHILD, BEFORE PARENT altered")
        super(Child, self).altered()
        print("CHILD, AFTER PARENT altered")


dad = Parent()
son = Child()

dad.implicit()
son.implicit()

dad.override()
son.override()

dad.altered()
son.altered()
