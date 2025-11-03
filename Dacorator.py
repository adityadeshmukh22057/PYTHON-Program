# def add(p1, p2):
#     print(f"{p1} + {p2} = {p1 + p2}")
    
# def subtract(p1, p2):
#     print(f"{p1} - {p2} = {p1 - p2}")

# def multiply(p1, p2):
#     print(f"{p1} * {p2} = {p1 * p2}")
    
# def divide(p1, p2):
#     print(f"{p1} / {p2} = {p1 / p2}")
#     print(f"{p1} // {p2} = {p1 // p2}")
    
# def execute(function, p1, p2):
#     function(p1, p2)
    
# execute(add, 10, 5)
# execute(subtract, 10, 5)
# execute(multiply, 10, 5)
# execute(divide, 10, 5)


# salary = float(input("Enter your salary: "))

# if salary > 100000:
#     bonus = salary * 0.10
# elif salary < 50000:
#     bonus = salary * 0.20
# else:
#     bonus = salary * 0.15
    
# print(f"your salary is {salary} and your bonus is {bonus} and total is {salary + bonus}")



# num = int(input("Enter a number: "))
# if num > 1:
#     for i in range(2, num):
#         if num % i == 0:
#             print("Not a prime number")
#             break
#     else:
#         print("Prime number")
# else:
#     print("Not a prime number")


Annual_income = float(input("Enter your annual income: "))

if Annual_income > 100000:
    tax = Annual_income * 0.30
elif Annual_income > 50000:
    tax = Annual_income * 0.20
elif Annual_income > 30000:
    tax = Annual_income * 0.10
    
else:
    tax = 0
print(f"Your annual income is {Annual_income} and your tax is {tax} and total is {Annual_income - tax}")