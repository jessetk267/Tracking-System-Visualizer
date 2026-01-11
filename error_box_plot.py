import numpy as np
import cmake_mlat
import matplotlib.pyplot as plt

references1 = np.array([
    [0, 0, 0],
    [1, 0, 1],
    [0, 1, 1],
    [1, 1, 0]
])

references2 = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

error_data1 = []

for i in range(11):
    for j in range(11):
        for k in range(11):
            true_point = np.array([i/10, j/10, k/10], dtype=np.float64)
            ranges = cmake_mlat.find_ranges(true_point, references1)
            estimated_point = cmake_mlat.find_point(references1, ranges)
            scalar_error = cmake_mlat.find_scalar_error(true_point, estimated_point)
            error_data1.append(scalar_error)
n = len(error_data1)

error_data2 = []

for i in range(11):
    for j in range(11):
        for k in range(11):
            true_point = np.array([i/10, j/10, k/10], dtype=np.float64)
            ranges = cmake_mlat.find_ranges(true_point, references2)
            estimated_point = cmake_mlat.find_point(references2, ranges)
            scalar_error = cmake_mlat.find_scalar_error(true_point, estimated_point)
            error_data2.append(scalar_error)

data = [error_data1, error_data2]

plt.figure()
plt.boxplot(data)
plt.xticks([1, 2], ["Regular Tetrahedron", "Right Tetrahedron"])
plt.ylabel("Scalar Error")
plt.title(f"Scalar Error Comparison (n = {n})")
plt.ticklabel_format(axis='y', style='sci', scilimits=(0, 0))
plt.show()