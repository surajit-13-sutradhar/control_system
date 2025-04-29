import numpy as np
import control as ctrl

roots = np.roots([1, 390, 49329, 2516020, 51819500, 359450000, 87000000])
print("the roots are:", roots)


# to find the minimum root magnitude
magnitudes = np.abs(roots)
min_magnitude = np.min(magnitudes)

# find dominant roots
dominant_roots = [np.round(root, 7) for root in roots if np.abs(root) <= 5 * min_magnitude]

print("the dominant roots are", dominant_roots)

G = ctrl.TransferFunction([1], [dominant_roots[0], 1])

t1, y1 = ctrl.step_response(G)