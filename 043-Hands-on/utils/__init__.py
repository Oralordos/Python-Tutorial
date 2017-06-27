def sayHello(name):
    'A function that takes in a name string and prints a greeting'
    print('Hello {}'.format(name))

def sayGoodbye(name):
    'A function that takes in a name string and prints a farewell'
    print('Goodbye {}'.format(name))

if __name__ == '__main__':
    print('Saying hello')
    sayHello('Bob')
    print('Saying goodbye')
    sayGoodbye('Polly')
