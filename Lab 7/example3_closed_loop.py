import numpy as np
import matplotlib.pyplot as plt
import control as cntrl

# Define the plant G(s)
numerator = [28]
denominator = [1, 10, 31, 30]
G = cntrl.TransferFunction(numerator, denominator)

# Time vector for simulation
time = np.linspace(0, 7, 1000)

# Different gain values to analyze
K_values = [0.0225, 1, 3]
colors = ['tab:blue', 'tab:orange', 'tab:green']

# Plotting the step responses
plt.figure(figsize=(10, 6))

for K, color in zip(K_values, colors):
    # Closed-loop transfer function: KG / (1 + KG)
    KG = K * G
    T_closed = cntrl.feedback(KG, 1)  # unity feedback means second arg is 1

    # Step response
    T, y_out = cntrl.step_response(T_closed, T=time)
    plt.plot(T, y_out, label=f'K = {K}', color=color)
    

    u = np.ones_like(T)
    error = u - y_out
    plt.plot(T, u, label=f'K = {K}', color=color)
    plt.plot(T, error, label=f'K = {K}', color=color)

# Labels and plot formatting
plt.title(r'Step Response of Unity Feedback System $G(s)$')
plt.xlabel('Time (seconds)')
plt.ylabel('Response')
plt.grid(True)
plt.legend()
plt.tight_layout()

# Optionally, display the transfer function in the plot
plt.text(3.5, 0.2, r'$G(s) = \frac{28}{s^3 + 10s^2 + 31s + 30}$', fontsize=12, bbox=dict(facecolor='white', edgecolor='gray'))

plt.show()
