from collections import deque

class MissionariesCannibals:
    def __init__(self):
        # (M_left, C_left, Boat)
        self.start_state = (3, 3, 'L')
        self.goal_state = (0, 0, 'R')

    def goalTest(self, state):
        return state == self.goal_state

    def is_safe(self, state):
        M_left, C_left, _ = state
        M_right = 3 - M_left
        C_right = 3 - C_left

        # Check left bank
        if M_left > 0 and C_left > M_left:
            return False
        # Check right bank
        if M_right > 0 and C_right > M_right:
            return False
        return True

    def successors(self, state):
        M_left, C_left, boat = state
        next_states = []

        moves = [(1,0),(0,1),(1,1),(2,0),(0,2)]  # possible boat moves

        for M_move, C_move in moves:
            if boat == 'L':
                new_M_left = M_left - M_move
                new_C_left = C_left - C_move
                new_boat = 'R'
            else:
                new_M_left = M_left + M_move
                new_C_left = C_left + C_move
                new_boat = 'L'

            # Validate move: cannot have negative or more than 3
            if 0 <= new_M_left <= 3 and 0 <= new_C_left <= 3:
                new_state = (new_M_left, new_C_left, new_boat)
                if self.is_safe(new_state):
                    next_states.append(new_state)

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
                    if next_state not in visited:
                        queue.append(path + [next_state])
        return None

if __name__ == "__main__":
    problem = MissionariesCannibals()
    solution = problem.bfs()

    print("Solution Path:")
    for step, state in enumerate(solution):
        print(f"Step {step}: {state}")
