import matplotlib.pyplot as plt
import numpy as np

# Values of K
K_values = [0, 0.02254, 1, 6, 8, 10, 12, 20, 50]

# Store root trajectories
all_roots = []

for K in K_values:
    # Coefficients of the cubic polynomial: s^3 + 10s^2 + 31s + (30 + 28K)
    coeffs = [1, 10, 31, 30 + 28 * K]
    roots = np.roots(coeffs)
    all_roots.append(roots)

# Transpose list of roots to group Root 1s, Root 2s, Root 3s
root_groups = list(zip(*all_roots))

# Plotting
plt.figure(figsize=(10, 6))
colors = ['blue', 'green', 'red']
labels = ['Root 1', 'Root 2', 'Root 3']

for i, roots in enumerate(root_groups):
    real_parts = [r.real for r in roots]
    imag_parts = [r.imag for r in roots]
    plt.plot(real_parts, imag_parts, 'o-', label=labels[i], color=colors[i])

# Format plot
plt.axhline(0, color='black', linestyle='--', linewidth=0.8)
plt.axvline(0, color='black', linestyle='--', linewidth=0.8)
plt.xlabel('Real Axis')
plt.ylabel('Imaginary Axis')
plt.title('Root Movement vs K for $s^3 + 10s^2 + 31s + (30 + 28K) = 0$')
plt.grid(True)
plt.legend()
plt.tight_layout()
plt.show()
