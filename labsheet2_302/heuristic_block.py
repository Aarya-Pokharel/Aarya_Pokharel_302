

def heuristic(current, goal):
    """
    Calculate the heuristic as the number of blocks
    that are not in their goal positions.
    """
    h = 0
    for i in range(len(current)):
        if current[i] != goal[i]:
            h += 1
    return h

# Example: Blocks from bottom to top
# Current state (bottom to top)
current = ['B', 'C', 'D', 'A']  # bottom -> top
# Goal state (bottom to top)
goal = ['A', 'B', 'C', 'D']

# Calculate heuristic
h_value = heuristic(current, goal)
print(f"Heuristic value (number of misplaced blocks): {h_value}")