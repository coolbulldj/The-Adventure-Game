# modules
import pygame as py
import sys
import time
# Classes


# Core Functions
from Modules.Core.CoreGUI.ButtonHandler import CheckButtons, ResetActiveButtons
from Modules.Core.CoreGUI.ScrollHandler import triggerScrollMotion
from Modules.Core.UIService import RenderAssets
import Modules.Core.InputService as InputService

# Setup Game
py.init()
screen = py.display.set_mode((800, 450), py.RESIZABLE)
Running = True

from gameloop import run

FPS_CAP = 60
LastFrameTime = time.time()
ElapedTime = 0
CurrentFrame = 0  # tracks the current frame rendered count

while Running:
    # Calculate Delta time
    # (the time the program took to run, this useful for calculating animations, lerps, tweens, etc)
    currentTime = time.time()
    dt = currentTime - LastFrameTime
    ElapedTime += dt
    LastFrameTime = currentTime
    time.sleep(max(1 / FPS_CAP - dt, 0))

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

        # Uses input service here as
        # 1. it allows more customizality
        # 2.it allows keys to be an looped through as an array
        elif event.type == py.KEYDOWN:
            InputService.KeyDown(event.key)
        elif event.type == py.KEYUP:
            InputService.KeyUp(event.key)
    ResetActiveButtons()
    #reset active buttons
    InputService.Tick(dt)

    # run game logic
    run(dt)

    # Render Screen
    screen.fill((0, 0, 0))
    sx, sy = screen.get_size()
    screenSize = [
        sx,
        sy,
    ]  # converts to an array as screen size must be passed as an array
    CurrentFrame += 1
    RenderAssets(screen, screenSize)  # renders all gui assets
    py.display.flip()