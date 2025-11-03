#closure

# def multiply(factor):
    
#     def multiply_by(x):
#         return x * factor
#     return multiply_by

# duble = multiply(2)
# tripple = multiply(3)

# print(duble(5))
# print(tripple(2))


def function():
    print("Insside function")
    def inner_function():
        print("Inside inner function")

    result = inner_function()
    print(f"the result is: {result} the type is {type(result)}")

function()
