products = []

count = int(input("Сколько товаров вы хотите ввести: "))
i = 1
while i <= count:
    title = input("Введите название товара: ")
    price = int(input("Введите цену товара: "))
    count_of_title = int(input("Введите количество товара: "))
    member = input("Введите единицу измерения: ")
    products.append(
        (
            i,
            {
                "название": title,
                "цена": price,
                "количество": count_of_title,
                "ед": member,
            },
        )
    )
    i += 1

print(products)
dict = {"название": [], "цена": [], "количество": [], "ед": []}
list_keys = ["название", "цена", "количество", "ед"]

for el in products:
    for key, value in el[1].items():
        dict[key].append(value)

dict["ед"] = list(set(dict["ед"]))
print(dict)
