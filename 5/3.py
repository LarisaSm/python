with open("input_3.txt", encoding="UTF-8") as file:
    list_file = file.readlines()

    list_file = list(map(lambda i: i.split(), list_file))
    salary = 0
    print("Сотрудники с окладом менее 20 000")
    for i in list_file:
        salary += float(i[1])
        if float(i[1]) < 20000:
            print(i[0])
    print(f"Средний доход всех сотрудников: {salary/len(list_file)}")
