import networkx as nx
import heapq

# Побудова графа
G = nx.Graph()
G.add_weighted_edges_from([
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
])

# Функція для алгоритму Дейкстри
def dijkstra(graph, start):
    """
    Знаходить найкоротші шляхи від вершини `start` до всіх інших вершин графа `graph`.

    Args:
        graph: Граф networkx.
        start: Початкова вершина.

    Returns:
        Словник з найкоротшими відстанями від `start` до всіх інших вершин.
    """
    distances = {node: float('inf') for node in graph.nodes}
    distances[start] = 0
    pq = [(0, start)]

    while pq:
        current_distance, current_node = heapq.heappop(pq)

        if current_distance > distances[current_node]:
            continue

        for neighbor in graph.neighbors(current_node):
            weight = graph[current_node][neighbor]['weight']
            distance = current_distance + weight
            if distance < distances[neighbor]:
                distances[neighbor] = distance
                heapq.heappush(pq, (distance, neighbor))

    return distances

# Знаходження всіх найкоротших шляхів
def dijkstra_all(graph):
    """
    Знаходить найкоротші шляхи між усіма вершинами графа `graph`.

    Returns:
        Словник {початкова_вершина: {кінцева_вершина: відстань}}
    """
    all_distances = {}
    for node in graph.nodes:
        all_distances[node] = dijkstra(graph, node)
    return all_distances

# Запуск алгоритму
results = dijkstra_all(G)

# Формування текстового звіту
output_lines = ["Згідно алгоритму Дейкстри",
                "Найкоротші шляхи з урахуванням ваги є такими:\n"]
for start, targets in results.items():
    output_lines.append(f"Від '{start}':")
    for dest, dist in targets.items():
        output_lines.append(f"  до '{dest}': {dist}")
    output_lines.append("")