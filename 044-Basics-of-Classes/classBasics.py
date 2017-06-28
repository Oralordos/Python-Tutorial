class Person:
    name = ''

    def sayName(self, otherText):
        print(self.name + otherText)

p = Person()
p.name = 'Bob'
l = Person()
l.name = 'Joe'

p.sayName(' says hi!')
l.sayName('')
