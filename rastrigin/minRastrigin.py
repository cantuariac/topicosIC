
import math
import numpy as np
from scipy.optimize import differential_evolution

def rastrigin(X):
	return 10*len(X) + sum([(x**2 - 10 * np.cos(2 * math.pi * x)) for x in X])

limites = [(-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12), (-5.12, 5.12)]

result = differential_evolution(rastrigin, limites)

print(rastrigin([0,0,0,0]))
print(result.x)
print(result.fun)
