import pyvista as pv
import numpy as np
import cmake_mlat
import colorcet as cc
from matplotlib import colors

# if target point is constrained to 0 <= x <= 1, etc.
references = np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
], dtype=np.float64)

true_point = np.array([0.5, 0.5, 0.5], dtype=np.float64)

#Important variables
ranges = cmake_mlat.find_ranges(true_point, references)

range_vectors = cmake_mlat.find_range_vectors(true_point, references)

estimated_point = cmake_mlat.find_point(references, ranges)

scalar_error = cmake_mlat.find_scalar_error(true_point, estimated_point)

vector_error = cmake_mlat.find_error_vector(true_point, estimated_point)


pl = pv.Plotter()
pl.show_grid()

def add_points(point, color, point_size, render_points_as_spheres):
    pl.add_points(
        point,
        color = color,
        point_size = point_size,
        render_points_as_spheres = render_points_as_spheres
    )
add_points(references, 'black', 20, True)
add_points(true_point, 'blue', 20, True)

for i in range(len(range_vectors)):
    pl.add_arrows(references[i], range_vectors[i], mag=1.0)

#Final Setups
pl.camera_position = [
    (4, 2.75, 2.25),
    (0.5, 0.5, 0.5),    # focal point
    (0, 0, 1)
]

pl.show_bounds(
    grid='back',
    all_edges=True,
    location='outer',
    bounds=(0,1,0,1,0,1)
)

pl.show()