class  Animal:
    pass

class Pets(Animal):
    pass

class Dog(Pets):

    @staticmethod
    def bark():
        print('Bark Bark')


obj = Dog()
obj.bark()
