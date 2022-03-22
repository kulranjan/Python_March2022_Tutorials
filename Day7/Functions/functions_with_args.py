def power_of_two(x):
    """This is a function used to get the power of 2 with the value x"""
    return x ** 2


print(power_of_two(4637388383994974646))

square_value = power_of_two(4637388383994974646)
print(square_value)


def name_of_the_person(fname, lname):
    return lname.title(), fname.title()


print(name_of_the_person("kumaran", "ramalingam"))
last_name, first_name = name_of_the_person("kumaran", "ramalingam")
print(last_name)
print(first_name)


def name_of_the_person(fname, lname):
    return (
        lname.title(),
        fname.title(),
    )  # Beyond 1st return statement nothing will get exectuted
    # return fname, lname
    print("Hello")


print(name_of_the_person("kumaran", "ramalingam"))
