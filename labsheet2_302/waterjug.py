from collections import deque


class WaterJug:
    def __init__(self, initial_state, goal_state):
        self.initial_state = initial_state
        self.goal_state = goal_state
        self.capacity_a = 4   # 4-litre jug
        self.capacity_b = 3   # 3-litre jug

    
    def goalTest(self, current_state):
        return current_state == self.goal_state

    
    def successor(self, state):
        a, b = state
        children = []

        # Fill 4-litre jug
        children.append((self.capacity_a, b))

        # Fill 3-litre jug
        children.append((a, self.capacity_b))

        # Empty 4-litre jug
        children.append((0, b))

        # Empty 3-litre jug
        children.append((a, 0))

        # Pour 4 -> 3
        transfer = min(a, self.capacity_b - b)
        children.append((a - transfer, b + transfer))

        # Pour 3 -> 4
        transfer = min(b, self.capacity_a - a)
        children.append((a + transfer, b - transfer))

        return children



def generate_path(CLOSED, goal_state):
    path = []
    while goal_state is not None:
        path.append(goal_state)
        goal_state = CLOSED[goal_state]
    path.reverse()
    return path



def BFS(problem):
    OPEN = deque([problem.initial_state])
    CLOSED = {}

    CLOSED[problem.initial_state] = None

    while OPEN:
        current = OPEN.popleft()

        if problem.goalTest(current):
            return generate_path(CLOSED, current)

        for child in problem.successor(current):
            if child not in CLOSED:
                OPEN.append(child)
                CLOSED[child] = current

    return None


def DFS(problem):
    OPEN = [problem.initial_state]
    CLOSED = {}

    CLOSED[problem.initial_state] = None

    while OPEN:
        current = OPEN.pop()

        if problem.goalTest(current):
            return generate_path(CLOSED, current)

        for child in problem.successor(current):
            if child not in CLOSED:
                OPEN.append(child)
                CLOSED[child] = current

    return None



if __name__ == "__main__":

    initial_state = (4, 0)   
    goal_state = (2, 0)      

    problem = WaterJug(initial_state, goal_state)

    print("Successors of initial state (4,0):")
    print(problem.successor(initial_state))

    print("\nBFS Solution Path:")
    bfs_path = BFS(problem)
    for state in bfs_path:
        print(state)

    print("\nDFS Solution Path:")
    dfs_path = DFS(problem)
    for state in dfs_path:
        print(state)