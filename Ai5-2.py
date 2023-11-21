# 2. Prim's Minimal Spanning Tree Algorithm 


class Graph:
    def __init__(self, vertices):
        self.V = vertices
        self.graph = [[0] * vertices for _ in range(vertices)]

    def add_edge(self, u, v, w):
        self.graph[u][v] = w
        self.graph[v][u] = w

    def prim_mst(self):
        key = [float('inf')] * self.V
        parent = [-1] * self.V
        mst_set = [False] * self.V

        key[0] = 0

        for cout in range(self.V):
            u = self.min_key(key, mst_set)
            mst_set[u] = True

            for v in range(self.V):
                if 0 < self.graph[u][v] < key[v] and not mst_set[v]:
                    key[v] = self.graph[u][v]
                    parent[v] = u

        mst = [(parent[i], i, self.graph[i][parent[i]]) for i in range(1, self.V)]
        return mst

    def min_key(self, key, mst_set):
        min_value = float('inf')
        min_index = -1

        for v in range(self.V):
            if key[v] < min_value and not mst_set[v]:
                min_value = key[v]
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

mst = g.prim_mst()

print("Edges in Prim's Minimal Spanning Tree:")
for edge in mst:
    print(edge)
