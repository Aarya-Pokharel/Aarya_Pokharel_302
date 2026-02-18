import random

class ModelBasedRoomCleanerAgent:
    def __init__(self, room_size=(5, 5)):
        self.room_size = room_size

    
        self.grid = [[random.choice([0, 1]) for _ in range(room_size[1])]
                     for _ in range(room_size[0])]

        self.current_position = (0, 0)
        self.visited = set()

    def display_room(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print()

    def perceive(self):
        x, y = self.current_position
        return self.grid[x][y]

    def update_model(self):
        self.visited.add(self.current_position)

    def act(self):
        x, y = self.current_position

        if self.perceive() == 1:
            print(f"Cell ({x},{y}) is Dirty → Cleaning")
            self.grid[x][y] = 0
        else:
            print(f"Cell ({x},{y}) is Clean")

        self.update_model()

    def move(self):
        x, y = self.current_position

        if y + 1 < self.room_size[1] and (x, y + 1) not in self.visited:
            self.current_position = (x, y + 1)
        elif x + 1 < self.room_size[0] and (x + 1, y) not in self.visited:
            self.current_position = (x + 1, y)
        else:
            for i in range(self.room_size[0]):
                for j in range(self.room_size[1]):
                    if (i, j) not in self.visited:
                        self.current_position = (i, j)
                        return
            self.current_position = None

    def is_room_clean(self):
        return all(cell == 0 for row in self.grid for cell in row)

    def run(self):
        print("Initial Room Status:")
        self.display_room()

        steps = 0
        while not self.is_room_clean():
            self.act()
            self.move()
            steps += 1

            if self.current_position is None:
                break

        print("Final Room Status:")
        self.display_room()
        print(f"Room cleaned in {steps} steps")


agent = ModelBasedRoomCleanerAgent()
agent.run()