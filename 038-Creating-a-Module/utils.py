def add(*vals):
    '''Adds vals together, returns sum

This function takes in as many numbers
as you want and sums them, it returns
the total sum of all of the numbers'''
    s = 0
    for v in vals:
        s = s + v
    return s

def sayName(name):
    'A function which prints hello and a name'
    print('Hello {}'.format(name))
