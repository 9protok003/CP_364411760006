"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

#  tuple
num = (10,20,30,40,50)
print(num,type(num))
print("")

# Display last item in tuple num
print(num[4], num[-1])

# Display first item in tuple num
print(num[0], num[-5])

print("")

# range indax (20,30,40)
print(num[1:4])

# Display negative index (20,30,40)
print(num[-4:-1])

print("")

# loop
for x in num:
    print(x)

for i in range(len(num)):
    print(num[i])

i = 1
while i < len(num):
    print(num[i])
    i += 1

print("")

# edit data in tuple
# 1. change tuple to list
# num = (10,20,30,40,50)
numlist = list(num)
numlist[0] = 100  # 10 --> 100
num = tuple(numlist)
print(num)

print("")

# add 1000 at index 2 of tuple num
numlist = list(num)
numlist.insert(2,1000)
num = tuple(numlist)
print(num)

print("")

# delete 30 form tuple num
numlist = list(num)
numlist.remove(30)
num = tuple(numlist)
print(num)

print("")

num2 = ("apple", "banana", "cherry")
num3 = num + num2
print(num3)

num3  = num3*2
print(num3)

print("")

a,b,c = num2
print(a,b,c)

print("")

a,*b = num2
print(a,b)

