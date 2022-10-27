"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

num = int(input("Enter : "))

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\final4.txt", "w")
    for x in range(1,16):
        if num % 3==0:
            print("MT")
        elif num % 5==0:
            print("MIT")
        elif num % 3==0 and num % 5==0:
            print("SAIYAI")

except:
    print("Cloud not found a file.")
finally:
    f.close()
    print("Done.")

