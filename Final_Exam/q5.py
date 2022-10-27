"""
Name: Aphisada Suksom
Id: 364411760006
Group: MIT421
"""


tuu = int(input("ลุงตู่ : "))
pom = int(input("ลุงป้อม : "))
tin = int(input("ลุงทิน : "))
manus = int(input("ลุงมานัส : "))
all = (tuu+pom+tin+manus)

if all <=100000:
    print("ไม่ต้องเสียภาษี")
elif all <=100000 and all >=500000:
    print("จะเสียภาษี 5%")
elif all <=500001 and all >= 999999:
    print("จะเสียภาษี 10 %")
elif all >= 1000000:
    print("จะเสียภาษี 20 %")