rt matplotlib.pyplot as plt
from scipy.integrate import solve_ivp
import control as ctrl
# control for system modelling

coeffs = [1, -6, 11, 6]
roots = np.roots(coeffs)
print("Roots", roots)

# Defining transfer 