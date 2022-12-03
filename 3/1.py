number1 = int(input())
number2 = int(input())


def division(num1, num2):

    return num1 / num2 if num2 != 0 else "На ноль делить нельзя"


print(division(number1, number2))
