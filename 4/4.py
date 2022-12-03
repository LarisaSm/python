lst_start = [2, 2, 2, 7, 23, 1, 44, 44, 3, 2, 10, 7, 4, 11]


def list_no_repeate(lst):
    generator = (param for param in lst if lst.count(param) == 1)
    for el in generator:
        print(el, end=" ")


def list_no_repeate2(lst):
    lst_result = [param for param in lst if lst.count(param) == 1]
    print(lst_result)


list_no_repeate(lst_start)
print(" ")
list_no_repeate2(lst_start)
