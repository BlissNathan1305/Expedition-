import matplotlib.pyplot as plt
import cartopy.crs as ccrs
import cartopy.feature as cfeature

# Set up the map
fig = plt.figure(figsize=(10, 8))
ax = plt.axes(projection=ccrs.LambertConformal())
ax.set_extent([-170, -30, -60, 80])  # Covers North and South America

# Add features
ax.add_feature(cfeature.LAND.with_scale('50m'))
ax.add_feature(cfeature.OCEAN.with_scale('50m'))
ax.add_feature(cfeature.BORDERS, linestyle=':')
ax.add_feature(cfeature.COASTLINE)

# Title
plt.title('Map of America', fontsize=15)

# Save as PNG
output_filename = "america_map.png"
plt.savefig(output_filename, bbox_inches='tight', dpi=300)

print(f"Map saved as {output_filename}")
