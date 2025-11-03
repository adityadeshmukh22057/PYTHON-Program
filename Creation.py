# num = int(input("Enter a number: "))
# if num % 2 != 0:
#     print(f"{num} is an Odd number.")
# else:
#     print(f"{num} is not an Odd number.")
    
    
# num = int(input("Enter a number: "))
# if num % 2 == 0:
#     print(f"{num} is an even number")
# else:
#     print(f"{num} is an odd number")
    
#     li = []
#     print(l1.)

# def function():
#     l1 = [ [10, 20], [30, 40], [50, 60] ]
    
#     for i in range(len(l1)):
#         for j in range(len(l1[i])):
#             print(f"[l1[{i}][{j}]] = {l1[i][j]}")
#         print('-' * 30)
# function()

# def function1():

#     person_info = [
#         {
#             "name": "John Doe",
#             "age": 30,
#             "city": "New York"
#         },
#         {
#             "name": "Jane Smith",
#             "age": 25,
#             "city": "Los Angeles"
#         },
#         {
#             "name": "Sam Brown",
#             "age": 22,
#             "city": "Chicago"
#         }
#     ]
    
#     for person in person_info:
#         print(f"Name = {person['name']}")
#         print(f"Age = {person['age']}")
#         print(f"City = {person['city']}")
#         print('-' * 30)

# function1()

def function9():
    l1 = [10, 20, 30, 40, 50]
    l2 = [40, 50, 60, 70, 90]
    
    common_elements = [element for element in l1 if element in l2]
    print("Common elements:", common_elements)
    
    

# function9()

    



# num1 = 100  # Global variable
# myName = "sangram"  # Global variable
# def function11():
#     global myName  # Declare myName as global at the start of the function
#     print(f"The number is {num1}")  # Access global num1 (read-only)
#     print(f"The name is {myName}")  # Print current global myName
#     myName = "sangram"  # Modify global myName
#     print(f"The name is now {myName}")  # Print updated myName
#     num2 = 879  # Local variable
#     print(f"The number is {num2}")  # Print local num2
#     print(f"The inner function of function1: {num2}")  # Clarified print message

# function11()
# print(f"The outer function of function1: {num1}")  # type: ignore # Print global num1 outside function
# print(f"The outer function of function1: {myName}")  # type: ignore # Print global myName outside function


def function12():
    num1 = 34
    print(f"The number is {num1}")  # Access local num1 (read-only)


result = function12()
print(f"the result is {result} and the type of result is {type(result)}")