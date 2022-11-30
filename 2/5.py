my_list = [7, 5, 3, 3, 2]
print(my_list)

number = int(input())
try:
    pos = my_list.index(number)
    pos = pos + my_list.count(number)

except:
    for el in my_list:
        if el < number:
            pos = my_list.index(el)
            break
        else:
            pos = -1

my_list.insert(pos, number) if pos != -1 else my_list.append(number)
print(my_list)
