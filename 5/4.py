dict = {"One": "Один", "Two": "Два", "Three": "Три", "Four": "Четыре"}

with open("input_4.txt", encoding="UTF-8") as file:
    flag = True
    while flag:
        str_file = file.readline()
        if str_file == "":
            flag = False
            break
        str_file = str_file.split()
        str_file[0] = dict.get(str_file[0])
        str_file = " ".join(str_file)
        with open("output_4.txt", "a", encoding="UTF-8") as file_output:
            print(str_file, file=file_output)
