import math


def new_function():
    return new_function.__name__


class Dummyclass:
    def __repr__(self) -> str:
        return "This is a simple class"


L1 = [
    1,
    2.0,
    3 - 78j,
    math.pi,
    2,
    2,
    4,
    bin(2333),
    hex(3),
    chr(67),
    [78, 91, 22],
    (100, 1000, 10000),
    "apple",
    "ZZ",
    "t",
    {89, "HBO", "Starworld", 7},
    dict(DC="Batman", Syncopy="Inception"),
    18,
    18,
    [1, 2, 3],
    [1, 2, 3],
]

L100 = L1.copy()
print(L1 == L100)
print(f"{L1 = }")
print()
list_methods = [
    "__add__",
    "__class__",
    "__class_getitem__",
    "__contains__",
    "__delattr__",
    "__delitem__",
    "__dir__",
    "__doc__",
    "__eq__",
    "__format__",
    "__ge__",
    "__getattribute__",
    "__getitem__",
    "__gt__",
    "__hash__",
    "__iadd__",
    "__imul__",
    "__init__",
    "__init_subclass__",
    "__iter__",
    "__le__",
    "__len__",
    "__lt__",
    "__mul__",
    "__ne__",
    "__new__",
    "__reduce__",
    "__reduce_ex__",
    "__repr__",
    "__reversed__",
    "__rmul__",
    "__setattr__",
    "__setitem__",
    "__sizeof__",
    "__str__",
    "__subclasshook__",
    "append",
    "clear",
    "copy",
    "count",
    "extend",
    "index",
    "insert",
    "pop",
    "remove",
    "reverse",
    "sort",
]

L1.append(78 - 2e33j)
print(f"L1.append('new_element') = {L1}")
print()
L1.append({67, 78, 89})
print(f"L1.append({67, 78, 89}) = {L1}")
print()
L1.extend((67, 78, 89))
print(f"L1.extend(67, 78, 89) = {L1}")
print()
print(f"{L1.count(18) = }")
print()
print(f"{L1.index([1, 2, 3]) = }")
L1.insert(8, "Hi there")
print()
print(f"L1.insert(8, 'Hi there') = {L1}")
print()
L1[8] = "I am overwritten"
print(f"{L1 = }")
print()
L1.pop()
print(f"L1.pop() = {L1}")
print()
L1.pop(15)
print(f"L1.pop(15) = {L1}")
L1.remove(3.141592653589793)
print()
print(f"L1.remove(3.141592653589793) = {L1}")
print()
L1.reverse()
print(f"L1.reverse() = {L1}")
print()
L1.reverse()
print(f"L1.reverse() = {L1}")
# print(f"{L1[::-1] = }")

print()
print(L1 + ["adding a list"] + [22])
print()
print(L1 * 2)
