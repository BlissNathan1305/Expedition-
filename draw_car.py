import matplotlib.pyplot as plt
import matplotlib.patches as patches

# Set up the figure
fig, ax = plt.subplots(figsize=(6, 4))

# Draw car body
car_body = patches.FancyBboxPatch((0.2, 0.3), 0.6, 0.2,
                                  boxstyle="round,pad=0.1",
                                  edgecolor="black", facecolor="blue")
ax.add_patch(car_body)

# Draw car top
car_top = patches.FancyBboxPatch((0.35, 0.4), 0.3, 0.15,
                                 boxstyle="round,pad=0.1",
                                 edgecolor="black", facecolor="lightblue")
ax.add_patch(car_top)

# Draw wheels
wheel1 = patches.Circle((0.3, 0.25), 0.07, color='black')
wheel2 = patches.Circle((0.7, 0.25), 0.07, color='black')
ax.add_patch(wheel1)
ax.add_patch(wheel2)

# Set limits and remove axes
ax.set_xlim(0, 1)
ax.set_ylim(0, 1)
ax.axis('off')

# Save the figure
output_filename = "simple_car.png"
plt.savefig(output_filename, bbox_inches='tight', dpi=300)

print(f"Car image saved as {output_filename}")
