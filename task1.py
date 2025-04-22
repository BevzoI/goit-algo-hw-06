import networkx as nx
import matplotlib
matplotlib.use('Agg')  # без GUI, не викликає Tkinter
import matplotlib.pyplot as plt

# Створення графа транспортної мережі
G = nx.Graph()

# Додавання вершин (зупинок)
stops = [
    "Центр", "Вокзал", "Університет", "Міська рада",
    "Парк", "Супермаркет", "Школа", "Лікарня"
]
G.add_nodes_from(stops)

# Додавання ребер (маршрутів між зупинками)
edges = [
    ("Центр", "Вокзал"),
    ("Центр", "Університет"),
    ("Центр", "Парк"),
    ("Вокзал", "Супермаркет"),
    ("Університет", "Школа"),
    ("Парк", "Школа"),
    ("Парк", "Лікарня"),
    ("Лікарня", "Міська рада"),
    ("Супермаркет", "Міська рада"),
    ("Школа", "Міська рада")
]
G.add_edges_from(edges)

# Аналіз характеристик
num_nodes = G.number_of_nodes()
num_edges = G.number_of_edges()
degree_info = dict(G.degree())

# Візуалізація графа
plt.figure(figsize=(10, 6))
pos = nx.spring_layout(G, seed=42)
nx.draw(G, pos, with_labels=True, node_size=1500, node_color='lightblue', font_size=10, font_weight='bold')
nx.draw_networkx_edge_labels(G, pos)
plt.title("Транспортна мережа міста")
plt.savefig("graph.png")  # Зберегти графік у файл

# Вивести інформацію про граф
print("Кількість зупинок (вершин):", num_nodes)
print("Кількість маршрутів (ребер):", num_edges)
print("Ступінь кожної вершини:")
for node, degree in degree_info.items():
    print(f" - {node}: {degree}")
