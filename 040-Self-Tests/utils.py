def add(*vals):
    '''Adds vals together, returns sum

This function takes in as many numbers
as you want and sums them, it returns
the total sum of all of the numbers'''
    s = _favoriteNumber
    for v in vals:
        s = s + v
    return s

def sayName(name):
    'A function which prints hello and a name'
    print('Hello {}'.format(name))

_favoriteNumber = 42

print('Module name is: {}'.format(__name__))

def _run():
    print('add(3, 4, 5, 6) == {}'.format(add(3, 4, 5, 6)))

if __name__ == '__main__':
    _run()
