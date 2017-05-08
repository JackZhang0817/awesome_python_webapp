class Animal(object):
    def run(self):
        print('Animal is running....')
class Dog(Animal):
    pass
dog = Dog()
dog.run()