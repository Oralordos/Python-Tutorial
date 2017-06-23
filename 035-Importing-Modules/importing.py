import random, time, sys

print('It is currently {}'.format(time.ctime()))
time.sleep(2)
num = random.randint(1, 10)
print('Your lucky number is {}'.format(num))
time.sleep(2)
if num == 4:
    print('That is not lucky')
    sys.exit()
print('You should try using it in a guessing game!')
