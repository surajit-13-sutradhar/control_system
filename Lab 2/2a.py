# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# defining the differential equation
def diff_eqn(t, h, q_value):
    dhdt = -0.1 * h + 0.1 * q_value
    return dhdt

# defining the function q(t)
# First declare an aray with different values of q[0]
q_steps = np.array([11, 20, 7, 1, 0])

# defining the initial conditions
h0 = [10] 

# defning the time span for the simulation
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 500)

# thresholds as percentages
thresholds = np.array[63.2, 86.5, 95.0, 98.2, 99.3]


for i in range(len(q_steps)):
    q_value = q_steps[i]  # pick current step input value
    
    # solve the differential equation
    sol = spi.solve_ivp(lambda t, h: diff_eqn(t, h, q_value), t_span, h0, t_eval=t_eval)

    t = sol.t
    h = sol.y[0]

    # final steady state height
    h_ss = h[-1] # last value at final time
    delta_h = h_ss - h[0]  # total change
    K = delta_h / (q_value - 10) if (q_value - 10) !=0 else 0  # steady state gain
    
    # now for each case, make a separate figure
    plt.figure(figsize=(12, 6))
    plt.plot(sol.t, sol.y[0], label=f'q₀(t=0⁺) = {q_value} m³/s', color='blue')
    
    plt.xlabel("Time (t)")
    plt.ylabel("Tank Level h(t) [m]")
    plt.title(f"Single-Tank System Response for Step Input: q₀ = {q_value} m³/s")
    plt.grid()
    plt.legend()
    plt.show()
