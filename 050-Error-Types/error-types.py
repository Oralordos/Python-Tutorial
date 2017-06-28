def err():
    5 / 0

def step3():
    err()

def step2():
    step3()

def step1():
    step2()

step1()
