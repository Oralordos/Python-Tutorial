print('Give me a number')
myNumber = int(input())

if myNumber > 1000:
    print('This is too big')
elif myNumber < 0:
    print('I want a positive number')
elif myNumber == 42:
    print('That is the meaning of life')
elif myNumber > 100:
    print('This is a fairly big number')
else:
    print('This number is pretty generic')
