# def function1(p1, p2):
#     result = p1 + p2
#     print(f'The sum of {p1} and {p2} is {result}')
#     return result
# function1(10, 20)

# def function2():
#     pass
# function2()

# def func(*hello):
#     print("hello my name is", hello[2])
    
# func("John", "Doe", "Smith")

# def func2():
#     return "Hello, World!"
# print(func2())

#Recersion example

# def fac(n):
#     if n == 1:
#         return 1
#     else:
#         return n * fac(n - 1)

# print(fac(5))

# Lambda function example
# x = lambda a, b, c: (a + b) * c
# print(x(2, 3, 4))  # Output: 20


# Local Variable
# x = 24
# print(f"The value of x is {x}")
# def func():
#     x = 42
#     return x
# print(f"The value of x in func is {func()}")

# Global Variable

# x = 34
# print(f"The value of x is {x}")
# def func2(p):
#     global x
#     x = 40
#     return x
# print(f"The value of x in func2 is {func2(23)}")


# def maximum_Num(val1, val2, val3):
#     if val1 > val2 and val1 > val3:
#         print(f"{val1} is the maximum number")
#     elif val2 > val1 and val2 > val3:
#         print(f"{val2} is the maximum number")
#     else:
#         print(f"{val3} is the maximum number")
# maximum_Num(10, 20, 30) 
        


# def Create_list():
    
#     l = []
#     for i in range(1, 31):
#         l.append(i**2)
#     return l
# print(Create_list())


# Prime Number

def Check_prime(num):
    if num > 1:
        print("it is not a prime number")
    if num == 2:
        print("it is a prime number")
        for i in range(2, num):
            if (num % i) == 0:
                print("it is not a prime number")
                break
        else:
            print("it is a prime number")
Check_prime(11)


# List

def add(number):
    total = 0
    for i in number:
        total += i
    return total
print(add([1, 2, 3, 4, 5]))


# Fabunacci Series

def fibonacci(n):
    if n == 1:
        return 0
    elif n == 2:
        return 1
    else:
        return fibonacci(n - 1) + fibonacci(n - 2)

print([fibonacci(i) for i in range(1, 11)])  # Prints Fibonacci series up to the 10th term


def function2():
    """
    Demonstrates list manipulation: pop, remove, count, and clear.
    Attempts to access an element after clearing the list will raise an error.
    """
    country = ["IND", "USA", "UK", "AUS", "CAN"]
    # Remove the element at index 3
    country.pop(3)
    print(country)
    # Remove "USA" from the list
    country.remove("USA")
    print(country)
    # Check if "UK" is present
    if country.count("UK") > 0:
        print("UK is present in the list")
    # Clear the list
    country.clear()
    # Attempt to access "IND" after clearing (will raise an error)
    try:
        print(country[0])
    except IndexError:
        print("List is empty, cannot access elements.")
function2()