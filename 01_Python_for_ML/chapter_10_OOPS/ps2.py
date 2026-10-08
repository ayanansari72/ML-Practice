class Calculator:
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @staticmethod
    def add(a, b):
        return a + b

    @staticmethod
    def subtract(a, b):
        return a - b

    def multiply(self):
        return self.x * self.y

    def divide(self):
        if self.y == 0:
            return "Error: Division by zero"
        return self.x / self.y


x = int(input("Enter x: "))
y = int(input("Enter y: "))

ayanu = Calculator(x, y)

print("Addition:", Calculator.add(x, y))
print("Subtraction:", Calculator.subtract(x, y))
print("Multiplication:", ayanu.multiply())
print("Division:", ayanu.divide())

