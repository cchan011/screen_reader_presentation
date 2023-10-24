import matplotlib
import random
import matplotlib.pyplot as plt
import numpy as np
import sympy as sp
import matplotlib.animation as animation
import time
import math

fig, ax = plt.subplots()
ax.set_xlim([-2, 4]) 
ax.set_ylim([-5, 5])
ax.set_title('Data point set 1 with best fit line')
ax.set_xlabel("x")
ax.set_ylabel("y")
ax.yaxis.set_label_coords(0.25, 0.7)
ax.spines['top'].set_color('none')
ax.spines['bottom'].set_position('zero')
ax.spines['left'].set_position('zero')
ax.spines['right'].set_color('none')

x = [-0.982, -0.86, 0, 1, 2, 3.48]
y = [-4, -2, 0, 0.693, 1.1, 1.5]

a = []
b = []

i = -0.982
while i < 3.48:
    j = math.log(i + 1)
    b.append(j)
    a.append(i)
    i += 0.01


ax.plot(x, y, "bo")
ax.plot(a, b, "b", linestyle = "dashed")

plt.show()