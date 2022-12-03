import math


def fact(n):
    for el in range(1, n + 1):
        yield math.factorial(el)


n_fact = int(input())
for el in fact(n_fact):
    print(el, end=" ")
