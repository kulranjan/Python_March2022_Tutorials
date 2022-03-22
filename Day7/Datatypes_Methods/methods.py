def f1():
    return "Hello Function"


# print(f1())


class Newclass:
    def f1():
        return "Hello Function"

    def f2():
        return "HELLO FUNCTION"


print(Newclass.f1())
print(Newclass.f2())

dt = [str(), dict(), list(), set(), int(), float()]

for DT in dt:
    print(type(DT))

print()

actual_data = ["G", {"name": "Kumaran"}, [1, 2, 3], {1, 2, 3}, 22, 67.2]

for DT in actual_data:
    print(type(DT))


instance1 = Newclass
instance2 = Newclass

NAME = "Kumaran"
EXP = "12 Years"

print()
print(dir(str()))
print()
print(dir(NAME))
