# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import solve_ivp

def second_order_system(t, y, R, L, C):
    VC, dVC_dt = y  # VC is the voltage across capacito, dVC_dt is the derivative of it
    Vin = 1 if t > 0 else 0
    d2VC_dt2 = (Vin - R * dVC_dt - VC / C) / L # Second order differential equation
    return [dVC_dt, d2VC_dt2]

# Parameters for Case 1: Undamped System
R = 0
L = 1
C = 0.5

# Time span and initial conditions
t_span = (0, 50)
y0 = [0, 0]  # VC(0) = 0 and dVC/dt(0) = 0

# Solving the system
sol = solve_ivp(second_order_system, t_span, y0, args=(R, L, C), t_eval=np.linspace(0, 50, 1000))

# Extract the voltage across the capacitor VC from the solution
VC = sol.y[0]

# Peak overshoot calculation (Mp)
steady_state_value = VC[-1]
peak_value = np.max(VC)
Mp = (peak_value - steady_state_value)/ steady_state_value

# Settling Time (ts)
tolerance = 0.0001
ts = np.where(np.abs(VC - steady_state_value) < tolerance)[0][0] # FInd when VC is in 1 % of steady state

# Steady State Gain (K)
K = steady_state_value  # For a unit step input, the steady-state gain is the final value of VC

# Print the results
print(f"Peak Overshoot (Mp): {Mp:.2f}")
print(f"Settling Time (ts): {sol.t[ts]:.2f} seconds")
print(f"Steady-State Gain (K): {K:.2f} V")

# Plotting the response VC(t)
plt.figure(figsize=(10, 6))
plt.plot(sol.t, VC, label='Voltage across Capacitor (VC)', color='b')
plt.title('Undamped Series RLC Circuit Response to Unit Step Input')
plt.xlabel('Time (seconds)')
plt.ylabel('Voltage across Capacitor (V)')
plt.grid(True)
plt.legend()
plt.show()
