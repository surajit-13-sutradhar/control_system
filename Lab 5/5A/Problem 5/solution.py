# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# System parameters
zeta = 0.215
omega_n = 1.608

# Transfer function
num = [-omega_n**2]
den = [1, 2*zeta*omega_n, omega_n**2]
G = ctrl.TransferFunction(num, den)

# Time vector
t = np.linspace(0, 10, 500)
t, y = ctrl.step_response(G, t)

# Plot
plt.figure(figsize=(10,6))
plt.plot(t, np.ones_like(t), 'b--', label='System Input (unit step u(0)=0)')
plt.plot(t, y, 'r-', linewidth=2, label='System Output')

plt.title('Comparison: Step Response of Negative Gain Second-Order System')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()
plt.show()
