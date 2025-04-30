import numpy as np
import matplotlib.pyplot as plt
import control as cntrl

# Define the transfer function G(s) = 28 / (s^3 + 10s^2 + 31s + 30)
numerator = [28]
denominator = [1, 10, 31, 30]
G = cntrl.TransferFunction(numerator, denominator)

# Define gain values to analyze
K_values = [0.225, 1, 3]

# Time vector for simulation (from 0 to 10 seconds, with 1000 steps)
time = np.linspace(0, 10, 1000)

# Create a new plot
plt.figure(figsize=(12, 8))

# Loop over different values of K to plot their step response and error
for K in K_values:
    KG = K * G                      # Multiply transfer function by gain
    T, y_out = cntrl.step_response(KG, T=time)  # Step response of K*G(s)

    u = np.ones_like(T)             # Step input (u(t) = 1 for all t)
    error = u - y_out               # Error = Input - Output

    # Plot output and error
    plt.plot(T, y_out, label=f'Output (K={K})')
    plt.plot(T, error, '--', label=f'Error (K={K})')

# Plot the input signal
plt.plot(time, np.ones_like(time), 'k--', linewidth=1.5, label='Step Input')

# Graph details
plt.title('Step Response and Error for K * G(s)')
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
