"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

# function with default parameter

def myfunc(msg = "MIT"):
    print("hello,",msg)

# calling function with keyword parameter
myfunc()
myfunc("Thungsong")

# function with keyword parameter
def myfunc(num1,num2,num3):
    print(num1,num2,num3)

def myfunc2(num1,num2,num3):
    print(num1,num2,num3)

# calling function with keyword parameter
myfunc2(num3=30,num1=10,num2=20)

# function with multiple keyword parameter
def myfunc3(**data): # **data --> dictionar
    print(data.keys())
    print(data.values())

# key=value
myfunc3(name="sam",major="MIT")

