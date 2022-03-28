


L1 = "apple orange jackfruit grapes".split()
t1 = 7, 8, 9, 10, 11, 12
s1 = {87, "apple", 3+4j}
d1 = dict(a=67, b=100, c="Goa")

for value in L1:
    print(value)
print()
for value in t1:
    print(value)
print()
for value in s1:
    print(value)
print()
for key, value in d1.items():
    print(key, value)
print()
print([value for value in L1])
print({value for value in s1})

# Generator Expression

print({key: value for key, value in d1.items()})
print()

generator = (i ** 2 for i in range(1,20))
for _ in range(10):
    print(next(generator))
print()
for _ in range(9):
    print(next(generator))
print()
# print(next(generator))
# print(next(generator))
print()

def normal_function():
    for x in range(3,10):
        return x**2

print(normal_function())

print()

def generator_function():
    for x in range(3,10):
        yield x ** 2

g1 = generator_function()
for x in range(5):
    print(next(g1))

def multi_yield():
    yield_str = "this will print the first string"
    yield yield_str
    yield_str = "This will print the second string"
    yield yield_str

print()

multi_object = multi_yield()
print(next(multi_object))
print(next(multi_object))



# simple example for decorator Function

def fib(a=0, b=1):
    """ Generator that yields Fibonacci Numbers, a and b are the seed values"""

    while True:
        yield a
        a, b = b, a + b

print()
f = fib()
for _ in range(10):
    print(next(f))


