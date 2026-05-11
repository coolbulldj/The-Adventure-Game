# modules
import uuid
import pygame as py
import sys


# Classes

#GUI Classes
from Classes.GUIClasses.Frame import Frame
from Classes.GUIClasses.TextLabel import TextLabel
from Classes.GUIClasses.TextButton import TextButton

#Core Functions
from Modules.Core.ButtonHandler import CheckButtons

Running = True


py.init()

screen = py.display.set_mode((800, 600), py.RESIZABLE)

#TestFrame = Frame()
TestLabel = TextLabel()
TestLabel.Font = "pressstart2p"

TestTB = TextButton()
TestTB.Font = "pressstart2p"

TestTB.Text = "Test Button !"

TestTB.BackgroundColor = (0,255,0)

TestTB.Size = [0.25, 0.2]

i = 0

def testClick():
    global i
    print("testing clicking!", i)
    i += 1

TestTB.Button.MouseButton1Up.Connect(testClick)

while Running:
    sx, sy = screen.get_size()
    screenSize = [sx, sy]  # convert tuple to array

    screen.fill((255, 255, 255))
    #TestFrame.render(screen, screenSize)
    TestLabel.render(screen, screenSize)
    TestTB.render(screen, screenSize)
    # py.draw.rect(screen, (255,0,0), (10, 10, 0, 10))
   # CheckButtons()
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