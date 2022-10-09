import functions.first as first
import functions.second as second
import functions.third as third
import functions.fourth as fourth
import functions.fifth as fifth
import functions.sixth as sixth
import numpy as np

def get_function_values(function, x1, x2, x3):
    if function == 1:
        value_x1 = first.function_value(x1)
        value_x2 = first.function_value(x2)
        value_x3 = first.function_value(x3)
    elif function == 2:
        value_x1 = second.function_value(x1)
        value_x2 = second.function_value(x2)
        value_x3 = second.function_value(x3)
    elif function == 3:
        value_x1 = third.function_value(x1)
        value_x2 = third.function_value(x2)
        value_x3 = third.function_value(x3)
    elif function == 4:
        value_x1 = fourth.function_value(x1)
        value_x2 = fourth.function_value(x2)
        value_x3 = fourth.function_value(x3)
    elif function == 5:
        value_x1 = fifth.function_value(x1)
        value_x2 = fifth.function_value(x2)
        value_x3 = fifth.function_value(x3)
    elif function == 6:
        value_x1 = sixth.function_value(x1)
        value_x2 = sixth.function_value(x2)
        value_x3 = sixth.function_value(x3)
    return value_x1, value_x2, value_x3
    
def get_x_values(a, b):
    x1 = a
    x2 = (a + b) / 2
    x3 = b
    return x1, x2, x3

def get_x4(x1, x2, x3, value_x1, value_x2, value_x3):
    if ((x2 - x3) * value_x1 +
        + (x3 - x1) * value_x2 +
        + (x1 - x2) * value_x3) == 0:
        return np.inf
    
    value = (
        (pow(x2, 2) - pow(x3, 2)) * value_x1 + 
        + (pow(x3, 2) - pow(x1, 2)) * value_x2 + 
        + (pow(x1, 2) - pow(x2, 2)) * value_x3
    ) / (
        (x2 - x3) * value_x1 +
        + (x3 - x1) * value_x2 +
        + (x1 - x2) * value_x3
    )
    return value / 2

def stop_test(current_x, x4, epsilon):
    if epsilon >= abs(x4 - current_x):
        return True
    return False

def renumber_xs(x1, x2, x3, x4):
    xs = [x1, x2, x3, x4]
    for j in range(len(xs) - 1):
        for i in range(len(xs) - 1):
            if xs[i + 1] < xs[i]:
                xs[i], xs[i + 1] = xs[i + 1], xs[i]
    return xs[0], xs[1], xs[2]

# Шаги со 2 по 7 начиная со 2 итерации:
def get_value(function, x1, x2, x3, epsilon):
    value_x1, value_x2, value_x3 = get_function_values(function, x1, x2, x3)
  
    min_value = min(value_x1, value_x2, value_x3)
    if min_value == value_x1:
        current_x = x1
    elif min_value == value_x2:
        current_x = x2
    else:
        current_x = x3
  
    x4 = get_x4(x1, x2, x3, value_x1, value_x2, value_x3)
    
    if stop_test(current_x, x4, epsilon):
        return x4
    
    x1, x2, x3 = renumber_xs(x1, x2, x3, x4)
    return get_value(function, x1, x2, x3, epsilon)
