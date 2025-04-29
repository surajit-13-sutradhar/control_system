# To analyze the frequency response of the series RLC circuit, where we apply a sinusoidal input and measure the system's gain at different frequencies, we can follow these steps:

# 1. Define the series RLC circuit's transfer function.
# 2. Apply a sinusoidal input.
# 3. Calculate the gain for each frequency.
# 4. Plot the input and output sinusoidal waveforms for various frequencies.

# Importing Libraries
import numpy as np
import matplotlib.pyplot as plt
from scipy.integrate import odeint

# Defining the series RLC circuit ODEs
def rlc_system(VC, t, R, L, C, Vin_func):
    dVC_dt = (Vin_func(t) - VC[0] / C - R * VC[1] / L) / L
    return [VC[1], dVC_dt]

# Sinusoidal input function Vin(t) = Asin(ωt)
def Vin(t, A, omega):
    return A * np.sin(omega * t)

# Parameters of the RLC circuit
R = 1   # Resistance (ohms)
L = 1   # Inductance (H)
C = 1   # Capacitance (F)

# Frequency range to analyse
frequencies = np.linspace(0.1, 5, 50)

# Input amplitude A
A = 1

# Time span for simmulatiom
t_span = np.linspace(0, 50, 1000)

# Initialise lists to store gain and output responses
gains = []
output_responses = []

# Solve the system for each frequency
for omega in frequencies:
    # Solve the ODE
    initial_conditions = [0, 0]  # Initial VC(0) = 0, initial dVC/dt = 0
    solution = odeint(rlc_system, initial_conditions, t_span, args=(R, L, C, lambda t: Vin(t, A, omega)))


    # Calculate the gain
    vc_output = solution[:, 0]  # VC(t) (output voltage)
    vin_input = Vin(t_span, A, omega)  # Vin(t) (input voltage)
    gain = np.max(np.abs(vc_output)) / np.max(np.abs(vin_input))

    # Store gain and output for plotting
    gains.append(gain)
    output_responses.append(vc_output)

# Plot the frequency response (gain vs frequency)
plt.figure(figsize=(10, 6))
plt.plot(frequencies, gains, label='Gain G(ω)', color='blue')
plt.xlabel('Frequency (ω)')
plt.ylabel('Gain G(ω)')
plt.title('Frequency Response of Series RLC Circuit')
plt.grid()
plt.legend()
plt.show()

# Plot the input and output for the first frequency (just as an example)
plt.figure(figsize=(10, 6))
omega_example = frequencies[10]  # Pick an example frequency (e.g., 10th in the list)
output_example = output_responses[10]
input_example = Vin(t_span, A, omega_example)

plt.plot(t_span, input_example, label='Input Vin(t)', linestyle='--')
plt.plot(t_span, output_example, label='Output VC(t)', color='red')
plt.xlabel('Time (t)')
plt.ylabel('Voltage (V)')
plt.title(f'Input and Output for ω = {omega_example:.2f} rad/s')
plt.legend()
plt.grid()
plt.show()