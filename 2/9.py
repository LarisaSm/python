n = int(input())

lst = {i: ((1 + 1 / i) ** i) for i in range(1, n + 1)}

print(sum(lst.values()))
