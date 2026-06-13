import pygame as py
from Classes.GUIClasses.GuiBase import GuiBase


class Frame(GuiBase):
    def __init__(self):
        super().__init__()

    def render(self, screen, *args):
        super().render(*args)
        self.renderUIStructures(screen)
        if self.BackgroundTransparency != 1:
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
        self.renderUIAssets(screen)
