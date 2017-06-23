def getNums():
    return 5, 10

nums = getNums()
print('nums={}'.format(nums))

x, y = nums
print('x={}'.format(x))
print('y={}'.format(y))

n = x, y
print('n={}'.format(n))

x2, y2 = getNums()
print('x2={}, y2={}'.format(x2, y2))

first, *rest, last = 1,2,3,4,5,6
print('first={}'.format(first))
print('rest={}'.format(rest))
print('last={}'.format(last))

numbers = (1, 3, 5), (4, 1)
print('numbers={}'.format(numbers))

a, (b, c) = numbers
print('a={}, b={}, c={}'.format(a, b, c))
