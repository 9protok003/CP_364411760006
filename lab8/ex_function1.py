"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

#  function
#  1. build-in function

print("hello, MIT421")
s = "RUTS"
print(len(s))

print("")

# 2. create by owner -- using "def" keyword

def myfunction1():
    print("hellom from function 1.")

def myfunction2(msg):
    print("hello, from function 2.",msg)

def myfunction3(num1,num2):
    print("hello, from function 3.")
    # return statement
    return num1+num2

# calling function
myfunction1()

# calling function with parameter
myfunction2("RUTS")

# calling function with parameter and return statement
rs = myfunction3(10,10) # num1:10 num2:10
print(rs) # num1:10 + num2:10 = 20

# print(myfunction3(20,20))
