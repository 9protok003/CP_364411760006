"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

# function with multiple parameter

def myfunc(*msg): #*msg --> tuple (...)
    print(msg)
    print(type(msg))

def myfunc2(*value):
    total = 0
    for x in value:
        total += x
    #print(total)
    return total

myfunc(10)
myfunc(10,20,30)

print("")

x = myfunc2(10)
x = myfunc2(5,15,30,55,60)
print(x)


