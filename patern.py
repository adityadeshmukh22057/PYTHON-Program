# rows = 5
# # Pyramid Pattern
# # for i in range(1, rows + 1):
# #     print(" " * (rows - i), end="")
# #     print("* " * i)

# # Diamond Pattern

# for i in range(1, rows + 1):
#     print(" " * (rows - i), end="")
#     print("* " * i)
    
# for i in range(rows - 1, 0, -1):
#     print(" " * (rows - i), end="")
#     print("* " * i)

def log(func):  # outer decorator
    def inner(*args, **kwargs):  # accept any number of arguments
        print(f"log: args = {args}, kwargs = {kwargs}")
        result = func(*args, **kwargs)
        print(f"Return value = {result}")
        return result
    return inner

@log
def add_1(*args):
    return sum(args)

# Example calls:
add_1(5, 10)             # two arguments
add_1(1, 2, 3, 4, 5)     # multiple arguments
