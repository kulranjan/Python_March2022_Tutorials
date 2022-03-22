def normal_arguments_function(x, y, z, a, b, c):
    return x ** 2, y / 200, z.upper(), a, b, c + 2


print(normal_arguments_function(10, 22, "zinc", 77, 88, 101))


def keyword_arguments_function(**kwargs):
    return kwargs["city"], kwargs["temp"]


print(keyword_arguments_function(city=["Madrid", "Malta"], temp=(17.2, 10.3)))
