hollywood_movies = {
    "Marvel": "Avengers",
    "Disney": "Frozen",
    "Universal Studios": "FF8",
    "Fox Studios": "Avatar",
    "Pixar Studios": "Cars",
    "Warner Bros": "Inception",
}
dictionary_methods = [
    "clear",
    "copy",
    "fromkeys",
    "get",
    "items",
    "keys",
    "pop",
    "popitem",
    "setdefault",
    "update",
    "values",
]

print(hollywood_movies["Universal Studios"])
print()
print(f"{hollywood_movies.get('Universal Studios') = }")
print()
print(f"{hollywood_movies.items() = }")
print()
print(f"{hollywood_movies.keys() = }")
print()
print(f"{hollywood_movies.values() = }")
print()
print(f"{hollywood_movies.pop('Warner Bros') = }")
print()
print(hollywood_movies)
print()
print(f"{hollywood_movies.popitem() = }")
print()
print(hollywood_movies)

d1 = dict(a=10, b=100)
d2 = dict(c=1, d="stringdata")

# d1.update(d2)
print(d2)
print(**d1, **d2)
