
import folium

# Create a map of the world
map_center = [0, 0]  # Coordinates for the center of the world
m = folium.Map(location=map_center, zoom_start=2)

# Save the map to an HTML file
m.save('static/map.html')

