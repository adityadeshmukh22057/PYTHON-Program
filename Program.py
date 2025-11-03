# sourcery skip: avoid-builtin-shadow
my_list = []

for i in range(5):
    element = int(input(f"Enter element {i+1}: "))
    my_list.append(element)
    

if len(my_list) >= 3:
    Remove_element = my_list.pop(2)
    print(f"Removed element: {Remove_element}")
else:
    print("List has less than 3 elements, cannot remove the third element.")
    

my_list.sort()
print("Sorted list:", my_list)



####################odd`##########################`
numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

odd_numbers = [num for num in numbers if num % 2 != 0]

print("Odd numbers in the list are:", odd_numbers)


##################### Mini-Max ##########################

numbers = list(map(int, input("Enter numbers separated by spaces: ").split()))

minimum = min(numbers)
maximum = max(numbers)

print("Minimum number:", minimum)
print("Maximum number:", maximum)

########################### tuple ##########################

my_tuple = (2, 4, 2, 8, 10)

print("Second element:", my_tuple[1])
print("Last element:", my_tuple[3])

value = int(input("Enter a value to check it occrance: "))

count = my_tuple.count(value)
print(f"The value {value} occurs {count} times in the tuple.")


####################### Set ##########################

fruits = {"Apple", "Banana", "Watermelon", "Grapes"}

new_fruits = fruits.add("Orange")
remove_fruits = fruits.discard("Banana")

print("Updated set of fruits:", fruits)


set1 = {"Alice", "Bob", "Charlie"}
set2 = {"Charlie", "David", "Eve"}

new_set = set1.intersection(set2)
print("Common elements in both sets:", new_set)

new_students = set1.union(set2)
print("All unique elements from both sets:", new_students)

not_in_set = set1.symmetric_difference(set2)

print("Elements in either set1 or set2 but not in both:", not_in_set)



############################# Dictionary ##########################

student = {
    1: "Aditya",
    2: "Aryan",
    3: "Pratik",
    4: "Rahul",
    5: "Rohan"
}

print("Original dictionary:", student)

student[6] = "Sagar"

remove_student = student.pop(2)
print("Updated dictionary:", student)

#################################################

cubes = {x: x**3 for x in range(1, 11)}
print(f"Cubes from 1 to 10: {cubes}")