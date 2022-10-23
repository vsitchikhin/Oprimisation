import functions.first as first
import functions.second as second
import functions.third as third
import functions.fourth as fourth
import functions.fifth as fifth
import functions.sixth as sixth

# Первый шаг: получение ряда Фибоначчи и количества элементов
def build_fibonacci_row(a, b, eps):
    fib1 = fib2 = 1
    
    fibonacci_row = [1, 1]
    
    while fib1 + fib2 <= abs((a + b) / eps):
        fibonacci_row.append(fib1 + fib2)
        fib1 = fib2
        fib2 = fibonacci_row[len(fibonacci_row) - 1]
    return fibonacci_row, len(fibonacci_row)

# Второй шаг: получение значений x1 и x2
def get_x1_x2(a, b, fib_n, fib_n1, fib_n2):
    x1 = a + (fib_n2 / fib_n) * (b - a)
    x2 = a + (fib_n1 / fib_n) * (b - a)
    return x1, x2

# Третий шаг: получение окончательных значений
def get_values(function, x1, x2, a, b, fib_row, elements_count, k, dist_const):
    value_x1, value_x2 = get_function_values(function, x1, x2)
    
    if value_x1 > value_x2:
        a = x1
        x1 = x2
        x2 = a + (fib_row[elements_count - 2 - k] / fib_row[elements_count - 1 - k]) * (b - a)
    else:
        b = x2
        x2 = x1
        x1 = a + (fib_row[elements_count - 3 - k] / fib_row[elements_count - 1 - k]) * (b - a)
        
    if k == elements_count - 3:
        x2 = x1 + dist_const
        value_x1, value_x2 = get_function_values(function, x1, x2)
        if value_x2 > value_x1:
            b = x2
        else:
            a = x1
        result = (a + b) / 2
        return result
    else:
        k = k + 1
        result = get_values(function, x1, x2, a, b, fib_row, elements_count, k, dist_const)
        return result
        

def get_function_values(function, x1, x2):
    if function == 1:
        value_x1 = first.function_value(x1)
        value_x2 = first.function_value(x2)
    elif function == 2:
        value_x1 = second.function_value(x1)
        value_x2 = second.function_value(x2)
    elif function == 3:
        value_x1 = third.function_value(x1)
        value_x2 = third.function_value(x2)
    elif function == 4:
        value_x1 = fourth.function_value(x1)
        value_x2 = fourth.function_value(x2)
    elif function == 5:
        value_x1 = fifth.function_value(x1)
        value_x2 = fifth.function_value(x2)
    elif function == 6:
        value_x1 = sixth.function_value(x1)
        value_x2 = sixth.function_value(x2)
    return value_x1, value_x2