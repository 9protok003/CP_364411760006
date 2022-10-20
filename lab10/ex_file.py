"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

#  File I/O

# Open File

f = open("test.txt")
print(f.read()) # read all text in afile
f.close()

print("-------------------------")

f = open("test.txt")
print(f.read(10)) # read 10 charecters from file
f.close()

f = open("test.txt","r")
print(f.readline())
print(f.readline())
f.close()

print("-----------------")

f = open("test.txt")
print(f.readline(2))
f.close()

print("--------------------")

f = open("test.txt")
line = f.readline()  # read line
for x in line:
    print(x)
f.close()

print(line)

print("-----------------------")

count = 1
for x in range(len(line)):
    print(count,line[x])
    if count ==3:
        break
    count += 1
