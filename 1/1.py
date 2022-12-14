# Базовые:

# 1) Поработайте с переменными, создайте несколько,
# выведите на экран, запросите у пользователя несколько чисел
# и строк и сохраните в переменные, выведите на экран.


def f1():
    a = input("введите что-нибудь: ")
    print(f"Вы ввели {a}")
    number = input("А теперь введите число: ")
    try:
        float(number)
        print(f"Вы ввели число {float(number)}. Вы молодец!")
        return True
    except ValueError:
        print("Вас просили ввести число!")
        return False


# 2) Пользователь вводит время в секундах.
# Переведите время в часы, минуты и секунды и выведите в формате чч:мм:сс.
# Используйте форматирование строк.


def f2():
    time = int(input("Введите время в секундах: "))
    hours = time // 3600
    minutes = (time - hours * 3600) // 60
    sec = time - hours * 3600 - minutes * 60
    print(hours, minutes, sec, sep=":")


# 3) Узнайте у пользователя число n.
# Найдите сумму чисел n + nn + nnn.
# Например, пользователь ввёл число 3. Считаем 3 + 33 + 333 = 369.


def f3():
    n = input("Введите число n: ")
    nn = n + n
    nnn = n + n + n
    print(int(n) + int(nn) + int(nnn))


# 4) Пользователь вводит целое положительное число.
# Найдите самую большую цифру в числе.
# Для решения используйте цикл while и арифметические операции.


def f4():
    n = int(input("Введите целое положительное число n: "))
    max = n % 10
    while n != 0:
        n = n // 10
        print(f"max = {max} n = {n}")
        if max < (n % 10):
            max = n % 10

    print(f"max = {max}")


# 5) Запросите у пользователя значения выручки и издержек фирмы.
# Определите, с каким финансовым результатом работает фирма
# (прибыль — выручка больше издержек, или убыток — издержки больше выручки).
# Выведите соответствующее сообщение. Если фирма отработала с прибылью,
# вычислите рентабельность выручки (соотношение прибыли к выручке).
# Далее запросите численность сотрудников фирмы и определите прибыль фирмы
# в расчете на одного сотрудника.


def f5():
    revenue = int(input("введите выручку фирмы: "))
    costs = int(input("введите издержки фирмы: "))
    if revenue > costs:
        print("Фирма работает с прибылью. Поздравляю")
        profitability = (revenue - costs) / revenue
        print(f"Рентабельность выручки: {profitability}")
        employees = int(input("введите численность сотрудников фирмы: "))
        print(f"Прибыль фирмы в расчете на одного сотрудника: {revenue / employees}")
    else:
        print("Фирма работает в убыток. Сочувствую")


# 6) Спортсмен занимается ежедневными пробежками.
# В первый день его результат составил a километров.
# Каждый день спортсмен увеличивал результат на 10 % относительно предыдущего.
# Требуется определить номер дня, на который результат спортсмена составит
# не менее b километров. Программа должна принимать значения параметров a и b
# и выводить одно натуральное число — номер дня.
# Например: a = 2, b = 3.
# Результат:
# 1-й день: 2
# 2-й день: 2,2
# 3-й день: 2,42
# 4-й день: 2,66
# 5-й день: 2,93
# 6-й день: 3,22
# Ответ: на 6-й день спортсмен достиг результата — не менее 3 км.


def f6():
    a = float(input("Введите количество километров a: "))
    b = float(input("Введите количество километров b: "))
    day = 1
    while a < b:
        print(f"{day}-й день: {a:.2f}")
        a = a + a * 0.1
        day += 1
    else:
        print(f"{day}-й день: {a:.2f}")
        a = a + a * 0.1

    print(f"Ответ: на {day}-й день спортсмен достиг результата - не менее {b} км.")


# Дополнительные:

# 7. Напишите программу, которая принимает на вход цифру,
# обозначающую день недели, и проверяет, является ли этот день выходным.

# Пример:

# - 6 -> да
# - 7 -> да
# - 1 -> нет


def f7():
    a = int(input("Введите номер дня недели: "))
    if 1 < a < 6:
        print("нет")
    elif 6 <= a <= 7:
        print("да")
    else:
        print("Нет такого номера среди дней недели")


# 8. Напишите программу для проверки истинности утверждения
# ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.


def f8():
    predicate = [0, 1]
    for i in predicate:
        for j in predicate:
            for l in predicate:
                result = (not (i or j or l)) == ((not i) and (not j) and (not l))
                print(f"¬({i} ⋁ {j} ⋁ {l}) = ¬{i} ⋀ ¬{j} ⋀ ¬{l} = {result}")


# 9. Напишите программу, которая принимает на вход координаты точки
# (X и Y), причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости,
# в которой находится эта точка (или на какой оси она находится).

# Пример:

# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3


def f9():
    x = float(input("Введите координаты Х: "))
    y = float(input("Введите координаты У: "))
    if x > 0 and y > 0:
        print("1 четверть ")
    elif x < 0 and y > 0:
        print("2 четверть ")
    elif x < 0 and y < 0:
        print("3 четверть ")
    elif x > 0 and y < 0:
        print("4 четверть ")
    else:
        print("координаты не должны быть равны 0")


# 10. Напишите программу, которая по заданному номеру четверти,
# показывает диапазон возможных координат точек в этой четверти (x и y).


def f10():
    number = int(input("Введите номер четверти: "))
    if number == 1:
        print("1 четверть: x > 0 и y > 0 ")
    elif number == 2:
        print("2 четверть: x < 0 and y > 0 ")
    elif number == 3:
        print("3 четверть: x < 0 and y < 0 ")
    elif number == 4:
        print("4 четверть: x > 0 and y < 0 ")
    else:
        print("Такой четверти не существует. Попробуйте еще раз.")


# 11. Напишите программу, которая принимает на вход координаты двух точек
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21


def f11():
    xa, ya = map(int, input("Введите координаты точки A через запятую: ").split(","))
    xb, yb = map(int, input("Введите координаты точки B через запятую: ").split(","))
    distance = ((xb - xa) ** 2 + (yb - ya) ** 2) ** 0.5
    print("{0:.2f}".format(distance))


# f1()
# f2()
# f3()
# f4()
# f5()
# f6()
# f7()
# f8()
# f9()
# f10()
# f11()
