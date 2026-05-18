import pygame as py
import random

from Modules.Core.CoreGUI.ScrollHandler import addScrollAsset, destoryScrollAsset
from Classes.GUIClasses.GuiBase import GuiBase


def clamp(x, minVal, maxVal):
    return min(max(minVal, x), maxVal)


class ScrollingFrame(GuiBase):
    def __init__(self):
        super().__init__()
        self.ScrollingBarSize = 0.05  # done by percentage of size
        self.ScrollSpeed = (
            -0.1
        )  # relative to the canvas size (done as a percentage of size)
        self.ScrollingBarColor = (255, 0, 0)
        self.ScrollingBackgroundColor = (55, 55, 55)
        self._CanvasSize = [0, 0]
        self._CanvasPos = [0, 0]
        self.AutoCanvasX = False
        self.AutoCanvasY = True
        addScrollAsset(self)

    def mouseMotion(self, motionData):
        x, y = motionData[0], motionData[1]

        stepX = self._CanvasSize[0] * self.ScrollSpeed * x
        stepY = self._CanvasSize[1] * self.ScrollSpeed * y

        newX = self._CanvasPos[0] + stepX
        newY = self._CanvasPos[1] + stepY

        # clamp positon so then the scrolling bar doesn't go out of frame
        newX = clamp(newX, 0, self._CanvasSize[0])
        newY = clamp(newY, 0, self._CanvasSize[1])

        print("he got motion motherfucker", self._CanvasPos)

        self._CanvasPos = [newX, newY]

    def render(self, screen, screenSize, posOffset=[0, 0]):
        super().render(screenSize, posOffset)
        # render frame
        py.draw.rect(
            screen,
            self.BackgroundColor,
            (
                self.AbsolutePos[0],
                self.AbsolutePos[1],
                self.AbsoluteSize[0],
                self.AbsoluteSize[1],
            ),
        )

        ranNum = random.randint(1, 2)

        # render y scrolling bar
        # scrolling bar background
        py.draw.rect(
            screen,
            self.ScrollingBackgroundColor,
            (
                self.AbsolutePos[0]
                + self.AbsoluteSize[0] * (1 - self.ScrollingBarSize),
                self.AbsolutePos[1],
                self.AbsoluteSize[0] * self.ScrollingBarSize,
                self.AbsoluteSize[1],
            ),
        )
        # render y scrolling bar
        scrollingXBarSize = self.AbsoluteSize[1] / (1 + self._CanvasSize[1])
        py.draw.rect(
            screen,
            self.ScrollingBarColor,
            (
                self.AbsolutePos[0]
                + self.AbsoluteSize[0] * (1 - self.ScrollingBarSize),
                self.AbsolutePos[1]
                + self._CanvasPos[1] * (self.AbsoluteSize[1] - scrollingXBarSize),
                self.AbsoluteSize[0] * self.ScrollingBarSize,
                scrollingXBarSize,
            ),
        )
