"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

# create file
import os
# create empty file
#try:
    #f = open("text2.txt","x")
#except:
   # print("File already exits.")

print("")

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\test3.txt", "x")
except Exception as e:
    print(e)

# write file

# mode "a"
try:
    f = open("test2.txt","a")
    f.write("Aphisada Suksom\n")
except:
    print("Cloud not found a fine name 'test2.txt'")
finally:
    f.close()

# mode "w"
try:
    f = open("test2.txt","w")
    f.write("Aphisada Suksom\n")
except:
    print("Cloud not found a fine name 'test2.txt'")
finally:
    f.close()

# delete file
if os.path.exists("test3.txt"):
    os.remove("test3.txt")
else:
    print("File not found.")