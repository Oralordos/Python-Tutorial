import random
number = random.randint(1, 100)

print('I have thought of a number between 1 and 100. Please attempt to guess it.')
for i in range(6, 0, -1):
    print('Enter a guess ({} guess{} left)'.format(i, 'es' if i != 1 else ''))
    guess = input()
    if not guess.isdigit():
        print('That is not a number')
        continue
    guessNum = int(guess)
    if guessNum == number:
        print('Correct!')
        break
    elif guessNum < number:
        print('Your guess is too low')
    else:
        print('Your guess is too high')
else:
    print('You were unable to guess the number')
    print('The correct answer was {}'.format(number))
