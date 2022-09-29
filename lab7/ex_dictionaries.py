"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

# Data collection - Dictionary
# keys:values

d = {"name":"Aphisada","age":19,"major":"MIT"}
print(type(d))
print(d)

# access to value in dictionary - using keys
print(d["name"])
print(d["age"])
print(d["major"])
#print(d["uni"])

print("")

# get()
z = d.get("name")
print(d.get("name"))
print(d.get("age"))
print(d.get("major"))

print("")

# key()
x = d.keys()
print(x,type(x))
#print(x[0])

print("")

# values()
y = d.values()
print(y)

print("")

# item()
z = d.items()
print(z,type(z))

print("")

# loop - for
# keys
for x in d:
    print(x)
for x in d.keys():
    print(x)

print("")

# values
for x in d:
    print(d[x])
for x in d.values():
    print(x)

print("")

# items
for x,y in d.items():
    print(x,y)

print("")

# changing value in dict
print(d)
# MIT --> AC
d["major"] = "AC"
print(d)

print("")

# update()
# 30 --> 26
d.update({"age":26})
print(d)

print("")

# add item to dict
d["university"] = "RUTS"
print(d)
d.update({"faculty":"MT"})
print(d)

print("")

# remove item in dict
# pop()
d.pop("university")
print(d)

print("")

# popitem()
d.popitem()
print(d)

print("")

# del keyword
if "majors" in d:
    del d["majors"]
else:
    print("No major key in d.")
print(d)

print("")

# clear()
d.clear()
print(d)

print("")

# copy dictionary
x = {1:100,2:200,3:[3,30,300]}
print(x)

y = x
print(y)

x[1] = 1000
print(x)
print(y)

print("")

# copy()
y = x.copy()
print(y)
x[1] = 10
print(x)
print(y)

print("")

print(x)
print(x[3][2])

