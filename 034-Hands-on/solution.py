def multi(*vals):
    prod = 1
    for v in vals:
        prod = prod * v
    return prod

def split(v):
    return 2, v-2

def combined(v):
    first, second = split(v)
    return multi(first, second)

print('multi(2, 3, 4) = {}'.format(multi(2, 3, 4)))
print('split(24) = {}'.format(split(24)))
print('combined(24) = {}'.format(combined(24)))
