import numpy as np
import cmake_mlat
import matplotlib.pyplot as plt

references = np.array([
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
])

error_data = []

for i in range(11):
    for j in range(11):
        for k in range(11):
            true_point = np.array([i/10, j/10, k/10], dtype=np.float64)
            ranges = cmake_mlat.find_ranges(true_point, references)
            estimated_point = cmake_mlat.find_point(references, ranges)
            scalar_error = cmake_mlat.find_scalar_error(true_point, estimated_point)
            error_data.append(scalar_error)
n = len(error_data)

plt.figure()
plt.hist(error_data, bins=25)
plt.xlabel("Scalar Error")
plt.ylabel("Count")
plt.title(f"Scalar Error Distribution (n = {n})")
plt.ticklabel_format(axis='x', style='sci', scilimits=(0, 0))
plt.show()
