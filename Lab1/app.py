import algorithms.first as first_algorithm
import algorithms.second as fibonacci
import algorithms.third as pauel

functions = [
  "(x - 1)^2",
  "4x^3 - 8x^2 - 11x + 5",
  "x + 3/x^2",
  "(x + 2,5)/(4 - x^2)",
  "-sin(x) - (sin(3x))/3",
  "-2sin(x) - sin(2x) - (2sin(3x))/3",
]

print("Доступные функции:")
for i in range(len(functions)):
  print(str(i + 1) + " - " + functions[i])

print("Введите номер функции: ")
function_number = int(input())

print("Выбранная функция - " + functions[function_number - 1] + "\n")


# Выполнение 1 алгоритма
a, b = 0, 0

epsilon = 0.01
dist_const = epsilon / 10
k = 0

print('Введите x0:')
x0 = float(input())
print('Введите h:')
h = float(input())

a, b = first_algorithm.get_local_minimum(x0, h, function_number, a, b)
print(f'Найденный отрезок: [{a}, {b}]')


# Выполнение 2 алгоритма
fib_row, elements_count = fibonacci.build_fibonacci_row(a, b, epsilon)
x1, x2 = fibonacci.get_x1_x2(a, b, fib_row[elements_count - 1], fib_row[elements_count - 2], fib_row[elements_count - 3])

result = fibonacci.get_values(function_number, x1, x2, a, b, fib_row, elements_count, k, dist_const)
result_func, _ = fibonacci.get_function_values(function_number, result, 0)
print('------------------------------------')
print('Метод Фибоначчи')
print(f'x* = {result} \nf* = {result_func}')


# Выполнение 3 алгоритма
x1, x2, x3 = pauel.get_x_values(a, b)
result = pauel.get_value(function_number, x1, x2, x3, epsilon)
result_func, _ = fibonacci.get_function_values(function_number, result, 0)
print('------------------------------------')
print('Метод Пауэла')
print(f'x* = {result} \nf* = {result_func}')
