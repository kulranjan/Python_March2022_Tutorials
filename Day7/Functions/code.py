def print_function(x):
    message = x
    print(f"The print function prints: {message.upper()}")


def return_function(x):
    message = x
    return message.title()


print(print_function("This is 7th day of the session"))
print()
print(return_function("This is 7th day of the session"))


def new_function(a, b, c):
    return a, b, c


print(new_function(1, b=2, c=5))
