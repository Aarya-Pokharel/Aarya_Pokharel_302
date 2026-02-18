from collections import deque

class ManGoatLionCabbage:
    def __init__(self):
        # L = Left bank, R = Right bank
        self.start_state = ('L', 'L', 'L', 'L')   # (Man, Goat, Lion, Cabbage)
        self.goal_state  = ('R', 'R', 'R', 'R')


    def goalTest(self, state):
        return state == self.goal_state

    def is_safe(self, state):
        man, goat, lion, cabbage = state

        # Goat and Lion alone
        if man != goat and goat == lion:
            return False

        # Goat and Cabbage alone
        if man != goat and goat == cabbage:
            return False

        return True

    def successors(self, state):
        man, goat, lion, cabbage = state
        next_states = []

        def move(entity_index=None):
            new_state = list(state)
            new_state[0] = 'R' if man == 'L' else 'L'
            if entity_index is not None:
                new_state[entity_index] = new_state[0]
            return tuple(new_state)

        # Man moves alone
        s = move()
        if self.is_safe(s):
            next_states.append(s)

        # Man takes Goat
        if man == goat:
            s = move(1)
            if self.is_safe(s):
                next_states.append(s)

        # Man takes Lion
        if man == lion:
            s = move(2)
            if self.is_safe(s):
                next_states.append(s)

        # Man takes Cabbage
        if man == cabbage:
            s = move(3)
            if self.is_safe(s):
                next_states.append(s)

        return next_states


    def bfs(self):
        queue = deque([[self.start_state]])
        visited = set()

        while queue:
            path = queue.popleft()
            current = path[-1]

            if self.goalTest(current):
                return path

            if current not in visited:
                visited.add(current)
                for next_state in self.successors(current):
                    queue.append(path + [next_state])

        return None


if __name__ == "__main__":
    problem = ManGoatLionCabbage()
    solution = problem.bfs()

    print("Solution Path:")
    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")