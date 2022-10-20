"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

#  Exception
print("start")

x = "MIT421"

try:
    print(x)
except NameError:
    print("variable name not define.")
except:
    print("Something went wrong.")
else:
    print("No error.")
finally:
    print("Error has been excepted.")

print("End")

