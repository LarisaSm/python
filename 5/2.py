with open("input.txt", encoding="UTF-8") as file:
    list_file = file.readlines()

    list_file = list(map(lambda i: i.split(), list_file))
    for i in range(len(list_file)):
        print(f"В строке {i+1} количество слов {len(list_file[i])}")
    print(f"Количество строк в файле: {len(list_file)}")
