def f1():
    return "Hello Function"


# print(f1())


class Newclass:
    def f1():
        return "Hello Function"

    def f2():
        return "HELLO FUNCTION"


class1 = Newclass
print(class1.f1())

class2 = Newclass
print(class2.f2())

string1 = "apple"
string2 = "Name of the school: Don Bosco"
print(string1.upper())
print()

print(dir(Newclass))
print()
print(dir(str))
print(type(str()))
print()
print(dir(string1))
print(dir(string1) == dir(string2) == dir(str))


print(string1.upper())
print(string1.find("E"))
