import networkx as nx
import matplotlib.pyplot as plt

graph = nx.Graph()

nodes = ["Kyiv", "Lviv", "Kharkiv", "Dnipro", "Odesa", "Donetsk", "Uzhhorod"]
graph.add_nodes_from(nodes)

edges = [("Kyiv", "Lviv", {'weight': 541}),
         ("Kyiv", "Kharkiv", {'weight': 479}),
         ("Kyiv", "Odesa", {'weight': 476}),
         ("Kyiv", "Dnipro", {'weight': 389}),
         ("Lviv", "Uzhhorod", {'weight': 248}),
         ("Kharkiv", "Dnipro", {'weight': 218}),
         ("Kharkiv", "Donetsk", {'weight': 335}),
         ("Odesa", "Lviv", {'weight': 796}),
         ("Odesa", "Uzhhorod", {'weight': 1018}),
         ("Donetsk", "Dnipro", {'weight': 226})]

graph.add_edges_from(edges)

plt.figure(figsize=(10, 10))
pos = nx.spring_layout(graph, seed=42)
nx.draw_networkx(graph, pos, with_labels=True, node_size=800, node_color="lightblue", font_size=16, font_weight="bold")

edge_labels = nx.get_edge_attributes(graph, 'weight')
nx.draw_networkx_edge_labels(graph, pos, edge_labels=edge_labels)

print("BFS: ", list(nx.bfs_edges(graph, source="Uzhhorod")))

print("DFS: ", list(nx.dfs_edges(graph, source="Uzhhorod")))

plt.show()
