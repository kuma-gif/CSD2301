# 1. เขียนโปรแกรมพิมพ์ชื่อคุณ 100 ครั้ง
# รับชื่อจากผู้ใช้
name = input("กรุณากรอกชื่อของคุณ: ")

# แปลงชื่อเป็นตัวอักษรตัวใหญ่ทั้งหมด
name = name.upper()

# วนลูป 100 ครั้ง
for i in range(100):
  # พิมพ์ชื่อผู้ใช้พร้อมอักษรตัวใหญ่ทั้งหมด
  print(name)


