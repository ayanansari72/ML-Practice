class Employee:
    language = "Python"  # This is a class attribute
    salary = 1200000    

    def __init__(self,name , salary,language):  # constructor
        print("Constructor called")
        self.name = name  # instance attribute
        self.salary = salary
        self.language = language
    def getInfo(self):
        print(f"The name is {self.name}. The language is {self.language}. The salary is {self.salary}")

    @staticmethod  # decorator(not need to pass self)
    def greet():
        print("Good morning")    

ayanu = Employee("Ayan", 50000, "Python")
print(ayanu.name)
print(ayanu.salary)
print(ayanu.language)


ayaz= Employee("Ayaz", 60000, "JavaScript")
print(ayaz.name)
print(ayaz.salary)
print(ayaz.language)
