import cec2017
import numpy as np
import numdifftools as nd

from matplotlib import pyplot as plt
from cec2017.functions import f1, f2, f3
UPPER_BOUND = 100
DIMENSIONALITY = 10


def booth_func(val):
    return pow(val[0]+2*val[1]-7, 2) + pow(2*val[0] + val[1] - 5, 2)


def create_plot(x, y, z, func):
    for i in range(x.shape[0]):
        for j in range(x.shape[1]):
            z[i, j] = func(np.array([x[i, j], y[i, j]]))
    return z


def gradient_ascent(func, lr, max_iter=1200, tol=0.000000001):
    x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY).astype("uint8")
    steps = [x]
    for i in range(max_iter):
        grad = nd.Gradient(func)(x)
        diff = lr*grad
        if np.abs(diff[0]) < tol and np.abs(diff[1]) < tol:
            break
        x = x - diff
        if x[0]>100 or x[1]>100:
            x = np.random.uniform(-UPPER_BOUND, UPPER_BOUND, size=DIMENSIONALITY).astype("uint8")
            lr /=2
        steps.append(x)
    return steps, x

working_func = f3

hist, x = gradient_ascent(working_func, 0.0000001)
print(len(hist), x)

MAX_X = 200
PLOT_STEP = 0.5

x_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
y_arr = np.arange(-MAX_X, MAX_X, PLOT_STEP)
X, Y = np.meshgrid(x_arr, y_arr)
Z = np.empty(X.shape)

Z = create_plot(X, Y, Z, working_func)
plt.contour(X, Y, Z, 20)
for i, point in enumerate(hist):
    try:
        plt.arrow(point[0], point[1], hist[i+1][0]-point[0], hist[i+1][1]-point[1], head_width=3, head_length=6, fc='k', ec='k')
    except:
        print("as")
plt.show()

