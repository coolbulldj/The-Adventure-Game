from Classes.GUIClasses.NonRendered.UIStructure import UIStructure
from Classes.GUIClasses.GuiBase import GuiBase
from Modules.Core.CoreGUI.GUIElementsList import GuiAssets


class UIGridLayout(UIStructure):
    def __init__(self):
        super().__init__()
        self.X_Padding = 0.05
        self.Y_Padding = 0.05

    def render(self, _):
        if self.Parent == "game" or not self.Parent:
            return

        # ensures no rounding gaps between elements during rendering
        realXPadding = self.X_Padding if self.X_Padding != 0 else -0.005
        realYPadding = self.Y_Padding if self.Y_Padding != 0 else -0.005

        parentWidth = self.Parent.Size[0]
        currentXOffset = 0
        currentYOffset = 0
        rowHeight = 0

        for childKey in self.Parent.Children:
            asset = GuiAssets.get(childKey)

            if not isinstance(asset, GuiBase):
                continue

            if currentXOffset > 0 and currentXOffset + asset.Size[0] > parentWidth:
                currentXOffset = 0
                currentYOffset += rowHeight + realYPadding
                rowHeight = 0

            asset.Pos = [
                currentXOffset + asset.Size[0] / 2,
                currentYOffset + asset.Size[1] / 2,
            ]

            rowHeight = max(rowHeight, asset.Size[1])
            currentXOffset += asset.Size[0] + realXPadding
