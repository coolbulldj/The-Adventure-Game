import pygame as py
from Classes.GUIClasses.GuiBase import GuiBase


class Frame(GuiBase):
    def __init__(self):
        super().__init__()

    def render(self, screen, *args):
        super().render(*args)
        self.renderUIStructures(screen)
        if self.BackgroundTransparency == 0:
            py.draw.rect(
                screen,
                self.BackgroundColor,
                (
                    self.AbsolutePos[0],
                    self.AbsolutePos[1],
                    self.AbsoluteSize[0],
                    self.AbsoluteSize[1],
                ),
                border_radius=self.BorderRadius,
            )
        elif self.BackgroundTransparency < 1:
            alpha = int(255 * (1 - self.BackgroundTransparency))
            frame_surface = py.Surface(
                (self.AbsoluteSize[0], self.AbsoluteSize[1]), py.SRCALPHA
            )
            # Draw the rectangle
            py.draw.rect(
                frame_surface,
                (
                    self.BackgroundColor[0],
                    self.BackgroundColor[1],
                    self.BackgroundColor[2],
                    alpha,
                ),
                (0, 0, self.AbsoluteSize[0], self.AbsoluteSize[1]),
                border_radius=self.BorderRadius,
            )

            screen.blit(
                frame_surface,
                (self.AbsolutePos[0], self.AbsolutePos[1]),
            )

        self.renderUIAssets(screen)
