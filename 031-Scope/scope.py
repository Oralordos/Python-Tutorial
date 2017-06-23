def unbound(x):
    ret = None
    if x < 10:
        ret = 'hello'
    return ret

def globalVar():
    global val
    val = 42

val = 'Test'
r = unbound(11)
print(r)


globalVar()
print(val)
