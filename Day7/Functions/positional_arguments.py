def normal_arguments_function(x, y, z, a, b, c):
    return x ** 2, y / 200, z.upper(), a, b, c + 2


print(normal_arguments_function(10, 22, "zinc", 77, 88, 101))


def positional_arguments_function(*args):
    for arg in args:
        print(arg * 2)


positional_arguments_function(10, 22, "zinc ", 77, 88, 101)


def name_of_the_person(*args):
    return type(args)  # Beyond 1st return statement nothing will get exectuted
    # return fname, lname


print(name_of_the_person("kumaran", "ramalingam"))
