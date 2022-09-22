"""
Name: {Aphisada Suksom}
SID: {364411760006}
Group: {MIT421}
"""
"""
# Question 1
เขียนโปรแกรมรับอินพุต 1 ตัว ที่เป็นจำนวนเต็ม และตรวจสอบว่าจำนวนที่รับมามีค่ามากกว่า 0 หรือไม่
 - ถ้ามีค่ามากกว่า 0 ให้พิมพ์คำว่า "More than 0."
 - ถ้ามีค่าน้อยกว่าหรือเท่ากับ 0  ให้พิมพ์คำว่า "Less than 0 or equal to 0."
"""

number = int(input("number : "))

if number >0:
    print("More than 0.")
elif number <=0:
    print("Less than 0 or equal to 0")
