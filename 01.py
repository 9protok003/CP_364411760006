mylist = []   # empty list
print(mylist)
print(len(mylist)) # retune intergar value --> 0

mylist = [10,20,30,40,50]
print(mylist)
print(len(mylist))
print(type(mylist))

#access to member in list
print(mylist[0], type(mylist[0]))
print(mylist[1])
print(mylist[2])
print(mylist[3])
print(mylist[4])
#print(mylist[5])

# negative indax
print(mylist[-1])
print(mylist[-2])
print(mylist[-3])
print(mylist[-4])
print(mylist[-5])

# rang indax [strat:stop]
mylist = [10,20,30,40,50]
# [20,30,40]
print(mylist[1:4])
# [10,20]
print(mylist[0:2])
# [20,30,40,50]
print(mylist[1:5])
print(mylist[1:])
# [40,50]
print(mylist[3:])

# range negative index [strat:stop]
# [20,30,40]
print(mylist[-4:-1])
# [10,20]
print(mylist[:-3])
# [20,30,40,50]
print(mylist[-4:])
# [40,50]
print(mylist[-2:])

# loop
# for

# ex_1
for x in mylist:
    print(x)
    print(x, x*10)

# ex_2
for x in range(len(mylist)):
    print(mylist[x])

# while
c = 0  # first index in list
while c < len(mylist):
    print(mylist[c],end=" ")
    c +=1