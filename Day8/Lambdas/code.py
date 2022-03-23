# def function1(x):
#     return x + (x * 2)


# print(function1(22))


# print((lambda x: x + (x * 2))(22))

# function1 = lambda x: x + (x * 2)
# print(function1(22))

print((lambda x, y, z: x + y + z)(8, 9, 10))
print((lambda x, y, z=3: x + y + z)(8, 9, z=20.00))
print((lambda *args: sum(args))(1, 2, 3))
print((lambda **kwargs: sum(kwargs.values()))(one=1, two=2, three=3))

print()


def uppercase(x):
    return x.upper()


print(list(map(uppercase, ["cat", "cow", "lamb"])))  # map(function, iterable)
print(
    list(map(lambda x: x.upper(), ["cat", "cow", "lamb"]))
)  # map(lambda function, iterable)
print()


def filterit(x):
    if "o" in x:
        return x


print(list(filter(filterit, ["cat", "cow", "lamb"])))  # filter(function, iterable)
print(
    list(filter(lambda x: "o" in x, ["cat", "cow", "lamb"]))
)  # filter(lambda function, iterable)


ids = ["id77", "id30", "id2", "id22", "id100"]
print(sorted(ids))  # lexicographic sort

print(sorted(ids, key=lambda x: int(x[2:]), reverse=True))
print(sorted(ids, key=lambda x: int(x[2:]), reverse=False))
