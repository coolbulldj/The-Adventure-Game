class Room:
    def __init__(self, name, doors, objects):
        self.Name = name
        self.doors = doors
        pass

    def describe(self):
        print(f"Room name : {self.Name}")
        if self.doors[0] == 1:
            print("There is a door to the North.")
        if self.doors[1] == 1:
            print("There is a door to the East.")
        if self.doors[2] == 1:
            print("There is a door to the South.")
        if self.doors[3] == 1:
            print("There is a door to the West.")
