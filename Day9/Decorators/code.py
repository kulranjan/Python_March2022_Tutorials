


# Inner Functions
# ================

# def outer_func(msg):
#     message = msg
#
#     def inner_func():
#         print(message)
#
#     inner_func()
#
# outer_func("Hello")

# Function Closures
# =================

# def outer_func(msg):
#     message = msg
#
#     def inner_func(newmsg):
#         print(" ".join((message, newmsg)))
#
#     return inner_func
#
# new_func = outer_func("Hello")
# new_func("there")
# print(new_func.__name__)

# Decorator function

# Decorator 1
#
def decorator_function(func):
    def wrapper_function():
        print("Something happened before the wrapper function is called")
        func()
        print("Something happened after the wrapper function is called")

    return wrapper_function
#
# @decorator_function
# def say_hello():
#     return ("Hello Decorator")

# say_hello = decorator_function(say_hello)
# say_hello()
print("\n")

# Decorator 2

# def do_twice(func):
#     def wrapper_do_twice():
#         func()
#         func()
#
#     return wrapper_do_twice
#
# @do_twice
# @decorator_function
# def say_hello():
#     print("Hello Decorator")
#
#
# say_hello()


# Decorator 3

#
# from functools import wraps
# def do_twice(func):
#     @wraps(func)
#     def wrapper_do_twice(*args, **kwargs):
#         func(*args, **kwargs)
#         return func(*args, **kwargs)
#
#     return wrapper_do_twice
#
# @do_twice
# def greet(name, age):
#     print("Creating Greet")
#     print(f"""Name: {name}
# Age: {age}""")
#
#
# greet("Kumaran", "XYZ")
# print(greet.__name__)

# Boilerplate template

from functools import wraps
def decorated_function(func):
    @wraps(func)
    def wrapped_function(*args, **kwargs):
        value = func(*args, **kwargs)
        return value

    return wrapped_function



# Decorator Example

import time

def timer(func):
    """ Print the runtime of the decorated function """

    @wraps(func)
    def wrapper_timer(*args, **kwargs):
        start_time = time.perf_counter()
        value = func(*args, **kwargs)
        end_time = time.perf_counter()
        run_time = end_time - start_time
        print(f"Finished {func.__name__!r} in {run_time:.4f} secs")
        return value

    return wrapper_timer

@timer
def waste_some_time(num_times):
    for _ in range(num_times):
        sum([i**2 for i in range(10000)])
    else:
        return "Loop finished"

print(waste_some_time(1000))









