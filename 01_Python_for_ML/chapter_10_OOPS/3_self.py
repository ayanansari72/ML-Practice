class Employee: 
    language = "Python" # This is a class attribute
    salary = 1200000

    def getInfo(self):
        print(f"The language is {self.language}. The salary is {self.salary}")

    @staticmethod #decorator(not need to pass self)
    def greet():
        print("Good morning")


ayanu= Employee()
# ayanu.language = "JavaScript" # This is an instance attribute
ayanu.greet()
ayanu.getInfo() 
# Employee.getInfo(ayanu)  # This is another way to call the method