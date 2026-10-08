class Employee:
    company = "Apna Bharat"

    def show(self):
        print(f"The company name is {self.company}")


class Coder(Employee):
    company = "Hamara UP"

    def show1(self):
        print(f"The company name is {self.company}")


class Student(Coder):
    company = "Hamara College"

    def show2(self):
        print(f"This is our college {self.company}")


# Objects
a = Employee()
b = Coder()
c = Student()

# Method calls
c.show()
c.show1()
c.show2()

print(a.Employee())