import pygame as py
from Classes.GUIClasses.NonRendered.UIStructure import UIStructure
from Classes.GUIClasses.TextLabel import TextLabel
from Modules.Core.CoreGUI.GUIElementsList import GuiAssets


class UIStroke(UIStructure):
    def __init__(self):
        super().__init__()
        self.Size = 0.05
        # defines how much of the corner is sized (done in percentage btw)
        self.RelativeAxis = (
            "Horoizontal"  # defines which axis the corner is relative to
        )
        self.Color = (0, 0, 0)
        self.Context = "border"  # defines where the stroke renders either
        # the border or the context of the asset (e.g for textlabel it will render
        # around the text )

    def render(self, screen):
        if not self.Parent:
            return

        if isinstance(self.Parent, TextLabel) and self.Context == "contextual":
            print("rendering text stroke for a text label")
        else:
            Offset = 0

            if self.RelativeAxis == "Horoizontal":
                Offset = self.Parent.AbsoluteSize[0] * self.Size
            elif self.RelativeAxis == "Vertical":
                Offset = self.Parent.AbsoluteSize[1] * self.Size
            else:
                print("UI Stroke Failed to use RelativeAxis:", self.RelativeAxis)
                return

            # xOffset = self.Parent.AbsoluteSize[0] * self.Size
            # yOffset = self.Parent.AbsoluteSize[1] * self.Size
            py.draw.rect(
                screen,
                self.Color,
                (
                    self.Parent.AbsolutePos[0] - Offset / 2,
                    self.Parent.AbsolutePos[1] - Offset / 2,
                    self.Parent.AbsoluteSize[0] + Offset,
                    self.Parent.AbsoluteSize[1] + Offset,
                ),
            )
