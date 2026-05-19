from Classes.GUIClasses.NonRendered.UIStructure import UIStructure
from Classes.GUIClasses.GuiBase import GuiBase
from Modules.Core.CoreGUI.GUIElementsList import GuiAssets 

class UIListLayout(UIStructure):
    def __init__(self):
        super().__init__()
        self.Padding = 0.05
        self.AlignmentDirection = "Vertical"

    def render(self):
        if self.Parent == "game":
            return
        currentOffset = 0

        for childKey in self.Parent.Children:
            asset = GuiAssets[childKey]

            if not isinstance(asset, GuiBase):
                continue
            currentOffset += asset.Size[1]
            asset.AbsolutePos = [self.Parent.AbsolutePos[1], (self.Parent.AbsolutePos[1]-self.Parent.AbsoluteSize[1]) + currentOffset]
    
            