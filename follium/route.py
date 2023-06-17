import folium
import osmnx as ox

# 定義起點和終點的地址或地標
origin_point = (23.054299, 113.372473)  # 广州大学的地理坐标
destination_point = (23.134470, 113.269534)  # 终点的地理坐标


# 使用osmnx進行路徑規劃
graph = ox.graph_from_address(origin_point, network_type='all')
route = ox.shortest_path(graph, origin_point, destination_point, weight='length')

# 創建地圖
m = folium.Map(location=[origin_point[0], origin_point[1]], zoom_start=13)

# 添加起點和終點標記
folium.Marker(location=[origin_point[0], origin_point[1]], popup=origin_point).add_to(m)
folium.Marker(location=[destination_point[0], destination_point[1]], popup=destination_point).add_to(m)

# 添加路徑線條
route_coordinates = [(graph.nodes[node]['y'], graph.nodes[node]['x']) for node in route]
folium.PolyLine(locations=route_coordinates, color='blue', weight=5).add_to(m)

# 顯示地圖
m.save('route_map.html')
