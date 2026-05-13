# modules
import pygame as py
import sys
import time


# Classes

# Core Functions
from Modules.Core.ButtonHandler import CheckButtons
from Modules.Core.UIService import RenderAssets

py.init()
screen = py.display.set_mode((800, 450), py.RESIZABLE)

Running = True

from gameloop import run

FPS_CAP = 60
LastFrameTime = time.time()
ElapedTime = 0

while Running:
    #Input processing
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            Running = False
        if event.type == py.MOUSEBUTTONUP:
            CheckButtons(py.mouse.get_pos(), True, 1)

    #Calculate Delta time
    currentTime = time.time()
    dt = currentTime - LastFrameTime
    ElapedTime += dt
    LastFrameTime = currentTime
    time.sleep(max(1 / FPS_CAP - dt, 0))

    #run game logic
    run(dt)

    #Render Screen
    screen.fill((0, 0, 0))
    sx, sy = screen.get_size()
    screenSize = [sx, sy]  # convert tuple to array
    RenderAssets(screen, screenSize) #renders all gui assets
    py.display.flip()
