"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

#  set --> {.....}
s = {10,20,30,40,50}
print(s,type(s))
print(len(s))

print("1")

# access to item set
print(s)

print("2")

for x in s:
    print(x,type(x))

print("3")

#  add item into set
# add 60 to s
s.add(60)
print(s)

print("4")

s2 = {"a", "b", "c"}
s.update(s2)
print(s)

print("5")

# delete item into set
#  remove()
s.remove(10)
print(s)

if 100 in s:
    s.remove(100)
    print(s)
else:
    print("No item in set.")

print("6")

#  pop()
p = s.pop()
print("delete-->",p)
print(s)

print("7")

# clear
print(s2)
s2.clear()
print(s2)

print("8")

# del
del s2
#print(s2)

print("9")

# join set
s1 = {10,20,30,40,50}
s2 = {10,50,100,200,300,400,500}

# update()
s1.update(s2)
print(s1)

# union() -- create new set
s3 = s1.union(s2)
print(s3)

print("10")

# intersection_update()
s3.intersection_update(s2)
print(s3)

# intersection --> create new set
s1 = {10,20,30,40,50}
s2 = {10,50,100,200,300,400,500}
s4 = s1.intersection(s2)
print(s4)

print("11")

# symmetric_difference()
s5 = s1.symmetric_difference(s2)
print(s5)

print("12")


