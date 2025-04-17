import random

class Airplane:
    Airline_name = "Buddha Airline"
    seat = 20
    
    def __init__(self, planeNo):
        self.planeNo = planeNo

    
    def book_ticket(self, passenger_name, price, fro, to):
        print(f'PlaneNo: {self.planeNo}\nName: {passenger_name}\nPrice: {price}\nFrom {fro} to {to}')


    def get_status(self):
        print(f'{Airplane.Airline_name} is flying on time.')

    
    def get_fare(self):
        print(f'The fare of Buddha Airline is {5500}.')


a = Airplane(random.randint(1200, 5555))

a.book_ticket("Laxman Sharma", 5500, "Kathmandu", "Pokhara")
a.get_status()
a.get_fare()


