def my_func(x, y):
    return x**y


def my_func_v2(x, y):
    sqr = 1
    for i in range(0, abs(y)):
        sqr *= x

    return 1 / sqr


print(my_func(9, -2))
print(my_func_v2(9, -2))
