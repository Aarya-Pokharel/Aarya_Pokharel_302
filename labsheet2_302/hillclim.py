
goal_state = (1, 2, 3,
              4, 5, 6,
              7, 8, 0)


moves = [(-1, 0), (1, 0), (0, -1), (0, 1)]

def get_neighbors(state):
    neighbors = []
    zero_pos = state.index(0)
    x, y = divmod(zero_pos, 3)

    for dx, dy in moves:
        nx, ny = x + dx, y + dy
        if 0 <= nx < 3 and 0 <= ny < 3:
            new_zero = nx * 3 + ny
            new_state = list(state)
            new_state[zero_pos], new_state[new_zero] = new_state[new_zero], new_state[zero_pos]
            neighbors.append(tuple(new_state))

    return neighbors


def misplaced_tiles(state):
    return sum(
        1 for i in range(9)
        if state[i] != 0 and state[i] != goal_state[i]
    )

def hill_climbing(start_state):
    current = start_state

    while True:
        current_h = misplaced_tiles(current)
        neighbors = get_neighbors(current)

        best = current
        best_h = current_h

        for neighbor in neighbors:
            h = misplaced_tiles(neighbor)
            if h < best_h:
                best = neighbor
                best_h = h

        # Stop if no better neighbor exists
        if best_h >= current_h:
            return current

        current = best


if __name__ == "__main__":

    start_state = (1, 2, 3,
                   4, 0, 6,
                   7, 5, 8)

    final_state = hill_climbing(start_state)

    print("Initial State:", start_state)
    print("Final State:", final_state)
    print("Heuristic Value:", misplaced_tiles(final_state))