"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

# list comprehension
num = []

for x in range(1,101):  # 1-100
    num.append(x)

print(num)

newlist = [x for x in num if x%3==0]
print(newlist)