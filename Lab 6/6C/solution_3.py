import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Time vector
T = np.linspace(0, 10, 1000)

# Define transfer function G(s) = 100 / s^2(s + 3)
G = ctrl.TransferFunction([50], np.polymul([1, 0, 0], [1, 4]))

# ---------------- STEP RESPONSE ----------------
# Input: Unit step
U_step = np.ones_like(T)
t_step, y_step = ctrl.forced_response(G, T, U_step)
e_step = U_step - y_step

plt.figure(figsize=(12, 6))
plt.plot(T, U_step, '--', label="Unit Step Input")
plt.plot(t_step, y_step, label="Step Output")
plt.plot(T, e_step, label="Error e(t)")
plt.title("Step Response and Error")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# ---------------- RAMP RESPONSE ----------------
# Input: Ramp (slope = 1)
U_ramp = T
t_ramp, y_ramp = ctrl.forced_response(G, T, U_ramp)
e_ramp = U_ramp - y_ramp

plt.figure(figsize=(12, 6))
plt.plot(T, U_ramp, '--', label="Ramp Input")
plt.plot(t_ramp, y_ramp, label="Ramp Output")
plt.plot(T, e_ramp, label="Error e(t)")
plt.title("Ramp Response and Error")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()

# ---------------- PARABOLIC RESPONSE ----------------
# Input: Parabolic
U_parabolic = pow(T, 2)
t_parabolic, y_parabolic = ctrl.forced_response(G, T, U_parabolic)
e_parabolic = U_parabolic - y_parabolic

plt.figure(figsize=(12, 6))
plt.plot(T, U_parabolic, '--', label="Parabolic Input")
plt.plot(t_parabolic, y_parabolic, label="Parabolic Output")
plt.plot(T, e_parabolic, label="Error e(t)")
plt.title("Parabolic Response and Error")
plt.xlabel("Time")
plt.ylabel("Amplitude")
plt.grid(True)
plt.legend()
plt.show()
