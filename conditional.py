# n = int(input("Enter the Number:"))

# for i in range(1,11, 2):
#     print(n, "x", i, "=", n * i)
    
    
# n = 1

# a = 7

# while n <= 10:
#     print(a, "x", n, "=", n * a)
#     n += 1

# while True:
    
#     num1 = int(input("Enter the first number: "))
#     num2 = int(input("Enter the second number: "))
    
#     print(num1+num2)
    
#     repeat = input("Do you want to continue? (yes/no): ")
#     if repeat == "yes":
#         break

# for i in range(1, 6):
#     for j in range(1, i+1):
#         print(j, end='')
#     print()
    
# for i in range(1, 101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)

# n = 1

# while n <= 10:
#     if n== 5:
#         print("hi Adi")
#     else:
#         print(n)
#     n += 1

    
# for n in range(1, 11):
#     if n == 2:
#         continue
#     print(n)
#     n += 1

# sum = 0
# for i in range(1, 51):
#     if i % 2 == 0:
#         print("The sum of even numbers from 1 to 50 is:", sum)
# 

# sum = 0
# for i in range(1, 11):
#     print(i ** 2)

# sum = 0

# n = 0

# while n < 10:
#     if n % 2 != 0:
#         sum += n
#         print(sum)
#     n += 1

# for i in range(1, 101):
#     if i % 8 == 0 and i % 12 == 0:
#         print(i)

# while True:
#     name = input("Enter the customer name: ")
#     total = 0
    
#     while True:
#         print("Enter the amount and quantity")
#         amount = float(input("Amount of the iteam:"))
#         quantity = int(input("Enter the quantity:"))
        
#         total += amount * quantity
#         repeat = input("Do you want to add more items? (yes/no): ")
#         if repeat == "no" or repeat == "no":
#             break
#         print("-"* 40)
#         print("Name:", name)
#         print("Total Amount:", total)
#         print("-"* 40)
#         print("Thank you for shopping with us!")
#     print("The number is zero")

l1 = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]

# for i in range(1, len(l1)+1):
#     print(f"index of l1 is -{i} = {l1[-i]}")
print(l1[-2:-1])
