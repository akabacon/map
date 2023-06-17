import osmnx as ox

import networkx as nx
origin_point = (23.054299, 113.372473)  # 广州大学的地理坐标
destination_point = (24.2272, 120.5807)  # 终点的地理坐标
G = ox.graph_from_address(origin_point, dist=6000,network_type='all') #第一步，获取道路数据

ox.plot_graph(G)

origin_node = ox.get_nearest_node(G, origin_point) #获取O最邻近的道路节点

destination_node = ox.get_nearest_node(G, destination_point) #获取D最邻近的道路节点

route = nx.shortest_path(G, origin_node, destination_node, weight='length') #请求获取最短路径

distance = nx.shortest_path_length(G, origin_node, destination_node, weight='length') #并获取路径长度

fig, ax = ox.plot_graph_route(G, route, origin_point=origin_point, destination_point=destination_point) #可视化结果

print(str(distance)) #输出最短路径距离