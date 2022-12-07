from random import randint

with open("input_5.txt", "w+", encoding="UTF-8") as file:
    list_file = [str(randint(1, 10)) for _ in range(randint(5, 10))]
    file.write(" ".join(list_file))
    file.seek(0)
    str_file = list(map(int, file.read().split()))
    print(sum(str_file))
