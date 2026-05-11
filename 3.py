def search(v):
    visited[v] = True
    for u in range(n):
        if matrix[v][u] == 1 and not visited[u]:
            parent[u] = v
            search(u)


def get_path_to_root(v, parent):
    path = []
    while v != -1:
        path.append(v)
        v = parent[v]
    path.reverse()
    return path


filename = 'matrix.txt'
with open(filename) as matrix:
    lines = [line.strip() for line in matrix if line.strip()]
if len(lines) == 0:
    exit('Файл пуст.')
matrix = []
n = len(lines)
for line in lines:
    row = list(map(int, line.split()))
    if len(row) != n:
        exit('Матрица должна быть квадратной')
    if not (all(row[i] == 0 or row[i] == 1 for i in range(0, n))):
        exit('Матрица содержит недопустимые элементы')
    matrix += [row]
edges = sum(matrix[i][j] for i in range(n) for j in range(i + 1, n))
if edges != n - 1:
    exit('граф не дерево')
parent = [-1] * n
visited = [False] * n
search(0)
if not all(visited):
    exit('Граф несвязный')
try:
    u = int(input(f"Введите первую вершину (0..{n - 1}): "))
    v = int(input(f"Введите вторую вершину (0..{n - 1}): "))
    if not (0 <= u < n and 0 <= v < n):
        print(f"Вершины должны быть в диапазоне от 0 до {n - 1}.")
except ValueError:
    exit('введите целые числа.')
path_u = get_path_to_root(u, parent)
path_v = get_path_to_root(v, parent)
lca = 0
for a, b in zip(path_u, path_v):
    if a == b:
        lca = a
    else:
        break
print(f"Наименьший общий предок вершин {u} и {v}: {lca}")
