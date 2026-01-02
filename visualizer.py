import pyvista as pv
import numpy as np

references = np.array([
    [0, 0, 0],
    [1, 0, 0],
    [0, 1, 0],
    [0, 0, 1]
])

true_point = np.array([0.5, 0.5, 0.5])
estimated_point = np.array([0.5, 0.5, 0.0])

plotter = pv.Plotter()
plotter.add_axes()
plotter.show_grid()

plotter.show_bounds(
    grid='front',
    location='outer',
    bounds=(0,1,0,1,0,1)
)

plotter.add_points(
    references,
    color="white",
    point_size=15,
    render_points_as_spheres=True,
    label="Anchors"
)

plotter.add_points(
    true_point,
    color="blue",
    point_size=20,
    render_points_as_spheres=True,
    label="True"
)

plotter.add_points(
    estimated_point,
    color="red",
    point_size=20,
    render_points_as_spheres=True,
    label="Estimated"
)

# Error vector
error_vec = estimated_point - true_point
arrow = pv.Arrow(start=true_point, direction=error_vec, scale=1.0)
plotter.add_mesh(arrow, color="yellow")

plotter.add_legend()
plotter.show()
