function = "x + 3/x^2"

def function_value(x, h=0):
  value = 0
  value += x + h
  value += 3 / (pow(x + h, 2))
  return value
