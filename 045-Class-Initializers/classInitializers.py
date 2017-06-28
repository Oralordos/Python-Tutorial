class Person:
    def __init__(self, name, age):
        self.name = name
        self.age = age

    def __del__(self):
        print('{} was deleted'.format(self.name))

    def sayHello(self):
        print('Hello, my name is {}'.format(self.name))

p = Person('Bob', 27)
o = Person('Joe', 15)

p.sayHello()
o.sayHello()

p = None
