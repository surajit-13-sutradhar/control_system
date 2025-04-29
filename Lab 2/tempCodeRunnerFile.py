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