from random import choice

def combineWords(*words):
    'A function that takes in any number of word strings and combines them into a single string, which it returns'
    t = ''
    for w in words:
        t += ' ' + w
    return t

def getRandomWord(*words):
    'A function which takes in any number of word strings and picks a random one, which it returns'
    return choice(words)

if __name__ == '__main__':
    print("combineWords('Hello', 'there', 'how', 'are', 'you') = {}".format(combineWords('Hello', 'there', 'how', 'are', 'you')))
    print("getRandomWord('this', 'is', 'a', 'test') = {}".format(getRandomWord('this', 'is', 'a', 'test')))
