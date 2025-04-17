class Programmer:
    company = "Esewa"

    def __init__(self, name:str, address:str, salary:int):
        self.name = name
        self.address = address
        self.salary = salary

obj = Programmer("Laxman", "Samakhusi", 10000)

print(obj.name, obj.address, obj.salary, obj.company)

print(obj.company)
        