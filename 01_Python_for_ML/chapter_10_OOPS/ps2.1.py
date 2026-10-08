import math

class Calculator:
    def __init__(self, n):
        self.n = n

    def square(self):
        print(f"The square is {self.n * self.n}")

    def cube(self):
        print(f"The cube is {self.n * self.n * self.n}")

    def squareroot(self):
        print(f"The square root is {math.sqrt(self.n)}")


n = int(input("Enter n: "))
ayanu = Calculator(n)

# Call the functions
ayanu.square()
ayanu.cube()
ayanu.squareroot()

        


        