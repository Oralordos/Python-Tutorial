person = {}
print('What is your name?')
person['name'] = input()
print('How old are you?')
age = input()
if not age.isdigit():
    print('That is not a number')
else:
    person['age'] = int(age)
    print('How tall are you in inches?')
    height = input()
    if not height.isdigit():
        print('That is not a number')
    else:
        person['height'] = int(height)
        print('What do you want to see?')
        choice = input()
        print(person.get(choice, 'Invalid item'))
