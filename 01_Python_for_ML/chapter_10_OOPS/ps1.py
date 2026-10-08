class Programmer:
    company = "Microsoft"
 
    def __init__(self, name, language):
        self.name = name
        self.language = language
 
    def getInfo(self):
        print(f"The name is {self.name}. The language is {self.language}")  

ayanu = Programmer("Ayan", "Python")
ayanu.getInfo()
print(ayanu.company)

ayaz = Programmer("Ayaz", "JavaScript")
ayaz.getInfo()
print(ayaz.company)