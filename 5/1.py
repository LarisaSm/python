with open("output.txt", "w+", encoding="UTF-8") as file:
    flag = True
    while flag:
        str_user = input()
        if str_user == "":
            flag = False
            break
        file.write(str_user + "\n")
        # print(str_user, file=file) - второй вариант записи построчно
