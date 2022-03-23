def outer_function(msg):  # Enclosing Function
    message = msg

    def inner_function():  # Local Function
        return message

    return inner_function


hello_func = outer_function("Hello this is outerfunction message")
print(hello_func())
print(hello_func.__name__)
print()


def generate_power(exponent):
    def power(base):
        return base ** exponent

    return power


raise_two = generate_power(2)  # 2 is exponent
raise_three = generate_power(3)  #  3 is exponent
raise_four = generate_power(4)  # 4 is exponent

print(raise_two)
print(raise_three)
print(raise_four)
print(raise_two(30))  # 30 is base
print(raise_three(100))  # 100 is base
print(raise_four(1000))  # 1000 is base
