# 3. Dijkstra's Minimal Spanning Tree Algorithm

class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[] for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u].append((v, w))
        self.graph[v].append((u, w))

    def dijkstra(self, start_vertex):
        dist = [float('inf')] * self.V
        dist[start_vertex] = 0
        visited = [False] * self.V

        for _ in range(self.V):
            u = self.min_distance(dist, visited)
            visited[u] = True

            for v, weight in self.graph[u]:
                if not visited[v] and dist[v] > dist[u] + weight:
                    dist[v] = dist[u] + weight

        return dist

    def min_distance(self, dist, visited):
        min_dist = float('inf')
        min_index = -1

        for v in range(self.V):
            if dist[v] < min_dist and not visited[v]:
                min_dist = dist[v]
                min_index = v

        return min_index


# Example usage:
g = Graph(5)
g.add_edge(0, 1, 2)
g.add_edge(0, 3, 1)
g.add_edge(1, 2, 3)
g.add_edge(1, 3, 3)
g.add_edge(2, 4, 1)
g.add_edge(3, 4, 4)

start_vertex = 0
shortest_paths = g.dijkstra(start_vertex)

print(f"Shortest paths from vertex {start_vertex}:")
for i, distance in enumerate(shortest_paths):
    print(f"To vertex {i}: {distance}")
