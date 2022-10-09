from math import sin
function = "-sin(x) - (sin(3x))/3"

def function_value(x, h=0):
  value = 0
  value += -sin(x + h)
  value -= (sin(3 * (x + h))) / 3
  return value

