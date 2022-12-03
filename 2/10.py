from random import randint

num = int(input())

lst = [randint(-num, num) for _ in range(num)]
mult = 1

with open("file.txt", "w+", encoding="utf-8") as file:
    count = randint(1, num)
    for _ in range(count):
        file.writelines(f"{randint(0,num-1)}\n")
    file.seek(0, 0)
    index_list = file.read().splitlines()
    for index in index_list:
        mult = mult * lst[int(index)]


print(f"index_list = {index_list}")
print(f"lst = {lst}")
print(f"mult = {mult}")
