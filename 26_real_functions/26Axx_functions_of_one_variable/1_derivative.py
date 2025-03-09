# %%
import numpy as np
import matplotlib.pyplot as plt


# %%
def f(x):
    return x**2 + 2


# %%
x_values = np.arange(0, 10, 1)
y_values = f(x_values)
y_values


# %%
def tangent_line(x):
    return 2 * x ** (2 - 1) + 2


# %%
tangent_line_x_values = np.arange(0, 10, 1)
tangent_line_y_values = tangent_line(x_values)
tangent_line_y_values

# %%
plt.plot(x_values, y_values)
plt.plot(tangent_line_x_values, tangent_line_y_values)

# %%
