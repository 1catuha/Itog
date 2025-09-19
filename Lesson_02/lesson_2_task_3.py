import math


def square(x):
    s = x**2
    return (s)


x = float(input("Длинна стороны квадрата: "))
result = square(x)
rounded = math.ceil(result)


print(rounded)
