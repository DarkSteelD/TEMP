import random

def generate_random_graph(N, M):
    edges = set()
    while len(edges) < M:
        u, v = random.randint(1, N), random.randint(1, N)
        if u != v:
            edges.add((u, v))
            edges.add((v, u))  # Гарантируем двусторонность рёбер
    return list(edges)

N = 400  # Количество вершин
M = 1700  # Примерное количество рёбер
edges = generate_random_graph(N, M)[:M] 
with open('ans.txt', 'w') as f:
    print(N, M, file=f)
    for edge in edges:
        print(f"{edge[0]} {edge[1]}", file=f)

# N, M = map(int, input().split())  # Читаем количество городов и дорог
# edges = [list(map(int, input().split())) for _ in range(M)]  # Список рёбер

# # Инициализация матрицы смежности
# adj_matrix = [[0 for _ in range(N)] for _ in range(N)]

# # Заполнение матрицы смежности
# for u, v in edges:
#     adj_matrix[u-1][v-1] = 1
#     adj_matrix[v-1][u-1] = 1
# print(adj_matrix)