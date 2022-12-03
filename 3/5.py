def sum_of_numbers(numbers):
    return sum(map(int, numbers.split()))


total_amount = 0
is_sum = True
while is_sum:
    numbers_str = input()
    if numbers_str.find("#") != -1:
        index = numbers_str.find("#")
        numbers_str = numbers_str[:index]
        is_sum = False
    total_amount += sum_of_numbers(numbers_str)
    print(total_amount)
