import numpy as np
import matplotlib.pyplot as plt
# from random import randint

# a = randint(0, 10)
# b = randint(0, 10)
# c = 0.5
# print(a, b, c)

x = np.arange(-2, 2.5, 0.5)  
y = np.arange(-2, 2.5, 0.5)
# x = np.arange(a, b, c)
# y = np.arange(a, b, c)
X, Y = np.meshgrid(x, y)

Z = X**2 + Y**2 + X*Y

fig = plt.figure()
ax = fig.add_subplot(111, projection='3d')
ax.plot_surface(X, Y, Z, cmap='inferno')

plt.savefig('plane.png')