# importing libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Defining the series RLC circuit ODEs
def rlc_system(VC, t, R, L, C, Vin_func):
    dVC_dt = (Vin_func(t) - VC[0] / C - R * VC[1] / L) / L
    return [VC[1], dVC_dt]   # VC[0] is the voltage across the capacitor, VC[1] is the rate of change of the voltage (Essentially linked to the current in the circuit)

# Sinusoidal input function Vin(t) = 1 (unit step)
def Vin(t):
    return 1

# Parameters of the RLC circuit (constant R = 1)
R = 1

# Time span for simulation
t_span = np.linspace(0, 50, 1000)

# List to store different configurations of L and C
L_C_configurations = [
    {'L': 1, 'C': 1, 'omega_n': 1},    # Case 1
    {'L': 0.5, 'C': 1, 'omega_n': np.sqrt(2)},  # Case 2
    {'L': 2, 'C': 1, 'omega_n': 0.5}
]

# Plotting the system response for each case
plt.figure(figsize = (16, 9))
for config in L_C_configurations:
    L = config['L']
    C = config['C']
    omega_n = config['omega_n']

    # Solving the ODE
    initial_conditions = [0, 0] # Initially, VC = 0 and dVC/dt = 0
    solution = odeint(rlc_system, initial_conditions, t_span, args=(R, L, C, Vin))

    # Extracting output
    VC_output = solution[:, 0]

    # Plotting the response VC t for each case
    plt.plot(t_span, VC_output, label=f'L = {L} H, C = {C} F, ωn = {omega_n:.2f}')
    
# Add labels and legend
plt.xlabel('Time (t)')
plt.ylabel('Voltage across Capacitor VC(t)')
plt.title('System Response for Different Natural Frequencies (ωn)')
plt.legend()
plt.grid(True)
plt.show()



