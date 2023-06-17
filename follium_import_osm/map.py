import folium
longitude=120.57650
latitue=24.23119

map = folium.Map(location=[latitue, longitude], zoom_start=10)
folium.GeoJson('pu.osm').add_to(map)

map.save('pu_map.html')
map