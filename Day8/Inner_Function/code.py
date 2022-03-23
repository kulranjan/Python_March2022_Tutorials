def outer_function(msg1, msg2):  # Enclosing Function
    message1 = msg1
    message2 = msg2

    def inner_function():  # Local Function
        print(message1, message2)

    inner_function()


outer_function("Hi", "Hello")


def factorial(number):

    if not isinstance(number, int):
        raise Warning("Sorry, 'number' variable must be an integer")

    if number < 0:
        raise Warning("Sorry, 'number' must be zero or positive")

    def inner_factorial(number):
        print(number)
        if number <= 1:
            return 1
        return number * inner_factorial(number - 1)

    return inner_factorial(number)


print(factorial(5))


# 5 * inner_factorial(4)
# 5 * 4 * inner_factorial(3)
# 5 * 4 * 3 * inner_Factorial(2)
