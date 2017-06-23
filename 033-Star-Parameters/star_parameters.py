def add(*nums):
    total = 0
    for n in nums:
        total = total + n
    return total

print(add(1, 2, 3, 4, 5, 6))

def createDict(**vals):
    v = {}
    for k in vals:
        v[k] = vals[k]
    return v

print(createDict(Name = 'Daniel', Age = 24))
