import matplotlib.pyplot as plt
import numpy as np
import os

def generate_world_map():
    # Create output directory if it doesn't exist
    output_dir = 'map_output'
    if not os.path.exists(output_dir):
        os.makedirs(output_dir)
    
    # Output file path
    output_file = os.path.join(output_dir, 'world_map.png')
    
    # Create figure with higher resolution
    plt.figure(figsize=(12, 8), dpi=300)
    
    # Simple world map using just matplotlib
    # Define the coordinates for continents (very simplified)
    
    # North America (simplified shape)
    na_x = [-170, -50, -50, -170, -170]
    na_y = [75, 75, 15, 15, 75]
    
    # South America (simplified shape)
    sa_x = [-80, -35, -35, -80, -80]
    sa_y = [15, 15, -60, -60, 15]
    
    # Europe (simplified shape)
    eu_x = [-10, 40, 40, -10, -10]
    eu_y = [75, 75, 35, 35, 75]
    
    # Africa (simplified shape)
    af_x = [-20, 50, 50, -20, -20]
    af_y = [35, 35, -35, -35, 35]
    
    # Asia (simplified shape)
    as_x = [40, 170, 170, 40, 40]
    as_y = [75, 75, 10, 10, 75]
    
    # Australia (simplified shape)
    au_x = [110, 155, 155, 110, 110]
    au_y = [-10, -10, -45, -45, -10]
    
    # Draw the continents
    plt.fill(na_x, na_y, 'lightgrey', edgecolor='black', label='North America')
    plt.fill(sa_x, sa_y, 'lightgrey', edgecolor='black', label='South America')
    plt.fill(eu_x, eu_y, 'lightgrey', edgecolor='black', label='Europe')
    plt.fill(af_x, af_y, 'lightgrey', edgecolor='black', label='Africa')
    plt.fill(as_x, as_y, 'lightgrey', edgecolor='black', label='Asia')
    plt.fill(au_x, au_y, 'lightgrey', edgecolor='black', label='Australia')
    
    # Set axis limits for the world
    plt.xlim(-180, 180)
    plt.ylim(-90, 90)
    
    # Add gridlines
    plt.grid(color='gray', linestyle='--', linewidth=0.5, alpha=0.5)
    
    # Add labels for longitude and latitude
    plt.xticks(np.arange(-180, 181, 30))
    plt.yticks(np.arange(-90, 91, 30))
    
    # Customize appearance
    plt.title('World Map', fontsize=15)
    plt.xlabel('Longitude')
    plt.ylabel('Latitude')
    
    # Save the map as PNG
    plt.savefig(output_file, bbox_inches='tight', dpi=300)
    plt.close()
    
    print(f"World map generated and saved to {output_file}")
    return output_file

if __name__ == "__main__":
    map_file = generate_world_map()
    print(f"Map is available for download at: {map_file}")
    print("To download through Termius:")
    print("1. Navigate to the file using SFTP in Termius")
    print("2. Right-click on the file and select 'Download'")
    print("3. Choose a destination on your local machine")
