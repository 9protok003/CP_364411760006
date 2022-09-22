"""
เขียนโปรแกรมเพื่อรับค่าอินพุตจากผู้ใช้เป็นเลขจำนวนเต็ม จำนวน 2 ชุดข้อมูล โดยมีข้อมูลชุดละ 10 ตัว
จากนั้นให้แสดงข้อมูลที่ซ้ำกัน และไม่ซ้ำกันจากข้อมูล 2 ชุดนั้ ทางหน้าจอ
"""

s1 = set()
for i in range(10):
    x = int(input(f"enter an integer {i+1}: "))
    s1.add(x)
print(s1)
s2 = set()
for i in range(10):
    x = int(input(f"enter an integer {i+1}: "))
    s2.add(x)
print(s2)

a = s1
b = s2

s3 = s1.intersection(s2)
print(s3)

s4 = s1.symmetric_difference(s2)
print(s4)





