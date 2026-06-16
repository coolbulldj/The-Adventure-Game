from Classes.GUIClasses.NonRendered.UIStructure import UIStructure
from Classes.GUIClasses.GuiBase import GuiBase


class UICorner(UIStructure):
    def __init__(self):
        super().__init__()
        self.RelativeAxis = (
            "Horoizontal"  # defines which axis the corner is relative to
        )
        self.Size = (
            0  # defines how much of the corner is sized (done in percentage btw)
        )
        self.AbsoluteSize = 0  # defines the corner radius

    def render(self, *args):
        super().render(*args)

        if not self.Parent or self.Parent == "game":
            return

        if not isinstance(self.Parent, GuiBase):
            return

        parentW, parentH = self.Parent.AbsoluteSize[0], self.Parent.AbsoluteSize[1]
        if parentW <= 0 or parentH <= 0:
            self.AbsoluteSize = 0
            self.Parent.BorderRadius = 0
            return

        if self.RelativeAxis in ("Horoizontal", "Horizontal"):
            radius = parentW * self.Size
        elif self.RelativeAxis == "Vertical":
            radius = parentH * self.Size
        else:
            radius = 0

        maxRadius = min(parentW, parentH) / 2
        radius = max(0, min(round(radius), round(maxRadius)))

        self.AbsoluteSize = radius
        self.Parent.BorderRadius = radius
