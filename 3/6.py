def int_func(word):
    return word.capitalize()


string = input()
print(" ".join(map(int_func, string.split())))
