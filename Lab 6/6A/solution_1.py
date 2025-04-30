# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# define zeroes array
zeroes = [-5, -3, -1, 0, 1, 3, 5]

# define transfer function

# time vector
t = np.linspace(0, 40, 400)

# this is outside the loop so that the plots are drawn in the same graph
plt.figure(figsize=(16, 9))

for zero in zeroes:
    # defining the transfer function
    G = ctrl.TransferFunction([1, zero], [1, 5, 6])
    t_out, y_out = ctrl.step_response(G, t)

    # plotting the graph
    plt.plot(t_out, y_out, label="Step Response", color="blue")
    plt.title("Step & Impulse Response")
    plt.xlabel("Time (s)")
    plt.ylabel("Response")
    plt.grid()
    plt.show()

plt.legend()
