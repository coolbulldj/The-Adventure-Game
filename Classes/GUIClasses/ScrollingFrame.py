import pygame as py
import random

from Modules.Core.CoreGUI.GUIElementsList import GuiAssets
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
        self.ScrollingBarColor = (255, 255, 255)
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

        self._CanvasPos = [newX, newY]

    def renderUIAssets(self, screen):
        AssetList = self._sortUIAssets()
        screenOffset = -self._CanvasPos[1] * self.AbsoluteSize[1]
        for child in AssetList:
            if isinstance(child, GuiBase):
                # rendering a GuiBase
                if not child.Visible:
                    continue
                child.render(
                    screen, self.AbsoluteSize, self.LastFrame, [0, screenOffset]
                )
            else:
                # rendering a UI Structure
                if not child.Enabled:
                    continue
                child.render()

    def _renderScrollingBars(self, screen):
        if self._CanvasSize[1] > 0:
            py.draw.rect(
                screen,
                self.ScrollingBackgroundColor,
                (
                    # self.AbsolutePos[0]
                    # + self.AbsoluteSize[0] * (1 - self.ScrollingBarSize),
                    # self.AbsolutePos[1],
                    # self.AbsoluteSize[0] * self.ScrollingBarSize,
                    # self.AbsoluteSize[1],
                    self.AbsolutePos[0]
                    + self.AbsoluteSize[0] * (1 - self.ScrollingBarSize),
                    self.AbsolutePos[1],
                    self.AbsoluteSize[0] * self.ScrollingBarSize,
                    self.AbsoluteSize[1],
                ),
            )

            barHeight = 1 / (1 + self._CanvasSize[1])

            # scroll rectangle
            py.draw.rect(
                screen,
                self.ScrollingBarColor,
                (
                    # self.AbsolutePos[0]
                    # + self.AbsoluteSize[0] * (1 - self.ScrollingBarSize),
                    # self.AbsolutePos[1],
                    # self.AbsoluteSize[0] * self.ScrollingBarSize,
                    # self.AbsoluteSize[1],
                    self.AbsolutePos[0]
                    + self.AbsoluteSize[0] * (1 - self.ScrollingBarSize),
                    self.AbsolutePos[1]
                    + self._CanvasPos[1] * self.AbsoluteSize[1] * barHeight,
                    self.AbsoluteSize[0] * self.ScrollingBarSize,
                    self.AbsoluteSize[1] * barHeight,
                ),
            )

    def render(self, screen, *args):
        if not self.Visible:
            return
        super().render(*args)
        self.renderUIStructures(screen)
        # screen surface
        surface = py.Surface((self.AbsoluteSize[0], self.AbsoluteSize[1]))

        # Color screen
        surface.fill(self.BackgroundColor)

        # calculate the canvas sizing for automatic canvas
        canvasX, canvasY = 0, 0
        if self.AutoCanvasX:
            for child in self.Children:
                if not isinstance(child, GuiBase):
                    continue

                canvasX = max(child.Pos[0], canvasX)
        if self.AutoCanvasY:
            for childKey in self.Children:
                # print(isinstance(child, GuiBase))
                child = GuiAssets[childKey]
                # print(type(child).__name__)
                if not isinstance(child, GuiBase):
                    continue
                # print(child.Pos[1])
                canvasY = max(child.Pos[1] + child.Size[1], canvasY)
        canvasY -= 1
        canvasY = max(0, canvasY)

        self._CanvasSize = [canvasX, canvasY]
        # render children
        self.renderUIAssets(surface)
        screen.blit(surface, (self.AbsolutePos[0], self.AbsolutePos[1]))
        self._renderScrollingBars(screen)
