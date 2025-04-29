import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# given system in first order
K = 1
tau = 4
G1 = ctrl.tf([K], [tau, 1])

# Second-order model
wn = 0.2
zeta = 1
G2 = ctrl.tf([wn**2], [1, 2*zeta*wn, wn**2])

# time vector
t = np.linspace(0, 40, 400)

# Step responses
t1, y1 = ctrl.step_response(G1, t)
t2, y2 = ctrl.step_response(G2, t)

# Plot
plt.figure(figsize=(10,6))
plt.plot(t, np.ones_like(t), 'b--', label='System Input (unit step)')
plt.plot(t1, y1, 'r-', linewidth=2, label='First-order Model Output')
plt.plot(t2, y2, 'g--', linewidth=2, label='Second-order Model Output')

plt.title('Comparison: Step Response of Approximate Models')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()
plt.show()