"""
Name: {Aphisada Suksom}
SID: {364411760006}
Group: {MIT421}
"""
"""
# Question 2
เขียนโปรแกรมรับอินพุต 1 ตัว ที่เป็นจำนวนจริง และตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่า 0, น้อยกว่า 0 หรือเท่ากับ 0
 - ถ้ามีค่ามากกว่า 0 ให้ตรวจสอบต่อว่าเป็นเลขคู่หรือเลขคี่
    - ถ้าเป็นเลขคู่ให้พิมพ์ "positive even."
    - ถ้าเป็นเลขคี่ให้พิมพ์ "positive odd."
 - ถ้ามีค่าน้อยกว่า 0 ให้ตรวจสอบต่อว่าเป็นเลขคู่หรือเลขคี่
    - ถ้าเป็นเลขคู่ให้พิมพ์ "negative even."
    - ถ้าเป็นเลขคี่ให้พิมพ์ "negative odd."
 - ถ้ามีค่าเท่ากับ 0 ให้พิมพ์ "zero."
"""

number = int(input("number : "))
if number % 2 == 0 and number :
    print("positive even.")
elif number % 2 != 0 and number :
    print("positive odd.")
else:
    print("zero")






