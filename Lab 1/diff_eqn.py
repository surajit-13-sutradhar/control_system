# importing libraries
import numpy as np
import matplotlib.pyplot as plt
import scipy

# Defining the differential equation
def diff_eqn(t, y, u_func):
    u = u_func(t)
    dydt = -0.1 * y + 0.1 * u
    return dydt

# Defining the input function u(t)
def u_func(t):
    return 20 if t > 0 else 10

# Initial condition
y0 = [10]

# Time span of the simulation
t_span = (0, 100)
t_eval = np.linspace(t_span[0], t_span[1], 500) # generate 500 points between 0 and 100 using numpy.linspace

# Solving the differential equation using scipy's solve_ivp
sol = scipy.integrate.solve_ivp(diff_eqn, t_span, y0, args=(u_func,), t_eval=t_eval)

# Plotting the results
plt.figure(figsize=(16, 9))
plt.plot(sol.t, sol.y[0], label='y(t)', color='blue')
plt.xlabel('Time (t)')
plt.ylabel('y(t)')
plt.title('Solution of the Differential Equation')
plt.grid()
plt.legend()
plt.show()