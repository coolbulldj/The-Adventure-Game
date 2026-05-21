from Classes.GUIClasses.NonRendered.UIStructure import UIStructure
from Classes.GUIClasses.GuiBase import GuiBase
from Modules.Core.CoreGUI.GUIElementsList import GuiAssets 

class UIListLayout(UIStructure):
    def __init__(self):
        super().__init__()
        self.Padding = -0.01
        self.AlignmentDirection = "Vertical"

    def render(self):
        if self.Parent == "game":
            return
        currentOffset = 0
        for childKey in self.Parent.Children:
            asset = GuiAssets[childKey]

            if not isinstance(asset, GuiBase):
                continue
            asset.Pos = [self.Parent.Pos[0], asset.Size[1] / 2 + currentOffset]
            currentOffset += asset.Size[1] + self.Padding
            