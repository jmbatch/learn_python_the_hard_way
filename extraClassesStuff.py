class GeekforGeeks:
 
    def __init__(self):
        self.geek = "GeekforGeeks"
 

    def print_Geek(self):
        print(self.geek)
 

class Addition:
    first = 0
    second = 0
    answer = 0

    # parameterized constructor
    def __init__(self, f, s):
        self.first = f
        self.second = s

    def display(self):
        print("first number = " + str(self.first))
        print("second number = " + str(self.second))
        print("Addition of two numbers = " + str(self.answer))

    def calculate(self):
        self.answer = self.first + self.second



print("This is a default constructor:")
obj = GeekforGeeks()
obj.print_Geek()


print("\nThis is a parametized constructor: ")
obj = Addition( 10, 1000)
obj.calculate()
obj.display()
