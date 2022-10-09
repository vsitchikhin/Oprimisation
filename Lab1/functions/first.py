import numpy as np
import sympy as sp

function = "(x - 1)^2"

def function_value(x, h=0):
  return pow((x + h - 1), 2)
