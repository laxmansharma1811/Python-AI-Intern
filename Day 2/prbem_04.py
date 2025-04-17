class Calculator:

    def __init__(self, number):
        self.number = number

    
    def square(self):
        square_number = self.number * self.number
        print(f'The square number is {square_number}')

    def cube(self):
        cube_number = self.number ** 3
        print(f'The cube number is {cube_number}')

    def square_root(self):
        print(f'The square root of number is {self.number ** 1/2}')

    @staticmethod
    def greet():
        print('Hello! How are you?')
        


square = Calculator(10)
cube = Calculator(10)
square_root = Calculator(4)
greet = Calculator.greet()

square.square()
cube.cube()
square_root.square_root()

        