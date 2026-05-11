def is_goal(state, N):
    for stack in state:
        if len(set(stack)) > 1:
            return False
    return True


def solve(initial, N):
    start = tuple(tuple(stack) for stack in initial)
    if is_goal(start, N):
        return []
    queue = [start]
    visited = {start: None}
    head = 0
    while head < len(queue):
        state = queue[head]
        head += 1
        state_list = [list(stack) for stack in state]
        for i in range(N):
            if not state_list[i]:
                continue
            for j in range(N):
                if i == j:
                    continue
                new_state = [list(stack) for stack in state_list]
                item = new_state[i].pop()
                new_state[j].append(item)
                new_state_tuple = tuple(tuple(stack) for stack in new_state)
                if new_state_tuple not in visited:
                    visited[new_state_tuple] = (state, (i + 1, j + 1))
                    if is_goal(new_state_tuple, N):
                        path = []
                        cur = new_state_tuple
                        while visited[cur] is not None:
                            prev, move = visited[cur]
                            path.append(f"{move[0]} {move[1]}")
                            cur = prev
                        path.reverse()
                        return path
                    queue.append(new_state_tuple)
    return None


try:
    line = input('Введите натуральное число: ').strip()
    if not line:
        exit('число не введено')
    N = int(line)
except ValueError:
    exit('N должно быть целым')
if N <= 0:
    exit('N должно быть натуральным')
containers = []
items = []
for i in range(N):
    container = input(f'Контейнер {i + 1}: ').strip()
    if not container or container == '0':
        containers.append([])
    else:
        cont = [x for x in container.split() if x != '0']
        containers.append(cont)
        items.extend(cont)
if len(set(items)) != N:
    exit('Количество типов элементов не совпадает с числом контейнеров')
if not any(len(set(c)) <= 1 for c in containers):
    exit('Сортировка невозможна: нет ни одного однородного или пустого контейнера')
solution = solve(containers, N)
if solution is None:
    exit('Сортировка невозможна')

if not solution:
    print("Сортировка не требуется")
else:
    print("Действия:")
    print("\n".join(solution))
