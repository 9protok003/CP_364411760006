"""
Name: {Aphisada Suksom}
SID: {364411760006}
Group: {MIT421}
"""
"""
# Question 5
เขียนโปรแกรมคำนวนผลการเรียนโดยรับค่าอินพุตคะแนน 1 ตัวที่เป็นจำนวนจริง จากนั้นตรวจสอบค่าคะแนนดังต่อไปนี้
    •	ถ้าคะแนนมอยู่ระหว่าง 80.00-100.0 ให้พิมพ์ A
    •	ถ้าคะแนนอยู่ระหว่าง 75.0 - 79.99 ให้พิมพ์ B+
    •	ถ้าคะแนนอยู่ระหว่าง 70.0 - 74.99 ให้พิมพ์ B
    •	ถ้าคะแนนอยู่ระหว่าง 65.0 - 69.99 ให้พิมพ์ C+
    •	ถ้าคะแนนอยู่ระหว่าง 60.0 - 64.99 ให้พิมพ์ C
    •	ถ้าคะแนนอยู่ระหว่าง 55.0 - 59.99 ให้พิมพ์ D+
    •	ถ้าคะแนนอยู่ระหว่าง 50.0 - 54.99 ให้พิมพ์ D
    •	ถ้าคะแนนน้อยกว่า 49.99 ให้พิมพ์ F
"""

number = float(input("number : "))

if number >= 80.0 and number <= 100.0:
    print("A")
elif number >= 75.0 and number <= 79.99:
    print("B+")
elif number >= 70.0 and number <= 74.99:
    print("B")
elif number >= 65.0 and number <= 69.99:
    print("C+")
elif number >= 60.0 and number <= 64.99:
    print("C")
elif number >= 55.0 and number <= 59.99:
    print("D+")
elif number >= 50.0 and number <= 54.99:
    print("D")
elif number <=49.99:
    print("F")
