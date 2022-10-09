import functions.first as first
import functions.second as second
import functions.third as third
import functions.fourth as fourth
import functions.fifth as fifth
import functions.sixth as sixth

# Первый шаг: вычисление f(x) и f(x + h)
def get_function_values(function_number, x, h):
    if function_number == 1:
        value_x = first.function_value(x)
        value_x_h = first.function_value(x, h)
    elif function_number == 2:
        value_x = second.function_value(x)
        value_x_h = second.function_value(x, h)
    elif function_number == 3:
        value_x = third.function_value(x)
        value_x_h = third.function_value(x, h)
    elif function_number == 4:
        value_x = fourth.function_value(x)
        value_x_h = fourth.function_value(x, h)
    elif function_number == 5:
        value_x = fifth.function_value(x)
        value_x_h = fifth.function_value(x, h)
    elif function_number == 6:
        value_x = sixth.function_value(x)
        value_x_h = sixth.function_value(x, h)
    return value_x, value_x_h

def get_xk(x, k, h):
    return x + pow(2, k - 1) * h

def step_four_and_five(x, k, h, function_number, a, b, x0):
    xk = get_xk(x0, k, h)
    xk_1 = get_xk(x0, k-1, h)
    value_xk, _ = get_function_values(function_number, xk, 0)
    value_xk_1, _ = get_function_values(function_number, xk_1, 0)
    
    if value_xk_1 <= value_xk:
        if h > 0:
            b = xk
        else:
            a = xk
        return a, b
    else:
        if h > 0:
            a = xk_1
        else:
            b = xk_1
        k += 1
        a,b = step_four_and_five(xk, k, h, function_number, a, b, x0)
        return a, b

def get_local_minimum(x, h, function_number, a, b):
    # Step 1:
    value_x, value_h = get_function_values(function_number, x, h)
    
    # Step 2:
    if value_x > value_h:
        a = x
        x1 = x + h
        k = 2
        a, b = step_four_and_five(x1, k, h, function_number, a, b, x)
        return a, b
    else:
        value_x, value_h = get_function_values(function_number, x, -h)
    
    # Step 3:
    if value_h >= value_x:
        a = x - h
        b = x + h
        return a, b
    else:
        b = x
        x1 = x - h
        h = -h
        k = 2
        a, b = step_four_and_five(x, k, h, function_number, a, b, x)
        return a, b
  