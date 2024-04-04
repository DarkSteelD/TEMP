N, M = map(int, input().split())  # Читаем количество городов и дорог
grid = [[0 for _ in range(N)] for _ in range(N)]
graph = {}
for _ in range(M):
    a, b = map(int, input().split())
    grid[a - 1][b - 1] = 1
    grid[b - 1][a - 1] = 1
    graph.setdefault(a, set()).add(b)  # Добавляем b в список соседей a
    graph.setdefault(b, set()).add(a)  # Добавляем a в список соседей b
# Находим матрицу смежности в степени 2 (без NumPy)
def vinograd_multiplication(G, H):
    if len(G[0]) != len(H):
        raise ValueError("Матрицы не могут быть перемножены")

    a, b, c = len(G), len(G[0]), len(H[0])
    R = [[0] * c for _ in range(a)]

    # Предварительные вычисления
    row_factor = [0] * a
    for i in range(a):
        for j in range(0, b - b % 2, 2):
            row_factor[i] += G[i][j] * G[i][j + 1]

    column_factor = [0] * c
    for i in range(c):
        for j in range(0, b - b % 2, 2):
            column_factor[i] += H[j][i] * H[j + 1][i]

    # Основной цикл умножения
    for i in range(a):
        for j in range(c):
            R[i][j] = -row_factor[i] - column_factor[j]
            for k in range(0, b - b % 2, 2):
                R[i][j] += (G[i][k] + H[k + 1][j]) * (G[i][k + 1] + H[k][j])
            if b % 2:
                R[i][j] += G[i][b - 1] * H[b - 1][j]

    return R
grid = vinograd_multiplication(grid, grid)
# for row in grid:
#     print(row)

# Подсчитываем количество общих соседей для каждой пары вершин
count = 0
for i in range(N):
    for j in range(i + 1, N):
        if grid[i][j] == 0:  # Игнорируем пары вершин без прямого соединения
            continue
        common_neighbors = len(graph[i + 1].intersection(graph[j + 1])) - 1 
        count += grid[i][j] * common_neighbors

print(int(count / 4))