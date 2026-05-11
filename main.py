# modules
import uuid

# Classes
from Classes.Adventurer import Adventurer as AdventurerClass
from Classes.Room import Room as RoomClass
from roomHandler import Rooms
from roomHandler import ConnectRooms

Running = True

Name = input("Enter your adventurer Name: ")
Gender = input("Enter your gender: male (m) or female(f) ")
Age = input("Enter age: ")

# Transform inputs into correct values
Age = int(Age)

if Gender == "f":
    Gender = "Female"
else:
    Gender = "Male"

Adventurer = AdventurerClass(Name, Gender, Age)

# Create rooms
Rooms.append([RoomClass("Room 1", [0, 1, 0, 0], [])])  # x = 0
Rooms.append([RoomClass("Room 2,", [0, 0, 0, 1], [])])  # x = 1


def mainLoop():
    x, y = Adventurer.pos[0], Adventurer.pos[1]

    x, y = int(x), int(y)

    if x < 0 or x > len(Rooms) - 1:
        print("Failed to find Room at cords:", x, y)
        return

    if y < 0 or y > len(Rooms[x]) - 1:
        print("Failed to find Room at cords:", x, y)
        return

    currentRoom = Rooms[x][y]

    if not currentRoom:
        print(
            f"Failed to find room at adventurer position: {Adventurer.pos[0]} x & {Adventurer.pos[1]} y"
        )
        return

    # Adventurer.describe()
    currentRoom.describe()

    choice = input("Please provide movement choice: ")

    if choice == "n":
        if currentRoom.doors[0] == 1:
            Adventurer.change_pos(0, 1)
        else:
            print("Can't move north as there is no door")
    elif choice == "e":
        if currentRoom.doors[1] == 1:
            Adventurer.change_pos(1, 0)
        else:
            print("Can't move east as there is no door")
    elif choice == "s":
        if currentRoom.doors[2] == 1:
            Adventurer.change_pos(0, -1)
        else:
            print("Can't move south as there is no door")
    elif choice == "w":
        if currentRoom.doors[3] == 1:
            Adventurer.change_pos(-1, 0)
        else:
            print("Can't move west as there is no door")
    elif choice == "q":
        return

    return True


import pygame as py
import sys
from Classes.GUIClasses.Frame import Frame

py.init()

screen = py.display.set_mode((800, 600), py.RESIZABLE)

TestFrame = Frame()

while Running:
    sx, sy = screen.get_size()
    screenSize = [sx, sy]  # convert tuple to array

    screen.fill((255, 255, 255))
    TestFrame.render(screen, screenSize)
    # py.draw.rect(screen, (255,0,0), (10, 10, 0, 10))
    py.display.flip()

    # result = mainLoop()

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            Running = False

    # if not result:
    #    Running = False
