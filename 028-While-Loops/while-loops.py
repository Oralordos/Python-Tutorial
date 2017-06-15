number = 0
while number == 0:
    print('Enter a number')
    x = input()
    if x.isdigit():
        number = int(x)
else:
    print('Success')
print('Your number is {}'.format(number))
