"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""

num = int(input("Enter : "))

try:
    f = open("C:\\Users\LabCom_MT-4\Desktop\\final1.txt", "w")
    for x in range(1,9):
        f.write(f'{x%3 and x%5}' )

except:
    print("Cloud not found a file.")
finally:
    f.close()
    print("Done.")

