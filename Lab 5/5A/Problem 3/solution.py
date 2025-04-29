# import libraries
import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# first order system parameters
K = -1
tau = 3
G = ctrl.TransferFunction([K], [tau, 1])

# time vector
t = np.linspace(0, 30, 400)

# step response
t_out, y_out = ctrl.step_response(G, t)

# plot
plt.figure(figsize=(16, 9))
plt.plot(t, np.ones_like(t) * 11, 'b--', label="System Input (unit step u(0)=10 shifted)")
plt.plot(t_out, y_out + 10, 'r-', linewidth=2, label='First-order Model Output')  # shifted by initial value

plt.title('Comparision: Step response of Approximate first order model')
plt.xlabel('Time (s)')
plt.ylabel('Magnitude')
plt.grid(True)
plt.legend()
plt.show()

