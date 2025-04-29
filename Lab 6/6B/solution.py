import numpy as np
import matplotlib.pyplot as plt
import control as ctrl

def first_order_pade_approximation(T):
    return ([-T/2, 1], [T/2, 1])

num_pade, den_pade = first_order_pade_approximation(2.5)

tf_den = [5, 1]

# multiplying numerator by 1.4
num_scaled = [coeff * 1.4 for coeff in num_pade]

final_den = np.polymul(den_pade, tf_den)

# final transder function
G = ctrl.TransferFunction(num_scaled, final_den)

# getting unit step response
t_out, y_out = ctrl.step_response(G)

# plotting the graph
# Plot the response
plt.figure(figsize=(10, 6))
plt.plot(t_out, y_out, 'b-', linewidth=2)
plt.grid(True)
plt.xlabel('Time (seconds)')
plt.ylabel('Amplitude')
plt.title('Step Response of G(s) = 1.4(1-1.25s)/((1+1.25s)(5s+1))')
plt.legend()
plt.show()