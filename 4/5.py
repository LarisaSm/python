from functools import reduce

lst = [el for el in range(100, 1001) if el % 2 == 0]


def reducer_func(el_prev, el):

    return el_prev * el


print(reduce(reducer_func, lst))
