import pygame as py
import os
from Classes.GUIClasses.GuiBase import GuiBase

ErrorImagePath = "Assets\Images\ImagePathFailure.png"

CachedImages = {}


def getImage(ImagePath: str):
    if ImagePath not in CachedImages:
        if (
            ImagePath == ""
        ):  # in future implement checks to make it so that it check whether image path points correctly
            ImagePath = ErrorImagePath
        CachedImages[ImagePath] = py.image.load(ImagePath).convert_alpha()
    return CachedImages[ImagePath]


class Image(GuiBase):
    def __init__(self):
        super().__init__()
        self.ImagePath = ""
        self.Image = getImage(self.ImagePath)

    def __setattr__(self, name, value):
        super().__setattr__(name, value)

        if name == "ImagePath":
            # Update image
            self.Image = getImage(value)

    def render(self, screen, screenSize, posOffset=[0, 0]):
        if super().render(screenSize, posOffset):  # this means the super is invisible
            # print(self.Visible)
            return

        ab_xs, ab_ys = self.AbsoluteSize

        # Draw backing frmae
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

        # Resize the original image to a new width of 100 and height of 50
        resized_image = py.transform.scale(self.Image, (ab_xs, ab_ys))

        screen.blit(resized_image, self.AbsolutePos)
        self.renderChildren(screen)
