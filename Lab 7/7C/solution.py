import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

# Create a figure with 7 subplots (one for each G(s))
plt.figure(figsize=(15, 12))

# --- CASE 1: G(s) = (s + 5) / (s^2 + 25) ---
G1 = ctrl.TransferFunction([1, 5], [1, 0, 25])  # (s + 5) / (s^2 + 25)
plt.subplot(3, 3, 1)
roots, gains = ctrl.root_locus(G1, plot=False)
for j in range(roots.shape[1]):
    plt.plot(roots[:, j].real, roots[:, j].imag, 'r', linewidth=2.5)
plt.plot(np.real(G1.poles()), np.imag(G1.poles()), 'rx', markersize=10, label='Poles')
plt.plot(np.real(G1.zeros()), np.imag(G1.zeros()), 'go', markersize=10, label='Zeros')
plt.title("G(s) = (s + 5) / (s² + 25)")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.xlim(-10, 10)
plt.ylim(-15, 15)
plt.legend()

# --- CASE 2: G(s) = (s - 5) / (s^2 + 25) ---
G2 = ctrl.TransferFunction([1, -5], [1, 0, 25])  # (s - 5) / (s^2 + 25)
plt.subplot(3, 3, 2)
roots, gains = ctrl.root_locus(G2, plot=False)
for j in range(roots.shape[1]):
    plt.plot(roots[:, j].real, roots[:, j].imag, 'b', linewidth=2.5)
plt.plot(np.real(G2.poles()), np.imag(G2.poles()), 'rx', markersize=10, label='Poles')
plt.plot(np.real(G2.zeros()), np.imag(G2.zeros()), 'go', markersize=10, label='Zeros')
plt.title("G(s) = (s - 5) / (s² + 25)")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.xlim(-10, 10)
plt.ylim(-15, 15)
plt.legend()

# --- CASE 3: G(s) = (s + 10) / (s + 5)^2 ---
G3 = ctrl.TransferFunction([1, 10], [1, 10, 25])  # (s + 10) / (s + 5)^2
plt.subplot(3, 3, 3)
roots, gains = ctrl.root_locus(G3, plot=False)
for j in range(roots.shape[1]):
    plt.plot(roots[:, j].real, roots[:, j].imag, 'b', linewidth=2.5)
plt.plot(np.real(G3.poles()), np.imag(G3.poles()), 'rx', markersize=10, label='Poles')
plt.plot(np.real(G3.zeros()), np.imag(G3.zeros()), 'go', markersize=10, label='Zeros')
plt.title("G(s) = (s + 10) / (s + 5)²")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.xlim(-15, 5)
plt.ylim(-10, 10)
plt.legend()

# --- CASE 4: G(s) = (s + 4)(s + 2) / (s + 5)(s + 1) ---
G4 = ctrl.TransferFunction([1, 6, 8], [1, 6, 5])  # (s + 4)(s + 2) / (s + 5)(s + 1)
plt.subplot(3, 3, 4)
roots, gains = ctrl.root_locus(G4, plot=False)
for j in range(roots.shape[1]):
    plt.plot(roots[:, j].real, roots[:, j].imag, 'b', linewidth=2.5)
plt.plot(np.real(G4.poles()), np.imag(G4.poles()), 'rx', markersize=10, label='Poles')
plt.plot(np.real(G4.zeros()), np.imag(G4.zeros()), 'go', markersize=10, label='Zeros')
plt.title("G(s) = (s + 4)(s + 2) / (s + 5)(s + 1)")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.xlim(-10, 5)
plt.ylim(-5, 5)
plt.legend()

# --- CASE 5: G(s) = (s + 10)(s - 10) / (s + 5)(s + 1) ---
G5 = ctrl.TransferFunction([1, 0, -100], [1, 6, 5])  # (s + 10)(s - 10) / (s + 5)(s + 1)
plt.subplot(3, 3, 5)
roots, gains = ctrl.root_locus(G5, plot=False)
for j in range(roots.shape[1]):
    plt.plot(roots[:, j].real, roots[:, j].imag, 'b', linewidth=2.5)
plt.plot(np.real(G5.poles()), np.imag(G5.poles()), 'rx', markersize=10, label='Poles')
plt.plot(np.real(G5.zeros()), np.imag(G5.zeros()), 'go', markersize=10, label='Zeros')
plt.title("G(s) = (s + 10)(s - 10) / (s + 5)(s + 1)")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.xlim(-15, 15)
plt.ylim(-10, 10)
plt.legend()

# --- CASE 6: G(s) = (s + 10)(s - 10) / (s + 5)(s - 1) ---
G6 = ctrl.TransferFunction([1, 0, -100], [1, 4, -5])  # (s + 10)(s - 10) / (s + 5)(s - 1)
plt.subplot(3, 3, 6)
roots, gains = ctrl.root_locus(G6, plot=False)
for j in range(roots.shape[1]):
    plt.plot(roots[:, j].real, roots[:, j].imag, 'b', linewidth=2.5)
plt.plot(np.real(G6.poles()), np.imag(G6.poles()), 'rx', markersize=10, label='Poles')
plt.plot(np.real(G6.zeros()), np.imag(G6.zeros()), 'go', markersize=10, label='Zeros')
plt.title("G(s) = (s + 10)(s - 10) / (s + 5)(s - 1)")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.xlim(-15, 15)
plt.ylim(-10, 10)
plt.legend()

# --- CASE 7: G(s) = (s^2 + s + 16) / (s^2 + 5s + 25) ---
G7 = ctrl.TransferFunction([1, 1, 16], [1, 5, 25])  # (s^2 + s + 16) / (s^2 + 5s + 25)
plt.subplot(3, 3, 7)
roots, gains = ctrl.root_locus(G7, plot=False)
for j in range(roots.shape[1]):
    plt.plot(roots[:, j].real, roots[:, j].imag, 'b', linewidth=2.5)
plt.plot(np.real(G7.poles()), np.imag(G7.poles()), 'rx', markersize=10, label='Poles')
plt.plot(np.real(G7.zeros()), np.imag(G7.zeros()), 'go', markersize=10, label='Zeros')
plt.title("G(s) = (s² + s + 16) / (s² + 5s + 25)")
plt.axhline(0, color='black', linewidth=0.8)
plt.axvline(0, color='black', linewidth=0.8)
plt.grid(True, linestyle="--", linewidth=0.7, alpha=0.7)
plt.xlabel("Real Axis")
plt.ylabel("Imaginary Axis")
plt.xlim(-10, 5)
plt.ylim(-10, 10)
plt.legend()

# Adjust layout and add a super title
plt.tight_layout()
plt.suptitle("Root Locus Plots for Given Transfer Functions", fontsize=16, y=1.05)
plt.show()