import sympy
import numpy as np

x, y = sympy.symbols('x y')

t = [[0, 0, 2], [np.sqrt(10), 0, np.sqrt(10)]]

exp1 = (x**2 - 2*x*t[0][0] + t[0][0]**2) + (y**2 - 2*y*t[0][1] + t[0][1]**2) - t[0][2]**2
exp2 = (x**2 - 2*x*t[1][0] + t[1][0]**2) + (y**2 - 2*y*t[1][1] + t[1][1]**2) - t[1][2]**2

result = sympy.solve([exp1, exp2], [x, y])

