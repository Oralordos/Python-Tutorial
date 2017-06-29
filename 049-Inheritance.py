class Animal:
    def __init__(self, name):
        self.name = name

    def sayHello(self):
        pass

class Snake(Animal):
    def sayHello(self):
        print('SSSSSssss')

class Dog(Animal):
    def sayHello(self):
        print('Bark!')

class Person(Animal):
    def __init__(self, name, age):
        super().__init__(name)
        self.age = age

    def sayHello(self):
        print('Hello, my name is {}'.format(self.name))

s = Snake('Kaa')
d = Dog('Rover')
p = Person('Jeff', 28)

animals = [s, d, p]
for a in animals:
    a.sayHello()
