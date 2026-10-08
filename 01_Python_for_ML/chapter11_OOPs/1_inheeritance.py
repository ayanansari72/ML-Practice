class Scammer:
    company = "Chetto fund"

    def __init__(self, name, scam_id):
        self.name = name
        self.scam_id = scam_id

    def abc(self):
        print(f"Scammer name: {self.name}, ID: {self.scam_id}, Company: {self.company}")


class Scammer2(Scammer):
    company = "2 din me paisa double"

    def bank(self):
        print(f"Bank Name: {self.name}, Company: {self.company}")


# Objects
a = Scammer("Nirav Modi", 101)
b = Scammer2("Malamaal Bank", 202)

# Method calls
a.abc()
b.abc()
b.bank()
 