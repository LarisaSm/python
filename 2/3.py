number = int(input())
# list

year_list = ["зима", "весна", "лето", "осень", "зима"]

print(year_list[number // 3])


# dict

year_dict = {
    1: "зима",
    2: "весна",
    3: "лето",
    4: "осень",
}

if 1 <= number <= 2 or number == 12:
    print(year_dict.get(1))
elif 3 <= number <= 5:
    print(year_dict.get(2))
elif 6 <= number <= 8:
    print(year_dict.get(3))
elif 9 <= number <= 11:
    print(year_dict.get(4))
else:
    print("Такого месяца нет в календаре")
