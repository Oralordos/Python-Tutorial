import math, random

def add(*vals):
    'Takes in any number of numbers, and returns the sum of them all'
    s = 0
    for v in vals:
        s += v
    return s

def findDistance(p1, p2):
    'Takes in two two-item tuples, which represent two points on a graph, and returns the distance between them'
    return math.sqrt((p2[0] - p1[0])**2 + (p2[1] - p1[1])**2)

def getRandom():
    'Returns a random number between one and one hundred'
    return random.randint(1, 100)

if __name__ == '__main__':
    print('add(4, 5, 6) = {}'.format(add(4, 5, 6)))
    print('findDistance((3, 5), (7, 3)) = {}'.format(findDistance((3, 5), (7, 3))))
    print('getRandom() = {}'.format(getRandom()))
