# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import control as ctrl
# control for system modelling

coeffs = [1, -6, 11, 6]
roots = np.roots(coeffs)
print("Roots", roots)

# Defining transfer function
num = [1]
den = [1, 0.1]

# Finding pole locations
root = np.roots(den)
print("Poles:", roots)

# Finding Settling time
t_settling = 5 / abs(root)
print("Settling time", t_settling)

# Steady state value
steady_value = 1/ den[1]
print("Steady state value:", steady_value)

# Defining the transfer function using the given numerator and denominator
system = ctrl.TransferFunction(num, den)

# For step response
t_step, y_step = ctrl.step_response(system)

# For impulse response
t_impulse, y_impulse = ctrl.impulse_response(system)

plt.figure()
plt.plot(t_step, y_step, label="Step Response", color="blue")
plt.plot(t_impulse, y_impulse, label="Impulse Response", color="red")
plt.title("Step & Impulse Response")
plt.xlabel("Time (s)")
plt.ylabel("Response")
plt.grid()
plt.show()
