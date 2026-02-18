import random

class RoomCleanerAgent:
    def __init__(self, room_size=(5, 5)):
        self.room_size = room_size
        self.grid = [[random.choice([0, 1]) for _ in range(room_size[1])]
                     for _ in range(room_size[0])]
        self.current_position = (0, 0)

    def display_room(self):
        for row in self.grid:
            print(" ".join(str(cell) for cell in row))
        print()

    def perceive(self):
        x, y = self.current_position
        return self.grid[x][y]

    def act(self):
        x, y = self.current_position
        if self.perceive() == 1:
            print(f"Cell ({x},{y}) is Dirty → Cleaning")
            self.grid[x][y] = 0
        else:
            print(f"Cell ({x},{y}) is Clean")

    def move(self):
        x, y = self.current_position
        if y < self.room_size[1] - 1:
            self.current_position = (x, y + 1)
        elif x < self.room_size[0] - 1:
            self.current_position = (x + 1, 0)
        else:
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
                self.current_position = (0, 0)

        print("Final Room Status:")
        self.display_room()
        print(f"Room cleaned in {steps} steps")

agent = RoomCleanerAgent()
agent.run()