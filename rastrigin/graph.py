import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from matplotlib import cm
import math
import numpy as np

def rosen(parametros):
    x1,x2 = parametros
    """função Rosenbrock"""
    return 100.0*(x1-x2**2)**2.0 + (x2-1)**2

def rastrigin(X, A=10):
	#A = kwargs.get('A', 10)
	return A + sum([(x**2 - A * np.cos(2 * math.pi * x)) for x in X])

X = np.linspace(-4, 4, 200)    
Y = np.linspace(-4, 4, 200) 
X, Y = np.meshgrid(X, Y)

Z = rastrigin([X, Y], A=10)

fig = plt.figure()
ax = fig.gca(projection='3d')

ax.plot_surface(X, Y, Z, rstride=1, cstride=1, cmap=cm.plasma, linewidth=0, antialiased=False) 
plt.show()

