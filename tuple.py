# a = ("Apple", "Banana", "Mango", "orange")

# print(a.index("Apple"))

# print("Before the tuple",type(a))

# a = list(a)
# print("After converting to list",type(a))
# a.append("Grapes")
# print(a)

# i=0
# while i < len(a):
#     print(a[i])
#     i += 1

# for i  in range(len(a)):
#     print(a[i])

# print((a[2::-1]))

# b = 53
# print(type(b))

import json

Student = {"Name": "Aditya", "Roll_No": 218, "Class": "Btech"}

# Dictionary operations demonstration

# 1. Using get() method
x = Student.get("Name")
print("Using get('Name'):", x)

# 2. Using items() method
y = Student.items()
print("Using items():", list(y))

# 3. Using copy() method
d = Student.copy()
print("Copy of dictionary:", d)

# 4. Using update() method correctly
print("\nBefore update:", Student)
Student.update({"Roll_No": 222, "Name": "Aditya Kumar"})
print("After update:", Student)

# 5. Alternative: Create new updated dictionary
Student_original = {"Name": "Aditya", "Roll_No": 218, "Class": "Btech"}
updated_student = Student_original.copy()
updated_student.update({"Roll_No": 222, "Name": "Aditya Kumar"})
print("\nOriginal unchanged:", Student_original)
print("Updated copy:", updated_student)
