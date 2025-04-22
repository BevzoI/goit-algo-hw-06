import networkx as nx

# Створення зваженого графа на основі попередньої структури
G_weighted = nx.Graph()

# Вузли залишаються ті самі
G_weighted.add_nodes_from(stops)

# Додаємо ребра з вагами (наприклад, час у хвилинах або умовна відстань)
weighted_edges = [
    ("Центр", "Вокзал", 5),
    ("Центр", "Університет", 4),
    ("Центр", "Парк", 3),
    ("Вокзал", "Супермаркет", 6),
    ("Університет", "Школа", 5),
    ("Парк", "Школа", 4),
    ("Парк", "Лікарня", 6),
    ("Лікарня", "Міська рада", 5),
    ("Супермаркет", "Міська рада", 4),
    ("Школа", "Міська рада", 3)
]
G_weighted.add_weighted_edges_from(weighted_edges)

# Застосовуємо алгоритм Дейкстри для знаходження найкоротших шляхів від кожної вершини
dijkstra_all_paths = dict(nx.all_pairs_dijkstra_path(G_weighted))
dijkstra_all_lengths = dict(nx.all_pairs_dijkstra_path_length(G_weighted))

# Підготуємо результати для зручного перегляду
shortest_paths_summary = {
    source: {
        target: {
            "шлях": dijkstra_all_paths[source][target],
            "довжина": dijkstra_all_lengths[source][target]
        }
        for target in dijkstra_all_paths[source]
    }
    for source in G_weighted.nodes
}

import ace_tools as tools; tools.display_dataframe_to_user(name="Найкоротші шляхи (Дейкстра)", dataframe=nx.to_pandas_adjacency(G_weighted, weight="weight"))

shortest_paths_summary
