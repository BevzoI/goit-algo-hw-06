from collections import deque

# Реалізація DFS для знаходження шляху
def dfs_path(graph, start, goal, path=None, visited=None):
    if path is None:
        path = []
    if visited is None:
        visited = set()

    path = path + [start]
    visited.add(start)

    if start == goal:
        return path

    for neighbor in graph.neighbors(start):
        if neighbor not in visited:
            new_path = dfs_path(graph, neighbor, goal, path, visited)
            if new_path:
                return new_path
    return None

# Реалізація BFS для знаходження шляху
def bfs_path(graph, start, goal):
    visited = set()
    queue = deque([(start, [start])])

    while queue:
        (vertex, path) = queue.popleft()
        if vertex == goal:
            return path
        for neighbor in graph.neighbors(vertex):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append((neighbor, path + [neighbor]))
    return None

# Пошук шляху від "Центр" до "Лікарня"
dfs_result = dfs_path(G, "Центр", "Лікарня")
bfs_result = bfs_path(G, "Центр", "Лікарня")

dfs_result, bfs_result

print("Шлях за допомогою DFS (глибина):", dfs_result)
print("Шлях за допомогою BFS (ширина):", bfs_result)
