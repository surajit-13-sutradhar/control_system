# Import required Python libraries
import numpy as np                     # Used for numerical operations (like working with arrays and complex numbers)
import matplotlib.pyplot as plt        # Used to plot graphs
import control as cntrl                # Used to work with control systems (transfer functions, poles, etc.)

# Define the transfer function G(s) = 28 / (s^3 + 10s^2 + 31s + 30)
# Numerator and Denominator of G(s)
numerator = [28]                       # 28 is the numerator constant
denominator = [1, 10, 31, 30]          # Coefficients of the polynomial in the denominator: s^3 + 10s^2 + 31s + 30

# Create a TransferFunction object G(s) using control library
G = cntrl.TransferFunction(numerator, denominator)

# Try different values of K to analyze how the system behaves when gain changes
K_values = [0.1, 1, 5, 10, 20, 50]     # These are the different gain values we'll test: low, medium, high

# A small helper function to decide system stability based on pole positions
def check_stability(poles):
    real_parts = [p.real for p in poles]  # Get real part of each pole
    if all(r < 0 for r in real_parts):    # If all real parts are negative
        return "Stable ✅"                # All poles are in left half → system is stable
    elif any(r > 0 for r in real_parts):  # If even one pole has positive real part
        return "Unstable ❌"              # System is unstable (pole in right half-plane)
    elif any(np.isclose(r, 0, atol=1e-5) for r in real_parts):  # If any pole lies very close to imaginary axis
        return "Marginally Stable ⚠️"    # Real part ≈ 0 → system is on the edge of stability
    else:
        return "Unknown"                 # Catch-all for any weird edge case

# Begin plotting the poles on a complex plane
plt.figure(figsize=(10, 6))  # Create a large plot window

# Loop through each value of K and analyze the poles
for K in K_values:
    KG = K * G  # Multiply G(s) by K → this gives the new transfer function K*G(s)
    poles = cntrl.poles(KG)  # Get the poles of the system (roots of the denominator)

    # Determine system stability for this K
    stability = check_stability(poles)

    # Print the poles and stability result in terminal
    print(f"K = {K}: Poles = {poles} => {stability}")

    # Plot the poles on the complex plane: Real vs Imaginary part
    plt.scatter([p.real for p in poles],  # X-axis: real part
                [p.imag for p in poles],  # Y-axis: imaginary part
                label=f'K={K} ({stability})',  # Legend label
                s=80)  # Size of the points

# Add a vertical line at Re(s) = 0 to indicate imaginary axis (boundary between stable and unstable)
plt.axvline(0, color='gray', linestyle='--', label='Imaginary Axis')

# Set plot titles and axis labels
plt.title('Pole Locations of K*G(s) for Various K')
plt.xlabel('Real')
plt.ylabel('Imaginary')
plt.grid(True)       # Add gridlines
plt.legend()         # Show legend for each K
plt.show()           # Display the final plot
