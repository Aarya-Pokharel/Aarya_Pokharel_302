class BlocksWorldHeuristic:
    def __init__(self, current_state, goal_state):
        """
        current_state and goal_state are dictionaries
        Example:
        {'A': 'B', 'B': 'table', 'C': 'A'}
        """
        self.current = current_state
        self.goal = goal_state


    def get_support_structure(self, block, state):
        structure = []
        while block != "table":
            structure.append(block)
            block = state.get(block, "table")
        structure.append("table")
        return structure

    def heuristic(self):
        e_p = 0

        for block in self.current:
            current_support = self.get_support_structure(block, self.current)
            goal_support = self.get_support_structure(block, self.goal)

            if current_support == goal_support:
                # Correct support structure
                e_p += len(current_support) - 1   # exclude table
            else:
                # Wrong support structure
                e_p -= len(current_support) - 1

        return e_p



if __name__ == "__main__":

    # Current state
    current_state = {
        'A': 'B',
        'B': 'table',
        'C': 'A'
    }

    # Goal state
    goal_state = {
        'A': 'table',
        'B': 'table',
        'C': 'A'
    }

    heuristic = BlocksWorldHeuristic(current_state, goal_state)
    value = heuristic.heuristic()

    print("Heuristic Value e(p):", value)