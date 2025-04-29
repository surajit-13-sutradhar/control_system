import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step

# Define the original transfer function G(s)
num_G = [0.2]
den_G = np.polymul([1, 0.25, 1], np.polymul([1, 2], [1, 3]))  # (s^2 + 0.25s + 1)(s+2)(s+3)
G = TransferFunction(num_G, den_G)

# First Approximation Ga(s) (only dominant complex conjugate poles)
num_Ga = [0.2]
den_Ga = [1, 0.25, 1]
Ga = TransferFunction(num_Ga, den_Ga)

# Second Approximation Gb(s) (adjusted model based on step response)
num_Gb = [0.2]
den_Gb = [1, 0.25, 1]
Gb = TransferFunction(num_Gb, den_Gb)

# Time array for simulation
t = np.linspace(0, 20, 1000)

# Step responses
t_G, y_G = step(G, T=t)
t_Ga, y_Ga = step(Ga, T=t)
t_Gb, y_Gb = step(Gb, T=t)

# Plotting
plt.figure(figsize=(12, 7))
plt.plot(t_G, y_G, label='Original System G(s)', color='blue', linewidth=2)
plt.plot(t_Ga, y_Ga, label='First Approximation Ga(s)', color='red', linestyle='--', linewidth=2)
plt.plot(t_Gb, y_Gb, label='Second Approximation Gb(s)', color='green', linestyle='-.', linewidth=2)

plt.title('Unit Step Response Comparison for New G(s)', fontsize=16)
plt.xlabel('Time (seconds)', fontsize=14)
plt.ylabel('Output', fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()
