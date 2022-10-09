# import methods.SearchSegment
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

algorithms = [
  "Поиск отрезка локализации минимума",
  "Метод Фибоначчи",
  "Метод параболической аппроксимации Пауэлла"
]

print("Доступные функции:")
for i in range(len(functions)):
  print(str(i + 1) + " - " + functions[i])

print("Введите номер функции: ")
function_number = input()
function_number = int(function_number)

print("Ваша функция - " + functions[function_number - 1] + "\n")

print("Доступные алгоритмы:")
for i in range(len(algorithms)):
  print(str(i + 1), " - " + algorithms[i])

print("Введите номер алгоритма:")
algorithm_number = input()
algorithm_number = int(algorithm_number)

print("Ваш алгоритм - " + algorithms[algorithm_number - 1] + "\n")

if algorithm_number == 1:
  a, b = 0, 0
  
  print('Введите x0:')
  x0 = float(input())
  print('Введите h:')
  h = float(input())
  
  a, b = first_algorithm.get_local_minimum(x0, h, function_number, a, b)
  print(f'Найденный отрезок: [{a}, {b}]')
  
elif algorithm_number == 2:
  print("Введите epsilon:")
  epsilon = float(input())
  print("Введите a:")
  a = float(input())
  print("Введите b:")
  b = float(input())
  
  dist_const = epsilon / 10
  k = 0
  fib_row, elements_count = fibonacci.build_fibonacci_row(a, b, epsilon)
  x1, x2 = fibonacci.get_x1_x2(a, b, fib_row[elements_count - 1], fib_row[elements_count - 2], fib_row[elements_count - 3])

  result = fibonacci.get_values(function_number, x1, x2, a, b, fib_row, elements_count, k, dist_const)
  result_f, _ = fibonacci.get_function_values(function_number, result, 0)
  print(f'x* = {result} \nf* = {result_f}')
  
elif algorithm_number == 3:
  print("Введите epsilon:")
  epsilon = float(input())
  print("Введите a:")
  a = float(input())
  print("Введите b:")
  b = float(input())
  
  x1, x2, x3 = pauel.get_x_values(a, b)
  result = pauel.get_value(function_number, x1, x2, x3, epsilon)
  result_func, _ = fibonacci.get_function_values(function_number, result, 0)
  print(f'x* = {result} \nf* = {result_func}')
else:
  print("Данного алгоритма не существу")