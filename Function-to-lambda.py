## Mohsen Pourdehghan


def add_numbers(a, b):
    return a + b

add_numbers = lambda a,b : a+b



def subtract_numbers(a, b):
    return a - b

subtract_numbers = lambda a,b : a-b



def multiply_numbers(a, b):
    return a * b

multiply_numbers = lambda a,b : a*b



def divide_numbers(a, b):
    if b != 0:
        return a / b
    else:
        print("Error: Division by zero is not allowed.")

divide_numbers = lambda a,b : a / b if b != 0 else print("Error: Division by zero is not allowed.")



def power(base, exponent):
    return base ** exponent

power = lambda base,exponent : base ** exponent
