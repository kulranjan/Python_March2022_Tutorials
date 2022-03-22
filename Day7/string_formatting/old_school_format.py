name = "Python"
errno = 6734343832

# Old School Format

print("Hello" + " " + name)
print("hello, %s" % name)
print("%x " % errno)
print("Hey %s, there is a 0x%x error" % (name, errno))
print("This is a decimal or integer %d" % 89.67)
print("this is an exponent %e" % 24.67)
print("this is an exponent %E" % 24)
print("This is a ASCII character %c" % "C")
print("this is a string  %r" % "representation")

print()
# Format string
print("Hey {}, this is the {} code".format(name, hex(errno)))
print("Hey {1}, this is the {0} code".format(name, hex(errno)))
print("Hey {}, this is the {:3.4f} code".format(name, 67.89236))
print(
    "Hey {name}, this is the {errno} code in line number {}".format(
        22, name=name, errno=errno
    )
)
print(
    "Hey {name}, this is the {errno} code in line number {}".format(
        22, name="Zelsky", errno=76348743
    )
)
print()

# F string format

print(f"Hey {name}, this is the {errno} code")
print(f"Hey {name.upper()}, this is the {hex(errno)} code")
print(f"True or False:  {len(name) < 10 = }")

d1 = dict(a1=10, b1=20)
print(f"Dictionary d1's a1 value {d1['a1']}")
print(f"{1 + 22}")
