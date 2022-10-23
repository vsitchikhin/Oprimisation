import math


def method_powell(f, a: float, b: float, eps=0.01):
    #шаг1
    x1 = a
    x2 = (a + b) / 2
    x3 = b

    X = [x1, x2, x3]
    #шаг2
    while (True):
        min_x = X[0]
        for i in X:
            if (f(i) < f(min_x)):
                min_x = i

        #шаг3
        num = (X[1] ** 2 - X[2] ** 2) * f(X[0]) + (X[2] ** 2 - X[0] ** 2) * f(X[1]) + (
                    X[0] ** 2 - X[1] ** 2) * f(X[2])
        denum = (X[1] - X[2]) * f(X[0]) + (X[2] - X[0]) * f(X[1]) + (X[0] - X[1]) * f(X[2])
        X.append(0.5 * (num / denum))
        #шаг4
        if (abs(X[3] - min_x) <= eps):
            break
        #шаг5
        X.sort()

        #шаг6
        max_x = 0
        for i in range(4):
            if (f(X[i]) > f(X[max_x])):
                max_x = i
        X.pop(max_x)

    #шаг7
    return X[-1]

def f1(x):
    return (x-1) ** 2

def f2(x):
    return 4*x**3 - 8*x**2 - 11*x + 5

def f3(x):
    if x^2 == 0:
        x+=0.00000001
    return x + 3/(x**2)

def f4(x):
    if 4-x**2 == 0:
        x+=0.00000001
    return (x+2.5)/(4-x**2)

def f5(x):
    return -math.sin(x) - (math.sin(3*x)/3)

def f6(x):
    return -2*math.sin(x) - math.sin(2*x) - (2*math.sin(3*x)/3)

























import functions.first as first
import functions.second as second
import functions.third as third
import functions.fourth as fourth
import functions.fifth as fifth
import functions.sixth as sixth
import numpy as np


def get_function_value(function, x):
    if function == 1:
        return first.function_value(x)
    elif function == 2:
        return second.function_value(x)
    elif function == 3:
        return third.function_value(x)
    elif function == 4:
        return fourth.function_value(x)
    elif function == 5:
        return fifth.function_value(x)

    return sixth.function_value(x)



def get_x_values(a, b):
    x1 = a
    x2 = (a + b) / 2
    x3 = b
    return x1, x2, x3


# Шаги со 2 по 7
def get_value(function, x1, x2, x3, epsilon):
    X = [x1, x2, x3]

    while(True):
        min_x = X[0]
        for i in X:
            if get_function_value(function, X[i]) < get_function_value(function, min_x):
                min_x = i

        num = (X[1] ** 2 - X[2] ** 2) * get_function_value(function, X[0]) \
              + (X[2] ** 2 - X[0] ** 2) * get_function_value(function, X[1]) \
              + (X[0] ** 2 - X[1] ** 2) * get_function_value(function, X[2])
        denum = (X[1] - X[2]) * get_function_value(function, X[0])\
                + (X[2] - X[0]) * get_function_value(function, X[1])\
                + (X[0] - X[1]) * get_function_value(function, X[2])

        X.append(0.5 * (num / denum))

        if (abs(X[3] - min_x) <= eps):
            break

        X.sort()

        max_x = 0
        for i in range(4):
            if (get_function_value(function, X[i]) > get_function_value(X[max_x])):
                max_x = i
        X.pop(max_x)

    return X[-1]