numbers = list(input())
print(numbers)
for i in range(0, len(numbers), 2):
    if i < len(numbers) - 1:
        (numbers[i], numbers[i + 1]) = (numbers[i + 1], numbers[i])
print(numbers)
