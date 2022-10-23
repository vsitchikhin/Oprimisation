import numpy as np

function = "(x + 2,5)/(4 - x^2)"

def function_value(x, h=0):
  if 4 - pow(x + h, 2) != 0:
    return (x + h + 2.5) / (4 - pow(x + h, 2))
  else:
    x += 0.0000000001
    return (x + h + 2.5) / (4 - pow(x + h, 2))
