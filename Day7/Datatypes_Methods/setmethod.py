a = {1, 2, 3, 4, 5}
b = {2, 3, 4, 5, 6}
c = {3, 4, 5, 6, 7}
d = {4, 5, 6, 7, 8}

set_methods = [
    "add",
    "clear",
    "copy",
    "difference",
    "difference_update",
    "discard",
    "intersection",
    "intersection_update",
    "isdisjoint",
    "issubset",
    "issuperset",
    "pop",
    "remove",
    "symmetric_difference",
    "symmetric_difference_update",
    "union",
    "update",
]
print()
print(f"{a.union(b) = }")
print(f"{a.union(b, c, d) = }")
print(f"{a.union([8, 9, 10]) = }")
print(f"same of a.union(b) {a | b = }")
# print(f"same of a.union(b) {a | [7, 8, 9 ,10] = }") # This is not allowed as the set comparison data is List DT
print(f"same of a.union(b) {a | b | c | d  = }")

x1 = {"foo", "bar", "baz"}
x2 = {"baz", "qux", "quux"}
print(x1 | x2)
print(x1.union(x2))
print(x1.union(("baz", "qux", "quizz")))

print()
print(f"{a.intersection(b) = }")
print(f"{a.intersection(b, c, d) = }")
print(f"same of a.intersection(b) {a & b = }")
print(f"same of a.intersection(b, c, d) {a & b & c & d = }")

print()
print(f"{a.difference(b) = }")
print(f"{b.difference(a) = }")
print(f"{b.difference(a, c, d) = }")
print(f"same of a.difference(b) {a - b = }")
print(f"same of a.difference(b, c, d) {a - b - c - d = }")

a = {1, 2, 3, 4, 5}
b = {10, 2, 3, 4, 50}
c = {1, 50, 101}

print()
print(f"{a.symmetric_difference(b) = }")
print(f"{a.symmetric_difference(c) = }")
print(f"same of a.symmetric_difference(b) {a ^ b = }")
print(f"same of a.symmetric_difference(b, c) {a ^ b ^ c  = }")


print()
x1 = {"foo", "bar", "baz"}
x1.add("slate")
print(f"add method of set {x1 = }")

print()
x1.remove("bar")
print(f"remove method of set {x1 = }")
# x1.remove("chalk") # If Element not present in set it will throw KeyError

print()
x1.discard("baz")
print(f"discard method of set {x1 = }")
# x1.discard("chalk") # If Element not present in set it will throw any error

print()
d = {100, 63, 567, 88, 55, 1.22, 0}
print(d)
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
d.pop()
print(f"set d is now after pop method {d = }")
# d.pop()
# print(f"set d is now after pop method {d = }")

print()
d1 = {4, 5, 6, 7, 8}
d2 = d1.copy()
print(f"set {d2 = }")

d1.clear()
print(f"set {d1 = }")
