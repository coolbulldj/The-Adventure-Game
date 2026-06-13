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

    def render(self, screen, *args):
        super().render(*args)  # this means the super is invisible

        ab_xs, ab_ys = self.AbsoluteSize
        self.renderUIStructures(screen)
        # Draw backing frmae
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

        # Resize the original image to a new width of 100 and height of 50
        resized_image = py.transform.scale(self.Image, (ab_xs, ab_ys))

        screen.blit(resized_image, self.AbsolutePos)
        self.renderUIAssets(screen)
