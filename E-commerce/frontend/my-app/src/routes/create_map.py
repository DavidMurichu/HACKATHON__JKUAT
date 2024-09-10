import folium

# Create a map centered around a global location
map_center = [0, 0]  # Coordinates for the intersection of the Equator and the Prime Meridian
m = folium.Map(location=map_center, zoom_start=2)  # Adjust zoom_start for a broader view

# Optionally, add markers or other elements to the map
# For example, add a marker at the center of the map
folium.Marker(location=[0, 0], popup='Center of the World').add_to(m)

# Save the map to an HTML file
m.save('public/map.html')
