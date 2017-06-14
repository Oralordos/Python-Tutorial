number = 0
print('Enter a number')
for i in range(3):
    num = input()
    if num.isdigit():
        number = int(num)
        break
    print('That is not an integer')
else:
    print('Since you cannot enter a number, I chose 0 for you')
print('Your number is {}'.format(number))
