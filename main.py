# modules
import pygame as py
import sys
import time
# Classes

# Core Functions
from Modules.Core.ButtonHandler import CheckButtons
from Modules.Core.CoreGUI.ScrollHandler import triggerScrollMotion
from Modules.Core.UIService import RenderAssets

# Setup Game
py.init()
screen = py.display.set_mode((800, 450), py.RESIZABLE)
Running = True

from gameloop import run

FPS_CAP = 60
LastFrameTime = time.time()
ElapedTime = 0

while Running:
    # Input processing
    mousePos = py.mouse.get_pos()
    for event in py.event.get():
        if event.type == py.QUIT:
            py.quit()
            sys.exit()
            Running = False
        elif event.type == py.MOUSEBUTTONUP:
            CheckButtons(mousePos, True, event.button)
        elif event.type == py.MOUSEBUTTONDOWN:
            CheckButtons(mousePos, False, event.button)
        elif event.type == py.MOUSEWHEEL:
            triggerScrollMotion([event.x, event.y])

    # Calculate Delta time
    # (the time the program took to run, this useful for calculating animations, lerps, tweens, etc)
    currentTime = time.time()
    dt = currentTime - LastFrameTime
    ElapedTime += dt
    LastFrameTime = currentTime
    time.sleep(max(1 / FPS_CAP - dt, 0))

    # run game logic
    run(dt)

    # Render Screen
    screen.fill((0, 0, 0))
    sx, sy = screen.get_size()
    screenSize = [
        sx,
        sy,
    ]  # converts to an array as screen size must be passed as an array
    RenderAssets(screen, screenSize)  # renders all gui assets
    py.display.flip()
