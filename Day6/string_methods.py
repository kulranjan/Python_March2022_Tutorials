s1 = "foo bar baz jaaz bazz"
s2 = "0447232220"
s3 = "    first line  second line    "

string_methods = [
    "capitalize",
    "casefold",
    "center",
    "count",
    "encode",
    "endswith",
    "expandtabs",
    "find",
    "format",
    "format_map",
    "index",
    "isalnum",
    "isalpha",
    "isascii",
    "isdecimal",
    "isdigit",
    "isidentifier",
    "islower",
    "isnumeric",
    "isprintable",
    "isspace",
    "istitle",
    "isupper",
    "join",
    "ljust",
    "lower",
    "lstrip",
    "maketrans",
    "partition",
    "removeprefix",
    "removesuffix",
    "replace",
    "rfind",
    "rindex",
    "rjust",
    "rpartition",
    "rsplit",
    "rstrip",
    "split",
    "splitlines",
    "startswith",
    "strip",
    "swapcase",
    "title",
    "translate",
    "upper",
    "zfill",
]
print(f"{s1 = }")
print(f"{s2 = }")
print(f"{s3 = }")
print()
print(f"{s1.upper() = }")
print(f"{s1.lower() = }")
print(f"{s1.capitalize() = }")
print(f"{s1.title() = }")
print(f"{s1.startswith('foo  ') = }")
print(f"{s1.endswith('zz') = }")
print(f"{s1.count('az') = }")
print(f"{s1.split() = }")
print(f"{s1.split(',') = }")
print(f"{s3.strip() = }")
print(f"{s2.isdigit() = }")
print(f"{s2.isdecimal() = }")
print(f"{s3.isalpha() = }")
print(f"{s1.index(' jaaz ') = }")
print(f"{s1.find(' jaaz', 10, len(s1)) = }")
print(f"{s1.replace(' baz ', ' BAZ ') = }")
print(f"{s1.replace('baz', 'BAZ', 1) = }")  # number 1 is n number of occurences
print(f"{s2.partition('723') = }")
print()
s4, s5 = "Hello", "How are you"
print(s4)
print(s5)

print(s4 + " " + s5)
print(" ".join((s4, s5, s2)))
print("Hi there {1} how are you, I hope you are in {0}".format("Kumaran", "Chennai"))
