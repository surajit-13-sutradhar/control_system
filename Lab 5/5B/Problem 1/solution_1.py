import numpy as np
import matplotlib.pyplot as plt
from scipy.signal import TransferFunction, step

# Define the original transfer function G(s)
num_G = [10]
den_G = np.polymul([1, 1], np.polymul([1, 5], [1, 10]))  
G = TransferFunction(num_G, den_G)

# Define the approximate first-order transfer function Ga(s)
num_Ga = [0.2]
den_Ga = [1, 1] 
Ga = TransferFunction(num_Ga, den_Ga)

# Define the approximate second-order transfer function Gb(s)
num_Gb = [1]
den_Gb = np.polymul([1, 1], [1, 5])  
Gb = TransferFunction(num_Gb, den_Gb)

# Time array for simulation
t = np.linspace(0, 10, 500)

# Step responses
t_G, y_G = step(G, T=t)
t_Ga, y_Ga = step(Ga, T=t)
t_Gb, y_Gb = step(Gb, T=t)

# Plotting
plt.figure(figsize=(10, 6))
plt.plot(t_G, y_G, label='Original System G(s)', color='blue', linewidth=2)
plt.plot(t_Ga, y_Ga, label='First-Order Approximation Ga(s)', color='red', linestyle='--', linewidth=2)
plt.plot(t_Gb, y_Gb, label='Second-Order Approximation Gb(s)', color='green', linestyle='-.', linewidth=2)

plt.title('Unit Step Response Comparison', fontsize=16)
plt.xlabel('Time (seconds)', fontsize=14)
plt.ylabel('Output', fontsize=14)
plt.grid(True)
plt.legend(fontsize=12)
plt.show()
