import numpy as np
import sympy as sp

function = "4x^3 - 8x^2 - 11x + 5"


def function_value(x, h=0):
  value = 0
  value += 4 * pow(x + h, 3)
  value -= 8 * pow(x + h, 2)
  value -= 11 * (x + h)
  value += 5
  return value
