# def f(): # Enclosing function of g()
#     print("Start f()")

#     def g(): # Local function
#         print("Start g()")
#         print("End g()")

#     g()
#     print("End of g()")


# f()


# x = "GLOBAL"


# def f():

#     # x = "ENCLOSING"

#     def g():
#         # x = "LOCAL"
#         print(x)

#     g()


# f()

# x = 20


# def f():
#     global x
#     x = 35
#     print(f"local scope variable {x = }")


# f()
# print(f"global scope variable {x = }")

x = 100


def f():
    x = 30

    def g():
        x = 40

        def zz():
            nonlocal x
            x = 50

    g()
    print(x)


f()
print(x)
