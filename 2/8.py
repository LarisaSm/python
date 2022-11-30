number = int(input())
list = [
    1,
]

for i in range(2, number + 1):
    list.append(i * list[i - 2])

print(list)
