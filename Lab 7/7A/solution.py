import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# --- CASE 1: G(s) = 1 / (s + a) ---
a_values = [5, 0, -5]

plt.figure(figsize=(15, 4))
for i, a in enumerate(a_values, 1):
    G1 = ctrl.TransferFunction([1], [1, a])
    plt.subplot(1, 3, i)
    
    roots, gains = ctrl.root_locus(G1, plot=False)
    for j in range(roots.shape[1]):
        plt.plot(roots[:, j].real, roots[:, j].imag, 'b', linewidth=2.5)
    plt.plot(np.real(G1.poles()), np.imag(G1.poles()), 'rx', markersize=10, label='Pole')
    plt.title(f"G(s) = 1/(s + {a})")
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.xlim(-10, 10)
    plt.ylim(-5, 5)
    plt.legend()

plt.tight_layout()
plt.suptitle("Root Locus for G(s) = 1/(s + a)", fontsize=16, y=1.05)
plt.show()


# --- CASE 2: G(s) = (s + b) / (s + 5) ---
b_values = [-2, 0, 2]

plt.figure(figsize=(15, 4))
for i, b in enumerate(b_values, 1):
    G2 = ctrl.TransferFunction([1, b], [1, 5])
    plt.subplot(1, 3, i)
    roots, gains = ctrl.root_locus(G2, plot=False)
    for j in range(roots.shape[1]):
        plt.plot(roots[:, j].real, roots[:, j].imag, 'b', linewidth=2.5)
    plt.plot(np.real(G2.poles()), np.imag(G2.poles()), 'rx', markersize=10, label='Pole')
    plt.plot(np.real(G2.zeros()), np.imag(G2.zeros()), 'go', markersize=10, label='Zero')
    plt.title(f"G(s) = (s + {b}) / (s + 5)")
    plt.axhline(0, color='black', linewidth=0.8)
    plt.axvline(0, color='black', linewidth=0.8)
    plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
    plt.xlabel("Real Axis")
    plt.ylabel("Imaginary Axis")
    plt.xlim(-10, 5)
    plt.ylim(-5, 5)
    plt.legend()

plt.tight_layout()
plt.suptitle("Root Locus for G(s) = (s + b)/(s + 5)", fontsize=16, y=1.05)
plt.show()