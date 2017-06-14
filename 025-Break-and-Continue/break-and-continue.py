print('Searching for a number')
finalNum = 0
for i in range(1, 10000):
    if i % 5 == 0 and i % 4 == 0 and i % 3 == 0:
        finalNum = i
        break
    if i % 10 != 0:
        continue
    print('Got to {}'.format(i))
print('Number is {}'.format(finalNum))
