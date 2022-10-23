import numpy as np

function = "x + 3/x^2"

def function_value(x, h=0):
  if pow(x + h, 2) == 0:
    return np.inf
  value = 0
  value += x + h
  value += 3 / (pow(x + h, 2))
  return value
