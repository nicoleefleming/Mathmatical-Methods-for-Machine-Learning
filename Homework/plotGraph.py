import math

import inline as inline
import matplotlib
from mpl_toolkits import mplot3d

import numpy as np
import matplotlib.pyplot as plt
#from lpsolve55 import *
import pip

#path = 'C:\Users\nefle\Downloads\lpsolve55‑5.5.2.5‑cp35‑cp35m‑win_amd64.whl'

def f(x, y):
    return (x-1)**2 + (y-2)**2

x = np.linspace(-10, 10, 10)
y = np.linspace(-10, 10, 10)

X, Y = np.meshgrid(x, y)
Z = f(X, Y)

fig = plt.figure()
ax = plt.axes(projection='3d')
ax.contour3D(X, Y, Z, 50, cmap='binary')
#ax = plt.axes(projection='3d')
#ax.plot_surface(X, Y, Z, rstride=1, cstride=1,
#                cmap='viridis', edgecolor='none')
ax.set_xlabel('x')
ax.set_ylabel('y')
ax.set_zlabel('z');

plt.show()