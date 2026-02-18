import heapq

goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)

moves = [(-1,0),(1,0),(0,-1),(0,1)]

def manhattan(state):
    distance = 0
    for i in range(9):
        if state[i] != 0:
            goal_index = goal_state.index(state[i])
            x1, y1 = divmod(i, 3)
            x2, y2 = divmod(goal_index, 3)
            distance += abs(x1 - x2) + abs(y1 - y2)
    return distance

def get_neighbors(state):
    neighbors = []
    zero = state.index(0)
    x, y = divmod(zero, 3)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_zero = nx * 3 + ny
            new_state = list(state)
            new_state[zero], new_state[new_zero] = new_state[new_zero], new_state[zero]
            neighbors.append(tuple(new_state))
    return neighbors

def a_star(start):
    pq = []
    heapq.heappush(pq, (manhattan(start), 0, start, []))
    visited = set()

    while pq:
        f, g, state, path = heapq.heappop(pq)

        if state == goal_state:
            return path + [state]

        if state in visited:
            continue

        visited.add(state)

        for neighbor in get_neighbors(state):
            heapq.heappush(
                pq,
                (g + 1 + manhattan(neighbor), g + 1, neighbor, path + [state])
            )

    return None


start_state = (1, 2, 3,
               4, 0, 6,
               7, 5, 8)

solution = a_star(start_state)

print("A* Solution:")
for step, s in enumerate(solution):
    print(step, s)