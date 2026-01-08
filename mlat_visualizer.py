import pyvista as pv
import numpy as np
import cmake_mlat
from pyvista import Text
import colorcet as cc
from matplotlib import colors

# if target point is constrained to 0 <= x <= 1, etc.
references = np.array([
    [0.0, 0.0, 0.0],
    [1.0, 0.0, 0.0],
    [0.0, 1.0, 0.0],
    [0.0, 0.0, 1.0],
], dtype=np.float64)

true_point = np.array([0.2, 0.8, 0.5], dtype=np.float64)

#Important variables
ranges = cmake_mlat.find_ranges(true_point, references)

range_vectors = cmake_mlat.find_range_vectors(true_point, references)

estimated_point = cmake_mlat.find_point(references, ranges)

scalar_error = cmake_mlat.find_scalar_error(true_point, estimated_point)

vector_error = cmake_mlat.find_error_vector(true_point, estimated_point)


pl = pv.Plotter(shape=(1, 2), border=False)
pl.show_grid()

pl.subplot(0, 0)
def add_points(point, color, point_size, render_points_as_spheres):
    pl.add_points(
        point,
        color = color,
        point_size = point_size,
        render_points_as_spheres = render_points_as_spheres
    )
add_points(references, 'black', 30, True)

add_points(estimated_point, 'black', 30, True)


lines = []
mesh = pv.MultiBlock(lines)

for i in range(len(references)):
    endpoint = references[i]+range_vectors[i]
    line = pv.Line(references[i], endpoint)
    midpoint = endpoint = references[i]+range_vectors[i]/2
    label = pv.Label('S'+str(i+1), position=midpoint, size=50)
    pl.add_actor(label)
    label = pv.Label('P' + str(i + 1), position=references[i]+0.05, size=50)
    pl.add_actor(label)
    pl.add_mesh(line, color='black', line_width=10, opacity=0.45)

#Final Setups
pl.camera_position = [
    (4, 2.25, 2),
    (0.5, 0.5, 0.5),    # focal point
    (0, 0, 1)
]

pl.show_bounds(
    grid='back',
    all_edges=True,
    location='outer',
    bounds=(0,1,0,1,0,1)
)

pl.subplot(0, 1)
legend = (
    "   True Point: "+str(true_point)+"\n\n\n"
    "   S1 = "+str(ranges[0])+"\n\n"
    "   S2 = "+str(ranges[1])+"\n\n"
    "   S3 = "+str(ranges[2])+"\n\n"
    "   S4 = "+str(ranges[3])+"\n\n\n"
    "   Estimated Point (E): "+str(estimated_point)+"\n\n\n"
    "   Scalar Error: "+str(scalar_error)+"\n\n"
    "   Error Vector: "+"\n\n   "+str(vector_error)+"\n"
)

pl.add_text(
    legend,
    position='left_edge',
    font_size=28,
)

pl.show()