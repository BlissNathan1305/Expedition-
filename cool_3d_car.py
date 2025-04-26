import matplotlib.pyplot as plt
from mpl_toolkits.mplot3d import Axes3D
from mpl_toolkits.mplot3d.art3d import Poly3DCollection
import numpy as np

# Initialize figure
fig = plt.figure(figsize=(10, 8))
ax = fig.add_subplot(111, projection='3d')

# Helper function to draw a 3D box
def draw_box(x_range, y_range, z_range, color):
    vertices = [
        [x_range[0], y_range[0], z_range[0]],
        [x_range[1], y_range[0], z_range[0]],
        [x_range[1], y_range[1], z_range[0]],
        [x_range[0], y_range[1], z_range[0]],
        [x_range[0], y_range[0], z_range[1]],
        [x_range[1], y_range[0], z_range[1]],
        [x_range[1], y_range[1], z_range[1]],
        [x_range[0], y_range[1], z_range[1]],
    ]
    faces = [
        [vertices[0], vertices[1], vertices[2], vertices[3]],
        [vertices[4], vertices[5], vertices[6], vertices[7]],
        [vertices[0], vertices[1], vertices[5], vertices[4]],
        [vertices[2], vertices[3], vertices[7], vertices[6]],
        [vertices[1], vertices[2], vertices[6], vertices[5]],
        [vertices[4], vertices[7], vertices[3], vertices[0]]
    ]
    box = Poly3DCollection(faces, facecolors=color, edgecolors='black', linewidths=1, alpha=0.9)
    ax.add_collection3d(box)

# Helper function to draw a 3D cylinder (for rounded wheels)
def draw_cylinder(center_x, center_y, center_z, radius, height, color):
    z = np.linspace(center_z, center_z + height, 2)
    theta = np.linspace(0, 2 * np.pi, 30)
    theta_grid, z_grid = np.meshgrid(theta, z)
    x_grid = center_x + radius * np.cos(theta_grid)
    y_grid = center_y + radius * np.sin(theta_grid)
    ax.plot_surface(x_grid, y_grid, z_grid, color=color, alpha=1.0, edgecolor='k')

# --------------------
# Draw parts of the car
# --------------------

# Car body (main)
draw_box((0, 4), (0, 2), (0, 1), 'blue')

# Car top (roof)
draw_box((1, 3), (0.5, 1.5), (1, 2), 'lightblue')

# Wheels (cylinders for rounded wheels)
wheel_positions = [(0.5, 0.2), (3.5, 0.2), (0.5, 1.8), (3.5, 1.8)]
for x, y in wheel_positions:
    draw_cylinder(x, y, -0.5, 0.2, 0.5, 'black')

# Windows (light gray boxes)
# Front window
draw_box((1.6, 2.4), (0.5, 0.6), (1.2, 1.8), 'lightgray')

# Left side window
draw_box((1.1, 1.5), (0.5, 1.5), (1.2, 1.8), 'lightgray')

# Right side window
draw_box((2.5, 2.9), (0.5, 1.5), (1.2, 1.8), 'lightgray')

# Headlights (yellow)
draw_box((0, 0.1), (0.4, 0.6), (0.4, 0.6), 'yellow')
draw_box((0, 0.1), (1.4, 1.6), (0.4, 0.6), 'yellow')

# Taillights (red)
draw_box((3.9, 4), (0.4, 0.6), (0.4, 0.6), 'red')
draw_box((3.9, 4), (1.4, 1.6), (0.4, 0.6), 'red')

# --------------------
# Settings
# --------------------

# Set 3D plot limits
ax.set_xlim(-1, 5)
ax.set_ylim(-2, 4)
ax.set_zlim(-1, 3)

# Hide axes
ax.axis('off')

# Set nice view angle
ax.view_init(elev=20, azim=-60)

# Save the figure as PNG
output_filename = "cool_3d_car.png"
plt.savefig(output_filename, bbox_inches='tight', dpi=300)

print(f"Cool 3D car image saved as {output_filename}")
