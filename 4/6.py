from itertools import count, cycle


def iter_int(start_count, end_count):
    for el in count(start_count):
        if el > end_count:
            break
        else:
            print(el, end=" ")


def inter_lst(end_cycle, lst):
    с = 0
    for el in cycle(lst):
        if с >= end_cycle:
            break
        print(el, end=" ")
        с += 1


start = int(input("С какого числа генерировать целые числа: "))
end = int(input("До какого числа генерировать целые числа: "))
iter_int(start, end)


lst_default = [1, 2, 3, 4, 5]
print("")
count_cycle = int(input("Введите количество повторений элементов списка: "))

inter_lst(count_cycle, lst_default)
print("")
