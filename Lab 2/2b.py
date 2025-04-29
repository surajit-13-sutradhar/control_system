# imported libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy.integrate as spi

# defining the differential equation
def diff_eqn(t, h, q_func):
    q = q_func(t)
    dhdt = -0.1 * h + 0.1 * q
    return dhdt

# defining the function q(t)
def step_input(t):
    return 11 if t >= 0 else 0

def ramp_input(t):
    return t if t>=0 else 0

def impulse_input(t):
    return 100 if -0.01 <= t <= 0.01 else 0

def sinusoidal_input(t):
    return 10 * np.sin(t) 


# mapping cases to functions
input_functions = [step_input, ramp_input, impulse_input, sinusoidal_input]
input_labels = ["Unit Step", "Ramp", "Impulse", "Sinusoidal"]

# defining the initial conditions
h0 = [10]

# time span
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 500)

# plotting each case
for i in range(len(input_functions)):
    q_func = input_functions[i]

    # solving the differential equation
    sol = spi.solve_ivp(lambda t, h:diff_eqn(t, h, q_func), t_span, h0, t_eval=t_eval)

    t = sol.t
    h = sol.y[0]

    # plotting
    plt.figure(figsize=(12, 6))
    plt.plot(t, h, label=f'{input_labels[i]}', color='blue')
    plt.xlabel('Time (t) [sec]')
    plt.ylabel('Tank Height h(t) [m]')
    plt.title(f'Single-Tank System Response: {input_labels[i]}')
    plt.grid()
    plt.legend()
    plt.show()


