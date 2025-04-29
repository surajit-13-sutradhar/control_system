# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# to generate random colours
import random

# define zero pairs in a two dimensional array
zeroes = [[-2 + 2j, -2 - 2j], [-0.5 + 2j, -0.5 - 2j], [2 + 2j, 2 - 2j]]

# define transfer function

# time vector
t = np.linspace(0, 40, 400)

# this is outside the loop so that the plots are drawn in the same graph
plt.figure(figsize=(16, 9))

for zero in zeroes:
    # defining the transfer function:= [(s + z[0])(s + z[1])] / [(s + 1)(s + 2)(s + 3)]
    G = ctrl.TransferFunction(np.polymul([1 , zero[0]], [1 , zero[1]]), np.polymul([1, 1], [1, 2], [1, 3]))
    t_out, y_out = ctrl.step_response(G, t)

    # plotting the graph
    # generating random colours
    random_colour = (random.random(), random.random(), random.random())
    plt.plot(t_out, y_out, label="Step Response", color=random_colour)


plt.title("Step & Impulse Response")
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.grid()
plt.show()
plt.legend()
