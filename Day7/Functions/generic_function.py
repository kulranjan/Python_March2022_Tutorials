# This function will have all the keyword types to deal with


def default_positional_keyword_arguments(city="XYZ", *args, **kwargs):
    print(city)
    print(args, len(args))
    print(kwargs)


d1 = dict(a=10, b=1)
default_positional_keyword_arguments("Chennai", 20, 10, 100, **d1)
