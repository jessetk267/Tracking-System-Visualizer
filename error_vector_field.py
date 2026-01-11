import points
import pyvista as pv
import numpy as np
import colorcet as cc
from matplotlib import colors
import cmake_mlat

#Vector Setup
points = []

vector_list = []

references = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

pl = pv.Plotter()
pl.show_grid()

def add_points(point, color, point_size, render_points_as_spheres):
    pl.add_points(
        point,
        color = color,
        point_size = point_size,
        render_points_as_spheres = render_points_as_spheres
    )
add_points(references, 'black', 25, True)

for i in range(5):
    for j in range(5):
        for k in range(5):
            true_point = np.array([i/5, j/5, k/5], dtype=np.float64)
            points.append(true_point)

            ranges = cmake_mlat.find_ranges(true_point, references)

            estimated_point = cmake_mlat.find_point(references, ranges)
            error_vector = cmake_mlat.find_error_vector(true_point, estimated_point)
            vector_list.append(error_vector)

vectors = np.array(vector_list, dtype=np.float32)

mesh = pv.PolyData(points)
mesh["vectors"] = vectors
mesh.set_active_vectors("vectors")

arrows = mesh.glyph(
    orient="vectors",
    scale="vectors",
    factor=4e14
)

pl.add_mesh(arrows, color="blue")

#Final Setups
pl.camera_position = [
    (4, 2.5, 2.25),
    (0.5, 0.5, 0.5),    # focal point
    (0, 0, 1)
]

pl.show_bounds(
    grid='back',
    all_edges=True,
    location='outer',
    bounds=(0, 1, 0, 1, 0, 1)
)

pl.show()
