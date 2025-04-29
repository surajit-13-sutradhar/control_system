# Importing libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# Defining the differential equation
def diff_eqn(t, h, q_val):
    dhdt = -0.1 * h + 0.1 * q_val
    return dhdt

# Setting up the input functions
q0_values = np.linspace(0, 50, 101)

h0 = [0]

t_span = (0, 200)
t_eval = np.linspace(t_span[0], t_span[1], 500)

hss_values = []

# Looping over each input
for q_val in q0_values:
    # Solve the ONE
    sol = spi.solve_ivp(lambda t, h:diff_eqn(t, h, q_val), t_span, h0, t_eval=t_eval)

    # get the final height as steady-state value
    hss = sol.y[0][-1] # last value
    hss_values.append(hss)


hss_values = np.array(hss_values)

# Plotting input vs steady-state output
plt.figure(figsize=(12, 6))
plt.plot(q0_values, hss_values, marker='o', linestyle='-', color='blue')
plt.xlabel('Input Flow q0 (m³/s)')
plt.ylabel('Steady-State Height hss (m)')
plt.title('Input Flow vs Steady-State Tank Height')
plt.grid()
plt.show()