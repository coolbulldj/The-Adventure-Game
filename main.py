# modules
import uuid
import pygame as py
import sys


# Classes

#Core Functions
from Modules.Core.ButtonHandler import CheckButtons


Running = True

py.init()

screen = py.display.set_mode((800, 450), py.RESIZABLE)

from gameloop import run

while Running:
    sx, sy = screen.get_size()
    screenSize = [sx, sy]  # convert tuple to array

    screen.fill((0, 0, 0))

    # py.draw.rect(screen, (255,0,0), (10, 10, 0, 10))
   # CheckButtons()
    run(screen, screenSize)
    py.display.flip()

    # result = mainLoop()

    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            Running = False
        if event.type == py.MOUSEBUTTONUP:
            CheckButtons(py.mouse.get_pos(), True, 1)

    # if not result:
    #    Running = False