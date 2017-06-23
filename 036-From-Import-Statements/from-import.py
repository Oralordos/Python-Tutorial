import sys
from random import choice

print('How many guesses can you get right?')
correct = 0
while True:
    c = None
    while c == None:
        print('Pick Heads (1) or Tails (2)')
        i = input()
        if i == '1':
            c = 'Heads'
        elif i == '2':
            c = 'Tails'
    rand = choice(['Heads', 'Tails'])
    if rand == c:
        correct = correct + 1
        print('That is correct!')
    else:
        print('That is incorrect\nYou got {} guess{} correct'.format(correct, 'es' if correct != 1 else ''))
        sys.exit()
