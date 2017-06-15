def addNumbers(x, y):
    return x + y

def getNext(current):
    if current == 'a':
        return 'b'
    else:
        return 'a'

def setItem(dataStructure, index, value):
    dataStructure[index] = value

def z(x):
    x = 25

x = addNumbers(5, 10)
print(x)
print(addNumbers(10, 10))

val = getNext('a')

l = [1,2,3,4]
setItem(l, 2, val)
print(l)

b = 12
z(b)
print(b)
