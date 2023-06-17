import folium
longitude=120.57650
latitue=24.23119

m = folium.Map(location=[longitude,latitue], zoom_start=4)

map_data = 'pu.json'
geojson = folium.features.GeoJson(map_data)
geojson.add_to(m)

m.save('pu_map.html')