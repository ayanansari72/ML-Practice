class Employee:
    name="Ayan"
    language="Python"
    salary=50000

ayanu=Employee() #creating an object of Employee class
print(ayanu.name)
print(ayanu.language)
print(ayanu.salary)
ayanu.salary=60000 #instance variable /attribute
print(ayanu.salary) #here instance variable will be printed
print(Employee.salary) #printing class variable/attribute
ayanu.name="Rony"
print(ayanu.name)
print(Employee.name)    